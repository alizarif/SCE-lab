"""The SCE questionnaire: exact wording (questionnaire.xlsx), skip logic, prompts, answer parsing."""
import json
import math
import re
from datetime import date

import pandas as pd

from .config import ROOT

# Direction codes follow the SCE public microdata: inflation items 1 = inflation, 2 = deflation;
# all other signed items 1 = increase, 3 = decrease.
SIGNED_WORDS = {
    "Q8v2": ("inflation", "deflation"), "Q9bv2": ("inflation", "deflation"), "Q1a": ("inflation", "deflation"),
    "Q23v2": ("increased", "decreased"), "Q27v2": ("increased", "decreased"),
    "Q25v2": ("increase", "decrease"), "Q26v2": ("increase", "decrease"),
    "Q31v2": ("increase", "decrease"), "C2": ("increase", "decrease"), "C3": ("increase", "decrease"),
}
DOWN_CODES = {2, 3}
# bin midpoints for a simple mean of the probability bins (<id>_binmean). NOTE: this is NOT the SCE's published
# Q9_mean etc., which the New York Fed computes by fitting a distribution to each respondent's bins.
DENSITY_MIDS = [14, 10, 6, 3, 1, -1, -3, -6, -10, -14]
FMT_KEY = {"choice": "fmt_choice", "signed": "fmt_choice", "multi": "fmt_multi", "percent": "fmt_percent",
           "number": "fmt_number", "density": "fmt_density", "commodities": "fmt_commodities",
           "roster": "fmt_roster", "open": "fmt_simple"}


def blank(v):
    return v is None or (isinstance(v, float) and math.isnan(v)) or str(v).strip().lower() in {"", "nan", "none"}


def truthy(v):
    return str(v).strip().lower() in {"true", "1", "yes", "y", "1.0"}


def fmt_num(v):
    try:
        f = float(v)
    except (TypeError, ValueError):
        return str(v)
    if f.is_integer():
        return str(int(f))
    return f"{round(f, 2):g}"


def _pairs(s):
    if blank(s):
        return []
    out = []
    for part in str(s).split("||"):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            a, b = part.split("=", 1)
            a = a.strip()
            try:
                a = int(float(a))
            except ValueError:
                pass
            out.append((a, b.strip()))
        else:
            out.append(part)
    return out


def _add_months(d, n):
    y, m = d.year, d.month + n
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    return date(y, m, 1)


class Questionnaire:
    def __init__(self, path=None):
        path = ROOT / (path or "questionnaire.xlsx")
        df = pd.read_excel(path, sheet_name="Questions")
        self.all = [self._parse(r) for r in df.to_dict("records")]
        self.by_id = {q["id"]: q for q in self.all}
        self.asked = [q for q in self.all if q["include"]]
        p = pd.read_excel(path, sheet_name="Prompts")
        self.prompts = {str(k): ("" if blank(t) else str(t)) for k, t in zip(p["key"], p["text"])}

    @staticmethod
    def _parse(r):
        raw_bins = _pairs(r.get("bins"))
        return {
            "id": str(r["id"]).strip(),
            "label": "" if blank(r.get("label")) else str(r["label"]).strip(),
            "type": str(r["type"]).strip(),
            "text": "" if blank(r.get("text")) else str(r["text"]),
            "module": str(r.get("module") or ""),
            "asked_of": "all" if blank(r.get("asked_of")) else str(r["asked_of"]).strip(),
            "options": [x for x in _pairs(r.get("options")) if isinstance(x, tuple)],
            "bins": [x if isinstance(x, str) else x[1] for x in raw_bins],
            "items": [x for x in _pairs(r.get("items")) if isinstance(x, tuple)],
            "instruction": "" if blank(r.get("instruction")) else str(r["instruction"]).strip(),
            "follow_of": None if blank(r.get("follow_of")) else str(r["follow_of"]).strip(),
            "show_if": "" if blank(r.get("show_if")) else str(r["show_if"]).strip(),
            "include": truthy(r.get("include")),
        }

    def option_label(self, qid, code):
        q = self.by_id.get(qid)
        if not q:
            return None
        for c, lab in q["options"]:
            if str(c) == str(code):
                return lab
        return None

    # ── placeholders ─────────────────────────────────────────────────
    @staticmethod
    def placeholders(survey_date, answers=None):
        def lab(n):
            return _add_months(survey_date, n).strftime("%B %Y")
        h = {"DATE": survey_date.strftime("%B %d, %Y").replace(" 0", " "), "DATE_ISO": survey_date.isoformat(),
             "H24": lab(24), "H36": lab(36), "H48": lab(48), "H60": lab(60), "LAST_WAVE": lab(-1)}
        answers = answers or {}
        # wording that depends on earlier answers (bracketed text in the FRBNY questionnaire)
        q10 = _codes(answers, "Q10")
        jobs = _num(answers, "Q11")
        many = jobs is not None and jobs > 1
        h["JOB"] = "main" if many else "current"                       # Q12new, Q13new, Q14new
        h["MAIN"] = "main " if many else ""                             # Q22new, Q23v2, Q24
        h["Q11_TEXT"] = ("Altogether, how many jobs do you have (including the job from which you were temporarily "
                         "laid off, but excluding volunteer or other unpaid work)?" if 4 in q10 else
                         "Altogether, how many jobs do you have, excluding volunteer and other unpaid work?")
        es1 = _codes(answers, "ES1")
        h["ES_WORK"] = ("independent contractor job" if 1 in es1 else "business" if 2 in es1 else
                        "family business" if 3 in es1 else "self-employed work")    # ES4, ES5
        for qid, (up, down) in SIGNED_WORDS.items():
            c = _code(answers.get(qid))
            h[f"{qid}_word"] = up if c == 1 else (down if c in DOWN_CODES else "change")
        return h

    @classmethod
    def fill(cls, text, survey_date, answers=None, extra=None):
        h = cls.placeholders(survey_date, answers)
        if extra:
            h.update(extra)
        text = str(text or "")
        for k, v in h.items():
            text = text.replace("{" + k + "}", str(v))
        return text

    # ── one question as the respondent sees it ───────────────────────
    def render(self, q, survey_date, answers):
        text = self.fill(q["text"], survey_date, answers)
        inst = self.prompts.get(f"instruction_{q['instruction']}", "") if q["instruction"] else ""
        parts = [text + (f"\n({inst})" if inst else "")]
        if q["options"]:
            parts.append("\n".join(f"{c}. {lab}" for c, lab in q["options"]))
        if q["bins"]:
            parts.append("\n".join(f"BIN{i}: {lab}" for i, lab in enumerate(q["bins"], 1)))
        if q["type"] == "commodities" and q["items"]:
            parts.append("\n".join(f"{a}: {b}" for a, b in q["items"]))
        if q["type"] == "roster" and q["items"]:
            parts.append("\n".join(f"R{a}: {b}" for a, b in q["items"]))
        parts.append(self.prompts.get(FMT_KEY.get(q["type"], "fmt_simple"), "Reply with ONLY: ANSWER: <your answer>"))
        return "\n\n".join(p for p in parts if p)

    # ── skip logic (routing notes of the FRBNY core questionnaire) ───
    def visible(self, q, respondent_type, answers):
        if q["asked_of"] == "new" and respondent_type != "new":
            return False
        if q["asked_of"] == "repeat" and respondent_type != "repeat":
            return False
        return show_if(q["show_if"], answers)


def _code(v):
    if isinstance(v, dict):
        v = v.get("direction", v.get("value"))
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _codes(answers, qid):
    v = answers.get(qid)
    v = v if isinstance(v, (list, tuple, set)) else ([] if v is None else [v])
    out = []
    for x in v:
        try:
            out.append(int(float(x)))
        except (TypeError, ValueError):
            pass
    return out


def _eq(answers, qid, val):
    v = answers.get(qid)
    if isinstance(v, (list, tuple, set)):
        return int(val) in _codes(answers, qid)
    return _code(v) == int(val)


def _num(answers, qid):
    try:
        v = answers.get(qid)
        return None if v is None else float(v)
    except (TypeError, ValueError):
        return None


def show_if(rule, answers):
    if not rule:
        return True
    q10 = _codes(answers, "Q10")
    employed_like = any(c in (1, 2, 4, 5) for c in q10)
    n_jobs = _num(answers, "Q11")
    self_emp = _eq(answers, "Q12new", 2)
    env = {
        "multiple_jobs": employed_like and (n_jobs or 0) > 1,      # Q12intro
        "employed_like": employed_like,
        "employed_and_jobs": employed_like and (n_jobs or 0) > 0,
        "self_employed_job": employed_like and (n_jobs or 0) > 0 and self_emp,
        "wage_employed": employed_like and (n_jobs or 0) > 0 and not self_emp,
        "wants_work_only": 3 in q10 and 4 not in q10 and 5 not in q10,
        # PDF: [if Q15 = 2 or Q10 includes codes 7, 8, or 9 without any other selections or Q11 = 0]
        "start_looking": _eq(answers, "Q15", 2) or (bool(q10) and set(q10) <= {7, 8, 9})
                         or (employed_like and n_jobs is not None and n_jobs == 0),
    }
    if rule in env:
        return bool(env[rule])
    if "==" in rule:
        left, right = rule.split("==", 1)
        return _eq(answers, left.strip(), int(right.strip()))
    return True


# ── parse a reply ────────────────────────────────────────────────────────
def _first_num(text):
    m = re.search(r"-?\d+(?:\.\d+)?", (text or "").replace(",", ""))
    return float(m.group(0)) if m else None


def _after(tag, text):
    m = re.search(rf"{tag}\s*:\s*(.+)", text or "", re.I)
    return m.group(1).strip() if m else None


def parse_answer(q, raw):
    text = raw or ""
    tagged = _after("ANSWER", text)
    body = tagged if tagged is not None else text
    t = q["type"]
    if t in ("choice", "signed"):
        n = _first_num(body)
        codes = {int(c) for c, _ in q["options"] if str(c).lstrip("-").isdigit()}
        if n is not None and int(n) in codes:
            return int(n)
        low = body.lower()
        for c, lab in sorted(q["options"], key=lambda x: -len(str(x[1]))):
            if str(lab).lower() in low:
                return int(c) if str(c).lstrip("-").isdigit() else c
        return None
    if t == "multi":
        valid = {int(c) for c, _ in q["options"] if str(c).lstrip("-").isdigit()}
        found = []
        for n in map(int, re.findall(r"\d+", body)):
            if n in valid and n not in found:
                found.append(n)
        return found or None
    if t == "percent":
        v = _first_num(body)
        return None if v is None else max(0.0, min(100.0, v))
    if t == "number":
        return _first_num(body)
    if t == "density":
        bins = []
        for i in range(1, 11):
            m = re.search(rf"BIN\s*{i}\s*:\s*(-?\d+(?:\.\d+)?)", text, re.I)
            bins.append(float(m.group(1)) if m else None)
        if all(v is None for v in bins):
            return None
        got = [v for v in bins if v is not None]
        den = sum(got)
        mean = (sum((v or 0) * mid for v, mid in zip(bins, DENSITY_MIDS)) / den) if den else None
        return {"bins": bins, "sum": round(den, 4), "mean": None if mean is None else round(mean, 4)}
    if t == "commodities":
        out = {}
        for iid, _ in q["items"]:
            m = re.search(rf"{re.escape(str(iid))}\s*:\s*(-?\d+(?:\.\d+)?)", text, re.I)
            out[str(iid)] = float(m.group(1)) if m else None
        return out if any(v is not None for v in out.values()) else None
    return body.strip() or None


def problem(q, parsed):
    """The SCE web form's checks → (prompt key, extra placeholders) for one more try, or None."""
    t = q["type"]
    if parsed is None:
        return ("error_E9" if t == "commodities" else "error_E1"), {}
    if t == "density" and parsed.get("sum") is not None and abs(parsed["sum"] - 100) > 0.5:
        return "density_reask", {"SUM": f"{parsed['sum']:g}"}
    if q["id"] == "Q10" and 3 in parsed and (1 in parsed or 2 in parsed):
        return "error_E8", {}
    return None


def answer_value(q, parsed, answers):
    """One number per question for statistics (microdata convention): codes for choices, the signed rate for
    part-2 questions (deflation / decrease negative), the mean for probability bins."""
    if parsed is None:
        return None
    t = q["type"]
    if t == "density":
        return parsed.get("mean")
    if t in ("choice", "signed"):
        return _code(parsed)
    if t in ("percent", "number"):
        v = float(parsed)
        if q["follow_of"]:
            c = _code(answers.get(q["follow_of"]))
            v = -abs(v) if c in DOWN_CODES else abs(v)
        return v
    return None


def answer_text(qn, q, parsed):
    """Readable answer, e.g. '3 = About the same', '3%', 'bins 0,5,10,...'."""
    if parsed is None:
        return ""
    t = q["type"]
    if t in ("choice", "signed"):
        lab = qn.option_label(q["id"], parsed)
        return f"{parsed} = {lab}" if lab else str(parsed)
    if t == "multi":
        return "; ".join(f"{c} = {qn.option_label(q['id'], c) or c}" for c in parsed)
    if t == "density":
        return "bins " + ", ".join("-" if v is None else fmt_num(v) for v in parsed["bins"]) + \
               (f" (sum {fmt_num(parsed['sum'])})" if parsed.get("sum") is not None else "")
    if t == "commodities":
        return "; ".join(f"{k}: {fmt_num(v)}" for k, v in parsed.items() if v is not None)
    if t == "percent" or (t == "number" and q["follow_of"]):
        return f"{fmt_num(parsed)}%"
    return fmt_num(parsed) if isinstance(parsed, (int, float)) else str(parsed)


def to_json(v):
    return "" if v is None else json.dumps(v, ensure_ascii=False)
