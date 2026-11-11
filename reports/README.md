# SCE monthly survey · report

Updated 2026-11-11 13:15 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 440 | 440 | 11 | 0 | 0 | 1.18 |
| 2026-11 | B_web_nomemory | 440 | 440 | 11 | 0 | 0 | 4.97 |
| 2026-11 | C_noweb_memory | 440 | 440 | 11 | 0 | 1 | 1.32 |
| 2026-11 | D_web_memory | 440 | 440 | 11 | 0 | 1 | 5.16 |

Total cost so far: **$42.99**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 440 | 3 | 3.22 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 440 | 4 | 4.06 | 0.41 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 440 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 440 | 4.5 | 4.29 | 0.38 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 440 | 3 | 3.05 | 0.36 | 2.38 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 440 | 4.14 | 4.1 | 0.63 | 2.89 | 5.86 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 440 | 2.91 | 2.98 | 0.35 | 1.84 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 440 | 4.33 | 4.37 | 0.52 | 2.94 | 5.9 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 440 | 3 | 2.83 | 0.33 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 440 | 3 | 3.12 | 0.28 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 440 | 3 | 2.86 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 440 | 3 | 3.21 | 0.29 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 440 | 55 | 53.95 | 3.97 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 440 | 55 | 55.2 | 4.96 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 440 | 55 | 53.57 | 4.13 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 440 | 60 | 58.42 | 4.24 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 440 | 50 | 50.35 | 3.61 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 440 | 60 | 58.28 | 10.29 | 30 | 75 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 440 | 50 | 50.48 | 3.44 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 440 | 60 | 58.98 | 8.54 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 440 | 60 | 58.09 | 4.65 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 440 | 55 | 54.86 | 5.02 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 440 | 60 | 57.8 | 4.68 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 440 | 55 | 52.56 | 4.94 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 273 | 10 | 12.45 | 4.9 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 273 | 15 | 14.76 | 5.67 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 274 | 10 | 11.95 | 5.06 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 274 | 15 | 15.69 | 6.19 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 440 | 3 | 2.82 | 2.04 | -10 | 25 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 440 | 3 | 2.66 | 3.12 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 440 | 3 | 2.83 | 3.13 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 440 | 3 | 2.72 | 2.87 | -10 | 50 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 440 | 3.5 | 3.59 | 0.66 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 440 | 4 | 4.27 | 0.62 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 440 | 3 | 3.54 | 0.9 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 440 | 4.5 | 4.51 | 0.61 | 3 | 8 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 440 | 5 | 6.98 | 5.44 | 0 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 440 | 5 | 8.41 | 6.8 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 440 | 5 | 7.08 | 6.13 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 440 | 5 | 8.43 | 6.61 | 0 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 440 | 3 | 2.68 | 0.53 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 440 | 2 | 2.16 | 1.15 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 440 | 3 | 2.71 | 0.47 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 440 | 2 | 1.98 | 1.17 | -2 | 3 |

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
