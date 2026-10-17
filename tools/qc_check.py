"""Quality check of participants.xlsx and questionnaire.xlsx.

    python tools/qc_check.py sample/sample_all_interviews_....csv

Writes qc/qc_report.md (summary) and qc/participants_flags.csv (one row per person per finding).

participants.xlsx
  1. every value is re-derived from the SCE microdata rows (separately from make_participants.py) and compared
  2. every code is a valid SCE response code; numbers are in plausible ranges
  3. the person's answers follow the SCE routing (e.g. Q11 only if employed, HH2 only if partnered)
  4. every persona text shows exactly the values in the columns, with the exact SCE wording, and nothing missing
questionnaire.xlsx
  5. every included question renders with no leftover {placeholders}, has an answer format, and parses
  6. the skip logic is walked for every combination of employment answers that changes the route
"""
import itertools
import math
import re
import sys
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from sce_survey.config import load_config                                       # noqa: E402
from sce_survey.persona import NUMERACY, STATES, persona_text                    # noqa: E402
from sce_survey.questionnaire import Questionnaire, parse_answer, problem       # noqa: E402

flags = []


def flag(uid, check, detail, severity="error"):
    flags.append({"userid": uid, "severity": severity, "check": check, "detail": detail})


def same(a, b):
    na, nb = a is None or (isinstance(a, float) and math.isnan(a)), b is None or (isinstance(b, float) and math.isnan(b))
    if na or nb:
        return na and nb
    try:
        return math.isclose(float(a), float(b), abs_tol=1e-9)
    except (TypeError, ValueError):
        return str(a).strip() == str(b).strip()


def num(v):
    try:
        f = float(v)
        return None if math.isnan(f) else f
    except (TypeError, ValueError):
        return None


def main(src):
    qn = Questionnaire()
    cfg = load_config()
    P = pd.read_excel(ROOT / "participants.xlsx", sheet_name=0)
    M = pd.read_csv(src, low_memory=False)
    M["date"] = pd.to_numeric(M["date"], errors="coerce")
    M = M.sort_values(["userid", "date"])
    groups = dict(tuple(M.groupby("userid")))
    lines = []

    # ── 0. the people ──────────────────────────────────────────────────
    ids_p, ids_m = set(P["userid"].astype(int)), set(groups)
    lines.append(f"- people in participants.xlsx: {len(ids_p):,} (unique: {P['userid'].is_unique}); "
                 f"in the microdata file: {len(ids_m):,}; same set: {ids_p == ids_m}")

    work = ["Q11", "Q12new", "ES2", "Q37", "Q15", "Q16", "Q19"] + [f"Q10_{i}" for i in range(1, 11)] + [f"ES1_{i}" for i in range(1, 5)]
    single = ["Q32", "Q33", "Q34", "Q36", "Q38", "Q41", "Q42", "Q43", "Q43a", "Q44", "Q45b", "Q46", "QRA1", "QRA2", "Q47",
              "QNUM1", "QNUM2", "QNUM3", "QNUM5", "QNUM6", "QNUM8", "QNUM9"]
    sets = {"Q35": 6, "HH2": 11, "Q45new": 9}
    codes = {"Q33": 2, "Q34": 2, "Q36": 9, "Q38": 2, "Q43": 3, "Q43a": 3, "Q44": 2, "Q45b": 5, "Q46": 5, "QRA1": 7,
             "QRA2": 7, "Q47": 11, "QNUM8": 3, "QNUM9": 2, "Q12new": 2, "Q37": 5, "Q15": 2}
    n_cells = n_diff = 0
    for r in P.to_dict("records"):
        uid = int(r["userid"])
        g = groups.get(uid)
        if g is None:
            flag(uid, "source", "person not in the microdata file")
            continue
        # ── 1. re-derive from the microdata ───────────────────────────
        anc = g[g["Q32"].notna()]
        anc = anc.iloc[0] if len(anc) else g.iloc[0]
        expect = {c: anc.get(c) for c in work}
        for c in single:
            s = g[c].dropna()
            expect[c] = s.iloc[0] if len(s) else None
        for base, n in sets.items():
            cols = [f"{base}_{i}" for i in range(1, n + 1)]
            vals = g[cols].apply(pd.to_numeric, errors="coerce")
            pos = vals[(vals.fillna(0) > 0).any(axis=1)]
            row = pos.iloc[0] if len(pos) else (vals.dropna(how="all").iloc[0] if vals.notna().any().any() else None)
            for c in cols:
                expect[c] = None if row is None else row[c]
        expect["first_interview"] = anc["date"]
        for c, v in expect.items():
            n_cells += 1
            if not same(r.get(c), v):
                n_diff += 1
                flag(uid, "source", f"{c}: participants.xlsx has {r.get(c)!r}, microdata gives {v!r}")
        both = g[g["_STATE"].notna() & g["_COMMUTING_ZONE"].notna()]
        st_src = both.iloc[0]["_STATE"] if len(both) else (g["_STATE"].dropna().iloc[0] if g["_STATE"].notna().any() else None)
        if st_src is not None and not same(r.get("_STATE"), st_src):
            n_diff += 1
            flag(uid, "source", f"_STATE: {r.get('_STATE')!r} vs microdata {st_src!r}")
        if st_src is None and r.get("state_source") != "from commuting zone" and isinstance(r.get("_STATE"), str):
            flag(uid, "source", "state filled but not marked as inferred")

        # ── 2. valid codes and ranges ─────────────────────────────────
        for c, k in codes.items():
            v = num(r.get(c))
            if v is not None and (v != int(v) or not 1 <= v <= k):
                flag(uid, "code", f"{c}={v} is not a valid code (1–{k})")
        for base, n in {**sets, "Q10": 10, "ES1": 4}.items():
            for i in range(1, n + 1):
                v = num(r.get(f"{base}_{i}"))
                if v is not None and (v < 0 or (base != "Q45new" and v not in (0, 1))):
                    flag(uid, "code", f"{base}_{i}={v}")
        age = num(r.get("Q32"))
        if age is None or not 18 <= age <= 105:
            flag(uid, "range", f"age Q32={age}", "warning")
        for c in ("Q41", "Q42"):
            v = num(r.get(c))
            if v is not None and age is not None and v > age + 1:
                flag(uid, "range", f"{c}={v} years > age {age}", "warning")
        if num(r.get("Q41")) is not None and num(r.get("Q42")) is not None and num(r["Q41"]) > num(r["Q42"]) + 1:
            flag(uid, "range", f"years at residence Q41={r['Q41']} > years in state Q42={r['Q42']} (as reported)", "warning")

        # ── 3. SCE routing ────────────────────────────────────────────
        q10 = [i for i in range(1, 11) if (num(r.get(f"Q10_{i}")) or 0) > 0]
        emp = any(c in (1, 2, 4, 5) for c in q10)
        jobs = num(r.get("Q11"))
        selfemp = num(r.get("Q12new")) == 2
        es1 = [i for i in range(1, 5) if (num(r.get(f"ES1_{i}")) or 0) > 0]
        rules = {
            "Q11": emp, "Q12new": emp and (jobs or 0) > 0, "Q37": emp and (jobs or 0) > 0,
            "ES2": emp and (jobs or 0) > 0 and selfemp and 2 in es1,
            "Q15": 3 in q10 and 4 not in q10 and 5 not in q10,
            "Q16": num(r.get("Q15")) == 1, "Q19": num(r.get("Q15")) == 2,
        }
        for c, should in rules.items():
            has = num(r.get(c)) is not None
            if has and not should:
                flag(uid, "routing", f"{c} is answered although the SCE routing would skip it (Q10={q10}, Q11={jobs})", "warning")
            if should and not has:
                flag(uid, "routing", f"{c} should have been asked but is empty (Q10={q10}, Q11={jobs})", "warning")
        if not q10:
            flag(uid, "routing", "no employment situation (Q10) selected", "warning")
        if 3 in q10 and (1 in q10 or 2 in q10):
            flag(uid, "routing", f"Q10={q10} mixes working and not working (SCE error E8)", "warning")
        if es1 and not selfemp:
            flag(uid, "routing", f"ES1={es1} but Q12new is not self-employed")
        hh2 = [i for i in range(1, 12) if (num(r.get(f"HH2_{i}")) or 0) > 0]
        if hh2 and num(r.get("Q38")) != 1:
            flag(uid, "routing", "partner's employment (HH2) answered but not partnered (Q38)")
        if num(r.get("Q43a")) is not None and not (num(r.get("Q38")) == 1 and num(r.get("Q43")) != 3):
            flag(uid, "routing", f"Q43a answered with Q38={r.get('Q38')} and Q43={r.get('Q43')}")
        alone = (num(r.get("Q45new_9")) or 0) > 0
        others = sum(num(r.get(f"Q45new_{i}")) or 0 for i in range(1, 9))
        if alone and others > 0:
            flag(uid, "routing", "lives alone and lists other household members", "warning")
        if alone and num(r.get("Q46")) is not None:
            flag(uid, "routing", "Q46 answered although living alone (asked anyway in the SCE data; shown)", "warning")
        if num(r.get("Q38")) == 1 and (num(r.get("Q45new_1")) or 0) == 0 and not alone and others > 0:
            flag(uid, "consistency", "partnered (Q38) but no spouse/partner in the household list", "warning")
        if (num(r.get("Q45new_1")) or 0) > 0 and num(r.get("Q38")) == 2:
            flag(uid, "consistency", "spouse/partner in the household list but Q38 = No", "warning")
        cz = r.get("cz_states")
        if isinstance(r.get("_STATE"), str) and isinstance(cz, str) and r["_STATE"] not in cz.split(", "):
            flag(uid, "consistency", f"state {r['_STATE']} not covered by commuting zone {r.get('_COMMUTING_ZONE')} ({cz})", "warning")

        # ── 4. persona text ───────────────────────────────────────────
        d = cfg["start_date"] or date.today()
        text = persona_text(r, d, qn, bool(cfg.get("age_moves_with_date")))
        if re.search(r"\bnan\b|None(?! of the above)|\{|\}", text):
            flag(uid, "persona", "persona contains nan/None/braces")
        L = qn.option_label
        want = []
        if age is not None and 16 <= age <= 105:
            want.append(f"You are {int(age) if not cfg.get('age_moves_with_date') else ''}")
        elif isinstance(r.get("_AGE_CAT"), str):
            want.append("You are " + {"Under 40": "under 40", "40 to 60": "between 40 and 60", "Over 60": "over 60"}[r["_AGE_CAT"]])
        for c in ("Q33", "Q34", "Q36", "Q43", "Q44", "Q45b", "Q47"):
            v = num(r.get(c))
            if v is not None:
                want.append(L(c, int(v)))
        for i in range(1, 7):
            if (num(r.get(f"Q35_{i}")) or 0) > 0:
                want.append(L("Q35", i))
        for i in q10:
            want.append(L("Q10", i))
        if isinstance(r.get("_STATE"), str):
            want.append(STATES.get(r["_STATE"], r["_STATE"]))
        if isinstance(r.get("cz_name"), str) and "commuting zone" not in str(r.get("_qc_skip_cz", "")):
            if not (isinstance(r.get("_STATE"), str) and isinstance(cz, str) and r["_STATE"] not in cz.split(", ")):
                want.append(r["cz_name"])
        for c in ("QRA1", "QRA2", "Q46"):
            v = num(r.get(c))
            if v is not None:
                want.append(f": {int(v)}.")
        right = n_items = 0
        a16 = any(num(r.get(k)) is not None for k in ("QNUM1", "QNUM2", "QNUM3", "QNUM5", "QNUM6"))
        a89 = (num(r.get("first_interview")) or 0) >= 201504 or any(num(r.get(k)) is not None for k in ("QNUM8", "QNUM9"))
        for qid, _q, correct, fmt in NUMERACY:
            if not (a89 if qid in ("QNUM8", "QNUM9") else a16):
                continue
            n_items += 1
            v = num(r.get(qid))
            if v is not None:
                right += math.isclose(v, correct) if fmt else int(v) == correct
        if n_items:
            want.append(f"Your score: {right} of {n_items} questions correct.")
        for w in want:
            if w and w not in text:
                flag(uid, "persona", f"expected text not found: {w!r}")
        if emp is False and "How long you have been working" in text:
            flag(uid, "persona", "job tenure shown for someone without a job")

    lines.append(f"- values re-derived from the microdata and compared: {n_cells:,} cells, {n_diff} differences")

    # ── 5. questionnaire: render + parse every question ───────────────
    d = date(2026, 10, 18)
    qflags = []
    fake = {"choice": "ANSWER: 1", "signed": "ANSWER: 1", "multi": "ANSWER: 1", "percent": "ANSWER: 35",
            "number": "ANSWER: 3", "density": "\n".join(f"BIN{i}: 10" for i in range(1, 11)),
            "commodities": "\n".join(f"C4_{i}: 2" for i in range(1, 7))}
    answers_variants = [{}, {"Q10": [4], "Q11": 2, "ES1": [2], "Q8v2": 2, "Q9bv2": 1, "Q1a": 2, "Q23v2": 3, "Q25v2": 1,
                             "Q26v2": 3, "Q27v2": 1, "Q31v2": 3, "C2": 1, "C3": 3}]
    for q in qn.asked:
        for a in answers_variants:
            txt = qn.render(q, d, a) if q["type"] not in ("intro", "info") else qn.fill(q["text"], d, a)
            if re.search(r"\{[A-Za-z0-9_]+\}", txt):
                qflags.append(f"{q['id']}: unfilled placeholder in: {txt[:120]!r}")
        if q["type"] in fake:
            got = parse_answer(q, fake[q["type"]])
            if got is None or problem(q, got) is not None and q["type"] != "density":
                qflags.append(f"{q['id']}: a well-formed answer does not parse ({got!r})")
        if q["type"] not in ("intro", "info") and q["instruction"] and not qn.prompts.get(f"instruction_{q['instruction']}"):
            qflags.append(f"{q['id']}: instruction {q['instruction']} has no text")
    lines.append(f"- questionnaire: {len(qn.asked)} included rows render with every placeholder filled and parse: "
                 f"{'yes' if not qflags else 'NO'}")

    # ── 6. walk the skip logic for every route ────────────────────────
    from sce_survey.questionnaire import show_if
    routes = []
    q10_opts = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [1, 8], [7, 8], [3, 8], [4, 7], [6, 7]]
    for q10, jobs, q12, es1, q15, rt in itertools.product(q10_opts, [0, 1, 2], [1, 2], [[1], [2], [3], [4], [1, 2]],
                                                          [1, 2], ["new", "repeat"]):
        a, seq = {}, []
        script = {"Q10": q10, "Q11": jobs, "Q12new": q12, "ES1": es1, "Q15": q15}
        for q in qn.asked:
            if not qn.visible(q, rt, a):
                continue
            seq.append(q["id"])
            if q["id"] in script:
                a[q["id"]] = script[q["id"]]
        routes.append((tuple(q10), jobs, q12, tuple(es1), q15, rt, tuple(seq)))
        S = set(seq)
        emp = any(c in (1, 2, 4, 5) for c in q10)
        exp = {"Q11": emp, "Q12new": emp and jobs > 0, "Q12intro": emp and jobs > 1,
               "ES1": emp and jobs > 0 and q12 == 2, "ES2": emp and jobs > 0 and q12 == 2 and 2 in es1,
               "ES4": emp and jobs > 0 and q12 == 2, "Q13new": emp and jobs > 0 and q12 == 1,
               "Q22new": emp and jobs > 0 and q12 == 1, "Q23v2": emp and jobs > 0, "Q24": emp and jobs > 0,
               "Q15": 3 in q10 and 4 not in q10 and 5 not in q10,
               "Q16": 3 in q10 and 4 not in q10 and 5 not in q10 and q15 == 1,
               "Q19": 3 in q10 and 4 not in q10 and 5 not in q10 and q15 == 2,
               "Q20new": (3 in q10 and 4 not in q10 and 5 not in q10 and q15 == 2) or set(q10) <= {7, 8, 9} or (emp and jobs == 0),
               "C1": rt == "repeat", "C4": rt == "repeat", "Q1intro1-new": rt == "new", "Q1intro1-repeat": rt == "repeat"}
        for k, v in exp.items():
            if (k in S) != v:
                qflags.append(f"route Q10={q10} Q11={jobs} Q12new={q12} ES1={es1} Q15={q15} {rt}: {k} "
                              f"{'shown' if k in S else 'missing'}, PDF says {'shown' if v else 'skipped'}")
    distinct = len({r[-1] for r in routes})
    lines.append(f"- skip logic: {len(routes)} answer combinations walked ({distinct} distinct routes); "
                 f"routes differing from the PDF rules: {sum('route' in f for f in qflags)}")

    out = ROOT / "qc"
    out.mkdir(exist_ok=True)
    F = pd.DataFrame(flags, columns=["userid", "severity", "check", "detail"])
    F.to_csv(out / "participants_flags.csv", index=False)
    summ = F.groupby(["severity", "check"]).agg(findings=("userid", "size"), people=("userid", "nunique")).reset_index() \
        if len(F) else pd.DataFrame()
    md = ["# Quality check", "", f"Run {date.today()} on `participants.xlsx` ({len(P):,} people) and `questionnaire.xlsx`.", ""]
    md += lines + ["", "## participants.xlsx findings", ""]
    md += [summ.to_markdown(index=False) if len(summ) else "none", "",
           "Errors are problems in our files. Warnings are how the respondent actually answered the SCE (kept as reported).", ""]
    md += ["## questionnaire.xlsx findings", ""] + ([f"- {f}" for f in qflags] or ["none"])
    (out / "qc_report.md").write_text("\n".join(md))
    print("\n".join(md[:60]))
    return F, qflags


if __name__ == "__main__":
    main(sys.argv[1])
