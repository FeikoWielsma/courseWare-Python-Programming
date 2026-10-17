from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")

# Each keyword becomes an output column name; each value is the pair (column to
# summarise, summary to apply).
per_site = (
    servers.groupby("site")
    .agg(
        servers=("hostname", "count"),
        total_cores=("cpu_cores", "sum"),
        total_disk_gb=("disk_gb", "sum"),
        mean_used_gb=("used_gb", "mean"),
    )
    .round(1)
    .reset_index()
)
print(per_site)

# The result is an ordinary frame, so it sorts and filters.
print(per_site.sort_values("total_cores", ascending=False))

# Grouping by two keys is the same call with a list. as_index=False keeps the
# answer flat and readable.
print(
    servers.groupby(["site", "role"], as_index=False)
    .agg(servers=("hostname", "count"), cores=("cpu_cores", "sum"))
    .head(8)
)
