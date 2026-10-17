from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")

# One grouping column, one column to summarise, one summary function. The
# grouping column becomes the index of the answer.
print(servers.groupby("site")["cpu_cores"].sum())
print(servers.groupby("role")["disk_gb"].mean().round(1))
print(servers.groupby("site").size())

# agg takes a list of functions and gives a column for each.
print(servers.groupby("site")["memory_gb"].agg(["count", "sum", "mean", "max"]).round(1))

# A dictionary applies a different summary to each column.
print(servers.groupby("site").agg({"cpu_cores": "sum", "disk_gb": "max", "used_gb": "mean"}))
