from pathlib import Path

import numpy as np
from numpy.typing import NDArray

DATA: Path = Path(__file__).resolve().parents[2] / "data"


def load_readings() -> NDArray[np.float64]:
    return np.loadtxt(DATA / "server-load.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))


def bar(value: float, scale: float = 1.0) -> str:
    return "#" * int(round(value * scale))


def main() -> None:
    load = load_readings()

    # axis=1 is the column dimension, so the servers go and the hours remain.
    per_hour = load.mean(axis=1)
    print("mean(axis=1) has shape", per_hour.shape, "-> one value per hour")

    # The rows are in order from midnight, so the row number is the hour.
    busiest = int(np.argmax(per_hour))
    quietest = int(np.argmin(per_hour))
    print(f"\nbusiest hour  : {busiest:02d}:00 at {per_hour[busiest]:.1f} % mean")
    print(f"quietest hour : {quietest:02d}:00 at {per_hour[quietest]:.1f} % mean")

    print("\nthe shape of the day, mean load per hour :")
    for hour, value in enumerate(per_hour):
        print(f"  {hour:02d}:00 {value:5.1f} {bar(value, 0.5)}")


if __name__ == "__main__":
    main()
