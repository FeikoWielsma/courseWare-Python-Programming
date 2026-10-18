import matplotlib

matplotlib.use("Agg")

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

tracks["decade"] = tracks["year"] // 10 * 10
per_decade = tracks.groupby("decade")["plays"].sum()
axes = per_decade.plot(kind="bar", title="Fictional plays by decade")
axes.set_ylabel("plays")
axes.get_figure().tight_layout()
axes.get_figure().savefig(DATA / "tracks-plot.png", dpi=120)
plt.close(axes.get_figure())
print(per_decade)
