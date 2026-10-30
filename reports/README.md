# SCE monthly survey · report

Updated 2026-10-30 12:32 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1120 | 1120 | 14 | 0 | 1 | 2.34 |
| 2026-10 | B_web_nomemory | 1120 | 1120 | 14 | 0 | 0 | 11.9 |
| 2026-10 | C_noweb_memory | 1120 | 1120 | 14 | 0 | 0 | 2.17 |
| 2026-10 | D_web_memory | 1120 | 1120 | 14 | 0 | 1 | 11.9 |

Total cost so far: **$28.31**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 1120 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 1120 | 4 | 4.19 | 0.34 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 1120 | 3 | 3.18 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 1120 | 4 | 4.18 | 0.34 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 1120 | 2.95 | 3.01 | 0.35 | 1.75 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 1120 | 4.29 | 4.28 | 0.51 | 3.04 | 5.71 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 1120 | 2.95 | 2.98 | 0.35 | 1.08 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 1120 | 4.24 | 4.26 | 0.53 | 2.89 | 6.29 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 1120 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 1120 | 3 | 3.21 | 0.29 | 2.5 | 4.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 1120 | 3 | 2.87 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 1120 | 3 | 3.21 | 0.28 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 1120 | 55 | 53.56 | 4.05 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 1120 | 60 | 57.72 | 4.17 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 1120 | 55 | 53.52 | 4.04 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 1120 | 60 | 57.55 | 3.86 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 1120 | 50 | 50.36 | 3.55 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 1120 | 55 | 53.48 | 9.14 | 30 | 75 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 1120 | 50 | 50.56 | 3.28 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 1120 | 55 | 54.01 | 9.14 | 25 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 1120 | 60 | 57.87 | 4.62 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 1120 | 55 | 54.19 | 4.92 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 1120 | 60 | 57.77 | 4.56 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 1120 | 55 | 54.41 | 4.75 | 35 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 669 | 10 | 12.21 | 5.25 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 671 | 15 | 15.3 | 5.41 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 669 | 10 | 12.08 | 5.15 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 670 | 15 | 15.46 | 5.67 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 1120 | 3 | 2.85 | 4.45 | -20 | 100 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 1120 | 3 | 2.71 | 3.57 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 1120 | 3 | 2.89 | 3.71 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 1120 | 3 | 2.74 | 4.81 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 1120 | 3.5 | 3.56 | 0.93 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 1120 | 4.5 | 4.47 | 0.78 | -8 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 1120 | 3.5 | 3.56 | 0.87 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 1120 | 4 | 4.46 | 0.67 | -3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 1120 | 5 | 7.3 | 6.38 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 1120 | 5 | 8.7 | 6.85 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 1120 | 5 | 7.12 | 6.08 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 1120 | 5 | 8.58 | 6.77 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 1120 | 3 | 2.68 | 0.51 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 1120 | 2 | 2 | 1.25 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 1120 | 3 | 2.68 | 0.51 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 1120 | 2 | 2.04 | 1.18 | -2.5 | 3.5 |

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
