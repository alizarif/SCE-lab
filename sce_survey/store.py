"""Where everything is saved.

data/interviews.csv                              one row per finished interview (ledger: who, when, arm, cost, errors)
data/responses/YYYY-MM/YYYY-MM-DD_<arm>.csv      one row per question answered (answer, raw reply, tokens, cost, ...)
data/logs/YYYY-MM/YYYY-MM-DD_<arm>.jsonl.gz      everything: system prompt, every message, every raw API response,
                                                 web-search results, re-asks, errors (one JSON object per interview)
data/runlog/YYYY-MM/YYYY-MM-DD.log               what the daily job did
"""
import csv
import gzip
import json
from collections import defaultdict
from pathlib import Path

import pandas as pd

from .config import DATA, LEDGER

RESP_COLS = ["interview_id", "date", "wave", "arm", "web", "memory", "userid", "respondent_type", "order",
             "question_id", "label", "type", "module", "value", "answer_text", "answer_json", "raw_response",
             "reasked", "reask_reason", "first_response", "prompt_tokens", "completion_tokens", "reasoning_tokens", "cost_usd",
             "latency_s", "attempts", "model", "provider", "error"]
LEDGER_COLS = ["interview_id", "userid", "arm", "web", "memory", "wave", "scheduled_date", "run_date",
               "started_utc", "finished_utc", "respondent_type", "status", "n_questions", "n_answered",
               "n_errors", "n_reasks", "n_calls", "prompt_tokens", "completion_tokens", "cost_usd",
               "web_results", "memory_waves", "model", "temperature"]


def _append_csv(path, rows, cols):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        if new:
            w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in cols})


def resp_path(d, arm):
    return DATA / "responses" / f"{d:%Y-%m}" / f"{d:%Y-%m-%d}_{arm}.csv"


def log_path(d, arm):
    return DATA / "logs" / f"{d:%Y-%m}" / f"{d:%Y-%m-%d}_{arm}.jsonl.gz"


def save_interview(run_date, arm, ledger_row, response_rows, log_record):
    """Called once per finished interview, so an interrupted run loses at most the interviews in progress."""
    _append_csv(resp_path(run_date, arm), response_rows, RESP_COLS)
    p = log_path(run_date, arm)
    p.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(p, "at", encoding="utf-8") as f:          # appends a gzip member; readers see one stream
        f.write(json.dumps(log_record, ensure_ascii=False, default=str) + "\n")
    _append_csv(LEDGER, [ledger_row], LEDGER_COLS)


def ledger():
    if not LEDGER.exists():
        return pd.DataFrame(columns=LEDGER_COLS)
    return pd.read_csv(LEDGER, dtype={"wave": str, "arm": str})


def done_keys():
    lg = ledger()
    lg = lg[lg["status"] == "complete"]
    return {(int(u), str(a), str(w)) for u, a, w in zip(lg["userid"], lg["arm"], lg["wave"])}


def responses(waves=None, arms=None):
    files = sorted((DATA / "responses").glob("*/*.csv"))
    if waves is not None:
        files = [f for f in files if f.parent.name in set(waves)]
    frames = []
    for f in files:
        arm = f.stem.split("_", 1)[1]
        if arms is not None and arm not in set(arms):
            continue
        frames.append(pd.read_csv(f, dtype={"wave": str, "arm": str}, low_memory=False))
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=RESP_COLS)


def answer_history(arms, before_wave, months):
    """{(userid, arm): [(wave, date, [(label, qid, answer_text), ...]), ...]} oldest first, for summary memory."""
    df = responses(arms=arms)
    if df.empty:
        return {}
    df = df[(df["wave"] < before_wave) & df["answer_text"].notna() & (df["answer_text"].astype(str) != "")]
    out = defaultdict(list)
    for (u, a, w), g in df.sort_values(["wave", "order"]).groupby(["userid", "arm", "wave"], sort=True):
        out[(int(u), str(a))].append((w, str(g["date"].iloc[0]),
                                      list(zip(g["label"].astype(str), g["question_id"], g["answer_text"].astype(str)))))
    return {k: v[-months:] for k, v in out.items()}


def thread_history(arms, before_wave, months):
    """{(userid, arm): [(wave, messages-without-system), ...]} from the logs, for thread memory."""
    out = defaultdict(list)
    for p in sorted((DATA / "logs").glob("*/*.jsonl.gz")):
        arm = p.name[len("YYYY-MM-DD_"):-len(".jsonl.gz")]
        if arm not in set(arms) or p.parent.name >= before_wave:
            continue
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                if rec.get("status") != "complete":
                    continue
                msgs = [m for m in rec.get("messages", []) if m.get("role") != "system"]
                out[(int(rec["userid"]), arm)].append((rec["wave"], msgs))
    return {k: sorted(v)[-months:] for k, v in out.items()}
