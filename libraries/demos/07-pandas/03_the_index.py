from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv")

by_title = tracks.set_index("title")
print(by_title.loc["Imagine", ["artist", "duration_s"]])
durations = pd.Series([183, 126], index=["Imagine", "Yesterday"])
limits = pd.Series([180, 240], index=["Yesterday", "Imagine"])
print(limits - durations)
