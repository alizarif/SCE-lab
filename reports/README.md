# SCE monthly survey · report

Updated 2026-11-06 13:14 · model `openai/gpt-6-luna` · arms: `A_noweb_nomemory` (web off, memory off), `B_web_nomemory` (web on, memory off), `C_noweb_memory` (web off, memory on), `D_web_memory` (web on, memory on)

## Progress

| wave | arm | interviews | people | days | question_errors | reasks | cost_usd |
|---|---|---|---|---|---|---|---|
| 2026-10 | A_noweb_nomemory | 1200 | 1200 | 15 | 0 | 1 | 2.52 |
| 2026-10 | B_web_nomemory | 1200 | 1200 | 15 | 0 | 0 | 12.76 |
| 2026-10 | C_noweb_memory | 1200 | 1200 | 15 | 0 | 0 | 2.33 |
| 2026-10 | D_web_memory | 1200 | 1200 | 15 | 0 | 1 | 12.76 |
| 2026-11 | A_noweb_nomemory | 240 | 240 | 6 | 0 | 0 | 0.64 |
| 2026-11 | B_web_nomemory | 240 | 240 | 6 | 0 | 0 | 2.72 |
| 2026-11 | C_noweb_memory | 240 | 240 | 6 | 0 | 0 | 0.72 |
| 2026-11 | D_web_memory | 240 | 240 | 6 | 0 | 1 | 2.82 |

Total cost so far: **$37.26**

## 2026-11: headline items

| item | label | arm | n | median | mean | sd | min | max |
|---|---|---|---|---|---|---|---|---|
| Q8v2part2 | Expected inflation rate (next 12 months) | A_noweb_nomemory | 240 | 3 | 3.22 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | B_web_nomemory | 240 | 4 | 4.11 | 0.4 | 3.5 | 5.5 |
| Q8v2part2 | Expected inflation rate (next 12 months) | C_noweb_memory | 240 | 3 | 3.2 | 0.25 | 3 | 4 |
| Q8v2part2 | Expected inflation rate (next 12 months) | D_web_memory | 240 | 4.5 | 4.26 | 0.35 | 3.5 | 5.5 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | A_noweb_nomemory | 240 | 3 | 3.05 | 0.37 | 2.38 | 4.92 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | B_web_nomemory | 240 | 4.18 | 4.18 | 0.62 | 2.98 | 5.86 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | C_noweb_memory | 240 | 2.9 | 3 | 0.35 | 2.36 | 4.16 |
| Q9_binmean | Inflation probabilities by range (next 12 months): mean using bin midpoints | D_web_memory | 240 | 4.33 | 4.36 | 0.49 | 3.3 | 5.56 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | A_noweb_nomemory | 240 | 3 | 2.84 | 0.33 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | B_web_nomemory | 240 | 3 | 3.16 | 0.28 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | C_noweb_memory | 240 | 3 | 2.88 | 0.31 | 2.5 | 3.5 |
| Q9bv2part2 | Expected inflation rate (2–3 years ahead) | D_web_memory | 240 | 3 | 3.22 | 0.28 | 2.5 | 3.5 |
| Q4new | Chance U.S. unemployment is higher (12 months) | A_noweb_nomemory | 240 | 55 | 54.12 | 4.05 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | B_web_nomemory | 240 | 55 | 56.15 | 4.8 | 40 | 65 |
| Q4new | Chance U.S. unemployment is higher (12 months) | C_noweb_memory | 240 | 55 | 53.77 | 4.07 | 40 | 60 |
| Q4new | Chance U.S. unemployment is higher (12 months) | D_web_memory | 240 | 60 | 59.35 | 3.87 | 45 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | A_noweb_nomemory | 240 | 50 | 50.48 | 3.58 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | B_web_nomemory | 240 | 55 | 52.46 | 9.85 | 30 | 70 |
| Q5new | Chance savings interest rates are higher (12 months) | C_noweb_memory | 240 | 50 | 50.44 | 3.47 | 40 | 60 |
| Q5new | Chance savings interest rates are higher (12 months) | D_web_memory | 240 | 55 | 55.67 | 8.54 | 35 | 75 |
| Q6new | Chance U.S. stock prices are higher (12 months) | A_noweb_nomemory | 240 | 60 | 57.77 | 4.83 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | B_web_nomemory | 240 | 55 | 54.48 | 5.16 | 40 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | C_noweb_memory | 240 | 60 | 57.58 | 4.82 | 45 | 65 |
| Q6new | Chance U.S. stock prices are higher (12 months) | D_web_memory | 240 | 55 | 52.54 | 4.99 | 40 | 65 |
| Q13new | Chance of losing main job (12 months) | A_noweb_nomemory | 141 | 10 | 12.59 | 4.69 | 5 | 40 |
| Q13new | Chance of losing main job (12 months) | B_web_nomemory | 141 | 15 | 15.04 | 5.43 | 5 | 50 |
| Q13new | Chance of losing main job (12 months) | C_noweb_memory | 141 | 10 | 11.77 | 4.44 | 5 | 35 |
| Q13new | Chance of losing main job (12 months) | D_web_memory | 142 | 15 | 16.01 | 6.4 | 5 | 60 |
| Q25v2part2 | Expected household income change (%) | A_noweb_nomemory | 240 | 3 | 2.74 | 1.43 | -5 | 10 |
| Q25v2part2 | Expected household income change (%) | B_web_nomemory | 240 | 3 | 2.32 | 2.22 | -10 | 10 |
| Q25v2part2 | Expected household income change (%) | C_noweb_memory | 240 | 3 | 2.55 | 2.08 | -10 | 10 |
| Q25v2part2 | Expected household income change (%) | D_web_memory | 240 | 3 | 2.44 | 1.95 | -10 | 8 |
| Q26v2part2 | Expected household spending change (%) | A_noweb_nomemory | 240 | 3.5 | 3.56 | 0.6 | 3 | 6 |
| Q26v2part2 | Expected household spending change (%) | B_web_nomemory | 240 | 4 | 4.34 | 0.54 | 3 | 6 |
| Q26v2part2 | Expected household spending change (%) | C_noweb_memory | 240 | 3.5 | 3.55 | 0.71 | 3 | 8 |
| Q26v2part2 | Expected household spending change (%) | D_web_memory | 240 | 4.5 | 4.5 | 0.59 | 3 | 8 |
| Q30new | Chance of missing a minimum debt payment (3 months) | A_noweb_nomemory | 240 | 5 | 7.2 | 5.89 | 0 | 35 |
| Q30new | Chance of missing a minimum debt payment (3 months) | B_web_nomemory | 240 | 5 | 8.77 | 6.87 | 2 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | C_noweb_memory | 240 | 5 | 7.38 | 6.29 | 0 | 50 |
| Q30new | Chance of missing a minimum debt payment (3 months) | D_web_memory | 240 | 5 | 9.01 | 7.07 | 1 | 50 |
| Q31v2part2 | Expected national home price change (%) | A_noweb_nomemory | 240 | 3 | 2.64 | 0.58 | -2.5 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | B_web_nomemory | 240 | 2 | 2.11 | 1.16 | -3 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | C_noweb_memory | 240 | 3 | 2.68 | 0.48 | 2 | 3.5 |
| Q31v2part2 | Expected national home price change (%) | D_web_memory | 240 | 2 | 1.95 | 1.19 | -2 | 3 |

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
