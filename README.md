# SCE monthly survey

The New York Fed Survey of Consumer Expectations (SCE) core questionnaire, run every month on 1,200 LLM personas
built from real SCE respondents. It runs every day on GitHub, on its own, until you stop it.

* **Who answers:** `participants.xlsx`, one row per person (1,200 drawn at random from the SCE respondents who joined the panel in 2016 or later, seed 2222), with the person's own SCE answers and their commuting zone.
  Each person's system prompt is the final persona template: role, who you are, numeracy questions with their answers
  and score. Exact SCE wording throughout; the age is the one the person reported in the SCE.
* **What is asked:** `questionnaire.xlsx`, the monthly core module in exact SCE wording and order, with the SCE's
  skip rules (labour questions depend on the employment answer, part-2 rates follow the direction, and so on).
  Intro screens are shown with the next question. Probabilities that do not add up to 100 are asked once more, as the
  SCE web form does. Repeat respondents (from their 2nd month) also get the home-price and commodity block C1–C4.
* **When:** every day at 8 am New York time. Each month every person is interviewed once: all 1,200 are spread evenly
  over the survey days of the month (from October 17: 15 days × 80 people; November: 30 days × 40 people). The day
  is drawn at random again every month, so someone interviewed on the 5th this month can be on any day next month.
* **Four types (arms):** every person is interviewed in all four, as separate conversations on the same day:

  | arm | web search | remembers last months |
  |---|---|---|
  | `A_noweb_nomemory` | no | no |
  | `B_web_nomemory` | yes, top 10 results | no |
  | `C_noweb_memory` | no | yes |
  | `D_web_memory` | yes, top 10 results | yes |

  Change or drop arms in `config.yaml` (`arms:`).

## Memory: same thread, or in the prompt?

OpenRouter does not keep conversations. Every API call sends the whole conversation again, so a "thread" is only
the list of messages the program sends. Both options are built in (`config.yaml` → `memory: mode:`):

* `summary` (default): at the start of this month's survey, the person sees their own answers from earlier months
  ("You took part in this survey before. Your answers in earlier months…"). It stays small however long the panel
  runs (12 months by default).
* `thread`: last month's entire conversation is sent again, and this month continues it ("One month later. Today's
  date is …"). This is the true "same thread", but every question then carries last month's ~40 questions as well,
  so each call costs about twice as much. It is limited to the last month (`thread_months`).

Memory is per arm. `C` and `D` remember only their own earlier interviews; `A` and `B` start fresh every month.

## Web search

In arms `B` and `D`, each interview starts with one web search through OpenRouter's web plugin (Exa, top 10 results)
for the latest U.S. economic news. The pages found (title, link, first 1,000 characters) are pasted into the
conversation, the persona notes what matters to them, and then the survey starts. Every later question can use what
was found. The search costs about $0.007 per interview. With `scope: question`, every question searches again; that
costs about 45 times more.

## What is saved (everything)

| file | content |
|---|---|
| `data/interviews.csv` | one row per interview: person, arm, month, scheduled and actual day, new/repeat, questions, errors, re-asks, API calls, tokens, cost, number of web results, months remembered |
| `data/responses/YYYY-MM/<day>_<arm>.csv` | one row per question: answer code/number, readable answer, all bins, raw reply, the first reply if re-asked, tokens, cost, time, model, provider, error |
| `data/logs/YYYY-MM/<day>_<arm>.jsonl.gz` | one JSON object per interview: settings, persona row, full system prompt, web results, every message, every raw API response |
| `data/runlog/YYYY-MM/<day>.log` | what each daily run did |
| `reports/README.md` | progress, cost, this month's table, trend charts (GitHub shows it in the `reports` folder) |
| `reports/stats_daily.csv`, `stats_monthly.csv` | for every numeric item × arm: n, mean, SD, median, min, max, p25, p75 |
| `reports/wide/YYYY-MM.csv` | one row per interview, one column per item, like the SCE microdata (signed rates, `Q9_bin1…10`, `Q9_binmean`, `C4_1…6`) |
| `reports/charts/` | per item: one panel per arm (median, mean, mean ± SD, min and max), plus the four arms' medians together |

Numbers follow the microdata conventions: choice items are codes; part-2 rates are signed (deflation or a decrease is
negative); probability items have the 10 bins plus `<id>_binmean`, a simple mean using bin midpoints 14, 10, 6, 3, 1, −1, −3, −6, −10, −14 (not the SCE's fitted `Q9_mean`).

---

## Setup, step by step

### 1. Accounts you need
* **GitHub** (free): <https://github.com/signup>.
* **OpenRouter** with credit: <https://openrouter.ai> → Keys → *Create key*. Use a new key; don't reuse the one that
  was pasted into a chat earlier. Optional: set a monthly credit limit on the key.

### 2. Test it on your Mac first (5 minutes)
In Terminal:
```bash
cd ~/"Downloads/Folders/Research In Progress/SCE/SCE_Monthly_Survey"
python3 -m pip install -r requirements.txt
python3 run.py persona                         # prints one participant's full system prompt
python3 run.py schedule                        # who is interviewed on which day this month
python3 run.py daily --dry-run --limit 8       # 8 fake interviews: no API calls, no cost (goes to data_dry_run/)
```
Then a small real pilot. Put your key in a file named `.env` in this folder (one line:
`OPENROUTER_API_KEY=sk-or-...`). It is never uploaded (`.gitignore`). Then:
```bash
python3 run.py daily --limit 4                 # 4 real interviews (one per arm), about $0.15
python3 run.py report
python3 run.py status
```
Look at `data/responses/…csv` and `reports/README.md`. If it looks right, delete the pilot so the real run starts
clean: delete the `data` and `reports` folders.

### 3. Create the repository
1. On GitHub: **+** (top right) → **New repository** → name e.g. `sce-monthly-survey` → choose **Private** → *Create*.
2. Upload the folder. The easiest way: on the new repository page click **uploading an existing file** and drag
   **everything inside** `SCE_Monthly_Survey` (including the hidden `.github` folder: in Finder press
   **Cmd + Shift + .** to show hidden files). Or, in Terminal:
   ```bash
   cd ~/"Downloads/Folders/Research In Progress/SCE/SCE_Monthly_Survey"
   git init -b main && git add . && git commit -m "SCE monthly survey"
   git remote add origin https://github.com/<your-user>/sce-monthly-survey.git
   git push -u origin main
   ```
   Check that `.github/workflows/daily_survey.yml` is on GitHub, and that `.env` is **not**. If the browser upload
   skipped the hidden `.github` folder: **Add file** → **Create new file** → type the name
   `.github/workflows/daily_survey.yml` → paste the file's content → *Commit*.

### 4. Add the API key as a secret
Repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret** →
Name `OPENROUTER_API_KEY`, Secret: your key → *Add secret*.

### 5. Let the job save its results
Repository → **Settings** → **Actions** → **General** → *Workflow permissions* → **Read and write permissions** → *Save*.

### 6. First runs
1. Tab **Actions** → **Daily SCE survey** → **Run workflow** → tick *Dry run* → *Run*. It should turn green in
   1–2 minutes (no cost; fake data that is not saved).
2. **Run workflow** again with *limit* `4`: four real interviews, committed to `data/` and `reports/`.
3. From then on it runs by itself every day at 8 am New York time. A run that is due but missed (GitHub delays, an
   outage) is caught up the next day, within the same month.

### 7. Watch it
* `reports/README.md` on GitHub: progress, cost, tables, charts.
* **Actions** tab: one run per day. A red run means it stopped (e.g. no OpenRouter credit), and GitHub emails you.
  Interviews not done are done on the next run.
* Locally: `git pull`, then `python3 run.py status`.

### 8. Change, pause, stop
* **Change settings:** edit `config.yaml` on GitHub (pencil icon) → *Commit*. The next run uses it.
* **Pause or stop:** set `enabled: false` (or set `end_date`). Or: **Actions** → **Daily SCE survey** → **⋯** → *Disable workflow*.
* **Different people:** replace `participants.xlsx`. To rebuild it from the sampling notebook's output:
  `python3 tools/make_participants.py path/to/sample_all_interviews_….csv` (it adds the commuting-zone names
  from `commuting_zones_2000.xlsx`).
* **Different questions:** `questionnaire.xlsx` → `include` column (TRUE/FALSE). Answer-format prompts are on the
  `Prompts` sheet.

## Time and cost (rough)

* One interview: ~37–43 API calls. A month: 1,200 people × 4 arms = 4,800 interviews ≈ 200,000 calls.
* Busiest days are at the start (80 people × 4 arms = 320 interviews ≈ 15–30 minutes with `concurrency: 30`).
  If a day ever needs more than `time_budget_minutes`, the rest runs the next day.
* Tokens: each call re-sends the conversation, about 125k input tokens per interview without web and ~220k with the
  pasted web results. With `openai/gpt-6-luna` ($0.10 / $0.50 per million tokens, plus its own thinking tokens) that
  is roughly **$0.015 per interview without web, $0.03 with web, ≈ $90–130 a month for all four arms**. OpenAI
  discounts the repeated (cached) part of the conversation, so it is often less. Larger models cost proportionally more: run a pilot (`--limit`), then check `python3 run.py status`.
* GitHub: private repositories get 2,000 free Actions minutes a month on the Free plan; this uses roughly
  300–900. The data grows the repository by about 50–150 MB a month.

## Quality check

`python3 tools/qc_check.py sample/sample_all_interviews_….csv` writes `qc/qc_report.md` and `qc/participants_flags.csv`.
Last run: 1,200 people, 84,000 values re-derived from the microdata with 0 differences; 0 errors in the personas;
59 questionnaire rows render and parse; 1,800 answer combinations walked through the skip logic, 0 differences from
the PDF routing. The skip rules were also checked against real SCE answers (2020–2025): each follow-up question was
answered by ~100% of the people the rule selects and by 0% of the others.

Warnings (kept, because they are how people answered the SCE): Q12new missing for some 2013 respondents (the
question started in August 2013); Q46 answered by some people who live alone (the SCE asked them); partner in Q38 but
not in the household list, or the reverse; 3 impossible or missing ages (shown as the SCE age group instead).

### Where the survey deliberately differs from the FRBNY questionnaire PDF
* Intro screens: the payment sentence ("You will receive $20…") is left out, and "just click on 'NEXT'" reads "just skip it".
* H2 / H15 ("enter your answer in the box … or by clicking on the scale") read "Please enter your answer (a number
  from 0 to 100)", and C4 asks for one signed number per item instead of two boxes, because a chat has no boxes or sliders.
* Q9c and Q9new2 say "over the 12-month period between …" (the PDF drops "12-month period between", a typo).
* ES4/ES5 are asked of every self-employed person (the PDF note "[if ES1==4 but not ES1==1,2,3]" is a typo; the SCE
  data show everyone self-employed answers them).
* Each answer ends with an answer-format line (e.g. "Reply with ONLY one line: ANSWER: <code>") so it can be read.
* `<id>_binmean` (e.g. `Q9_binmean`) is a simple mean using bin midpoints. It is not the SCE's published `Q9_mean`,
  which the New York Fed computes by fitting a distribution to each respondent's bins.

Bracketed wording in the PDF follows the person's answers, as in the SCE: "current"/"main" job (Q12new, Q13new,
Q14new, Q22new, Q23v2, Q24), the laid-off version of Q11, "independent contractor job"/"business"/"family business"
(ES4, ES5), inflation/deflation and increase/decrease in the part-2 questions, and the month-year periods. The main-job
screen (Q12intro) appears for people with more than one job. The SCE web form's checks are repeated once with its own
messages: E1 (no answer), E3 (probabilities not adding up to 100), E8 (working and "not working but would like to work"
both chosen) and E9 (C4 left empty).

## Files

```
config.yaml              all settings
participants.xlsx        the 1,200 personas (sheet "participants"; persona_preview = the text as of the build date)
commuting_zones_2000.xlsx  names of the SCE commuting-zone codes (USDA ERS 2000 Commuting Zone IDs)
sample/                  the seed-2222 draw (joined 2016–2025): list of people, all their SCE interviews (all variables),
                         their first interviews only (tenure = 1), and the sample-vs-SCE comparison table
questionnaire.xlsx       questions (exact SCE wording, skip rules) + answer-format prompts
run.py                   command line (daily, report, schedule, status, persona)
sce_survey/              persona.py · questionnaire.py · schedule.py · llm.py · interview.py · runner.py · store.py · report.py
tools/make_participants.py   rebuild participants.xlsx from SCE microdata rows
tools/qc_check.py        quality check of participants.xlsx and questionnaire.xlsx → qc/
.github/workflows/daily_survey.yml   the daily GitHub job
```

Notes. The persona describes the person at their first SCE interview, including the age they reported then
(`age_moves_with_date: true` in config.yaml adds the years since). Numeracy shows every question the person was asked
(QNUM1–6 together; QNUM8–9 from April 2015 on); a skipped one is shown as "(no answer)" and counts as not correct. The SCE's
`_COMMUTING_ZONE` codes are the USDA ERS **2000** Commuting Zone IDs: all 635 codes in the microdata are 2000 IDs, and
99.98% of SCE interviews have a state that the zone covers. (The 2020 delineation numbers its 598 zones differently.)
The persona names the zone after the 2003 metro/micro area of its most populous county, e.g. "Commuting zone where
you live (your local labor market): Memphis, TN-MS-AR." The line is left out in the rare case where the zone does not
cover the person's state.
People who joined the SCE before April 2015 have no risk (QRA) or health answers, and only 5 numeracy questions;
those lines are left out of their persona.
