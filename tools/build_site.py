"""Assemble the public website (GitHub Pages) from site/ and the aggregate data in dashboard/data/.

    python tools/build_dashboard.py      # aggregate data → dashboard/data/
    python tools/build_site.py           # → _site/ (index.html, site.css, scripts, data/)

site/page.html is the same page the claude.ai dashboard uses; site/dash.js stands in for that dashboard's runtime.
Only the aggregate files from dashboard/data/ are copied; nothing person-level is published.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC, DATA, OUT = ROOT / "site", ROOT / "dashboard" / "data", ROOT / "_site"
FILES = ["arms", "choices", "density", "groups", "news", "pair_bins", "pair_fit", "panel", "quality", "questions",
         "real_history", "runs_daily", "schedule", "stats_daily", "stats_monthly", "stats_mtd", "status"]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>SCE Lab Live</title>
<meta name="description" content="A daily replication of the New York Fed Survey of Consumer Expectations, answered by LLM personas of 1,200 real SCE respondents.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<link rel="stylesheet" href="site.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
</head>
<body>
<div id="dash-root">
"""
FOOT = """
<p class="sce-foot sce">Built automatically from the project's GitHub repository after every survey run. Only totals and averages are published here; no individual respondent's record is shown.</p>
</div>
<script src="dash.js"></script>
<script src="core.js"></script>
<script src="charts.js"></script>
<script src="pages.js"></script>
</body>
</html>
"""


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "data").mkdir(parents=True)
    page = (SRC / "page.html").read_text()
    a, b = page.index("<style>"), page.index("</style>")
    css = (SRC / "tokens.css").read_text() + page[a + len("<style>"):b]
    body = page[b + len("</style>"):]
    for s in ("core.js", "charts.js", "pages.js"):
        body = body.replace(f'<script src="{s}"></script>', "")
    (OUT / "site.css").write_text(css)
    (OUT / "index.html").write_text(HEAD + body.strip() + FOOT)
    for s in ("dash.js", "core.js", "charts.js", "pages.js"):
        shutil.copy(SRC / s, OUT / s)
    for f in FILES:
        shutil.copy(DATA / f"{f}.json", OUT / "data" / f"{f}.json")
    (OUT / ".nojekyll").write_text("")
    print(f"site → {OUT.relative_to(ROOT)} ({len(FILES)} data files)")


if __name__ == "__main__":
    main()
