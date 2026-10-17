"""OpenRouter chat-completions calls (async, with retries), plus an offline fake for dry runs.

OpenRouter keeps no conversation on its side: every call sends the whole conversation so far."""
import asyncio
import os
import random
import re
import time

import httpx


class Fatal(Exception):
    """A problem that retrying will not fix (bad key, no credit)."""


class LLM:
    def __init__(self, cfg, dry_run=False):
        self.cfg = cfg
        self.dry_run = dry_run
        self.base = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
        self.key = os.environ.get("OPENROUTER_API_KEY", "")
        if not dry_run and not self.key:
            raise Fatal("OPENROUTER_API_KEY is not set (GitHub: Settings → Secrets → Actions; local: .env file)")
        self.client = None if dry_run else httpx.AsyncClient(timeout=httpx.Timeout(180, connect=30))
        self.consecutive_errors = 0

    async def close(self):
        if self.client:
            await self.client.aclose()

    def body(self, messages, web=False):
        c = self.cfg
        b = {"model": c["model"], "messages": messages, "max_tokens": c.get("max_tokens") or 400,
             "usage": {"include": True}}
        if c.get("temperature") is not None:
            b["temperature"] = c["temperature"]
        if c.get("top_p") is not None:
            b["top_p"] = c["top_p"]
        if c.get("reasoning"):
            b["reasoning"] = c["reasoning"]
        if c.get("provider"):
            b["provider"] = c["provider"]
        if web:
            w = c.get("web", {})
            plug = {"id": "web", "max_results": int(w.get("max_results", 10))}
            if w.get("engine"):
                plug["engine"] = w["engine"]
            b["plugins"] = [plug]
        return b

    async def chat(self, messages, web=False):
        """→ dict(content, response (full JSON), latency_s, attempts, error)."""
        body = self.body(messages, web)
        if self.dry_run:
            return {"content": fake_reply(messages, web), "response": {"dry_run": True}, "latency_s": 0.0,
                    "attempts": 1, "error": None, "request": {k: v for k, v in body.items() if k != "messages"}}
        t0, last = time.monotonic(), None
        for attempt in range(1, 7):
            try:
                r = await self.client.post(f"{self.base}/chat/completions", json=body, headers={
                    "Authorization": f"Bearer {self.key}", "X-Title": "SCE monthly survey"})
                if r.status_code in (401, 402, 403):
                    raise Fatal(f"OpenRouter refused the request (HTTP {r.status_code}): {r.text[:300]}")
                if r.status_code == 429 or r.status_code >= 500:
                    last = f"HTTP {r.status_code}: {r.text[:200]}"
                    await asyncio.sleep(min(60, 2 ** attempt + random.random() * 2))
                    continue
                data = r.json()
                if r.status_code >= 400 or "error" in data and not data.get("choices"):
                    last = f"HTTP {r.status_code}: {str(data.get('error', data))[:300]}"
                    if r.status_code == 400:
                        break                                  # bad request: retrying will not help
                    await asyncio.sleep(min(60, 2 ** attempt))
                    continue
                msg = (data.get("choices") or [{}])[0].get("message") or {}
                content = msg.get("content") or ""
                if not content.strip():
                    last = f"empty reply (finish_reason={data['choices'][0].get('finish_reason')})"
                    await asyncio.sleep(2 ** attempt)
                    continue
                self.consecutive_errors = 0
                return {"content": content, "response": data, "latency_s": round(time.monotonic() - t0, 2),
                        "attempts": attempt, "error": None, "request": {k: v for k, v in body.items() if k != "messages"}}
            except Fatal:
                raise
            except (httpx.HTTPError, ValueError) as e:
                last = f"{type(e).__name__}: {e}"
                await asyncio.sleep(min(60, 2 ** attempt))
        self.consecutive_errors += 1
        if self.consecutive_errors >= int(self.cfg.get("max_consecutive_errors", 25)):
            raise Fatal(f"{self.consecutive_errors} failed calls in a row; last error: {last}")
        return {"content": "", "response": None, "latency_s": round(time.monotonic() - t0, 2), "attempts": 6,
                "error": last or "unknown error", "request": {k: v for k, v in body.items() if k != "messages"}}


def fake_reply(messages, web=False):
    """Offline answers in the requested format (for --dry-run tests of the whole pipeline)."""
    last = messages[-1]["content"]
    rnd = random.Random(hash(last) % 10 ** 9)
    if web:
        return "- Prices still rising a bit.\n- Job market cooling.\n- Rates on hold."
    if "add up to" in last and "all ten again" in last.lower():
        return "\n".join(f"BIN{i}: {v}" for i, v in enumerate([2, 5, 13, 30, 30, 10, 5, 3, 1, 1], 1))
    if "BIN1:" in last:
        vals = [2, 5, 13, 30, 30, 10, 5, 3, 1, 1] if rnd.random() > .1 else [2, 5, 13, 30, 30, 10, 5, 3, 1, 0]
        return "\n".join(f"BIN{i}: {v}" for i, v in enumerate(vals, 1))
    if "C4_1:" in last:
        return "\n".join(f"C4_{i}: {rnd.choice([2, 3, 4, 5])}" for i in range(1, 7))
    if "code,code" in last:
        return "ANSWER: 1"
    if "number from 0 to 100" in last:
        return f"ANSWER: {rnd.choice([10, 20, 35, 50, 60])}"
    if "numeric code" in last:
        codes = re.findall(r"^(\d+)\. ", last, re.M)
        return f"ANSWER: {codes[0] if codes else 1}"
    return f"ANSWER: {rnd.choice([1, 2, 3, 4, 5])}"
