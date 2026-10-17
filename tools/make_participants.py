"""Build participants.xlsx (one row per person) from SCE microdata rows of the sampled people.

Input: a CSV/XLSX with the SCE public-microdata columns for the sampled people, one or more rows per userid, e.g.
the file `sample_all_interviews_....csv` written by SCE_Sample_1200.ipynb (all interviews, all variables).

    python tools/make_participants.py path/to/sample_all_interviews_....csv
    python tools/make_participants.py path/to/sample.csv --out participants.xlsx --preview-date 2026-10-16

Which answers are used (the SCE asks the persona questions at a person's first interview):
  * work items (Q10 employment, Q11 jobs, Q12new, ES1, ES2, Q37, Q15, Q16, Q19) come from ONE interview: the first
    one with an age (Q32), so they describe the same moment;
  * every other item: the first answer the person gave, in date order.
"""
import argparse
import sys
from datetime import date
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sce_survey.persona import persona_text                      # noqa: E402
from sce_survey.questionnaire import Questionnaire               # noqa: E402

WORK = (["Q11", "Q12new", "ES2", "Q37", "Q15", "Q16", "Q19"] + [f"Q10_{i}" for i in range(1, 11)]
        + [f"ES1_{i}" for i in range(1, 5)])
SETS = {"Q35": 6, "HH2": 11, "Q45new": 9}          # multi-answer items stored as dummies: taken together
SINGLE = ["Q32", "Q33", "Q34", "Q36", "Q38", "Q41", "Q42", "Q43", "Q43a", "Q44", "Q45b", "Q46",
          "QRA1", "QRA2", "Q47", "QNUM1", "QNUM2", "QNUM3", "QNUM5", "QNUM6", "QNUM8", "QNUM9",
          "_REGION_CAT", "_AGE_CAT", "_EDU_CAT", "_HH_INC_CAT", "_NUM_CAT"]


def build(df):
    df = df.copy()
    df["date"] = pd.to_numeric(df["date"], errors="coerce")
    df = df.sort_values(["userid", "date"])
    rows = []
    for uid, g in df.groupby("userid", sort=True):
        anchor = g[g["Q32"].notna()].head(1) if "Q32" in g else g.head(0)
        anchor = anchor.iloc[0] if len(anchor) else g.iloc[0]
        r = {"userid": int(uid), "first_interview": int(anchor["date"]) if pd.notna(anchor["date"]) else None,
             "sce_interviews": int(len(g)), "sce_first_month": int(g["date"].min()), "sce_last_month": int(g["date"].max()),
             "weight": round(float(pd.to_numeric(g.get("weight"), errors="coerce").mean()), 6) if "weight" in g else None}
        for c in WORK:
            r[c] = anchor.get(c) if c in g else None
        # state and commuting zone from the same (earliest) interview, so they always agree
        both = g[g["_STATE"].notna() & g["_COMMUTING_ZONE"].notna()]
        st = both["_STATE"] if len(both) else g["_STATE"].dropna()
        czs = both["_COMMUTING_ZONE"] if len(both) else g["_COMMUTING_ZONE"].dropna()
        r["_STATE"] = st.iloc[0] if len(st) else None
        r["_COMMUTING_ZONE"] = int(czs.iloc[0]) if len(czs) else None
        for c in SINGLE:
            if c in g:
                s = g[c].dropna()
                r[c] = s.iloc[0] if len(s) else None
        for base, n in SETS.items():
            cols = [f"{base}_{i}" for i in range(1, n + 1) if f"{base}_{i}" in g]
            if not cols:
                continue
            filled = g[cols].apply(pd.to_numeric, errors="coerce")
            has = filled[(filled.fillna(0) > 0).any(axis=1)]
            pick = has.iloc[0] if len(has) else filled.dropna(how="all").head(1).squeeze() if filled.notna().any().any() else None
            for c in cols:
                r[c] = None if pick is None else pick.get(c)
        rows.append(r)
    return pd.DataFrame(rows)


def add_commuting_zones(people, path):
    """Names for the SCE commuting-zone codes (= USDA ERS 2000 Commuting Zone IDs), from commuting_zones_2000.xlsx."""
    path = Path(path)
    if not path.exists():
        print(f"{path.name} not found: no commuting-zone names added")
        return people
    cz = pd.read_excel(path, sheet_name=0)
    cz = cz.rename(columns={"CZ2000": "_COMMUTING_ZONE", "states": "cz_states", "main_county": "cz_main_county",
                            "n_counties": "cz_n_counties", "cz_population_2000": "cz_population_2000"})
    keep = ["_COMMUTING_ZONE", "cz_name", "cz_states", "cz_main_county", "cz_n_counties", "cz_population_2000"]
    people["_COMMUTING_ZONE"] = pd.to_numeric(people["_COMMUTING_ZONE"], errors="coerce").astype("Int64")
    cz["_COMMUTING_ZONE"] = cz["_COMMUTING_ZONE"].astype("Int64")
    out = people.merge(cz[keep], on="_COMMUTING_ZONE", how="left")
    # a missing state is filled from the commuting zone when the zone lies in one state only
    out["state_source"] = out["_STATE"].notna().map({True: "microdata", False: ""})
    one = out["_STATE"].isna() & out["cz_states"].notna() & ~out["cz_states"].fillna("").str.contains(",")
    out.loc[one, "_STATE"] = out.loc[one, "cz_states"]
    out.loc[one, "state_source"] = "from commuting zone"
    print(f"commuting zone named for {out['cz_name'].notna().sum():,} of {len(out):,} people")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="CSV or XLSX with SCE microdata rows of the sampled people")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "participants.xlsx"))
    ap.add_argument("--cz", default=str(Path(__file__).resolve().parent.parent / "commuting_zones_2000.xlsx"),
                    help="commuting-zone names (USDA ERS 2000 IDs)")
    ap.add_argument("--preview-date", default=date.today().isoformat(),
                    help="date used for the persona_preview column (age grows with the date)")
    a = ap.parse_args()
    src = Path(a.source)
    df = pd.read_csv(src, low_memory=False) if src.suffix.lower() == ".csv" else pd.read_excel(src)
    people = add_commuting_zones(build(df), a.cz)
    qn = Questionnaire()
    d = date.fromisoformat(a.preview_date)
    people["persona_preview"] = [persona_text(r, d, qn) for r in people.to_dict("records")]
    with pd.ExcelWriter(a.out) as w:
        people.to_excel(w, sheet_name="participants", index=False)
        pd.DataFrame({"column": ["userid", "first_interview", "sce_interviews", "weight", "persona_preview",
                                 "_COMMUTING_ZONE, cz_*", "everything else"],
                      "meaning": ["SCE respondent id", "YYYYMM of the interview the persona comes from (age is counted from here)",
                                  "number of real SCE interviews of this person", "mean SCE survey weight",
                                  f"the persona text as of {d} (read only: the survey rebuilds it every day from the columns)",
                                  "SCE commuting zone = USDA ERS 2000 Commuting Zone ID; cz_name etc. from commuting_zones_2000.xlsx "
                                  "(from the same interview as the state)",
                                  "SCE public-microdata variables with their microdata codes; edit with care"]}
                     ).to_excel(w, sheet_name="about", index=False)
    print(f"wrote {a.out}: {len(people):,} people")


if __name__ == "__main__":
    main()
