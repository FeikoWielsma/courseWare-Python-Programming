from pathlib import Path

import numpy as np
from numpy.typing import NDArray

DATA: Path = Path(__file__).resolve().parents[2] / "data"
SERVERS: list[str] = ["web01", "web02", "web03", "db01", "cache01"]


def load_readings() -> NDArray[np.float64]:
    return np.loadtxt(DATA / "server-load.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))


def main() -> None:
    load = load_readings()

    # axis=0 is the row dimension, so the hours go and the servers remain.
    means = load.mean(axis=0)
    lows = load.min(axis=0)
    highs = load.max(axis=0)
    print("mean(axis=0) has shape", means.shape, "-> one value per server")

    print(f"\n{'server':<9}{'mean':>8}{'min':>8}{'max':>8}")
    for name, mean, low, high in zip(SERVERS, means, lows, highs, strict=True):
        print(f"{name:<9}{mean:8.1f}{low:8.1f}{high:8.1f}")

    busiest = int(np.argmax(means))
    peakiest = int(np.argmax(highs))
    print(f"\nbusiest on average : {SERVERS[busiest]} at {means[busiest]:.1f} %")
    print(f"highest single peak: {SERVERS[peakiest]} at {highs[peakiest]:.1f} %")


if __name__ == "__main__":
    main()
