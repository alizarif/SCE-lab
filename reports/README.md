# SCE monthly survey · report

Updated 2026-10-29 12:24 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1040 | 1040 | 13 | 0 | 1 | 2.18 |
| 2026-10 | B_web_nomemory | 1040 | 1040 | 13 | 0 | 0 | 11.07 |
| 2026-10 | C_noweb_memory | 1040 | 1040 | 13 | 0 | 0 | 2.02 |
| 2026-10 | D_web_memory | 1040 | 1040 | 13 | 0 | 1 | 11.07 |

Total cost so far: **$26.33**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 1040 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 1040 | 4 | 4.19 | 0.34 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 1040 | 3 | 3.18 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 1040 | 4 | 4.18 | 0.35 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 1040 | 2.94 | 3.01 | 0.35 | 1.75 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 1040 | 4.25 | 4.27 | 0.51 | 3.04 | 5.71 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 1040 | 2.95 | 2.98 | 0.35 | 1.08 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 1040 | 4.23 | 4.25 | 0.53 | 2.89 | 6.29 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 1040 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 1040 | 3 | 3.21 | 0.29 | 2.5 | 4.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 1040 | 3 | 2.87 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 1040 | 3 | 3.2 | 0.28 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 1040 | 55 | 53.57 | 4.06 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 1040 | 60 | 57.8 | 4.18 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 1040 | 55 | 53.53 | 4.04 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 1040 | 60 | 57.61 | 3.9 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 1040 | 50 | 50.39 | 3.56 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 1040 | 55 | 54.27 | 8.9 | 30 | 75 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 1040 | 50 | 50.59 | 3.28 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 1040 | 55 | 54.84 | 8.81 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 1040 | 60 | 57.93 | 4.61 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 1040 | 55 | 54.15 | 5.02 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 1040 | 60 | 57.82 | 4.6 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 1040 | 55 | 54.36 | 4.79 | 35 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 628 | 10 | 12.18 | 5.14 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 629 | 15 | 15.35 | 5.42 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 628 | 10 | 12.11 | 5.15 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 629 | 15 | 15.49 | 5.47 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 1040 | 3 | 2.86 | 4.56 | -20 | 100 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 1040 | 3 | 2.7 | 3.36 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 1040 | 3 | 2.88 | 3.52 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 1040 | 3 | 2.75 | 4.94 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 1040 | 3.5 | 3.56 | 0.94 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 1040 | 4 | 4.47 | 0.79 | -8 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 1040 | 3.5 | 3.56 | 0.87 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 1040 | 4 | 4.46 | 0.69 | -3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 1040 | 5 | 7.33 | 6.37 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 1040 | 5 | 8.74 | 6.88 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 1040 | 5 | 7.16 | 6.03 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 1040 | 5 | 8.58 | 6.71 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 1040 | 3 | 2.68 | 0.51 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 1040 | 2 | 2.04 | 1.21 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 1040 | 3 | 2.68 | 0.52 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 1040 | 2 | 2.07 | 1.14 | -2.5 | 3.5 |

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
