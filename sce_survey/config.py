"""Settings (config.yaml), paths, logging."""
import logging
import os
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
# dry runs (fake answers) write to data_dry_run/ and reports_dry_run/, never mixed with real results
_DRY = os.environ.get("SCE_DRY_RUN") == "1"
DATA = ROOT / ("data_dry_run" if _DRY else "data")
REPORTS = ROOT / ("reports_dry_run" if _DRY else "reports")
LEDGER = DATA / "interviews.csv"

log = logging.getLogger("sce")


def _load_dotenv():
    """Local runs: read OPENROUTER_API_KEY from a .env file next to config.yaml (never committed)."""
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _as_date(v):
    if v in (None, "", "null"):
        return None
    if isinstance(v, date):
        return v
    return datetime.strptime(str(v)[:10], "%Y-%m-%d").date()


def load_config(path=None):
    _load_dotenv()
    cfg = yaml.safe_load(Path(path or ROOT / "config.yaml").read_text())
    cfg["start_date"] = _as_date(cfg.get("start_date"))
    cfg["end_date"] = _as_date(cfg.get("end_date"))
    cfg.setdefault("arms", [{"id": "A", "web": False, "memory": False}])
    for a in cfg["arms"]:
        a["id"] = str(a["id"])
        a["web"] = bool(a.get("web"))
        a["memory"] = bool(a.get("memory"))
    cfg.setdefault("web", {})
    cfg.setdefault("memory", {})
    cfg.setdefault("prompts", {})
    cfg.setdefault("report", {})
    return cfg


def setup_logging(run_date, to_file=True):
    log.setLevel(logging.INFO)
    log.handlers.clear()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    log.addHandler(sh)
    if to_file:
        p = DATA / "runlog" / f"{run_date:%Y-%m}" / f"{run_date:%Y-%m-%d}.log"
        p.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(p, encoding="utf-8")
        fh.setFormatter(fmt)
        log.addHandler(fh)
    return log
