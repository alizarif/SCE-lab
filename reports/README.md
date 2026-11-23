# SCE monthly survey · report

Updated 2026-11-23 13:13 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on), `E_customweb_nomemory` (web own searches, memory off, from 2026-12)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 920 | 920 | 23 | 0 | 0 | 2.45 |
| 2026-11 | B_web_nomemory | 920 | 920 | 23 | 0 | 0 | 10.42 |
| 2026-11 | C_noweb_memory | 920 | 920 | 23 | 0 | 5 | 2.75 |
| 2026-11 | D_web_memory | 920 | 920 | 23 | 0 | 3 | 10.81 |

Total cost so far: **$56.80**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 920 | 3 | 3.22 | 0.26 | 3 | 4.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 920 | 4.5 | 4.26 | 0.45 | 3.5 | 6.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 920 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 920 | 4.5 | 4.43 | 0.44 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 920 | 3.01 | 3.05 | 0.36 | 2.11 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 920 | 4.36 | 4.35 | 0.64 | 2.89 | 6.69 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 920 | 2.96 | 2.99 | 0.34 | 1.84 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 920 | 4.53 | 4.5 | 0.55 | 2.94 | 6.27 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 920 | 3 | 2.83 | 0.32 | 2 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 920 | 3 | 3.21 | 0.3 | 2.5 | 4.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 920 | 3 | 2.88 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 920 | 3.5 | 3.25 | 0.29 | 2.5 | 4.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 920 | 55 | 53.79 | 3.97 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 920 | 55 | 55.12 | 5.08 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 920 | 55 | 53.66 | 4.02 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 920 | 60 | 58.36 | 4.14 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 920 | 50 | 50.4 | 3.47 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 920 | 65 | 63.04 | 9 | 30 | 80 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 920 | 50 | 50.63 | 3.35 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 920 | 65 | 62.55 | 7.99 | 35 | 80 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 920 | 60 | 58.14 | 4.56 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 920 | 55 | 54.41 | 4.84 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 920 | 60 | 57.82 | 4.55 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 920 | 50 | 52.02 | 5.01 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 558 | 10 | 12.62 | 5.12 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 559 | 15 | 14.94 | 5.85 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 559 | 10 | 12.08 | 5.04 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 565 | 15 | 16.03 | 6.13 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 920 | 3 | 3 | 4.39 | -10 | 100 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 920 | 3 | 2.82 | 4.53 | -15 | 100 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 920 | 3 | 2.92 | 3.7 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 920 | 3 | 2.75 | 4.13 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 920 | 3.5 | 3.61 | 0.75 | -2 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 920 | 4 | 4.42 | 0.71 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 920 | 3.5 | 3.57 | 0.83 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 920 | 5 | 4.63 | 0.63 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 920 | 5 | 7.37 | 5.98 | 0 | 40 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 920 | 5 | 8.73 | 6.95 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 920 | 5 | 7.18 | 5.88 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 920 | 5 | 8.66 | 6.58 | 0 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 920 | 3 | 2.69 | 0.5 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 920 | 2 | 1.68 | 1.58 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 920 | 3 | 2.69 | 0.5 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 920 | 2 | 1.84 | 1.28 | -3 | 3.5 |

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
