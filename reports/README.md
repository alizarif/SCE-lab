# SCE monthly survey · report

Updated 2026-10-23 12:31 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 560 | 560 | 7 | 0 | 1 | 1.17 |
| 2026-10 | B_web_nomemory | 560 | 560 | 7 | 0 | 0 | 5.97 |
| 2026-10 | C_noweb_memory | 560 | 560 | 7 | 0 | 0 | 1.09 |
| 2026-10 | D_web_memory | 560 | 560 | 7 | 0 | 1 | 5.97 |

Total cost so far: **$14.20**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 560 | 3 | 3.2 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 560 | 4 | 4.22 | 0.33 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 560 | 3 | 3.18 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 560 | 4.5 | 4.23 | 0.35 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 560 | 2.94 | 3.01 | 0.36 | 2.24 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 560 | 4.31 | 4.31 | 0.51 | 3.04 | 5.71 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 560 | 2.95 | 2.98 | 0.33 | 2.04 | 4.42 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 560 | 4.31 | 4.3 | 0.53 | 3.02 | 6.29 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 560 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 560 | 3 | 3.22 | 0.29 | 2.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 560 | 3 | 2.87 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 560 | 3 | 3.23 | 0.28 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 560 | 55 | 53.62 | 4.09 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 560 | 60 | 58.55 | 3.79 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 560 | 55 | 53.51 | 4.12 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 560 | 60 | 58.48 | 3.21 | 45 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 560 | 50 | 50.43 | 3.53 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 560 | 55 | 53.03 | 8.57 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 560 | 50 | 50.57 | 3.27 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 560 | 55 | 53.12 | 8.62 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 560 | 60 | 58 | 4.46 | 45 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 560 | 55 | 54.04 | 5.19 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 560 | 60 | 57.89 | 4.55 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 560 | 55 | 54.3 | 4.83 | 35 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 344 | 10 | 12.06 | 5.03 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 345 | 15 | 15.51 | 5.21 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 345 | 10 | 12.16 | 5.29 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 345 | 15 | 15.81 | 5.62 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 560 | 3 | 2.77 | 3.71 | -20 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 560 | 3 | 2.68 | 3.67 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 560 | 3 | 2.85 | 3.47 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 560 | 3 | 2.68 | 4.67 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 560 | 3.5 | 3.54 | 0.97 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 560 | 4.5 | 4.49 | 0.84 | -8 | 8 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 560 | 3.5 | 3.56 | 0.81 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 560 | 4.5 | 4.53 | 0.66 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 560 | 5 | 7.42 | 6.59 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 560 | 5 | 8.77 | 7.13 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 560 | 5 | 7.38 | 6.59 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 560 | 5 | 8.75 | 7.17 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 560 | 3 | 2.68 | 0.5 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 560 | 2 | 1.76 | 1.38 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 560 | 3 | 2.69 | 0.5 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 560 | 2 | 1.8 | 1.32 | -2.5 | 3.5 |

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
