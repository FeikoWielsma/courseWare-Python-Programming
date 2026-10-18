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
    means = plays.mean(axis=1)
    lows = plays.min(axis=1)
    highs = plays.max(axis=1)
    for day, mean, low, high in zip(DAYS, means, lows, highs, strict=True):
        print(f"{day}: mean {mean:.1f}, min {low}, max {high}")
    print(f"busiest day: {DAYS[int(np.argmax(means))]}")


if __name__ == "__main__":
    main()
