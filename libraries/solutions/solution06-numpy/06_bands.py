from pathlib import Path

import numpy as np
from numpy.typing import NDArray

DATA: Path = Path(__file__).resolve().parents[2] / "data"
SERVERS: list[str] = ["web01", "web02", "web03", "db01", "cache01"]
BANDS: list[str] = ["critical", "warning", "fine"]


def load_readings() -> NDArray[np.float64]:
    return np.loadtxt(DATA / "server-load.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))


def classify(load: NDArray[np.float64]) -> NDArray[np.str_]:
    return np.where(load > 90.0, "critical", np.where(load > 60.0, "warning", "fine"))


def main() -> None:
    load = load_readings()
    labels = classify(load)

    print("labels shape :", labels.shape, "dtype", labels.dtype)
    print("\nreadings per band :")
    for band in BANDS:
        print(f"  {band:<9} {int((labels == band).sum()):>3}")

    # A mask of booleans sums along an axis just as numbers do.
    warnings_per_server = (labels == "warning").sum(axis=0)
    criticals_per_server = (labels == "critical").sum(axis=0)
    print("\nper server :")
    for name, warn, crit in zip(SERVERS, warnings_per_server, criticals_per_server, strict=True):
        print(f"  {name:<9} {int(warn)} warning, {int(crit)} critical")

    out = DATA / "server-load-hourly-mean.csv"
    np.savetxt(out, load.mean(axis=1), delimiter=",", fmt="%.2f")
    print(f"\nwrote {out.name}, {load.shape[0]} hourly means")


if __name__ == "__main__":
    main()
