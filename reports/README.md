# SCE monthly survey · report

Updated 2026-10-17 19:29 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 4 | 4 | 1 | 0 | 0 | 0.01 |
| 2026-10 | B_web_nomemory | 2 | 2 | 1 | 0 | 0 | 0.02 |
| 2026-10 | C_noweb_memory | 1 | 1 | 1 | 0 | 0 | 0 |
| 2026-10 | D_web_memory | 1 | 1 | 1 | 0 | 0 | 0.01 |

Total cost so far: **$0.04**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 4 | 3 | 3.12 | 0.25 | 3 | 3.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 2 | 4.75 | 4.75 | 0.35 | 4.5 | 5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 1 | 4 | 4 |  | 4 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 1 | 4.5 | 4.5 |  | 4.5 | 4.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 4 | 3.42 | 3.48 | 0.58 | 2.98 | 4.09 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 2 | 5.03 | 5.03 | 0.39 | 4.75 | 5.3 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 1 | 4.42 | 4.42 |  | 4.42 | 4.42 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 1 | 4.3 | 4.3 |  | 4.3 | 4.3 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 4 | 3 | 3 | 0.41 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 2 | 3.75 | 3.75 | 0.35 | 3.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 1 | 3 | 3 |  | 3 | 3 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 1 | 3.5 | 3.5 |  | 3.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 4 | 55 | 56.25 | 2.5 | 55 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 2 | 60 | 60 | 0 | 60 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 1 | 60 | 60 |  | 60 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 1 | 60 | 60 |  | 60 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 4 | 47.5 | 47.5 | 2.89 | 45 | 50 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 2 | 65 | 65 | 0 | 65 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 1 | 50 | 50 |  | 50 | 50 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 1 | 55 | 55 |  | 55 | 55 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 4 | 60 | 58.75 | 7.5 | 50 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 2 | 42.5 | 42.5 | 3.54 | 40 | 45 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 1 | 45 | 45 |  | 45 | 45 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 1 | 45 | 45 |  | 45 | 45 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 2 | 10 | 10 | 0 | 10 | 10 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 4 | 2.5 | 2.5 | 1.29 | 1 | 4 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 2 | 1.5 | 1.5 | 0.71 | 1 | 2 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 1 | -5 | -5 |  | -5 | -5 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 1 | 1 | 1 |  | 1 | 1 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 4 | 3.75 | 3.62 | 0.48 | 3 | 4 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 2 | 4.5 | 4.5 | 0.71 | 4 | 5 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 1 | 4 | 4 |  | 4 | 4 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 1 | 5 | 5 |  | 5 | 5 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 4 | 5 | 4.25 | 1.5 | 2 | 5 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 2 | 5 | 5 | 0 | 5 | 5 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 1 | 5 | 5 |  | 5 | 5 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 1 | 10 | 10 |  | 10 | 10 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 4 | 2.5 | 2.5 | 0.58 | 2 | 3 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 2 | 2 | 2 | 0 | 2 | 2 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 1 | 2 | 2 |  | 2 | 2 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 1 | 2.5 | 2.5 |  | 2.5 | 2.5 |

All items, by day and by month: [stats_daily.csv](stats_daily.csv) · [stats_monthly.csv](stats_monthly.csv) · one row per interview: [wide/](wide/)

## Trends

Solid line = median · dashed = mean · band = mean ± SD · dotted = min and max.

### Q8v2part2 · Expected inflation rate (next 12 months)
![Q8v2part2: median by arm](charts/compare_Q8v2part2.png)
![Q8v2part2 by day](charts/daily_Q8v2part2.png)

### Q9_binmean · Inflation probabilities by range (next 12 months): mean using bin midpoints
![Q9_binmean: median by arm](charts/compare_Q9_binmean.png)
![Q9_binmean by day](charts/daily_Q9_binmean.png)

### Q9bv2part2 · Expected inflation rate (2–3 years ahead)
![Q9bv2part2: median by arm](charts/compare_Q9bv2part2.png)
![Q9bv2part2 by day](charts/daily_Q9bv2part2.png)

### Q4new · Chance U.S. unemployment is higher (12 months)
![Q4new: median by arm](charts/compare_Q4new.png)
![Q4new by day](charts/daily_Q4new.png)

### Q5new · Chance savings interest rates are higher (12 months)
![Q5new: median by arm](charts/compare_Q5new.png)
![Q5new by day](charts/daily_Q5new.png)

### Q6new · Chance U.S. stock prices are higher (12 months)
![Q6new: median by arm](charts/compare_Q6new.png)
![Q6new by day](charts/daily_Q6new.png)

### Q13new · Chance of losing main job (12 months)
![Q13new: median by arm](charts/compare_Q13new.png)
![Q13new by day](charts/daily_Q13new.png)

### Q25v2part2 · Expected household income change (%)
![Q25v2part2: median by arm](charts/compare_Q25v2part2.png)
![Q25v2part2 by day](charts/daily_Q25v2part2.png)

### Q26v2part2 · Expected household spending change (%)
![Q26v2part2: median by arm](charts/compare_Q26v2part2.png)
![Q26v2part2 by day](charts/daily_Q26v2part2.png)

### Q30new · Chance of missing a minimum debt payment (3 months)
![Q30new: median by arm](charts/compare_Q30new.png)
![Q30new by day](charts/daily_Q30new.png)

### Q31v2part2 · Expected national home price change (%)
![Q31v2part2: median by arm](charts/compare_Q31v2part2.png)
![Q31v2part2 by day](charts/daily_Q31v2part2.png)
