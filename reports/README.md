# SCE monthly survey · report

Updated 2026-11-10 13:16 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 400 | 400 | 10 | 0 | 0 | 1.07 |
| 2026-11 | B_web_nomemory | 400 | 400 | 10 | 0 | 0 | 4.53 |
| 2026-11 | C_noweb_memory | 400 | 400 | 10 | 0 | 1 | 1.2 |
| 2026-11 | D_web_memory | 400 | 400 | 10 | 0 | 1 | 4.69 |

Total cost so far: **$41.85**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 400 | 3 | 3.22 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 400 | 4 | 4.01 | 0.38 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 400 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 400 | 4 | 4.23 | 0.33 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 400 | 3 | 3.05 | 0.36 | 2.38 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 400 | 4.06 | 4.04 | 0.61 | 2.89 | 5.86 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 400 | 2.93 | 2.99 | 0.36 | 1.84 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 400 | 4.28 | 4.31 | 0.49 | 2.94 | 5.56 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 400 | 3 | 2.83 | 0.33 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 400 | 3 | 3.1 | 0.28 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 400 | 3 | 2.86 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 400 | 3 | 3.2 | 0.29 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 400 | 55 | 53.96 | 4.02 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 400 | 55 | 55.04 | 5.04 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 400 | 55 | 53.68 | 4.07 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 400 | 60 | 58.42 | 4.29 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 400 | 50 | 50.34 | 3.72 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 400 | 60 | 57.06 | 9.94 | 30 | 75 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 400 | 50 | 50.42 | 3.5 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 400 | 60 | 58.15 | 8.39 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 400 | 60 | 58.1 | 4.74 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 400 | 55 | 55 | 5.08 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 400 | 60 | 57.78 | 4.71 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 400 | 55 | 52.84 | 4.88 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 251 | 10 | 12.52 | 4.95 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 251 | 15 | 14.82 | 5.82 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 252 | 10 | 12 | 5.13 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 252 | 15 | 15.85 | 6.24 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 400 | 3 | 2.85 | 1.89 | -5 | 25 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 400 | 3 | 2.68 | 3.11 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 400 | 3 | 2.87 | 3.18 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 400 | 3 | 2.73 | 2.95 | -10 | 50 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 400 | 3.5 | 3.58 | 0.66 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 400 | 4 | 4.24 | 0.63 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 400 | 3.25 | 3.56 | 0.83 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 400 | 4 | 4.46 | 0.6 | 3 | 8 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 400 | 5 | 7.04 | 5.6 | 0 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 400 | 5 | 8.33 | 6.69 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 400 | 5 | 7.13 | 6.02 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 400 | 5 | 8.44 | 6.58 | 0 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 400 | 3 | 2.69 | 0.53 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 400 | 2 | 2.25 | 1.04 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 400 | 3 | 2.71 | 0.47 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 400 | 2 | 2.03 | 1.14 | -2 | 3 |

All items, by day and by month: [stats_daily.csv](stats_daily.csv) · [stats_monthly.csv](stats_monthly.csv) · one row per interview: [wide/](wide/)

## Trends

Solid line = median · dashed = mean · band = mean ± SD · dotted = min and max.

### Q8v2part2 · Expected inflation rate (next 12 months)
![Q8v2part2: median by arm](charts/compare_Q8v2part2.png)
![Q8v2part2 by month](charts/monthly_Q8v2part2.png)
![Q8v2part2 by day](charts/daily_Q8v2part2.png)

### Q9_binmean · Inflation probabilities by range (next 12 months): mean using bin midpoints
![Q9_binmean: median by arm](charts/compare_Q9_binmean.png)
![Q9_binmean by month](charts/monthly_Q9_binmean.png)
![Q9_binmean by day](charts/daily_Q9_binmean.png)

### Q9bv2part2 · Expected inflation rate (2–3 years ahead)
![Q9bv2part2: median by arm](charts/compare_Q9bv2part2.png)
![Q9bv2part2 by month](charts/monthly_Q9bv2part2.png)
![Q9bv2part2 by day](charts/daily_Q9bv2part2.png)

### Q4new · Chance U.S. unemployment is higher (12 months)
![Q4new: median by arm](charts/compare_Q4new.png)
![Q4new by month](charts/monthly_Q4new.png)
![Q4new by day](charts/daily_Q4new.png)

### Q5new · Chance savings interest rates are higher (12 months)
![Q5new: median by arm](charts/compare_Q5new.png)
![Q5new by month](charts/monthly_Q5new.png)
![Q5new by day](charts/daily_Q5new.png)

### Q6new · Chance U.S. stock prices are higher (12 months)
![Q6new: median by arm](charts/compare_Q6new.png)
![Q6new by month](charts/monthly_Q6new.png)
![Q6new by day](charts/daily_Q6new.png)

### Q13new · Chance of losing main job (12 months)
![Q13new: median by arm](charts/compare_Q13new.png)
![Q13new by month](charts/monthly_Q13new.png)
![Q13new by day](charts/daily_Q13new.png)

### Q25v2part2 · Expected household income change (%)
![Q25v2part2: median by arm](charts/compare_Q25v2part2.png)
![Q25v2part2 by month](charts/monthly_Q25v2part2.png)
![Q25v2part2 by day](charts/daily_Q25v2part2.png)

### Q26v2part2 · Expected household spending change (%)
![Q26v2part2: median by arm](charts/compare_Q26v2part2.png)
![Q26v2part2 by month](charts/monthly_Q26v2part2.png)
![Q26v2part2 by day](charts/daily_Q26v2part2.png)

### Q30new · Chance of missing a minimum debt payment (3 months)
![Q30new: median by arm](charts/compare_Q30new.png)
![Q30new by month](charts/monthly_Q30new.png)
![Q30new by day](charts/daily_Q30new.png)

### Q31v2part2 · Expected national home price change (%)
![Q31v2part2: median by arm](charts/compare_Q31v2part2.png)
![Q31v2part2 by month](charts/monthly_Q31v2part2.png)
![Q31v2part2 by day](charts/daily_Q31v2part2.png)
