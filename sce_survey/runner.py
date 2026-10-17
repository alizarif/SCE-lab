"""The daily job: interview everyone scheduled for today (and anyone from earlier this month not done yet)."""
import asyncio
import time
from collections import Counter

import pandas as pd

from .config import ROOT, log, setup_logging
from .interview import run_interview
from .llm import LLM, Fatal
from .questionnaire import Questionnaire
from .schedule import month_plan, today, wave_of
from .store import answer_history, done_keys, ledger, save_interview, thread_history


def load_participants(cfg):
    p = pd.read_excel(ROOT / cfg.get("participants_file", "participants.xlsx"), sheet_name=0)
    p = p[p["userid"].notna()].copy()
    p["userid"] = p["userid"].astype(int)
    p = p.drop_duplicates("userid")
    if cfg.get("max_participants"):
        p = p.head(int(cfg["max_participants"]))
    return {int(r["userid"]): r for r in p.to_dict("records")}


def due_today(cfg, people, run_date, arms=None):
    plan = month_plan(cfg, list(people), run_date.year, run_date.month)
    wave = wave_of(run_date)
    done = done_keys()
    arms = arms or cfg["arms"]
    todo = [(d, a["id"], u) for u, d in plan.items() if d <= run_date for a in arms if (u, a["id"], wave) not in done]
    return sorted(todo), plan


def run_daily(cfg, run_date=None, dry_run=False, limit=None, arm_ids=None):
    run_date = run_date or today(cfg)
    setup_logging(run_date)
    log.info("=== SCE monthly survey · run date %s · model %s%s ===", run_date, cfg["model"], " · DRY RUN" if dry_run else "")
    if not cfg.get("enabled", True):
        log.info("enabled: false in config.yaml → nothing to do")
        return 0
    if cfg.get("start_date") and run_date < cfg["start_date"]:
        log.info("start_date %s is later than today → nothing to do", cfg["start_date"])
        return 0
    if cfg.get("end_date") and run_date > cfg["end_date"]:
        log.info("end_date %s has passed → the survey is finished (set a later end_date to continue)", cfg["end_date"])
        return 0
    people = load_participants(cfg)
    arms = [a for a in cfg["arms"] if not arm_ids or a["id"] in arm_ids]
    todo, plan = due_today(cfg, people, run_date, arms)
    wave = wave_of(run_date)
    n_today = sum(1 for d in plan.values() if d == run_date)
    late = sum(1 for d, _, _ in todo if d < run_date)
    log.info("wave %s · %d participants · %d scheduled today · %d arms · %d interviews to do (%d left over from earlier days)",
             wave, len(people), n_today, len(arms), len(todo), late)
    if limit:
        todo = todo[: int(limit)]
        log.info("--limit %s: running only %d interviews", limit, len(todo))
    if not todo:
        return 0

    # who has been interviewed before (per arm) → new / repeat respondent; and the memory each arm gets
    lg = ledger()
    lg = lg[(lg["status"] == "complete") & (lg["wave"] < wave)]
    seen_before = {(int(u), str(a)) for u, a in zip(lg["userid"], lg["arm"])}
    mem_arms = [a["id"] for a in arms if a["memory"]]
    mem = {}
    if mem_arms:
        if cfg["memory"].get("mode", "summary") == "thread":
            mem = thread_history(mem_arms, wave, int(cfg["memory"].get("thread_months", 1)))
        else:
            mem = answer_history(mem_arms, wave, int(cfg["memory"].get("months", 12)))
        log.info("memory loaded for %d person-arm pairs (%s mode)", len(mem), cfg["memory"].get("mode", "summary"))

    qn = Questionnaire(cfg.get("questionnaire_file"))
    arm_by = {a["id"]: a for a in arms}
    rtype = cfg.get("respondent_type", "auto")

    async def main():
        llm = LLM(cfg, dry_run=dry_run)
        ctx = {"cfg": cfg, "qn": qn, "llm": llm}
        sem = asyncio.Semaphore(int(cfg.get("concurrency", 8)))
        t0 = time.monotonic()
        budget = float(cfg.get("time_budget_minutes", 300)) * 60
        stats = Counter()
        fatal = []

        async def one(sched, arm_id, uid):
            async with sem:
                if fatal or time.monotonic() - t0 > budget:
                    stats["postponed"] += 1
                    return
                arm = arm_by[arm_id]
                rt = rtype if rtype in ("new", "repeat") else ("repeat" if (uid, arm_id) in seen_before else "new")
                try:
                    led, rows, rec = await run_interview(ctx, people[uid], arm, sched, run_date, rt,
                                                         mem.get((uid, arm_id)) if arm["memory"] else None)
                except Fatal as e:
                    fatal.append(str(e))
                    return
                except Exception as e:                  # one broken interview must not stop the day
                    log.exception("interview %s %s failed: %s", arm_id, uid, e)
                    stats["failed"] += 1
                    return
                save_interview(run_date, arm_id, led, rows, rec)
                stats["done"] += 1
                stats["cost"] += led["cost_usd"] or 0
                stats["errors"] += led["n_errors"]
                if stats["done"] % 25 == 0:
                    log.info("… %d / %d interviews done · $%.2f so far", stats["done"], len(todo), stats["cost"])

        try:
            await asyncio.gather(*(one(*t) for t in todo))
        finally:
            await llm.close()
        if stats["done"]:
            (ROOT / ".did_work").write_text(str(stats["done"]))    # tells the GitHub job to update the report
        if fatal:
            log.error("STOPPED: %s", fatal[0])
        log.info("finished: %d interviews done, %d failed, %d postponed to the next run · %d question errors · "
                 "cost $%.4f · %.1f min", stats["done"], stats["failed"], stats["postponed"], stats["errors"],
                 stats["cost"], (time.monotonic() - t0) / 60)
        return 1 if fatal else 0

    return asyncio.run(main())
