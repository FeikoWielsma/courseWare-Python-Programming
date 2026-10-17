from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

CRITICALITY = {
    "web": "front line",
    "database": "critical",
    "cache": "front line",
    "build": "internal",
    "logging": "internal",
    "mail": "critical",
    "storage": "critical",
    "network": "critical",
    "monitoring": "internal",
}

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

# .str gives every string method, applied down the column.
servers["distro"] = servers["os"].str.split().str[0]
servers["family"] = servers["role"].str.upper().str[:3]

# .map translates values through a dictionary.
servers["tier"] = servers["role"].map(CRITICALITY)

# np.where is a vectorised if-else : one condition, two answers.
used_pct = servers["used_gb"] / servers["disk_gb"] * 100
servers["alert"] = np.where(used_pct > 75, "FULL", "ok")

# A missing value never compares true, so the host that was never measured
# would quietly read "ok".
servers.loc[used_pct.isna(), "alert"] = "unknown"

print(servers[["role", "distro", "family", "tier", "alert"]].head(8))

print(sorted(servers["distro"].unique()))
print(servers["tier"].value_counts().to_dict())
print(servers["alert"].value_counts().to_dict())
