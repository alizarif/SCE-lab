"""Build the data files the online dashboard reads.

    python tools/build_dashboard.py            → dashboard/data/*.json

Each file is a JSON array of plain row objects (one table each). The GitHub job runs this after every survey day,
and the dashboard's daily refresh uploads the files. Nothing here calls the API or changes the survey data.
"""
import gzip
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from sce_survey.config import DATA, load_config            # noqa: E402
from sce_survey.questionnaire import Questionnaire          # noqa: E402
from sce_survey.report import long_values                   # noqa: E402
from sce_survey.schedule import month_plan, survey_days, today, wave_of   # noqa: E402
from sce_survey.store import ledger, responses              # noqa: E402

OUT = ROOT / "dashboard" / "data"
SAMPLE_GLOB = "sample/sample_all_interviews_*.csv"

ARM_NAMES = {"A_noweb_nomemory": "A · no web, no memory", "B_web_nomemory": "B · web, no memory",
             "C_noweb_memory": "C · no web, memory", "D_web_memory": "D · web, memory"}

# Items the dashboard follows day by day, per person and against the real SCE answers.
KEY = ["Q8v2part2", "Q9bv2part2", "Q1apart2", "Q9_binmean", "Q9c_binmean", "Q9new2_binmean",
       "Q4new", "Q5new", "Q6new", "Q13new", "Q14new", "Q22new", "Q17new",
       "Q23v2part2", "Q24_binmean", "Q25v2part2", "Q26v2part2", "Q27v2part2", "Q30new", "Q31v2part2",
       "C1_binmean", "C2part2", "C3part2", "C4_1", "C4_2", "C4_3", "C4_4", "C4_5", "C4_6", "Q3", "Q1", "Q2", "Q28", "Q29"]
PERSON_ITEMS = ["Q8v2part2", "Q9bv2part2", "Q1apart2", "Q9_binmean", "Q4new", "Q5new", "Q6new", "Q13new",
                "Q25v2part2", "Q26v2part2", "Q30new", "Q31v2part2", "Q1", "Q2"]
GROUP_ITEMS = ["Q8v2part2", "Q9bv2part2", "Q1apart2", "Q4new", "Q6new", "Q13new", "Q25v2part2", "Q26v2part2",
               "Q30new", "Q31v2part2"]
REAL_ITEMS = ["Q8v2part2", "Q9bv2part2", "Q1apart2", "Q9_binmean", "Q9c_binmean", "Q4new", "Q5new", "Q6new",
              "Q13new", "Q14new", "Q22new", "Q23v2part2", "Q25v2part2", "Q26v2part2", "Q27v2part2", "Q30new",
              "Q31v2part2", "Q3", "Q1", "Q2", "Q28", "Q29"]
PAIR_ITEMS = ["Q8v2part2", "Q9bv2part2", "Q4new", "Q5new", "Q6new", "Q13new", "Q25v2part2", "Q26v2part2",
              "Q30new", "Q31v2part2"]
MEDIAN_ITEMS = {"Q8v2part2", "Q9bv2part2", "Q1apart2", "Q23v2part2", "Q25v2part2", "Q26v2part2", "Q27v2part2",
                "Q31v2part2", "C2part2", "C3part2", "C4_1", "C4_2", "C4_3", "C4_4", "C4_5", "C4_6"}
SIGNED = {"Q8v2part2": "Q8v2", "Q9bv2part2": "Q9bv2", "Q1apart2": "Q1a", "Q23v2part2": "Q23v2",
          "Q25v2part2": "Q25v2", "Q26v2part2": "Q26v2", "Q27v2part2": "Q27v2", "Q31v2part2": "Q31v2",
          "C2part2": "C2", "C3part2": "C3"}
MIDPOINTS = [14, 10, 6, 3, 1, -1, -3, -6, -10, -14]
DENSITY = ["Q9", "Q9c", "Q9new2", "Q24", "C1"]
BIN_SHORT = ["≥12%", "8–12%", "4–8%", "2–4%", "0–2%", "0 to −2%", "−2 to −4%", "−4 to −8%", "−8 to −12%", "≤−12%"]


def r(x, k=2):
    if x is None:
        return None
    try:
        if pd.isna(x):
            return None
    except (TypeError, ValueError):
        pass
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (float, np.floating)):
        return round(float(x), k)
    return x


def rows(df, k=2):
    out = []
    for rec in df.to_dict("records"):
        out.append({c: r(v, k) for c, v in rec.items()})
    return out


def write(name, data):
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / f"{name}.json"
    p.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":"), allow_nan=False))
    return p.stat().st_size


def stats(lv, by):
    g = lv.groupby(by + ["item"])["value"]
    s = g.agg(n="count", mean="mean", sd="std", median="median", min="min", max="max",
              p25=lambda x: x.quantile(.25), p75=lambda x: x.quantile(.75)).reset_index()
    return s


def labels(qn):
    lab = {}
    for q in qn.all:
        lab[q["id"]] = q["label"]
        if q["type"] == "density":
            lab[f"{q['id']}_binmean"] = q["label"].replace("probabilities by range", "density mean")
        if q["type"] == "commodities":
            for part in str(q.get("items") or "").split("||"):
                if "=" in part:
                    k, v = part.split("=", 1)
                    lab[k.strip()] = "Expected change: " + v.strip().replace("The price of ", "").replace(
                        "The cost of ", "")
    return lab


def options(q):
    out = {}
    for part in str(q.get("options") or "").split("||"):
        if "=" in part:
            k, v = part.split("=", 1)
            try:
                out[int(k.strip())] = v.strip()
            except ValueError:
                pass
    return out


def people_frame():
    p = pd.read_excel(ROOT / "participants.xlsx")
    p = p[p["userid"].notna()].copy()
    p["userid"] = p["userid"].astype(int)
    emp = []
    for _, x in p.iterrows():
        if x.get("Q10_1") == 1 or x.get("Q10_2") == 1:
            emp.append("Working")
        elif x.get("Q10_7") == 1:
            emp.append("Retired")
        elif x.get("Q10_3") == 1 or x.get("Q10_4") == 1:
            emp.append("Looking / laid off")
        else:
            emp.append("Other not working")
    p["employment"] = emp
    p["gender"] = p["Q33"].map({1: "Female", 2: "Male"})
    p["homeowner"] = p["Q43"].map({1: "Owns home", 2: "Rents", 3: "Other housing"})
    p["age_group"] = p["_AGE_CAT"]
    p["education"] = p["_EDU_CAT"]
    p["income"] = p["_HH_INC_CAT"]
    p["numeracy"] = p["_NUM_CAT"]
    p["region"] = p["_REGION_CAT"]
    return p


GROUP_DIMS = [("age_group", "Age"), ("gender", "Gender"), ("education", "Education"), ("income", "Household income"),
              ("numeracy", "Numeracy"), ("region", "Region"), ("homeowner", "Housing"), ("employment", "Work status")]


def real_answers():
    """The 1,200 people's own SCE answers (2016–2025), signed and with density means from bin midpoints."""
    files = sorted(ROOT.glob(SAMPLE_GLOB))
    if not files:
        return None
    s = pd.read_csv(files[0], low_memory=False).copy()
    s["userid"] = s["userid"].astype(int)
    s["date"] = s["date"].astype(int)
    for part, d in SIGNED.items():
        if part in s and d in s:
            s[part] = np.where(s[d] == 2 if d in ("Q8v2", "Q9bv2", "Q1a") else s[d] == 3, -s[part].abs(), s[part])
    for q in DENSITY:
        cols = [f"{q}_bin{i}" for i in range(1, 11)]
        if all(c in s for c in cols):
            b = s[cols].astype(float)
            tot = b.sum(axis=1)
            s = s.copy()
            s[f"{q}_binmean"] = np.where(tot > 0, (b.values * MIDPOINTS).sum(axis=1) / tot.replace(0, np.nan), np.nan)
    return s


def news(cfg, waves_keep=2):
    out = []
    for f in sorted((DATA / "logs").glob("*/*.jsonl.gz")):
        if f.parent.name not in waves_keep:
            continue
        day, arm = f.stem.replace(".jsonl", "").split("_", 1)
        cnt, meta = Counter(), {}
        n_int = 0
        with gzip.open(f, "rt") as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                res = rec.get("web_results") or []
                if not res:
                    continue
                n_int += 1
                for w in res:
                    u = (w.get("url") or "").split("#")[0]
                    if not u:
                        continue
                    cnt[u] += 1
                    if u not in meta:
                        dom = urlparse(u).netloc.lower().removeprefix("www.")
                        meta[u] = {"title": (w.get("title") or dom).strip()[:200], "domain": dom,
                                   "snippet": " ".join((w.get("content") or "").split())[:280]}
        for u, n in cnt.most_common(25):
            out.append({"date": day, "arm": arm, "url": u, **meta[u], "interviews": n,
                        "share": round(n / n_int, 3) if n_int else None})
    return out


def main():
    cfg = load_config()
    qn = Questionnaire(cfg.get("questionnaire_file"))
    lab = labels(qn)
    qby = {q["id"]: q for q in qn.all}
    sizes = {}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    run_day = today(cfg)
    arms = [a["id"] for a in cfg["arms"]]

    lg = ledger()
    df = responses()
    if not df.empty:
        df["date"] = df["date"].astype(str)
        df["wave"] = df["wave"].astype(str)
        df["userid"] = df["userid"].astype(int)
    lv = long_values(df) if not df.empty else pd.DataFrame(columns=["interview_id", "date", "wave", "arm", "userid",
                                                                      "item", "value"])
    waves = sorted(lv["wave"].unique()) if len(lv) else []
    cur_wave = wave_of(run_day)
    keep_waves = sorted(set(waves[-3:]))
    people = people_frame()

    # ---------- questions (what each item is) ----------
    qrows, order = [], 0
    for q in qn.all:
        if q["type"] in ("intro",):
            continue
        order += 1
        base = {"module": q["module"], "type": q["type"], "unit": q.get("unit") if isinstance(q.get("unit"), str) else "",
                "text": " ".join(str(q.get("text") or "").split())[:700]}
        ids = [q["id"]]
        if q["type"] == "density":
            ids = [f"{q['id']}_binmean"]
        if q["type"] == "commodities":
            ids = [k for k in lab if k.startswith(q["id"] + "_")]
        for i in ids:
            qrows.append({"item": i, "label": lab.get(i, i), "order": order, "key": i in KEY,
                          "stat": "median" if i in MEDIAN_ITEMS or i.endswith("_binmean") else "mean",
                          "unit": "%" if (base["type"] in ("percent", "density", "commodities") or base["unit"] == "%"
                                          or i.endswith("part2")) else "", **{k: v for k, v in base.items() if k != "unit"}})
    sizes["questions"] = write("questions", qrows)

    # ---------- runs by day and arm ----------
    run_rows = []
    if not lg.empty:
        lg["run_date"] = lg["run_date"].astype(str)
        lg["dur"] = (pd.to_datetime(lg["finished_utc"]) - pd.to_datetime(lg["started_utc"])).dt.total_seconds()
        for (d, a), g in lg.groupby(["run_date", "arm"]):
            run_rows.append({"date": d, "arm": a, "interviews": len(g),
                             "complete": int((g["status"] == "complete").sum()),
                             "questions": int(g["n_questions"].sum()), "answered": int(g["n_answered"].sum()),
                             "errors": int(g["n_errors"].sum()), "reasks": int(g["n_reasks"].sum()),
                             "calls": int(g["n_calls"].sum()), "prompt_tokens": int(g["prompt_tokens"].sum()),
                             "completion_tokens": int(g["completion_tokens"].sum()),
                             "cost": round(float(g["cost_usd"].fillna(0).sum()), 4),
                             "seconds_per_interview": round(float(g["dur"].mean()), 1),
                             "late": int((g["scheduled_date"].astype(str) < d).sum())})
    sizes["runs_daily"] = write("runs_daily", run_rows)

    # ---------- schedule (this month and next) ----------
    sched = []
    y, m = run_day.year, run_day.month
    done = set()
    if not lg.empty:
        done = {(int(u), str(w)) for u, w, s in zip(lg["userid"], lg["wave"].astype(str), lg["status"]) if s == "complete"}
    ids = people["userid"].tolist()
    for (yy, mm) in [(y, m), (y + (m == 12), m % 12 + 1)]:
        plan = month_plan(cfg, ids, yy, mm)
        w = f"{yy:04d}-{mm:02d}"
        per = Counter(plan.values())
        did = Counter(plan[u] for u in plan if (u, w) in done)
        if not lg.empty:
            per_arm_done = lg[(lg["wave"].astype(str) == w) & (lg["status"] == "complete")].groupby("scheduled_date").size()
        else:
            per_arm_done = pd.Series(dtype=int)
        for d in survey_days(cfg, yy, mm):
            sched.append({"date": d.isoformat(), "wave": w, "people": per.get(d, 0),
                          "interviews_planned": per.get(d, 0) * len(arms),
                          "interviews_done": int(per_arm_done.get(d.isoformat(), 0)),
                          "status": "done" if per_arm_done.get(d.isoformat(), 0) >= per.get(d, 0) * len(arms) > 0
                          else ("due" if d <= run_day else "upcoming")})
    sizes["schedule"] = write("schedule", sched)

    # ---------- status (one row) ----------
    cur = lg[lg["wave"].astype(str) == cur_wave] if not lg.empty else lg
    last_run = lg["run_date"].max() if not lg.empty else None
    last = lg[lg["run_date"] == last_run] if last_run else lg
    status = [{
        "generated_utc": now, "today": run_day.isoformat(), "wave": cur_wave, "model": cfg["model"],
        "participants": len(people), "arms": len(arms),
        "interviews_total": int(len(lg)), "people_total": int(lg["userid"].nunique()) if not lg.empty else 0,
        "cost_total": round(float(lg["cost_usd"].fillna(0).sum()), 2) if not lg.empty else 0.0,
        "interviews_month": int(len(cur)), "people_month": int(cur["userid"].nunique()) if len(cur) else 0,
        "interviews_month_target": len(people) * len(arms),
        "cost_month": round(float(cur["cost_usd"].fillna(0).sum()), 2) if len(cur) else 0.0,
        "last_run_date": last_run, "interviews_last_run": int(len(last)),
        "cost_last_run": round(float(last["cost_usd"].fillna(0).sum()), 2) if len(last) else 0.0,
        "errors_last_run": int(last["n_errors"].sum()) if len(last) else 0,
        "reasks_last_run": int(last["n_reasks"].sum()) if len(last) else 0,
        "days_run": int(lg["run_date"].nunique()) if not lg.empty else 0,
        "start_date": str(cfg.get("start_date")), "web_results": int(cfg.get("web", {}).get("max_results", 10)),
        "concurrency": int(cfg.get("concurrency", 8)), "memory_mode": cfg.get("memory", {}).get("mode", "summary"),
        "reasoning": json.dumps(cfg.get("reasoning")) if cfg.get("reasoning") else "",
    }]
    sizes["status"] = write("status", status)

    # ---------- statistics ----------
    if len(lv):
        recent = sorted(lv["date"].unique())[-180:]
        sd = stats(lv[lv["item"].isin(KEY) & lv["date"].isin(recent)], ["date", "arm"])
        sd["date"] = sd["date"].astype(str)
        sizes["stats_daily"] = write("stats_daily", rows(sd.sort_values(["item", "arm", "date"]), 3))
        sm = stats(lv[~lv["item"].str.contains(r"_bin\d+$", regex=True)], ["wave", "arm"])
        sm["label"] = sm["item"].map(lab).fillna(sm["item"])
        sizes["stats_monthly"] = write("stats_monthly", rows(sm.sort_values(["item", "arm", "wave"]), 3))
        # month to date (how the monthly number builds up day by day)
        mtd = []
        lvk = lv[lv["item"].isin(KEY)]
        for w in keep_waves:
            sub = lvk[lvk["wave"] == w]
            for d in sorted(sub["date"].unique()):
                s = stats(sub[sub["date"] <= d], ["arm"])
                s["date"], s["wave"] = d, w
                mtd += rows(s[["date", "wave", "arm", "item", "n", "mean", "median", "p25", "p75"]], 3)
        sizes["stats_mtd"] = write("stats_mtd", mtd)
    else:
        for n in ("stats_daily", "stats_monthly", "stats_mtd"):
            sizes[n] = write(n, [])

    # ---------- answer shares for choice questions ----------
    ch = []
    if not df.empty:
        for qid in [q["id"] for q in qn.all if q["type"] in ("choice", "multi", "signed")]:
            sub = df[df["question_id"] == qid]
            if sub.empty:
                continue
            opts = options(qby[qid])
            for (w, a), g in sub.groupby(["wave", "arm"]):
                codes = []
                for v, js in zip(g["value"], g["answer_json"]):
                    if qby[qid]["type"] == "multi":
                        try:
                            codes += [int(c) for c in json.loads(js)]
                        except (TypeError, ValueError):
                            pass
                    elif pd.notna(v):
                        codes.append(int(v))
                n_resp = int(g["answer_json"].notna().sum())
                c = Counter(codes)
                for code in sorted(set(opts) | set(c)):
                    ch.append({"wave": w, "arm": a, "item": qid, "code": code, "answer": opts.get(code, str(code)),
                               "n": c.get(code, 0), "share": round(c.get(code, 0) / n_resp, 4) if n_resp else None,
                               "respondents": n_resp})
    sizes["choices"] = write("choices", ch)

    # ---------- average density forecast (probability per bin) ----------
    den = []
    if len(lv):
        for q in DENSITY:
            sub = lv[lv["item"].str.fullmatch(fr"{q}_bin\d+")]
            if sub.empty:
                continue
            g = sub.groupby(["wave", "arm", "item"])["value"].mean().reset_index()
            for rec in g.itertuples():
                b = int(rec.item.rsplit("bin", 1)[1])
                den.append({"wave": rec.wave, "arm": rec.arm, "question": q, "bin": b, "range": BIN_SHORT[b - 1],
                            "midpoint": MIDPOINTS[b - 1], "prob": round(float(rec.value), 2)})
    sizes["density"] = write("density", den)

    # ---------- groups ----------
    grp = []
    if len(lv):
        lvg = lv[lv["item"].isin(GROUP_ITEMS) & lv["wave"].isin(keep_waves)].merge(people[["userid"] + [d for d, _ in GROUP_DIMS]], on="userid",
                                                     how="left")
        for dim, dname in GROUP_DIMS:
            s = lvg.dropna(subset=[dim]).groupby(["wave", "arm", dim, "item"])["value"].agg(
                n="count", mean="mean", median="median").reset_index().rename(columns={dim: "group"})
            s["dimension"] = dname
            grp += rows(s, 3)
    sizes["groups"] = write("groups", grp)

    # ---------- panel composition (aggregate only; no person-level rows leave the repository) ----------
    month_done = set()
    if not lg.empty:
        month_done = set(lg[(lg["status"] == "complete") & (lg["wave"].astype(str) == cur_wave)]["userid"].astype(int))
    people["interviewed_month"] = people["userid"].isin(month_done)
    panel = []
    for dim, dname in GROUP_DIMS + [("_STATE", "State")]:
        g = people.dropna(subset=[dim]).groupby(dim).agg(people=("userid", "count"),
                                                         interviewed_month=("interviewed_month", "sum")).reset_index()
        g["share"] = (g["people"] / len(people)).round(4)
        g["dimension"], g["group"] = dname, g[dim].astype(str)
        panel += rows(g[["dimension", "group", "people", "share", "interviewed_month"]], 4)
    sizes["panel"] = write("panel", panel)
    plan_now = month_plan(cfg, ids, y, m)

    # ---------- real SCE answers of the same people ----------
    real = real_answers()
    rh, rvl, pbins = [], [], []
    if real is not None:
        real = real.copy()
        real["year"] = real["date"] // 100
        for it in REAL_ITEMS:
            if it not in real:
                continue
            s = real.groupby("year")[it].agg(n="count", mean="mean", median="median",
                                             p25=lambda x: x.quantile(.25), p75=lambda x: x.quantile(.75)).reset_index()
            s = s[s["n"] > 0]
            s["item"] = it
            rh += rows(s, 3)
        # last real answer vs this month's persona answer: only aggregates (correlation, binned medians)
        if len(lv) and waves:
            w = waves[-1]
            llm = lv[(lv["wave"] == w) & lv["item"].isin(PAIR_ITEMS)]
            rs = real.sort_values("date")
            for it in PAIR_ITEMS:
                if it not in rs:
                    continue
                last = rs.dropna(subset=[it]).groupby("userid")[it].last().rename("real")
                pct = it in MEDIAN_ITEMS
                edges = [-np.inf, 0, 2, 4, 6, 10, np.inf] if pct else [-np.inf, 20, 40, 60, 80, np.inf]
                names = ["below 0%", "0–2%", "2–4%", "4–6%", "6–10%", "10% or more"] if pct else \
                        ["0–19%", "20–39%", "40–59%", "60–79%", "80–100%"]
                for arm in arms:
                    pr = llm[(llm["item"] == it) & (llm["arm"] == arm)].set_index("userid")["value"].rename("persona")
                    d = pd.concat([last, pr], axis=1, join="inner").dropna()
                    if len(d) < 5:
                        continue
                    corr = d["real"].corr(d["persona"]) if d["real"].std() > 0 and d["persona"].std() > 0 else None
                    rvl.append({"wave": w, "item": it, "arm": arm, "people": int(len(d)), "corr": r(corr, 3),
                                "gap": r((d["persona"] - d["real"]).median(), 2),
                                "real_median": r(d["real"].median(), 2), "persona_median": r(d["persona"].median(), 2)})
                    d["bin"] = pd.cut(d["real"], edges, labels=False, right=False)
                    for b_, g in d.groupby("bin"):
                        if len(g) < 5:              # small cells are left out
                            continue
                        pbins.append({"wave": w, "item": it, "arm": arm, "bin": int(b_), "range": names[int(b_)],
                                      "people": int(len(g)), "real_median": r(g["real"].median(), 2),
                                      "persona_median": r(g["persona"].median(), 2),
                                      "persona_p25": r(g["persona"].quantile(.25), 2),
                                      "persona_p75": r(g["persona"].quantile(.75), 2)})
    sizes["real_history"] = write("real_history", rh)
    sizes["pair_fit"] = write("pair_fit", rvl)
    sizes["pair_bins"] = write("pair_bins", pbins)

    # ---------- answer quality per item ----------
    qual = []
    if not df.empty:
        g = df.groupby(["wave", "arm", "question_id"])
        q = g.agg(asked=("interview_id", "count"), answered=("answer_json", lambda x: int(x.notna().sum())),
                  reasked=("reasked", lambda x: int(pd.to_numeric(x, errors="coerce").fillna(0).astype(bool).sum())),
                  errors=("error", lambda x: int(x.notna().sum())),
                  latency=("latency_s", "mean"), cost=("cost_usd", "sum")).reset_index()
        q = q.rename(columns={"question_id": "item"})
        q["label"] = q["item"].map(lab).fillna(q["item"])
        reasons = df[df["reask_reason"].notna()].groupby(["wave", "arm", "question_id"])["reask_reason"].agg(
            lambda x: ", ".join(f"{k} ({v})" for k, v in Counter(x).most_common(3)))
        q["reask_reasons"] = [reasons.get((a, b, c), "") for a, b, c in zip(q["wave"], q["arm"], q["item"])]
        qual = rows(q, 3)
    sizes["quality"] = write("quality", qual)

    # ---------- news the web arms read ----------
    sizes["news"] = write("news", news(cfg, set(keep_waves[-1:]) if keep_waves else set()))

    sizes["arms"] = write("arms", [{"arm": a["id"], "name": ARM_NAMES.get(a["id"], a["id"]), "web": bool(a["web"]),
                                    "memory": bool(a["memory"])} for a in cfg["arms"]])
    total = sum(sizes.values())
    for k, v in sorted(sizes.items()):
        print(f"{k:18s} {v / 1024:9.1f} KB")
    print(f"{'total':18s} {total / 1024:9.1f} KB → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
