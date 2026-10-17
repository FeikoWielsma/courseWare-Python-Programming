from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

print(servers.loc["db01", "memory_gb"])
print(servers.loc["db01"])
print(servers.loc["db01", ["site", "role", "disk_gb"]])
print(servers.loc[:, ["site", "role"]].head(3))

# A label slice includes both ends. That is unlike every other slice in Python,
# and it is the single most surprising thing about loc.
print(servers.loc["web01":"db01", "site":"os"])
