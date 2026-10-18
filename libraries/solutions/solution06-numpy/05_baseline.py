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
    baseline = np.median(plays, axis=0)
    deviation = plays - baseline
    print(baseline.shape, deviation.shape)
    day, hour = np.unravel_index(np.argmax(deviation), deviation.shape)
    print(f"largest increase: {DAYS[day]} {hour:02d}:00, +{deviation[day, hour]:.1f}")
    capped = plays.copy()
    capped[capped > 10] = 10
    print(f"capped maximum: {capped.max()}, original maximum: {plays.max()}")


if __name__ == "__main__":
    main()
