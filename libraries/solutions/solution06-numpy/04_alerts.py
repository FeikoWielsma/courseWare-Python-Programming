from pathlib import Path

import numpy as np
from numpy.typing import NDArray

DATA: Path = Path(__file__).resolve().parents[2] / "data"
SERVERS: NDArray[np.str_] = np.array(["web01", "web02", "web03", "db01", "cache01"])
THRESHOLD: float = 80.0


def load_readings() -> NDArray[np.float64]:
    return np.loadtxt(DATA / "server-load.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))


def main() -> None:
    load = load_readings()

    busy = load > THRESHOLD
    print("mask shape :", busy.shape, "same as the data, one True or False each")
    print("readings over", THRESHOLD, "% :", int(busy.sum()))

    hours, servers = np.nonzero(busy)
    print("\nthe alerts, in order :")
    for hour, server in zip(hours, servers, strict=True):
        print(f"  {SERVERS[server]} at {hour:02d}:00 -> {load[hour, server]:.1f} %")

    # any() with an axis answers the question per server rather than overall.
    ever_busy = busy.any(axis=0)
    print("\never over the line :", ", ".join(SERVERS[ever_busy]))
    print("never over the line:", ", ".join(SERVERS[~ever_busy]))

    # Combining conditions needs brackets around each one, because & binds
    # tighter than the comparison operators do.
    middling = (load > 60.0) & (load <= THRESHOLD)
    print("\nreadings between 60 and 80 :", int(middling.sum()))


if __name__ == "__main__":
    main()
