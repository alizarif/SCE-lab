# SCE monthly survey · report

Updated 2026-10-22 14:08 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 480 | 480 | 6 | 0 | 1 | 1.01 |
| 2026-10 | B_web_nomemory | 480 | 480 | 6 | 0 | 0 | 5.12 |
| 2026-10 | C_noweb_memory | 480 | 480 | 6 | 0 | 0 | 0.94 |
| 2026-10 | D_web_memory | 480 | 480 | 6 | 0 | 1 | 5.12 |

Total cost so far: **$12.18**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 480 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 480 | 4 | 4.21 | 0.34 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 480 | 3 | 3.17 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 480 | 4 | 4.22 | 0.36 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 480 | 2.95 | 3.02 | 0.36 | 2.24 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 480 | 4.29 | 4.29 | 0.52 | 3.04 | 5.71 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 480 | 2.95 | 2.98 | 0.32 | 2.04 | 4.42 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 480 | 4.28 | 4.27 | 0.53 | 3.02 | 6.29 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 480 | 3 | 2.88 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 480 | 3 | 3.22 | 0.29 | 2.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 480 | 3 | 2.86 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 480 | 3 | 3.22 | 0.28 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 480 | 55 | 53.54 | 4.06 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 480 | 60 | 58.86 | 3.53 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 480 | 55 | 53.47 | 4.1 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 480 | 60 | 58.71 | 3.18 | 45 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 480 | 50 | 50.27 | 3.57 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 480 | 55 | 53.08 | 8.54 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 480 | 50 | 50.54 | 3.25 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 480 | 55 | 53.22 | 8.43 | 35 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 480 | 60 | 58.04 | 4.38 | 45 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 480 | 55 | 54.52 | 5.01 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 480 | 60 | 57.99 | 4.47 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 480 | 55 | 54.73 | 4.63 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 298 | 10 | 11.93 | 4.74 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 299 | 15 | 15.48 | 5.17 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 299 | 10 | 12.06 | 5.26 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 299 | 15 | 15.84 | 5.64 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 480 | 3 | 2.85 | 3.94 | -20 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 480 | 3 | 2.79 | 3.87 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 480 | 3 | 2.98 | 3.62 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 480 | 3 | 2.79 | 4.95 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 480 | 3.5 | 3.55 | 1.03 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 480 | 4.5 | 4.49 | 0.89 | -8 | 8 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 480 | 3.5 | 3.57 | 0.84 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 480 | 4.5 | 4.53 | 0.68 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 480 | 5 | 7.34 | 6.36 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 480 | 5 | 8.82 | 7.23 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 480 | 5 | 7.35 | 6.61 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 480 | 5 | 8.77 | 7.21 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 480 | 3 | 2.7 | 0.46 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 480 | 2 | 1.67 | 1.42 | -2.5 | 3 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 480 | 3 | 2.72 | 0.46 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 480 | 2 | 1.73 | 1.35 | -2.5 | 3.5 |

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
