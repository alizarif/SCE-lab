# SCE monthly survey · report

Updated 2026-11-07 13:12 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 280 | 280 | 7 | 0 | 0 | 0.75 |
| 2026-11 | B_web_nomemory | 280 | 280 | 7 | 0 | 0 | 3.17 |
| 2026-11 | C_noweb_memory | 280 | 280 | 7 | 0 | 0 | 0.84 |
| 2026-11 | D_web_memory | 280 | 280 | 7 | 0 | 1 | 3.28 |

Total cost so far: **$38.40**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 280 | 3 | 3.22 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 280 | 4 | 4.04 | 0.43 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 280 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 280 | 4 | 4.24 | 0.35 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 280 | 3.02 | 3.05 | 0.37 | 2.38 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 280 | 4.08 | 4.06 | 0.66 | 2.89 | 5.86 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 280 | 2.91 | 3 | 0.35 | 2.36 | 4.16 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 280 | 4.33 | 4.34 | 0.48 | 3.3 | 5.56 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 280 | 3 | 2.83 | 0.33 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 280 | 3 | 3.14 | 0.29 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 280 | 3 | 2.86 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 280 | 3 | 3.21 | 0.29 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 280 | 55 | 54.11 | 4.05 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 280 | 55 | 55.46 | 5.27 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 280 | 55 | 53.75 | 4 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 280 | 60 | 58.71 | 4.39 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 280 | 50 | 50.39 | 3.81 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 280 | 55 | 54.29 | 10.27 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 280 | 50 | 50.5 | 3.51 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 280 | 55 | 56.8 | 8.66 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 280 | 60 | 57.96 | 4.75 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 280 | 55 | 54.96 | 5.12 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 280 | 60 | 57.7 | 4.75 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 280 | 55 | 52.7 | 4.9 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 170 | 10 | 12.52 | 4.82 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 170 | 15 | 14.94 | 6.3 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 170 | 10 | 12 | 5.64 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 171 | 15 | 15.96 | 6.54 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 280 | 3 | 2.81 | 1.61 | -5 | 15 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 280 | 3 | 2.5 | 2.34 | -10 | 15 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 280 | 3 | 2.73 | 2.44 | -10 | 20 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 280 | 3 | 2.56 | 1.94 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 280 | 3.5 | 3.58 | 0.65 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 280 | 4 | 4.3 | 0.67 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 280 | 3.5 | 3.57 | 0.79 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 280 | 4 | 4.5 | 0.62 | 3 | 8 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 280 | 5 | 7.23 | 6.04 | 0 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 280 | 5 | 8.56 | 6.91 | 2 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 280 | 5 | 7.32 | 6.56 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 280 | 5 | 8.82 | 6.88 | 1 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 280 | 3 | 2.67 | 0.56 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 280 | 2 | 2.23 | 1.12 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 280 | 3 | 2.7 | 0.48 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 280 | 2 | 2 | 1.15 | -2 | 3 |

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
