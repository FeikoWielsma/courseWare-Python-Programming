from pathlib import Path

import numpy as np
from numpy.typing import NDArray

DATA: Path = Path(__file__).resolve().parents[2] / "data"
SERVERS: list[str] = ["web01", "web02", "web03", "db01", "cache01"]
CEILING: float = 90.0


def load_readings() -> NDArray[np.float64]:
    return np.loadtxt(DATA / "server-load.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))


def main() -> None:
    load = load_readings()

    # median(axis=0) is (5,) and load is (24, 5). Lined up from the right the
    # 5s match, so the baseline applies to every row with no reshaping.
    baseline = np.median(load, axis=0)
    deviation = load - baseline
    print("baseline shape  :", baseline.shape)
    print("deviation shape :", deviation.shape)

    print("\nfurthest above its own normal :")
    worst_per_server = deviation.max(axis=0)
    for name, base, worst in zip(SERVERS, baseline, worst_per_server, strict=True):
        print(f"  {name:<9} median {base:5.1f} %   worst +{worst:5.1f} points")

    # argmax on a 2-D array counts through the flattened array, so the position
    # has to be unravelled back into a row and a column.
    hour, server = np.unravel_index(np.argmax(deviation), deviation.shape)
    print(
        f"\nworst reading overall : {SERVERS[server]} at {hour:02d}:00, "
        f"{deviation[hour, server]:.1f} points above its median"
    )

    # A slice or a mask writes through to the parent, so cap a copy.
    capped = load.copy()
    capped[capped > CEILING] = CEILING
    print(f"\ncapped at {CEILING} % : max is now {capped.max():.1f} %")
    print(f"original untouched : max is still {load.max():.1f} %")


if __name__ == "__main__":
    main()
