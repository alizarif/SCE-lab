"""Who is interviewed on which day.

Each month, every participant is interviewed once (in every arm). All participants are spread evenly over the
survey days of that month: from the start date (or the 1st) to the last day of the month (or the end date). In the
first month that is the days left; in later months it is every day of the month.

The order is drawn at random again every month (from the seed and the month), so a person interviewed on the 5th
this month can be interviewed on any day next month. With N people and D days, each day gets N/D people (±1).
"""
import calendar
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import numpy as np


def today(cfg):
    return datetime.now(ZoneInfo(cfg.get("timezone") or "UTC")).date()


def survey_days(cfg, year, month):
    first = date(year, month, 1)
    last = date(year, month, calendar.monthrange(year, month)[1])
    lo = max(first, cfg["start_date"]) if cfg.get("start_date") else first
    hi = min(last, cfg["end_date"]) if cfg.get("end_date") else last
    if hi < lo:
        return []
    return [lo + timedelta(days=i) for i in range((hi - lo).days + 1)]


def month_plan(cfg, userids, year, month):
    """{userid: interview date} for one month: a new random order each month, split evenly over its survey days."""
    days = survey_days(cfg, year, month)
    if not days:
        return {}
    ids = sorted(int(u) for u in userids)
    rng = np.random.default_rng([int(cfg.get("seed", 0)), year, month])     # same seed + month = same plan
    order = rng.permutation(len(ids))
    n, d = len(ids), len(days)
    return {ids[k]: days[(rank * d) // n] for k, rank in enumerate(order)}


def wave_of(d):
    return f"{d.year:04d}-{d.month:02d}"


def months_between(a, b):
    out, y, m = [], a.year, a.month
    while (y, m) <= (b.year, b.month):
        out.append((y, m))
        m += 1
        if m > 12:
            y, m = y + 1, 1
    return out
