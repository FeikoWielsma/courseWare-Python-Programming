from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_excel(DATA / "tracks.xlsx", sheet_name="tracks")
print(pd.ExcelFile(DATA / "tracks.xlsx").sheet_names)
print(tracks[["title", "genre", "plays"]].head(3))
