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
    per_hour = plays.mean(axis=0)
    busiest = int(np.argmax(per_hour))
    quietest = int(np.argmin(per_hour))
    print(f"busiest hour: {busiest:02d}:00, mean {per_hour[busiest]:.1f} plays")
    print(f"quietest hour: {quietest:02d}:00, mean {per_hour[quietest]:.1f} plays")
    for hour, value in enumerate(per_hour):
        print(f"{hour:02d}:00 {value:.1f} {'#' * int(round(value))}")


if __name__ == "__main__":
    main()
