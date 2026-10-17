from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
LOGFILE = DATA / "cli-sample.log"


def count_levels(path: Path) -> Counter[str]:
    return Counter(line.split()[2] for line in path.read_text(encoding="utf-8").splitlines())


def main() -> None:
    for level, count in count_levels(LOGFILE).most_common():
        print(f"{level:<6}{count}")


if __name__ == "__main__":
    main()
