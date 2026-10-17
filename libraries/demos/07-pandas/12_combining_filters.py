from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"
COLUMNS = ["site", "role", "cpu_cores", "disk_gb"]

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

# & and | rather than and and or, because and and or ask a whole Series for one
# true-or-false answer and it refuses.
print(servers[(servers["cpu_cores"] >= 8) & (servers["disk_gb"] >= 2000)][COLUMNS])
print(servers[(servers["role"] == "database") | (servers["role"] == "build")][COLUMNS])

# ~ negates a mask.
print(servers[~servers["site"].isin(["AMS", "RTM"])][COLUMNS])

# isin replaces a chain of ORs.
print(servers[servers["role"].isin(["cache", "logging", "storage"])][COLUMNS])

# between replaces two comparisons, and includes both ends.
print(servers[servers["memory_gb"].between(8, 64)][COLUMNS])
