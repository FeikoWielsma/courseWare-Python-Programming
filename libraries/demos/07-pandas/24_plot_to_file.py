from pathlib import Path

# Agg draws to a file and never opens a window, which is what a script wants.
# matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")
servers["free_gb"] = servers["disk_gb"] - servers["used_gb"]

per_site = servers.groupby("site")[["used_gb", "free_gb"]].sum().round(0).sort_values("used_gb")
print(per_site)
servers.plot()
figure, axes = plt.subplots(1, 2, figsize=(11, 4.5))

# The frame plots itself; ax= says which panel to draw into.
per_site.plot(kind="barh", stacked=True, ax=axes[0])
axes[0].set_title("Disk used and free, by site")
axes[0].set_xlabel("GB")

servers.groupby("role")["cpu_cores"].sum().sort_values().plot(kind="bar", ax=axes[1])
axes[1].set_title("CPU cores by role")
axes[1].set_ylabel("cores")

figure.tight_layout()
plt.plot()
plt.show()
output = DATA / "servers-plot.png"
figure.savefig(output, dpi=120)
plt.close(figure)
print(output.name, output.stat().st_size, "bytes")
