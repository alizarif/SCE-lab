# SCE monthly survey · report

Updated 2026-10-21 12:18 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 400 | 400 | 5 | 0 | 0 | 0.84 |
| 2026-10 | B_web_nomemory | 400 | 400 | 5 | 0 | 0 | 4.26 |
| 2026-10 | C_noweb_memory | 400 | 400 | 5 | 0 | 0 | 0.78 |
| 2026-10 | D_web_memory | 400 | 400 | 5 | 0 | 1 | 4.27 |

Total cost so far: **$10.15**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 400 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 400 | 4 | 4.16 | 0.33 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 400 | 3 | 3.17 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 400 | 4 | 4.16 | 0.34 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 400 | 2.9 | 3.02 | 0.36 | 2.24 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 400 | 4.19 | 4.23 | 0.51 | 3.04 | 5.51 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 400 | 2.95 | 2.98 | 0.33 | 2.04 | 4.42 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 400 | 4.19 | 4.2 | 0.5 | 3.02 | 5.37 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 400 | 3 | 2.88 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 400 | 3 | 3.19 | 0.29 | 2.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 400 | 3 | 2.86 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 400 | 3 | 3.2 | 0.28 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 400 | 55 | 53.48 | 4.12 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 400 | 60 | 59.34 | 3.45 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 400 | 55 | 53.3 | 4.13 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 400 | 60 | 59.05 | 3.02 | 45 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 400 | 50 | 50.3 | 3.6 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 400 | 55 | 52.79 | 8.59 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 400 | 50 | 50.51 | 3.35 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 400 | 55 | 52.6 | 8.46 | 35 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 400 | 60 | 58.05 | 4.49 | 45 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 400 | 55 | 55.08 | 4.8 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 400 | 60 | 58 | 4.57 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 400 | 55 | 55.14 | 4.41 | 45 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 247 | 10 | 11.64 | 4.47 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 248 | 15 | 15.26 | 5.11 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 248 | 10 | 11.9 | 5.25 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 248 | 15 | 15.71 | 5.53 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 400 | 3 | 2.78 | 3.39 | -20 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 400 | 3 | 2.74 | 3.32 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 400 | 3 | 2.94 | 3.07 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 400 | 3 | 2.81 | 5.3 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 400 | 3.5 | 3.53 | 1.05 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 400 | 4 | 4.47 | 0.67 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 400 | 3.5 | 3.58 | 0.71 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 400 | 4 | 4.5 | 0.69 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 400 | 5 | 7.07 | 6.15 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 400 | 5 | 8.45 | 6.93 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 400 | 5 | 7.23 | 6.52 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 400 | 5 | 8.57 | 7.18 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 400 | 3 | 2.71 | 0.45 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 400 | 2 | 1.54 | 1.51 | -2.5 | 3 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 400 | 3 | 2.72 | 0.46 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 400 | 2 | 1.6 | 1.44 | -2.5 | 3.5 |

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
