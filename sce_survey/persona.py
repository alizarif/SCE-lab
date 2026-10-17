"""The persona system prompt (the final template), built from one row of participants.xlsx.

Every value uses the exact SCE response wording. Lines marked optional in the template are dropped when the
answer is missing or the question was not asked of that person."""
import math

from .questionnaire import blank, fmt_num

STATES = {"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
          "CT": "Connecticut", "DC": "the District of Columbia", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
          "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
          "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
          "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
          "NC": "North Carolina", "ND": "North Dakota", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
          "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
          "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
          "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
          "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}

INCOME_TEXT = ("Total combined pre-tax income of all members of your household (including you) during the past "
               "12 months (includes money from all jobs, net income from business, farm or rent, pensions, interest "
               "on savings or bonds, dividends, social security income, unemployment benefits, Food Stamps, workers "
               "compensation or disability benefits, child support, alimony, scholarships, fellowships, grants, "
               "inheritances and gifts, and any other money income received by members of your household who are "
               "15 years of age or older)")

# numeracy items: (id, question, correct answer, how the answer is written)
NUMERACY = [
    ("QNUM1", "In a sale, a shop is selling all items at half price. Before the sale, a sofa costs $300. "
              "How much will it cost in the sale?", 150, "${}"),
    ("QNUM2", "Let's say you have $200 in a savings account. The account earns ten per cent interest per year. "
              "Interest accrues at each anniversary of the account. If you never withdraw money or interest "
              "payments, how much will you have in the account at the end of two years?", 242, "${}"),
    ("QNUM3", "In the BIG BUCKS LOTTERY, the chances of winning a $10.00 prize are 1%. What is your best guess "
              "about how many people would win a $10.00 prize if 1,000 people each buy a single ticket from "
              "BIG BUCKS?", 10, "{} people"),
    ("QNUM5", "If the chance of getting a disease is 10 percent, how many people out of 1,000 would be expected "
              "to get the disease?", 100, "{} people"),
    ("QNUM6", "The chance of getting a viral infection is 0.0005. Out of 10,000 people, about how many of them "
              "are expected to get infected?", 5, "{} people"),
    ("QNUM8", "Imagine that the interest rate on your savings account was 1% per year and inflation was 2% per "
              "year. After one year, how much would you be able to buy with the money in this account?", 3, None),
    ("QNUM9", "Please tell me whether this statement is true or false: Buying a single company's stock usually "
              "provides a safer return than a stock mutual fund.", 2, None),
]


def _v(row, k):
    v = row.get(k)
    return None if blank(v) else v


def _i(row, k):
    v = _v(row, k)
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _f(row, k):
    v = _v(row, k)
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _picked(row, base, n):
    out = []
    for i in range(1, n + 1):
        v = _f(row, f"{base}_{i}")
        if v is not None and v > 0:
            out.append(i)
    return out


def current_age(row, survey_date, moves=False):
    """Q32 as the person reported it; with moves=True, plus the whole years since that interview."""
    age = _f(row, "Q32")
    if age is None:
        return None
    if not moves:
        return int(age)
    ym = _i(row, "first_interview")          # YYYYMM of the interview the persona comes from
    if not ym:
        return int(age)
    months = (survey_date.year - ym // 100) * 12 + (survey_date.month - ym % 100)
    return int(age + max(0, months) // 12)


def persona_text(row, survey_date, qn, age_moves=False):
    L = lambda qid, code: qn.option_label(qid, code)  # exact SCE response wording
    out = []

    # who you are
    block = []
    age = current_age(row, survey_date, age_moves)
    if age is not None and 16 <= (_f(row, "Q32") or 0) <= 105:
        block.append(f"You are {age} years old.")
    elif _v(row, "_AGE_CAT"):                       # Q32 missing or impossible (e.g. 0, 720): the SCE's age group
        grp = {"Under 40": "under 40", "40 to 60": "between 40 and 60", "Over 60": "over 60"}.get(str(row["_AGE_CAT"]))
        if grp:
            block.append(f"You are {grp} years old.")
    if L("Q33", _i(row, "Q33")):
        block.append(f"Your gender: {L('Q33', _i(row, 'Q33'))}.")
    if L("Q34", _i(row, "Q34")):
        block.append(f"Hispanic, Latino or Spanish origin: {L('Q34', _i(row, 'Q34'))}.")
    race = [L("Q35", c) for c in _picked(row, "Q35", 6)]
    if race:
        block.append(f"Race (one or more): {', '.join(race)}.")
    out.append("\n".join(block))

    if L("Q36", _i(row, "Q36")):
        out.append("Highest level of school completed, or highest degree received: "
                   f"{L('Q36', _i(row, 'Q36'))}.")

    # work
    block = []
    emp = _picked(row, "Q10", 10)
    if emp:
        block.append(f"Current employment situation: {'; '.join(L('Q10', c) for c in emp)}.")
    jobs = _f(row, "Q11")
    if jobs is not None:
        block.append(f"Number of jobs you have, excluding volunteer and other unpaid work: {fmt_num(jobs)}.")
    main = "main " if (jobs or 0) > 1 else ""
    q12 = _i(row, "Q12new")
    if q12 in (1, 2):
        pre = "Main job means the one at which you usually work the most hours. " if main else ""
        block.append(f"{pre}In your {main}job: {'you work for someone else' if q12 == 1 else 'you are self-employed'}.")
    es1 = _picked(row, "ES1", 4)
    if es1 and q12 == 2:
        block.append(f"Type of self-employment: {'; '.join(L('ES1', c) for c in es1)}.")
    if _f(row, "ES2") is not None and q12 == 2:
        block.append(f"Paid employees in your business, excluding yourself: {fmt_num(_f(row, 'ES2'))}.")
    employed = any(c in (1, 2, 4, 5) for c in emp)          # Q37 is asked only of people with a job
    if L("Q37", _i(row, "Q37")) and employed:
        block.append(f"How long you have been working at your {main}job: {L('Q37', _i(row, 'Q37'))}.")
    q15 = _i(row, "Q15")
    if q15 in (1, 2):
        block.append(f"Currently looking for a job: {L('Q15', q15)}.")
        if q15 == 1 and _f(row, "Q16") is not None:
            block.append(f"I have been unemployed for {fmt_num(_f(row, 'Q16'))} month(s).")
        if q15 == 2 and _f(row, "Q19") is not None:
            block.append(f"I have been out of work for {fmt_num(_f(row, 'Q19'))} month(s).")
    if block:
        out.append("\n".join(block))

    # partner
    block = []
    q38 = _i(row, "Q38")
    if q38 in (1, 2):
        block.append(f"Married or living as a partner with someone: {L('Q38', q38)}.")
    hh2 = _picked(row, "HH2", 11)
    if q38 == 1 and hh2:
        block.append(f"Your spouse/partner's current employment situation: {'; '.join(L('HH2', c) for c in hh2)}.")
    if block:
        out.append("\n".join(block))

    # place
    block = []
    st = _v(row, "_STATE")
    if st:
        block.append(f"State of your primary residence: {STATES.get(str(st).strip().upper(), st)}.")
    cz = _v(row, "cz_name")
    cz_states = [x.strip() for x in str(_v(row, "cz_states") or "").split(",") if x.strip()]
    if cz and (not st or not cz_states or str(st).strip().upper() in cz_states):   # skip the rare zone/state mismatch
        block.append(f"Commuting zone where you live (your local labor market): {cz}.")
    if _f(row, "Q41") is not None:
        block.append(f"Years you have lived at your primary residence: {fmt_num(_f(row, 'Q41'))}.")
    if _f(row, "Q42") is not None:
        block.append(f"Years in total you have lived in the State in which you currently live: {fmt_num(_f(row, 'Q42'))}.")
    if block:
        out.append("\n".join(block))

    # home
    block = []
    q43 = _i(row, "Q43")
    if L("Q43", q43):
        block.append(f"Own or rent your current primary residence: {L('Q43', q43)}.")
    if L("Q43a", _i(row, "Q43a")):
        word = {1: "owned", 2: "rented"}.get(q43, "owned/rented")
        block.append(f"In whose name it is {word}: {L('Q43a', _i(row, 'Q43a'))}.")
    if L("Q44", _i(row, "Q44")):
        block.append(f"Own any other home(s): {L('Q44', _i(row, 'Q44'))}.")
    if block:
        out.append("\n".join(block))

    alone = (_f(row, "Q45new_9") or 0) > 0
    roster_q = qn.by_id.get("Q45new")
    names = dict(roster_q["items"]) if roster_q else {}
    if alone:
        out.append("People who usually live in your primary residence, other than yourself: "
                   f"{names.get(9, 'None of the above, I live alone')}.")
    else:
        who = [f"{names.get(i, i)} ({fmt_num(_f(row, f'Q45new_{i}'))})" for i in range(1, 9)
               if (_f(row, f"Q45new_{i}") or 0) > 0]
        if who:
            out.append(f"People who usually live in your primary residence, other than yourself: {' · '.join(who)}.")

    if L("Q45b", _i(row, "Q45b")):
        out.append(f"Your health: {L('Q45b', _i(row, 'Q45b'))}.")

    q46 = _i(row, "Q46")
    if q46:                                          # shown whenever the person answered it
        out.append("How financial decisions are made in your household, on a scale from 1 (Someone else in my "
                   "household makes all financial decisions) through 3 (I share financial decisions equally with "
                   "someone else in my household) to 5 (I make all financial decisions myself): " f"{q46}.")

    block = []
    if _i(row, "QRA1"):
        block.append("Willingness to take risks regarding financial matters, on a scale from 1 (Not willing at all) "
                     f"to 7 (Very willing): {_i(row, 'QRA1')}.")
    if _i(row, "QRA2"):
        block.append(f"Willingness to take risks in daily activities, same scale: {_i(row, 'QRA2')}.")
    if block:
        out.append("\n".join(block))

    if L("Q47", _i(row, "Q47")):
        out.append(f"{INCOME_TEXT}: {L('Q47', _i(row, 'Q47'))}.")

    # numeracy: the exact questions, the answers given, the score
    # which numeracy questions the person was asked: QNUM1-6 together (a skipped one counts as not correct,
    # as in the SCE's numeracy score); QNUM8 and QNUM9 only from April 2015 on
    first = _i(row, "first_interview") or 0
    asked_16 = any(_f(row, k) is not None for k in ("QNUM1", "QNUM2", "QNUM3", "QNUM5", "QNUM6"))
    asked_89 = first >= 201504 or any(_f(row, k) is not None for k in ("QNUM8", "QNUM9"))
    items, right = [], 0
    for qid, question, correct, fmt in NUMERACY:
        if not (asked_89 if qid in ("QNUM8", "QNUM9") else asked_16):
            continue
        v = _f(row, qid)
        if v is None:
            items.append(f"- {question} Your answer: (no answer)")
            continue
        if fmt:
            ans = fmt.format(fmt_num(v))
            ok = math.isclose(v, correct, abs_tol=1e-6)
        else:
            ans = L(qid, int(v)) or fmt_num(v)
            ok = int(v) == correct
        right += ok
        items.append(f"- {question} Your answer: {ans}")
    if items:
        out.append("You were asked the following questions to see how people use numbers in everyday life and "
                   "gave these answers:\n" + "\n".join(items) +
                   f"\nYour score: {right} of {len(items)} questions correct.")

    return "\n\n".join(x for x in out if x.strip())


def system_prompt(row, survey_date, qn, cfg):
    p = cfg["prompts"]
    fill = lambda s: qn.fill(s, survey_date)
    parts = [fill(p.get("role", "")).strip(), persona_text(row, survey_date, qn, bool(cfg.get("age_moves_with_date"))),
             fill(p.get("after_persona", "")).strip()]
    return "\n\n".join(x for x in parts if x)
