# SCE monthly survey · report

Updated 2026-10-25 12:18 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 720 | 720 | 9 | 0 | 1 | 1.51 |
| 2026-10 | B_web_nomemory | 720 | 720 | 9 | 0 | 0 | 7.66 |
| 2026-10 | C_noweb_memory | 720 | 720 | 9 | 0 | 0 | 1.4 |
| 2026-10 | D_web_memory | 720 | 720 | 9 | 0 | 1 | 7.67 |

Total cost so far: **$18.24**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 720 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 720 | 4.5 | 4.23 | 0.33 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 720 | 3 | 3.18 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 720 | 4 | 4.23 | 0.34 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 720 | 2.95 | 3.02 | 0.35 | 2.24 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 720 | 4.33 | 4.32 | 0.49 | 3.04 | 5.71 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 720 | 2.95 | 2.98 | 0.34 | 2.04 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 720 | 4.29 | 4.29 | 0.52 | 3.02 | 6.29 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 720 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 720 | 3 | 3.22 | 0.28 | 2.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 720 | 3 | 2.86 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 720 | 3 | 3.22 | 0.28 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 720 | 55 | 53.6 | 4.2 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 720 | 60 | 58.65 | 3.63 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 720 | 55 | 53.51 | 4.09 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 720 | 60 | 58.4 | 3.29 | 45 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 720 | 50 | 50.35 | 3.54 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 720 | 55 | 53.35 | 8.46 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 720 | 50 | 50.6 | 3.29 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 720 | 55 | 53.66 | 8.52 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 720 | 60 | 57.92 | 4.6 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 720 | 55 | 53.81 | 5.09 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 720 | 60 | 57.83 | 4.58 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 720 | 55 | 54.08 | 4.8 | 35 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 445 | 10 | 12.11 | 5.14 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 446 | 15 | 15.41 | 5.42 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 446 | 10 | 12.13 | 5.07 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 446 | 15 | 15.67 | 5.51 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 720 | 3 | 2.74 | 3.36 | -20 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 720 | 3 | 2.62 | 3.35 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 720 | 3 | 2.8 | 3.14 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 720 | 3 | 2.65 | 4.17 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 720 | 3.5 | 3.54 | 0.9 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 720 | 4.5 | 4.5 | 0.78 | -8 | 8 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 720 | 3.5 | 3.53 | 0.8 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 720 | 4.5 | 4.51 | 0.63 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 720 | 5 | 7.25 | 6.35 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 720 | 5 | 8.62 | 6.83 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 720 | 5 | 7.2 | 6.25 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 720 | 5 | 8.51 | 6.86 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 720 | 3 | 2.68 | 0.5 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 720 | 2 | 1.89 | 1.33 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 720 | 3 | 2.68 | 0.53 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 720 | 2 | 1.93 | 1.23 | -2.5 | 3.5 |

All items, by day and by month: [stats_daily.csv](stats_daily.csv) · [stats_monthly.csv](stats_monthly.csv) · one row per interview: [wide/](wide/)

## Trends

Solid line = median · dashed = mean · band = mean ± SD · dotted = min and max.

### Q8v2part2 · Expected inflation rate (next 12 months)
![Q8v2part2: median by arm](charts/compare_Q8v2part2.png)
![Q8v2part2 by day](charts/daily_Q8v2part2.png)

### Q9_binmean · Inflation probabilities by range (next 12 months): mean using bin midpoints
![Q9_binmean: median by arm](charts/compare_Q9_binmean.png)
![Q9_binmean by day](charts/daily_Q9_binmean.png)

### Q9bv2part2 · Expected inflation rate (2–3 years ahead)
![Q9bv2part2: median by arm](charts/compare_Q9bv2part2.png)
![Q9bv2part2 by day](charts/daily_Q9bv2part2.png)

### Q4new · Chance U.S. unemployment is higher (12 months)
![Q4new: median by arm](charts/compare_Q4new.png)
![Q4new by day](charts/daily_Q4new.png)

### Q5new · Chance savings interest rates are higher (12 months)
![Q5new: median by arm](charts/compare_Q5new.png)
![Q5new by day](charts/daily_Q5new.png)

### Q6new · Chance U.S. stock prices are higher (12 months)
![Q6new: median by arm](charts/compare_Q6new.png)
![Q6new by day](charts/daily_Q6new.png)

### Q13new · Chance of losing main job (12 months)
![Q13new: median by arm](charts/compare_Q13new.png)
![Q13new by day](charts/daily_Q13new.png)

### Q25v2part2 · Expected household income change (%)
![Q25v2part2: median by arm](charts/compare_Q25v2part2.png)
![Q25v2part2 by day](charts/daily_Q25v2part2.png)

### Q26v2part2 · Expected household spending change (%)
![Q26v2part2: median by arm](charts/compare_Q26v2part2.png)
![Q26v2part2 by day](charts/daily_Q26v2part2.png)

### Q30new · Chance of missing a minimum debt payment (3 months)
![Q30new: median by arm](charts/compare_Q30new.png)
![Q30new by day](charts/daily_Q30new.png)

### Q31v2part2 · Expected national home price change (%)
![Q31v2part2: median by arm](charts/compare_Q31v2part2.png)
![Q31v2part2 by day](charts/daily_Q31v2part2.png)
