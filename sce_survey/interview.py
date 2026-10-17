"""One interview: one persona, one arm, one conversation, the whole monthly questionnaire."""
import json
from datetime import datetime, timezone

from .persona import system_prompt
from .questionnaire import answer_text, answer_value, parse_answer, problem, to_json


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _usage(res):
    data = res.get("response") or {}
    u = data.get("usage") or {}
    det = u.get("completion_tokens_details") or {}
    return {"prompt_tokens": u.get("prompt_tokens"), "completion_tokens": u.get("completion_tokens"),
            "reasoning_tokens": det.get("reasoning_tokens"), "cost_usd": u.get("cost"),
            "provider": data.get("provider"), "model_used": data.get("model")}


def _annotations(res):
    data = res.get("response") or {}
    try:
        anns = data["choices"][0]["message"].get("annotations") or []
    except (KeyError, IndexError, TypeError):
        return []
    out = []
    for a in anns:
        c = a.get("url_citation") or a
        if c.get("url"):
            out.append({"url": c.get("url"), "title": c.get("title") or "", "content": c.get("content") or ""})
    seen, uniq = set(), []
    for a in out:
        if a["url"] not in seen:
            seen.add(a["url"])
            uniq.append(a)
    return uniq


def memory_block(cfg, history):
    lines = [cfg["prompts"].get("memory_header", "Your answers in earlier months:")]
    for wave, d, items in history:
        y, m = map(int, wave.split("-"))
        month = datetime(y, m, 1).strftime("%B %Y")
        lines.append(f"\n{month} (interviewed {d}):")
        lines += [f"- {label}: {ans}" for label, _qid, ans in items]
    return "\n".join(lines)


async def run_interview(ctx, row, arm, scheduled, run_date, respondent_type, memory=None):
    """→ (ledger_row, response_rows, log_record). memory = summary history list or thread history list."""
    cfg, qn, llm = ctx["cfg"], ctx["qn"], ctx["llm"]
    userid = int(row["userid"])
    wave = f"{run_date:%Y-%m}"
    iid = f"{wave}_{arm['id']}_{userid}"
    started = _now()
    sys = system_prompt(row, run_date, qn, cfg)
    messages = [{"role": "system", "content": sys}]
    calls, rows, answers = [], [], {}
    lead = []                       # text that goes in front of the first question
    mem_mode = cfg["memory"].get("mode", "summary")
    memory_waves = []
    if arm["memory"] and memory:
        memory_waves = [m[0] for m in memory]
        if mem_mode == "thread":
            for _wave, msgs in memory:
                messages += msgs
            lead.append(qn.fill(cfg["prompts"].get("thread_bridge", ""), run_date))
        else:
            lead.append(memory_block(cfg, memory))

    async def call(qid, web=False):
        res = await llm.chat(list(messages), web=web)
        u = _usage(res)
        calls.append({"n": len(calls) + 1, "question_id": qid, "web": web, "user": messages[-1]["content"],
                      "reply": res["content"], "error": res["error"], "latency_s": res["latency_s"],
                      "attempts": res["attempts"], "request_params": res.get("request"), "response": res["response"]})
        return res, u

    # web search: once, before the survey starts
    w = cfg["web"]
    web_results, web_cost = [], 0.0
    if arm["web"] and w.get("scope", "interview") == "interview":
        # only the news request goes in this turn (the search engine reads it as the query);
        # memory, if any, comes with the first question
        opening = qn.fill(w.get("prompt", "Latest U.S. economy news as of {DATE}."), run_date).strip()
        if arm["memory"] and memory and mem_mode == "thread":      # "one month later" comes before this month's news
            opening = "\n\n".join(lead + [opening])
            lead = []
        messages.append({"role": "user", "content": opening})
        res, u = await call("WEB", web=True)
        web_cost += u["cost_usd"] or 0
        web_results = _annotations(res)
        if w.get("keep_results_in_conversation", True) and any(r["content"] for r in web_results):
            n = int(w.get("result_chars", 1000))
            pasted = "\n\n".join(f"[{i}] {r['title']} ({r['url']})\n{r['content'][:n].strip()}"
                                 for i, r in enumerate(web_results, 1))
            messages[-1]["content"] = opening + "\n\nWhat the search found:\n\n" + pasted
        messages.append({"role": "assistant", "content": res["content"] or "(no search results)"})

    intros = []
    order = 0
    for q in qn.asked:
        if not qn.visible(q, respondent_type, answers):
            continue
        if q["type"] in ("intro", "info"):
            intros.append(qn.fill(q["text"], run_date, answers))
            continue
        order += 1
        user = "\n\n".join(lead + intros + [qn.render(q, run_date, answers)])
        lead, intros = [], []
        messages.append({"role": "user", "content": user})
        res, u = await call(q["id"], web=arm["web"] and w.get("scope") == "question")
        raw = res["content"]
        parsed = parse_answer(q, raw) if raw else None
        first = None
        cost = u["cost_usd"] or 0
        ptok, ctok, rtok = u["prompt_tokens"] or 0, u["completion_tokens"] or 0, u["reasoning_tokens"] or 0
        if raw:
            messages.append({"role": "assistant", "content": raw})
        prob = problem(q, parsed) if raw else None      # an API failure is not re-asked
        if prob and prob[0] == "density_reask" and not cfg.get("density_reask", True):
            prob = None
        if prob and cfg.get("reask", True):
            # the SCE web form does not move on: show its message and ask once more
            first = raw
            key, extra = prob
            messages.append({"role": "user", "content": qn.fill(qn.prompts.get(key, ""), run_date, extra=extra)})
            res2, u2 = await call(q["id"] + ":" + key)
            if res2["content"]:
                raw, parsed = res2["content"], parse_answer(q, res2["content"])
                messages.append({"role": "assistant", "content": raw})
            else:
                messages.pop()
            cost += u2["cost_usd"] or 0
            ptok += u2["prompt_tokens"] or 0
            ctok += u2["completion_tokens"] or 0
            rtok += u2["reasoning_tokens"] or 0
            reask_reason = key
        else:
            reask_reason = None
        if parsed is not None:
            answers[q["id"]] = parsed
        rows.append({"interview_id": iid, "date": run_date.isoformat(), "wave": wave, "arm": arm["id"],
                     "web": arm["web"], "memory": arm["memory"], "userid": userid, "respondent_type": respondent_type,
                     "order": order, "question_id": q["id"], "label": q["label"], "type": q["type"],
                     "module": q["module"], "value": answer_value(q, parsed, answers),
                     "answer_text": answer_text(qn, q, parsed), "answer_json": to_json(parsed), "raw_response": raw,
                     "reasked": first is not None, "reask_reason": reask_reason, "first_response": first, "prompt_tokens": ptok,
                     "completion_tokens": ctok, "reasoning_tokens": rtok or None, "cost_usd": round(cost, 8),
                     "latency_s": res["latency_s"], "attempts": res["attempts"], "model": u["model_used"] or cfg["model"],
                     "provider": u["provider"], "error": res["error"]})

    total = lambda k: sum((c["response"] or {}).get("usage", {}).get(k) or 0 for c in calls if isinstance(c["response"], dict))
    ledger_row = {"interview_id": iid, "userid": userid, "arm": arm["id"], "web": arm["web"], "memory": arm["memory"],
                  "wave": wave, "scheduled_date": scheduled.isoformat(), "run_date": run_date.isoformat(),
                  "started_utc": started, "finished_utc": _now(), "respondent_type": respondent_type,
                  "status": "complete", "n_questions": len(rows),
                  "n_answered": sum(1 for r in rows if r["answer_json"]), "n_errors": sum(1 for r in rows if r["error"]),
                  "n_reasks": sum(1 for r in rows if r["reasked"]), "n_calls": len(calls),
                  "prompt_tokens": total("prompt_tokens"), "completion_tokens": total("completion_tokens"),
                  "cost_usd": round(total("cost"), 6), "web_results": len(web_results),
                  "memory_waves": " ".join(memory_waves), "model": cfg["model"], "temperature": cfg.get("temperature")}
    log_record = {**ledger_row, "settings": {k: cfg.get(k) for k in ("model", "temperature", "max_tokens", "top_p",
                                                                     "reasoning", "provider", "reask", "density_reask", "age_moves_with_date")},
                  "web_settings": w if arm["web"] else None,
                  "memory_settings": cfg["memory"] if arm["memory"] else None,
                  "persona": {k: v for k, v in row.items() if k != "persona_preview"},
                  "system_prompt": sys, "web_results": web_results, "answers": answers,
                  "messages": messages, "calls": calls}
    return ledger_row, rows, json.loads(json.dumps(log_record, default=str))
