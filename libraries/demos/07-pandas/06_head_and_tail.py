from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"
COLUMNS = ["site", "role", "cpu_cores", "disk_gb"]

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

print(servers[COLUMNS].head())
print(servers[COLUMNS].head(2))
print(servers[COLUMNS].tail(3))

# Reproducible because the seed is fixed.
print(servers[COLUMNS].sample(3, random_state=0))
