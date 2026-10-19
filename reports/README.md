# SCE monthly survey · report

Updated 2026-10-19 14:48 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 240 | 240 | 3 | 0 | 0 | 0.5 |
| 2026-10 | B_web_nomemory | 240 | 240 | 3 | 0 | 0 | 2.56 |
| 2026-10 | C_noweb_memory | 240 | 240 | 3 | 0 | 0 | 0.47 |
| 2026-10 | D_web_memory | 240 | 240 | 3 | 0 | 1 | 2.56 |

Total cost so far: **$6.08**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 240 | 3 | 3.21 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 240 | 4 | 4.2 | 0.33 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 240 | 3 | 3.2 | 0.26 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 240 | 4 | 4.19 | 0.31 | 3.5 | 4.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 240 | 2.98 | 3.04 | 0.38 | 2.24 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 240 | 4.24 | 4.28 | 0.49 | 3.04 | 5.51 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 240 | 3.01 | 3.01 | 0.35 | 2.3 | 4.42 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 240 | 4.2 | 4.24 | 0.45 | 3.04 | 5.26 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 240 | 3 | 2.91 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 240 | 3 | 3.2 | 0.29 | 2.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 240 | 3 | 2.89 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 240 | 3 | 3.22 | 0.27 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 240 | 55 | 53.46 | 4.26 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 240 | 60 | 59.15 | 3.57 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 240 | 55 | 53.5 | 4.04 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 240 | 60 | 59.06 | 3.15 | 45 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 240 | 50 | 50.31 | 3.69 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 240 | 55 | 51.69 | 8.46 | 30 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 240 | 50 | 50.77 | 3.53 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 240 | 55 | 50.94 | 8.41 | 35 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 240 | 60 | 58.15 | 4.53 | 45 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 240 | 55 | 54.4 | 4.98 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 240 | 60 | 58 | 4.81 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 240 | 55 | 54.73 | 4.48 | 45 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 146 | 10 | 11.61 | 3.57 | 5 | 25 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 147 | 15 | 15.34 | 4.88 | 5 | 35 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 147 | 10 | 11.87 | 4.97 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 147 | 15 | 15.95 | 5.47 | 5 | 35 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 240 | 3 | 2.92 | 3.98 | -20 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 240 | 3 | 2.85 | 3.89 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 240 | 3 | 2.98 | 3.84 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 240 | 3 | 2.96 | 6.68 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 240 | 3.5 | 3.57 | 1.21 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 240 | 4.5 | 4.57 | 0.74 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 240 | 3.5 | 3.62 | 0.79 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 240 | 4.5 | 4.58 | 0.76 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 240 | 5 | 7.14 | 6.43 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 240 | 5 | 8.57 | 7.33 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 240 | 5 | 7.41 | 6.89 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 240 | 5 | 8.59 | 7.45 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 240 | 3 | 2.71 | 0.46 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 240 | 2 | 1.68 | 1.42 | -2.5 | 3 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 240 | 3 | 2.75 | 0.45 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 240 | 2 | 1.71 | 1.37 | -2 | 3.5 |

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
