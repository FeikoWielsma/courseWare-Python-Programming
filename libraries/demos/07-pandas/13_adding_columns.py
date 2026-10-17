from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

# A scalar on the right-hand side is broadcast to every row.
servers["managed"] = True

# A Series on the right-hand side is computed element by element. There is no
# loop to write, and no loop worth writing.
servers["free_gb"] = servers["disk_gb"] - servers["used_gb"]
servers["used_pct"] = (servers["used_gb"] / servers["disk_gb"] * 100).round(1)
print(servers[["disk_gb", "used_gb", "free_gb", "used_pct", "managed"]].head(5))

# assign returns a new frame rather than modifying this one, which is what you
# want in the middle of a chain.
report = (
    servers.assign(gb_per_core=lambda frame: (frame["memory_gb"] / frame["cpu_cores"]).round(2))
    .sort_values("gb_per_core", ascending=False)
    .head(4)
)
print(report[["site", "role", "cpu_cores", "memory_gb", "gb_per_core"]])

print(servers.drop(columns=["managed", "free_gb"]).columns.tolist())
