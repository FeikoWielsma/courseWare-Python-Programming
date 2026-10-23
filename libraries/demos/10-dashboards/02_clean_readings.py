from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

history = pd.read_csv(DATA / "sensor-history.csv", parse_dates=["last_changed"])
history["value"] = pd.to_numeric(history["state"], errors="coerce")

print(history[history["value"].isna()]["state"].value_counts())

readings = history.dropna(subset=["value"])
print(len(history), "rows,", len(readings), "readings")
