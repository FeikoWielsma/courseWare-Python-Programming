from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv", parse_dates=["last_patched"])

servers.info()

# print(servers.describe().round(1).to_string())
print(servers.describe(include="str").to_string())

# # The non-null counts in info() are the fastest missing-data check there is.
# print(servers.isna().sum())
