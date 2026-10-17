# Quality check

Run 2026-10-17 on `participants.xlsx` (1,200 people) and `questionnaire.xlsx`.

- people in participants.xlsx: 1,200 (unique: True); in the microdata file: 1,200; same set: True
- values re-derived from the microdata and compared: 84,000 cells, 0 differences
- questionnaire: 59 included rows render with every placeholder filled and parse: yes
- skip logic: 1800 answer combinations walked (22 distinct routes); routes differing from the PDF rules: 0

## participants.xlsx findings

| severity   | check       |   findings |   people |
|:-----------|:------------|-----------:|---------:|
| warning    | consistency |         42 |       42 |
| warning    | range       |          1 |        1 |
| warning    | routing     |        161 |      158 |

Errors are problems in our files. Warnings are how the respondent actually answered the SCE (kept as reported).

## questionnaire.xlsx findings

none