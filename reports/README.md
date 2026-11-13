# SCE monthly survey · report

Updated 2026-11-13 15:13 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 520 | 520 | 13 | 0 | 0 | 1.39 |
| 2026-11 | B_web_nomemory | 520 | 520 | 13 | 0 | 0 | 5.87 |
| 2026-11 | C_noweb_memory | 520 | 520 | 13 | 0 | 2 | 1.56 |
| 2026-11 | D_web_memory | 520 | 520 | 13 | 0 | 1 | 6.09 |

Total cost so far: **$45.28**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 520 | 3 | 3.23 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 520 | 4 | 4.15 | 0.46 | 3.5 | 6.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 520 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 520 | 4.5 | 4.37 | 0.42 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 520 | 3.01 | 3.06 | 0.36 | 2.38 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 520 | 4.19 | 4.2 | 0.65 | 2.89 | 6.69 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 520 | 2.93 | 2.99 | 0.36 | 1.84 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 520 | 4.41 | 4.44 | 0.54 | 2.94 | 6.17 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 520 | 3 | 2.84 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 520 | 3 | 3.16 | 0.29 | 2.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 520 | 3 | 2.87 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 520 | 3 | 3.23 | 0.29 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 520 | 55 | 54.01 | 3.97 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 520 | 55 | 55.55 | 5.16 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 520 | 55 | 53.69 | 4.07 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 520 | 60 | 58.53 | 4.39 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 520 | 50 | 50.33 | 3.55 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 520 | 65 | 59.71 | 10.13 | 30 | 75 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 520 | 50 | 50.51 | 3.38 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 520 | 60 | 60.01 | 8.46 | 35 | 80 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 520 | 60 | 58.05 | 4.64 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 520 | 55 | 54.61 | 4.95 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 520 | 60 | 57.81 | 4.62 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 520 | 55 | 52.3 | 4.93 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 321 | 10 | 12.74 | 5.23 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 321 | 15 | 15.11 | 5.86 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 322 | 10 | 12.17 | 5.09 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 324 | 15 | 16.15 | 6.3 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 520 | 3 | 2.85 | 2.11 | -10 | 25 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 520 | 3 | 2.66 | 3.06 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 520 | 3 | 2.84 | 2.98 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 520 | 3 | 2.72 | 2.75 | -10 | 50 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 520 | 3.5 | 3.6 | 0.68 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 520 | 4 | 4.32 | 0.75 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 520 | 3.5 | 3.56 | 0.89 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 520 | 4.5 | 4.57 | 0.62 | 3 | 8 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 520 | 5 | 7.15 | 5.64 | 0 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 520 | 5 | 8.57 | 6.76 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 520 | 5 | 7.13 | 5.99 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 520 | 5 | 8.7 | 6.81 | 0 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 520 | 3 | 2.68 | 0.52 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 520 | 2 | 2.13 | 1.16 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 520 | 3 | 2.71 | 0.47 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 520 | 2 | 1.96 | 1.2 | -2.5 | 3 |

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
