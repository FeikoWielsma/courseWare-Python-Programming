from pathlib import Path

import numpy as np
from numpy.typing import NDArray

DATA: Path = Path(__file__).resolve().parents[2] / "data"
DAYS: list[str] = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def load_plays() -> NDArray[np.int64]:
    return np.loadtxt(DATA / "plays-hourly.csv", delimiter=",", skiprows=1,
                      usecols=range(1, 25), dtype=np.int64)


def main() -> None:
    plays = load_plays()
    print(plays.shape, plays.dtype, plays.size)
    print(plays[:2, :6])


if __name__ == "__main__":
    main()
