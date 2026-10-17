from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")
print(servers.index)

by_host = servers.set_index("hostname")
print(by_host.index)
print(by_host.loc["db01", ["site", "role", "memory_gb"]])

# This is the part that has no spreadsheet equivalent.
quota = pd.Series([500, 2000, 8000], index=["web01", "db01", "log01"], name="quota_gb")
used = pd.Series([6600.0, 1450.0, 64.5], index=["log01", "db01", "web01"], name="used_gb")

print(quota)
print(used)
# Subtracting aligns on the label, not the row number.
print(quota - used)
