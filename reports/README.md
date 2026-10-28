# SCE monthly survey · report

Updated 2026-10-28 12:21 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 960 | 960 | 12 | 0 | 1 | 2.01 |
| 2026-10 | B_web_nomemory | 960 | 960 | 12 | 0 | 0 | 10.22 |
| 2026-10 | C_noweb_memory | 960 | 960 | 12 | 0 | 0 | 1.87 |
| 2026-10 | D_web_memory | 960 | 960 | 12 | 0 | 1 | 10.22 |

Total cost so far: **$24.32**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 960 | 3 | 3.19 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 960 | 4 | 4.22 | 0.33 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 960 | 3 | 3.18 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 960 | 4 | 4.21 | 0.33 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 960 | 2.94 | 3.01 | 0.36 | 1.75 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 960 | 4.33 | 4.32 | 0.49 | 3.04 | 5.71 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 960 | 2.95 | 2.98 | 0.34 | 1.08 | 4.79 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 960 | 4.28 | 4.29 | 0.51 | 2.94 | 6.29 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 960 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 960 | 3 | 3.22 | 0.29 | 2.5 | 4.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 960 | 3 | 2.87 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 960 | 3 | 3.22 | 0.28 | 2.5 | 4 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 960 | 55 | 53.56 | 4.11 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 960 | 60 | 57.81 | 4.19 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 960 | 55 | 53.51 | 4.07 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 960 | 60 | 57.61 | 3.88 | 40 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 960 | 50 | 50.39 | 3.55 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 960 | 55 | 54.31 | 9.02 | 30 | 75 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 960 | 50 | 50.59 | 3.32 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 960 | 55 | 54.85 | 8.93 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 960 | 60 | 57.96 | 4.61 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 960 | 55 | 54.07 | 5.07 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 960 | 60 | 57.83 | 4.59 | 40 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 960 | 55 | 54.29 | 4.81 | 35 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 583 | 10 | 12.2 | 5.15 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 585 | 15 | 15.36 | 5.42 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 584 | 10 | 12.16 | 5.21 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 584 | 15 | 15.53 | 5.52 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 960 | 3 | 2.82 | 4.44 | -20 | 100 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 960 | 3 | 2.69 | 3.42 | -15 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 960 | 3 | 2.85 | 3.3 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 960 | 3 | 2.73 | 4.89 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 960 | 3.5 | 3.55 | 0.94 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 960 | 4.5 | 4.5 | 0.78 | -8 | 10 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 960 | 3.5 | 3.55 | 0.85 | -5 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 960 | 4.5 | 4.49 | 0.63 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 960 | 5 | 7.34 | 6.29 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 960 | 5 | 8.8 | 6.93 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 960 | 5 | 7.21 | 6.12 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 960 | 5 | 8.63 | 6.74 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 960 | 3 | 2.68 | 0.49 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 960 | 2 | 2.01 | 1.25 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 960 | 3 | 2.68 | 0.52 | -2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 960 | 2 | 2.05 | 1.15 | -2.5 | 3.5 |

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
