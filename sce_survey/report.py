"""Statistics and trend charts.

reports/stats_daily.csv     date × arm × item: n, mean, sd, median, min, max, p25, p75
reports/stats_monthly.csv   month × arm × item: the same
reports/wide/YYYY-MM.csv    one row per interview, one column per item (like the SCE microdata)
reports/charts/*.png        trend of median, mean, mean ± sd and min–max, one panel per arm
reports/README.md           progress, cost, latest-month table and the charts (GitHub shows it on the repo page)
"""
import json
from datetime import datetime

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt   # noqa: E402
import numpy as np                # noqa: E402
import pandas as pd               # noqa: E402

from .config import REPORTS, log  # noqa: E402
from .questionnaire import Questionnaire   # noqa: E402
from .store import ledger, responses       # noqa: E402

INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e0", "#fcfcfb"
BLUE, BLUE_BAND, BLUE_RANGE = "#1c5cab", "#b7d3f6", "#86b6ef"


def long_values(df):
    """One numeric value per (interview, item). Density → <id>_binmean and <id>_bin1..10; C4 → C4_1..6."""
    keep = ["interview_id", "date", "wave", "arm", "userid"]
    base = df[df["value"].notna() & (df["type"] != "density")][keep + ["question_id", "value"]]
    base = base.rename(columns={"question_id": "item"})
    extra = []
    for r in df[df["type"].isin(["density", "commodities"]) & df["answer_json"].notna()].itertuples():
        try:
            a = json.loads(r.answer_json)
        except (TypeError, ValueError):
            continue
        k = {c: getattr(r, c) for c in keep}
        if r.type == "density":
            if a.get("mean") is not None:
                extra.append({**k, "item": f"{r.question_id}_binmean", "value": a["mean"]})
            for i, b in enumerate(a.get("bins") or [], 1):
                if b is not None:
                    extra.append({**k, "item": f"{r.question_id}_bin{i}", "value": b})
        else:
            extra += [{**k, "item": iid, "value": v} for iid, v in a.items() if v is not None]
    out = pd.concat([base, pd.DataFrame(extra)], ignore_index=True) if extra else base
    out["value"] = pd.to_numeric(out["value"], errors="coerce")
    return out.dropna(subset=["value"])


def summarize(lv, by):
    g = lv.groupby(by + ["item"])["value"]
    s = g.agg(n="count", mean="mean", sd="std", median="median", min="min", max="max",
              p25=lambda x: x.quantile(.25), p75=lambda x: x.quantile(.75)).reset_index()
    return s.round(4)


def item_labels(qn):
    lab = {q["id"]: q["label"] for q in qn.all}
    out = dict(lab)
    for q in qn.all:
        if q["type"] == "density":
            out[f"{q['id']}_binmean"] = f"{q['label']}: mean using bin midpoints"
    return out


def chart(stats, item, xcol, title, path, arms):
    d = stats[stats["item"] == item]
    if d.empty:
        return False
    n = len(arms)
    cols = 2 if n > 1 else 1
    rows = int(np.ceil(n / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(5.2 * cols, 3.1 * rows), sharey=True, squeeze=False)
    fig.patch.set_facecolor(SURF)
    xs_all = sorted(d[xcol].astype(str).unique())
    pos = {x: i for i, x in enumerate(xs_all)}
    for ax, arm in zip(axes.flat, arms):
        a = d[d["arm"] == arm].sort_values(xcol)
        ax.set_facecolor(SURF)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        for s in ("left", "bottom"):
            ax.spines[s].set_color(GRID)
        ax.grid(axis="y", color=GRID, lw=.6)
        ax.tick_params(colors=INK2, labelsize=8)
        ax.set_title(arm, fontsize=9.5, color=INK, loc="left", fontweight="bold")
        if a.empty:
            ax.text(.5, .5, "no data yet", ha="center", va="center", transform=ax.transAxes, color=INK2, fontsize=9)
            continue
        x = [pos[v] for v in a[xcol].astype(str)]
        sd = a["sd"].fillna(0)
        ax.fill_between(x, a["mean"] - sd, a["mean"] + sd, color=BLUE_BAND, alpha=.55, lw=0, label="mean ± SD")
        ax.plot(x, a["min"], color=BLUE_RANGE, lw=1, ls=":", label="min / max")
        ax.plot(x, a["max"], color=BLUE_RANGE, lw=1, ls=":")
        ax.plot(x, a["mean"], color=BLUE, lw=1.5, ls="--", label="mean")
        ax.plot(x, a["median"], color=BLUE, lw=2, marker="o", ms=4, label="median")
        last = a.iloc[-1]
        ax.annotate(f"median {last['median']:g}", (x[-1], last["median"]), xytext=(4, 4),
                    textcoords="offset points", fontsize=7.5, color=INK2)
        step = max(1, len(xs_all) // 6)
        ax.set_xticks(range(0, len(xs_all), step))
        ax.set_xticklabels([xs_all[i][5:] if xcol == "date" else xs_all[i] for i in range(0, len(xs_all), step)])
        ax.set_xlim(-.5, len(xs_all) - .5)
    for ax in list(axes.flat)[n:]:
        ax.set_visible(False)
    h, l = axes.flat[0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper right", ncol=4, fontsize=8, frameon=False, labelcolor=INK2)
    fig.suptitle(title, x=.01, ha="left", fontsize=11, color=INK)
    fig.tight_layout(rect=(0, 0, 1, .93))
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=130, facecolor=SURF)
    plt.close(fig)
    return True


ARM_COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]


def compare_chart(stats, item, xcol, title, path, arms):
    """Medians of all arms on one axis (fixed colour per arm, legend + end labels)."""
    d = stats[stats["item"] == item]
    if d.empty:
        return False
    xs_all = sorted(d[xcol].astype(str).unique())
    pos = {x: i for i, x in enumerate(xs_all)}
    fig, ax = plt.subplots(figsize=(8.5, 3.6))
    fig.patch.set_facecolor(SURF)
    ax.set_facecolor(SURF)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.grid(axis="y", color=GRID, lw=.6)
    ax.tick_params(colors=INK2, labelsize=8)
    for i, arm in enumerate(arms):
        a = d[d["arm"] == arm].sort_values(xcol)
        if a.empty:
            continue
        x = [pos[v] for v in a[xcol].astype(str)]
        col = ARM_COLORS[i % len(ARM_COLORS)]
        ax.plot(x, a["median"], color=col, lw=2, marker="o", ms=4, label=arm)
        ax.annotate(arm, (x[-1], a["median"].iloc[-1]), xytext=(5, 0), textcoords="offset points",
                    fontsize=7.5, color=INK2, va="center")
    step = max(1, len(xs_all) // 8)
    ax.set_xticks(range(0, len(xs_all), step))
    ax.set_xticklabels([xs_all[i][5:] if xcol == "date" else xs_all[i] for i in range(0, len(xs_all), step)])
    ax.set_xlim(-.5, len(xs_all) - .5 + max(1, len(xs_all) * .15))
    ax.legend(fontsize=8, frameon=False, labelcolor=INK2, loc="upper left", ncol=min(4, len(arms)))
    ax.set_title(title, loc="left", fontsize=10.5, color=INK)
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=130, facecolor=SURF)
    plt.close(fig)
    return True


def _md_table(df):
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in df.itertuples(index=False):
        out.append("| " + " | ".join("" if pd.isna(v) else (f"{v:g}" if isinstance(v, float) else str(v)) for v in r) + " |")
    return "\n".join(out)


def make_report(cfg):
    REPORTS.mkdir(parents=True, exist_ok=True)
    qn = Questionnaire(cfg.get("questionnaire_file"))
    labels = item_labels(qn)
    df = responses()
    lg = ledger()
    arms = [a["id"] for a in cfg["arms"]]
    if df.empty:
        (REPORTS / "README.md").write_text("# SCE monthly survey · report\n\nNo interviews yet.\n")
        log.info("report: no data yet")
        return
    lv = long_values(df)
    daily = summarize(lv, ["date", "arm"])
    monthly = summarize(lv, ["wave", "arm"])
    for s in (daily, monthly):
        s.insert(s.columns.get_loc("item") + 1, "label", s["item"].map(labels).fillna(""))
    daily.to_csv(REPORTS / "stats_daily.csv", index=False)
    monthly.to_csv(REPORTS / "stats_monthly.csv", index=False)

    wide_dir = REPORTS / "wide"
    wide_dir.mkdir(exist_ok=True)
    for w, g in lv.groupby("wave"):
        wide = g.pivot_table(index=["interview_id", "date", "wave", "arm", "userid"], columns="item",
                             values="value", aggfunc="first").reset_index()
        wide.to_csv(wide_dir / f"{w}.csv", index=False)

    waves = sorted(lv["wave"].unique())
    charts = cfg["report"].get("charts") or []
    made = []
    for item in charts:
        title = f"{item} · {labels.get(item, '')}"
        ok_m = chart(monthly, item, "wave", title + " · by month", REPORTS / "charts" / f"monthly_{item}.png", arms) \
            if len(waves) > 1 else False
        ok_d = chart(daily, item, "date", title + " · by day", REPORTS / "charts" / f"daily_{item}.png", arms)
        st, xc = (monthly, "wave") if len(waves) > 1 else (daily, "date")
        compare_chart(st, item, xc, title + " · median by arm", REPORTS / "charts" / f"compare_{item}.png", arms)
        if ok_m or ok_d:
            made.append((item, ok_m, ok_d))

    # README
    cur = waves[-1]
    lines = [f"# SCE monthly survey · report", "",
             f"Updated {datetime.now():%Y-%m-%d %H:%M} · model `{cfg['model']}` · arms: " +
             ", ".join(f"`{a['id']}` (web {'on' if a['web'] else 'off'}, memory {'on' if a['memory'] else 'off'})"
                       for a in cfg["arms"]), ""]
    if not lg.empty:
        prog = lg[lg["status"] == "complete"].groupby(["wave", "arm"]).agg(
            interviews=("interview_id", "count"), people=("userid", "nunique"), days=("run_date", "nunique"),
            question_errors=("n_errors", "sum"), reasks=("n_reasks", "sum"), cost_usd=("cost_usd", "sum")).reset_index()
        prog["cost_usd"] = prog["cost_usd"].round(2)
        lines += ["## Progress", "", _md_table(prog), "",
                  f"Total cost so far: **${lg['cost_usd'].sum():.2f}**", ""]
    head = monthly[(monthly["wave"] == cur) & monthly["item"].isin(charts)].copy()
    if not head.empty:
        head["item"] = pd.Categorical(head["item"], charts, ordered=True)
        head = head.sort_values(["item", "arm"])
        head = head[["item", "label", "arm", "n", "median", "mean", "sd", "min", "max"]]
        for c in ("median", "mean", "sd", "min", "max"):
            head[c] = head[c].round(2)
        lines += [f"## {cur}: headline items", "", _md_table(head), "",
                  "All items, by day and by month: [stats_daily.csv](stats_daily.csv) · "
                  "[stats_monthly.csv](stats_monthly.csv) · one row per interview: [wide/](wide/)", ""]
    lines += ["## Trends", "", "Solid line = median · dashed = mean · band = mean ± SD · dotted = min and max.", ""]
    for item, ok_m, ok_d in made:
        lines.append(f"### {item} · {labels.get(item, '')}")
        lines.append(f"![{item}: median by arm](charts/compare_{item}.png)")
        if ok_m:
            lines.append(f"![{item} by month](charts/monthly_{item}.png)")
        if ok_d:
            lines.append(f"![{item} by day](charts/daily_{item}.png)")
        lines.append("")
    (REPORTS / "README.md").write_text("\n".join(lines))
    log.info("report: %d interviews, %d items, %d charts → " + REPORTS.name + "/", df["interview_id"].nunique(),
             lv["item"].nunique(), sum(a + b for _, a, b in made))
