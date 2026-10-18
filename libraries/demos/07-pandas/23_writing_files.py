from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

report = tracks.reset_index().sort_values("plays", ascending=False)
report.to_csv(DATA / "tracks-report.csv", index=False)
report.to_csv(DATA / "tracks-report.tsv", sep="\t", index=False)
per_genre = tracks.groupby("genre", as_index=False)["plays"].sum()
with pd.ExcelWriter(DATA / "tracks-report.xlsx", engine="openpyxl") as workbook:
    report.to_excel(workbook, sheet_name="tracks", index=False)
    per_genre.to_excel(workbook, sheet_name="per genre", index=False)
print(pd.ExcelFile(DATA / "tracks-report.xlsx").sheet_names)
