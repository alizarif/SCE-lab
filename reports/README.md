# SCE monthly survey · report

Updated 2026-10-24 12:16 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 640 | 640 | 8 | 0 | 1 | 1.35 |
| 2026-10 | B_web_nomemory | 640 | 640 | 8 | 0 | 0 | 6.82 |
| 2026-10 | C_noweb_memory | 640 | 640 | 8 | 0 | 0 | 1.25 |
| 2026-10 | D_web_memory | 640 | 640 | 8 | 0 | 1 | 6.82 |

Total cost so far: **$16.23**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 640 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 640 | 4.5 | 4.24 | 0.33 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 640 | 3 | 3.18 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 640 | 4.5 | 4.24 | 0.34 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 640 | 2.95 | 3.02 | 0.36 | 2.24 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 640 | 4.33 | 4.33 | 0.5 | 3.04 | 5.71 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 640 | 2.95 | 2.98 | 0.34 | 2.04 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 640 | 4.33 | 4.31 | 0.52 | 3.02 | 6.29 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 640 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 640 | 3 | 3.23 | 0.28 | 2.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 640 | 3 | 2.86 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 640 | 3 | 3.23 | 0.28 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 640 | 55 | 53.62 | 4.14 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 640 | 60 | 58.43 | 3.69 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 640 | 55 | 53.54 | 4.07 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 640 | 60 | 58.27 | 3.27 | 45 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 640 | 50 | 50.35 | 3.54 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 640 | 55 | 53.44 | 8.46 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 640 | 50 | 50.58 | 3.32 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 640 | 55 | 53.66 | 8.48 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 640 | 60 | 57.97 | 4.55 | 45 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 640 | 55 | 53.84 | 5.16 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 640 | 60 | 57.91 | 4.57 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 640 | 55 | 54.13 | 4.83 | 35 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 400 | 10 | 12.11 | 5.25 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 401 | 15 | 15.42 | 5.5 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 401 | 10 | 12.12 | 5.18 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 401 | 15 | 15.7 | 5.6 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 640 | 3 | 2.74 | 3.53 | -20 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 640 | 3 | 2.66 | 3.48 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 640 | 3 | 2.83 | 3.29 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 640 | 3 | 2.67 | 4.39 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 640 | 3.5 | 3.53 | 0.93 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 640 | 4.5 | 4.51 | 0.81 | -8 | 8 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 640 | 3.5 | 3.54 | 0.83 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 640 | 4.5 | 4.52 | 0.64 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 640 | 5 | 7.28 | 6.42 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 640 | 5 | 8.64 | 6.91 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 640 | 5 | 7.23 | 6.42 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 640 | 5 | 8.55 | 6.92 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 640 | 3 | 2.68 | 0.5 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 640 | 2 | 1.82 | 1.38 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 640 | 3 | 2.69 | 0.53 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 640 | 2 | 1.87 | 1.28 | -2.5 | 3.5 |

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
