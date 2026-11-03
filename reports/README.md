# SCE monthly survey · report

Updated 2026-11-03 13:15 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 120 | 120 | 3 | 0 | 0 | 0.32 |
| 2026-11 | B_web_nomemory | 120 | 120 | 3 | 0 | 0 | 1.36 |
| 2026-11 | C_noweb_memory | 120 | 120 | 3 | 0 | 0 | 0.36 |
| 2026-11 | D_web_memory | 120 | 120 | 3 | 0 | 0 | 1.4 |

Total cost so far: **$33.80**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 120 | 3 | 3.22 | 0.25 | 3 | 3.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 120 | 4 | 4.17 | 0.39 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 120 | 3 | 3.2 | 0.25 | 3 | 3.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 120 | 4 | 4.26 | 0.37 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 120 | 3.03 | 3.07 | 0.39 | 2.5 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 120 | 4.19 | 4.21 | 0.57 | 2.98 | 5.69 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 120 | 2.96 | 3.04 | 0.39 | 2.4 | 4.16 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 120 | 4.32 | 4.32 | 0.48 | 3.31 | 5.52 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 120 | 3 | 2.85 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 120 | 3 | 3.21 | 0.26 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 120 | 3 | 2.87 | 0.3 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 120 | 3 | 3.22 | 0.29 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 120 | 55 | 54.33 | 3.61 | 45 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 120 | 55 | 57.21 | 3.98 | 45 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 120 | 55 | 53.75 | 4.16 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 120 | 60 | 59.08 | 3.61 | 45 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 120 | 50 | 50.33 | 3.53 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 120 | 55 | 53.88 | 9.45 | 35 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 120 | 50 | 50.46 | 3.43 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 120 | 55 | 55.17 | 8.45 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 120 | 60 | 57.75 | 4.76 | 50 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 120 | 55 | 55.08 | 4.63 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 120 | 60 | 57.67 | 4.98 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 120 | 55 | 53.04 | 4.5 | 45 | 60 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 72 | 10 | 12.71 | 5.17 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 72 | 15 | 15.21 | 6.42 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 72 | 10 | 12.22 | 4.66 | 5 | 35 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 72 | 15 | 16.28 | 7.38 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 120 | 3 | 2.8 | 1.3 | -2 | 10 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 120 | 3 | 2.25 | 2.05 | -10 | 5 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 120 | 3 | 2.39 | 2.11 | -10 | 5 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 120 | 3 | 2.4 | 1.69 | -8 | 5 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 120 | 3.5 | 3.55 | 0.55 | 3 | 5 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 120 | 4 | 4.38 | 0.53 | 3 | 6 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 120 | 3.25 | 3.49 | 0.57 | 3 | 6 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 120 | 4 | 4.46 | 0.52 | 3 | 5.5 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 120 | 5 | 6.98 | 5.56 | 2 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 120 | 5 | 8.18 | 6.07 | 2 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 120 | 5 | 6.94 | 6.4 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 120 | 5 | 8.54 | 6.8 | 1 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 120 | 3 | 2.71 | 0.49 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 120 | 2 | 1.88 | 1.37 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 120 | 3 | 2.69 | 0.49 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 120 | 2 | 2.06 | 1.02 | -2 | 3 |

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
