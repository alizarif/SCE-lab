# SCE monthly survey · report

Updated 2026-11-16 22:03 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 640 | 640 | 16 | 0 | 0 | 1.71 |
| 2026-11 | B_web_nomemory | 640 | 640 | 16 | 0 | 0 | 7.24 |
| 2026-11 | C_noweb_memory | 640 | 640 | 16 | 0 | 4 | 1.92 |
| 2026-11 | D_web_memory | 640 | 640 | 16 | 0 | 1 | 7.51 |

Total cost so far: **$48.75**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 640 | 3 | 3.23 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 640 | 4 | 4.22 | 0.48 | 3.5 | 6.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 640 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 640 | 4.5 | 4.42 | 0.43 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 640 | 3.02 | 3.06 | 0.36 | 2.38 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 640 | 4.3 | 4.3 | 0.67 | 2.89 | 6.69 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 640 | 2.96 | 3 | 0.35 | 1.84 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 640 | 4.5 | 4.49 | 0.56 | 2.94 | 6.27 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 640 | 3 | 2.83 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 640 | 3 | 3.19 | 0.3 | 2.5 | 4.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 640 | 3 | 2.88 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 640 | 3.5 | 3.24 | 0.3 | 2.5 | 4.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 640 | 55 | 53.91 | 3.98 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 640 | 55 | 55.24 | 5.13 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 640 | 55 | 53.7 | 4.01 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 640 | 60 | 58.43 | 4.31 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 640 | 50 | 50.36 | 3.51 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 640 | 65 | 61.02 | 9.71 | 30 | 75 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 640 | 50 | 50.62 | 3.38 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 640 | 60 | 60.92 | 8.2 | 35 | 80 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 640 | 60 | 58.11 | 4.63 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 640 | 55 | 54.57 | 4.78 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 640 | 60 | 57.89 | 4.61 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 640 | 55 | 52.2 | 4.96 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 402 | 10 | 12.71 | 4.97 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 403 | 15 | 15.17 | 5.99 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 403 | 10 | 12.17 | 4.85 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 406 | 15 | 16.24 | 6.37 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 640 | 3 | 2.91 | 2.8 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 640 | 3 | 2.71 | 3.04 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 640 | 3 | 2.89 | 3.41 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 640 | 3 | 2.7 | 2.69 | -10 | 50 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 640 | 3.5 | 3.61 | 0.71 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 640 | 4 | 4.38 | 0.73 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 640 | 3.5 | 3.57 | 0.87 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 640 | 5 | 4.61 | 0.61 | 3 | 8 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 640 | 5 | 7.29 | 5.74 | 0 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 640 | 5 | 8.57 | 6.52 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 640 | 5 | 7.21 | 5.9 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 640 | 5 | 8.78 | 6.68 | 0 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 640 | 3 | 2.68 | 0.51 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 640 | 2 | 1.98 | 1.31 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 640 | 3 | 2.7 | 0.47 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 640 | 2 | 1.94 | 1.21 | -2.5 | 3.5 |

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
