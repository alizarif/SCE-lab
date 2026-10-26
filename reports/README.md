# SCE monthly survey · report

Updated 2026-10-26 12:24 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 800 | 800 | 10 | 0 | 1 | 1.68 |
| 2026-10 | B_web_nomemory | 800 | 800 | 10 | 0 | 0 | 8.52 |
| 2026-10 | C_noweb_memory | 800 | 800 | 10 | 0 | 0 | 1.55 |
| 2026-10 | D_web_memory | 800 | 800 | 10 | 0 | 1 | 8.52 |

Total cost so far: **$20.28**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 800 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 800 | 4.5 | 4.24 | 0.33 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 800 | 3 | 3.18 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 800 | 4 | 4.23 | 0.33 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 800 | 2.94 | 3.02 | 0.35 | 2.22 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 800 | 4.33 | 4.33 | 0.49 | 3.04 | 5.71 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 800 | 2.95 | 2.99 | 0.34 | 2.04 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 800 | 4.28 | 4.3 | 0.51 | 3.02 | 6.29 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 800 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 800 | 3 | 3.23 | 0.28 | 2.5 | 4.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 800 | 3 | 2.86 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 800 | 3 | 3.23 | 0.27 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 800 | 55 | 53.62 | 4.12 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 800 | 60 | 58.04 | 4.22 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 800 | 55 | 53.51 | 4.11 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 800 | 60 | 57.81 | 3.86 | 40 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 800 | 50 | 50.41 | 3.55 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 800 | 55 | 53.2 | 8.49 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 800 | 50 | 50.65 | 3.26 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 800 | 55 | 53.72 | 8.44 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 800 | 60 | 57.89 | 4.65 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 800 | 55 | 53.8 | 5.03 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 800 | 60 | 57.75 | 4.61 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 800 | 55 | 54.06 | 4.78 | 35 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 485 | 10 | 12.22 | 5.36 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 486 | 15 | 15.41 | 5.56 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 486 | 10 | 12.23 | 5.43 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 486 | 15 | 15.59 | 5.6 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 800 | 3 | 2.72 | 3.34 | -20 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 800 | 3 | 2.62 | 3.27 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 800 | 3 | 2.81 | 3.11 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 800 | 3 | 2.62 | 4.04 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 800 | 3.5 | 3.56 | 0.92 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 800 | 4.5 | 4.51 | 0.79 | -8 | 8 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 800 | 3.5 | 3.55 | 0.83 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 800 | 4.5 | 4.52 | 0.65 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 800 | 5 | 7.34 | 6.47 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 800 | 5 | 8.73 | 6.99 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 800 | 5 | 7.24 | 6.36 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 800 | 5 | 8.54 | 6.8 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 800 | 3 | 2.67 | 0.5 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 800 | 2 | 1.9 | 1.31 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 800 | 3 | 2.67 | 0.53 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 800 | 2 | 1.94 | 1.21 | -2.5 | 3.5 |

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
