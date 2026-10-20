# SCE monthly survey · report

Updated 2026-10-20 12:19 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 320 | 320 | 4 | 0 | 0 | 0.67 |
| 2026-10 | B_web_nomemory | 320 | 320 | 4 | 0 | 0 | 3.42 |
| 2026-10 | C_noweb_memory | 320 | 320 | 4 | 0 | 0 | 0.62 |
| 2026-10 | D_web_memory | 320 | 320 | 4 | 0 | 1 | 3.42 |

Total cost so far: **$8.13**

## 2026-10: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 320 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 320 | 4 | 4.14 | 0.35 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 320 | 3 | 3.18 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 320 | 4 | 4.15 | 0.33 | 3.5 | 4.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 320 | 2.89 | 3.01 | 0.36 | 2.24 | 4.48 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 320 | 4.18 | 4.18 | 0.52 | 3.04 | 5.51 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 320 | 2.97 | 2.98 | 0.34 | 2.3 | 4.42 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 320 | 4.19 | 4.18 | 0.49 | 3.04 | 5.26 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 320 | 3 | 2.88 | 0.32 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 320 | 3 | 3.17 | 0.3 | 2.5 | 4 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 320 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 320 | 3 | 3.19 | 0.28 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 320 | 55 | 53.47 | 4.19 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 320 | 60 | 59.27 | 3.59 | 40 | 70 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 320 | 55 | 53.36 | 4.16 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 320 | 60 | 59.03 | 3.04 | 45 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 320 | 50 | 50.33 | 3.62 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 320 | 55 | 51.7 | 8.37 | 30 | 65 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 320 | 50 | 50.56 | 3.41 | 35 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 320 | 55 | 51.62 | 8.4 | 35 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 320 | 60 | 58.19 | 4.46 | 45 | 70 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 320 | 55 | 54.72 | 4.78 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 320 | 60 | 58.09 | 4.63 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 320 | 55 | 54.83 | 4.34 | 45 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 200 | 10 | 11.82 | 4.84 | 5 | 60 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 201 | 15 | 15.47 | 5.21 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 201 | 10 | 11.92 | 5.56 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 201 | 15 | 15.97 | 5.76 | 5 | 45 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 320 | 3 | 2.86 | 3.7 | -20 | 50 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 320 | 3 | 2.84 | 3.6 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 320 | 3 | 2.97 | 3.42 | -10 | 50 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 320 | 3 | 2.88 | 5.88 | -10 | 100 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 320 | 3.5 | 3.54 | 1.14 | -10 | 10 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 320 | 4 | 4.48 | 0.7 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 320 | 3.5 | 3.57 | 0.74 | 3 | 10 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 320 | 4 | 4.5 | 0.72 | 3 | 10 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 320 | 5 | 7.22 | 6.41 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 320 | 5 | 8.46 | 7.06 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 320 | 5 | 7.38 | 6.93 | 0 | 60 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 320 | 5 | 8.69 | 7.61 | 0 | 60 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 320 | 3 | 2.71 | 0.45 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 320 | 2 | 1.68 | 1.39 | -2.5 | 3 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 320 | 3 | 2.74 | 0.45 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 320 | 2 | 1.7 | 1.36 | -2.5 | 3.5 |

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
