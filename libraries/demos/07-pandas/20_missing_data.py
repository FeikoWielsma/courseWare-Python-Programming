from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

# An empty field in the file becomes NaN. isna() gives a mask of the same
# shape, and summing a mask counts it.
print(servers.isna().sum())
print(servers[servers.isna().any(axis=1)][["site", "used_gb", "last_patched"]])

# dropna() removes every row with any hole, which is usually too much.
print(len(servers), len(servers.dropna()))
print(len(servers.dropna(subset=["used_gb"])))

# fillna with a dictionary fills each column with its own sensible value, which
# is safer than one blanket value for the whole frame.
filled = servers.fillna({"used_gb": 0.0, "last_patched": "never"})
print(filled[["site", "used_gb", "last_patched"]].loc[["db02", "build02", "mon01"]])

# NaN is quietly skipped by the summaries, so a mean is a mean of what is
# there. Whether that is the answer you wanted is a judgement call.
print(round(servers["used_gb"].mean(), 1))
print(servers["used_gb"].count())
