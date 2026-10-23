from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

history = pd.read_csv(DATA / "sensor-history.csv", parse_dates=["last_changed"])

print(history.head(3))
print(history.dtypes)
print(history["entity_id"].value_counts())
