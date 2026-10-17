from pathlib import Path

import numpy as np

DATA = Path(__file__).resolve().parents[2] / "data"
SERVERS = ["web01", "web02", "web03", "db01", "cache01"]

load = np.loadtxt(DATA / "server-load.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))
print(load)
print(load.shape, load.dtype)

# axis=0 collapses the hours, leaving one number per server.
for name, mean, peak in zip(SERVERS, load.mean(axis=0), load.max(axis=0), strict=True):
    print(f"{name:<8} mean {mean:5.1f} %   peak {peak:5.1f} %")

# axis=1 collapses the servers, leaving one number per hour.
per_hour = load.mean(axis=1)
print(int(np.argmax(per_hour)), "busiest hour")
print(int(np.argmin(per_hour)), "quietest hour")

# A mask reads as the question it answers.
hours, servers = np.nonzero(load > 80.0)
for hour, server in zip(hours, servers, strict=True):
    print(f"{SERVERS[server]} at {hour:02d}:00 -> {load[hour, server]:.1f} %")

# Writing an array back out is the mirror image of reading one in.
out = DATA / "server-load-hourly-mean.csv"
np.savetxt(out, per_hour, delimiter=",", fmt="%.2f")
print("wrote", out.name, per_hour.size, "rows")
