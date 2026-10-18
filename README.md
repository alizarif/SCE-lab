# SCE monthly survey

The New York Fed Survey of Consumer Expectations (SCE) core questionnaire, run every month on 1,200 LLM personas
built from real SCE respondents. It runs every day on GitHub, on its own, until you stop it.

* **Who answers:** `participants.xlsx`, one row per person (1,200 drawn at random from the SCE respondents who joined the panel in 2016 or later, seed 2222), with the person's own SCE answers and their commuting zone.
  Each person's system prompt is the final persona template: role, who you are, numeracy questions with their answers
  and score. Exact SCE wording throughout; the age is the one the person reported in the SCE.
* **What is asked:** `questionnaire.xlsx`, the monthly core module in exact SCE wording and order, with the SCE's
  skip rules (labour questions depend on the employment answer, part-2 rates follow the direction, and so on).
  Intro screens are shown with the next question. Probabilities that do not add up to 100 are asked once more, as the
  SCE web form does. Repeat respondents (from their 2nd month) also get the home-price and commodity block C1–C4.
* **When:** every day at 8 am New York time. Each month every person is interviewed once: all 1,200 are spread evenly
  over the survey days of the month (from October 17: 15 days × 80 people; November: 30 days × 40 people). The day
  is drawn at random again every month, so someone interviewed on the 5th this month can be on any day next month.
* **Four types (arms):** every person is interviewed in all four, as separate conversations on the same day:

  | arm | web search | remembers last months |
  |---|---|---|
  | `A_noweb_nomemory` | no | no |
  | `B_web_nomemory` | yes, top 10 results | no |
  | `C_noweb_memory` | no | yes |
  | `D_web_memory` | yes, top 10 results | yes |
