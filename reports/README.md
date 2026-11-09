# SCE monthly survey · report

Updated 2026-11-09 13:17 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 360 | 360 | 9 | 0 | 0 | 0.96 |
| 2026-11 | B_web_nomemory | 360 | 360 | 9 | 0 | 0 | 4.08 |
| 2026-11 | C_noweb_memory | 360 | 360 | 9 | 0 | 1 | 1.08 |
| 2026-11 | D_web_memory | 360 | 360 | 9 | 0 | 1 | 4.22 |

Total cost so far: **$40.71**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 360 | 3 | 3.22 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 360 | 4 | 4.02 | 0.39 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 360 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 360 | 4 | 4.23 | 0.33 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 360 | 3 | 3.04 | 0.36 | 2.38 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 360 | 4.11 | 4.07 | 0.62 | 2.89 | 5.86 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 360 | 2.93 | 2.99 | 0.35 | 1.84 | 4.16 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 360 | 4.29 | 4.32 | 0.5 | 2.94 | 5.56 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 360 | 3 | 2.83 | 0.33 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 360 | 3 | 3.13 | 0.27 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 360 | 3 | 2.86 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 360 | 3 | 3.21 | 0.28 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 360 | 55 | 53.99 | 4 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 360 | 55 | 55.06 | 5.12 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 360 | 55 | 53.6 | 4.08 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 360 | 60 | 58.36 | 4.31 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 360 | 50 | 50.29 | 3.71 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 360 | 60 | 56.08 | 9.85 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 360 | 50 | 50.44 | 3.51 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 360 | 60 | 57.5 | 8.41 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 360 | 60 | 58.03 | 4.75 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 360 | 55 | 54.76 | 5.1 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 360 | 60 | 57.74 | 4.68 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 360 | 55 | 52.71 | 4.86 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 221 | 10 | 12.48 | 4.67 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 221 | 15 | 14.75 | 5.9 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 222 | 10 | 11.89 | 5.17 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 222 | 15 | 15.81 | 6.13 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 360 | 3 | 2.88 | 1.93 | -5 | 25 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 360 | 3 | 2.67 | 3.26 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 360 | 3 | 2.88 | 3.34 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 360 | 3 | 2.74 | 3.08 | -10 | 50 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 360 | 3.5 | 3.58 | 0.67 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 360 | 4 | 4.26 | 0.65 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 360 | 3.25 | 3.57 | 0.84 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 360 | 4 | 4.47 | 0.61 | 3 | 8 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 360 | 5 | 7.1 | 5.76 | 0 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 360 | 5 | 8.35 | 6.76 | 2 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 360 | 5 | 7.19 | 6.17 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 360 | 5 | 8.46 | 6.49 | 1 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 360 | 3 | 2.69 | 0.54 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 360 | 2 | 2.21 | 1.05 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 360 | 3 | 2.71 | 0.47 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 360 | 2 | 2.01 | 1.14 | -2 | 3 |

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
