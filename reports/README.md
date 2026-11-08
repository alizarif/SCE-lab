# SCE monthly survey · report

Updated 2026-11-08 13:14 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 320 | 320 | 8 | 0 | 0 | 0.85 |
| 2026-11 | B_web_nomemory | 320 | 320 | 8 | 0 | 0 | 3.62 |
| 2026-11 | C_noweb_memory | 320 | 320 | 8 | 0 | 0 | 0.96 |
| 2026-11 | D_web_memory | 320 | 320 | 8 | 0 | 1 | 3.75 |

Total cost so far: **$39.55**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 320 | 3 | 3.23 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 320 | 4 | 4.03 | 0.41 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 320 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 320 | 4 | 4.23 | 0.34 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 320 | 3 | 3.05 | 0.37 | 2.38 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 320 | 4.14 | 4.08 | 0.64 | 2.89 | 5.86 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 320 | 2.91 | 3 | 0.36 | 1.84 | 4.16 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 320 | 4.3 | 4.32 | 0.49 | 3.3 | 5.56 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 320 | 3 | 2.83 | 0.33 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 320 | 3 | 3.13 | 0.28 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 320 | 3 | 2.86 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 320 | 3 | 3.21 | 0.29 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 320 | 55 | 54.06 | 4.06 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 320 | 55 | 55.28 | 5.17 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 320 | 55 | 53.66 | 4.08 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 320 | 60 | 58.5 | 4.37 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 320 | 50 | 50.36 | 3.79 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 320 | 60 | 55.19 | 9.98 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 320 | 50 | 50.38 | 3.57 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 320 | 60 | 57.2 | 8.52 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 320 | 60 | 58 | 4.81 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 320 | 55 | 54.5 | 5.21 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 320 | 60 | 57.75 | 4.76 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 320 | 55 | 52.61 | 4.9 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 196 | 10 | 12.57 | 4.8 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 196 | 15 | 14.97 | 6.07 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 197 | 10 | 11.88 | 5.37 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 197 | 15 | 15.91 | 6.36 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 320 | 3 | 2.91 | 2.01 | -5 | 25 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 320 | 3 | 2.67 | 3.46 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 320 | 3 | 2.91 | 3.52 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 320 | 3 | 2.75 | 3.25 | -10 | 50 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 320 | 3.5 | 3.6 | 0.69 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 320 | 4 | 4.29 | 0.66 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 320 | 3.5 | 3.59 | 0.87 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 320 | 4 | 4.48 | 0.63 | 3 | 8 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 320 | 5 | 7.22 | 5.99 | 0 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 320 | 5 | 8.53 | 6.98 | 2 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 320 | 5 | 7.35 | 6.41 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 320 | 5 | 8.72 | 6.71 | 1 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 320 | 3 | 2.68 | 0.55 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 320 | 2 | 2.22 | 1.08 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 320 | 3 | 2.7 | 0.47 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 320 | 2 | 2 | 1.16 | -2 | 3 |

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
