from pathlib import Path

import numpy as np
from numpy.typing import NDArray

DATA: Path = Path(__file__).resolve().parents[2] / "data"
CSV: Path = DATA / "server-load.csv"

SERVERS: list[str] = ["web01", "web02", "web03", "db01", "cache01"]


def load_readings() -> NDArray[np.float64]:
    return np.loadtxt(CSV, delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))


def main() -> None:
    load = load_readings()

    print("file  :", CSV.name)
    print("shape :", load.shape, " (24 hours by 5 servers)")
    print("dtype :", load.dtype)
    print("size  :", load.size, "readings in total")

    print("\ncolumns :", ", ".join(SERVERS))
    print("first two rows :")
    print(load[:2])


if __name__ == "__main__":
    main()
