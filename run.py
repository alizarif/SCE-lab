"""SCE monthly survey: command line.

    python run.py daily                      interview everyone due today (what GitHub runs every day)
    python run.py daily --dry-run --limit 8  offline test: fake answers, no API calls, no cost
                                             (written to data_dry_run/, never mixed with real data)
    python run.py daily --limit 4            a small real pilot (4 interviews)
    python run.py daily --date 2026-10-20    run as if today were that date
    python run.py report                     statistics, trend charts, reports/README.md
    python run.py schedule [--month 2026-11] how many people are interviewed on each day
    python run.py status                     progress of the current month, cost so far
    python run.py persona 70109867           print the full system prompt of one participant
"""
import argparse
import os
import sys
from collections import Counter
from datetime import date

if "--dry-run" in sys.argv:                 # must be set before sce_survey is imported
    os.environ["SCE_DRY_RUN"] = "1"

from sce_survey.config import load_config   # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["daily", "report", "schedule", "status", "persona"])
    ap.add_argument("arg", nargs="?", help="userid for 'persona'")
    ap.add_argument("--date", help="YYYY-MM-DD (default: today in the configured time zone)")
    ap.add_argument("--month", help="YYYY-MM for 'schedule'")
    ap.add_argument("--dry-run", action="store_true", help="fake answers, no API calls (data_dry_run/, reports_dry_run/)")
    ap.add_argument("--limit", type=int, help="run at most this many interviews")
    ap.add_argument("--arms", help="comma-separated arm ids to run (default: all)")
    a = ap.parse_args()
    cfg = load_config()
    d = date.fromisoformat(a.date) if a.date else None

    if a.command == "daily":
        from sce_survey.runner import run_daily
        sys.exit(run_daily(cfg, d, dry_run=a.dry_run, limit=a.limit,
                           arm_ids=a.arms.split(",") if a.arms else None))

    if a.command == "report":
        from sce_survey.config import setup_logging
        from sce_survey.report import make_report
        from sce_survey.schedule import today
        setup_logging(d or today(cfg), to_file=False)
        make_report(cfg)
        return

    from sce_survey.runner import load_participants
    from sce_survey.schedule import month_plan, today
    d = d or today(cfg)

    if a.command == "schedule":
        y, m = map(int, (a.month or f"{d:%Y-%m}").split("-"))
        plan = month_plan(cfg, list(load_participants(cfg)), y, m)
        c = Counter(plan.values())
        print(f"{y}-{m:02d}: {len(plan)} people × {len(cfg['arms'])} arms, over {len(c)} days")
        for day in sorted(c):
            print(f"  {day}  {c[day]:4d} people  ({c[day] * len(cfg['arms'])} interviews)")
        return

    if a.command == "status":
        from sce_survey.store import ledger
        people = load_participants(cfg)
        plan = month_plan(cfg, list(people), d.year, d.month)
        lg = ledger()
        wave = f"{d:%Y-%m}"
        cur = lg[(lg["wave"] == wave) & (lg["status"] == "complete")]
        due = sum(1 for x in plan.values() if x <= d)
        print(f"{wave} · today {d} · enabled={cfg.get('enabled', True)}")
        for arm in cfg["arms"]:
            n = (cur["arm"] == arm["id"]).sum()
            print(f"  {arm['id']:<20} done {n:5d} · due by today {due:5d} · month total {len(plan):5d}")
        print(f"cost this month ${cur['cost_usd'].sum():.2f} · all months ${lg['cost_usd'].sum():.2f} "
              f"· interviews so far {len(lg)}")
        return

    if a.command == "persona":
        from sce_survey.persona import system_prompt
        from sce_survey.questionnaire import Questionnaire
        people = load_participants(cfg)
        uid = int(a.arg) if a.arg else next(iter(people))
        print(system_prompt(people[uid], d, Questionnaire(cfg.get("questionnaire_file")), cfg))


if __name__ == "__main__":
    main()
