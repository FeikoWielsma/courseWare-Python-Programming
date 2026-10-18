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
    binge = plays > 10
    print(f"hours over 10 plays: {int(binge.sum())}")
    days, hours = np.nonzero(binge)
    for day, hour in zip(days, hours, strict=True):
        print(f"{DAYS[day]} {hour:02d}:00: {plays[day, hour]} plays")
    names = np.array(DAYS)
    print(names[binge.any(axis=1)])
    print(f"between 6 and 10: {int(((plays > 6) & (plays <= 10)).sum())}")


if __name__ == "__main__":
    main()
