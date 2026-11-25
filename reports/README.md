# SCE monthly survey · report

Updated 2026-11-25 13:13 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on), `E_customweb_nomemory` (web own searches, memory off, from 2026-12)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 1000 | 1000 | 25 | 0 | 1 | 2.67 |
| 2026-11 | B_web_nomemory | 1000 | 1000 | 25 | 0 | 0 | 11.32 |
| 2026-11 | C_noweb_memory | 1000 | 1000 | 25 | 0 | 5 | 3 |
| 2026-11 | D_web_memory | 1000 | 1000 | 25 | 0 | 3 | 11.76 |

Total cost so far: **$59.12**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 1000 | 3 | 3.21 | 0.26 | 3 | 4.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 1000 | 4.5 | 4.23 | 0.46 | 3.5 | 6.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 1000 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 1000 | 4.5 | 4.42 | 0.43 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 1000 | 3 | 3.05 | 0.36 | 2.11 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 1000 | 4.33 | 4.31 | 0.64 | 2.71 | 6.69 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 1000 | 2.96 | 2.99 | 0.34 | 1.84 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 1000 | 4.51 | 4.49 | 0.55 | 2.94 | 6.27 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 1000 | 3 | 2.84 | 0.32 | 2 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 1000 | 3 | 3.2 | 0.3 | 2.5 | 4.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 1000 | 3 | 2.88 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 1000 | 3.5 | 3.24 | 0.29 | 2.5 | 4.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 1000 | 55 | 53.74 | 3.97 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 1000 | 55 | 55.16 | 5.23 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 1000 | 55 | 53.6 | 3.99 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 1000 | 60 | 58.52 | 4.14 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 1000 | 50 | 50.33 | 3.51 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 1000 | 65 | 63.41 | 8.78 | 30 | 80 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 1000 | 50 | 50.6 | 3.34 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 1000 | 65 | 62.79 | 7.87 | 35 | 80 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 1000 | 60 | 58.12 | 4.61 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 1000 | 55 | 54.29 | 4.82 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 1000 | 60 | 57.82 | 4.53 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 1000 | 50 | 51.83 | 4.99 | 35 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 611 | 10 | 12.6 | 5.08 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 612 | 15 | 14.89 | 5.77 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 612 | 10 | 12.06 | 5.06 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 618 | 15 | 16.1 | 6.12 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 1000 | 3 | 2.99 | 4.5 | -10 | 100 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 1000 | 3 | 2.82 | 4.62 | -15 | 100 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 1000 | 3 | 2.93 | 3.88 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 1000 | 3 | 2.82 | 5.04 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 1000 | 3.5 | 3.6 | 0.73 | -2 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 1000 | 4 | 4.39 | 0.71 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 1000 | 3.5 | 3.56 | 0.83 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 1000 | 5 | 4.62 | 0.63 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 1000 | 5 | 7.31 | 6.01 | 0 | 40 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 1000 | 5 | 8.66 | 6.93 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 1000 | 5 | 7.18 | 6.06 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 1000 | 5 | 8.67 | 6.61 | 0 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 1000 | 3 | 2.69 | 0.52 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 1000 | 2 | 1.7 | 1.54 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 1000 | 3 | 2.7 | 0.49 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 1000 | 2 | 1.83 | 1.28 | -3 | 3.5 |

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
