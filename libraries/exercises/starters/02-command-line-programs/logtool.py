from collections import Counter
from pathlib import Path

LOGFILE = Path("data") / "listening.log"


def main() -> None:
    counts: Counter[tuple[str, str]] = Counter()
    for line in LOGFILE.read_text(encoding="utf-8").splitlines():
        _day, _time, level, action, title = line.split(maxsplit=4)
        if level == "INFO" and action in {"PLAY", "SKIP"}:
            counts[action, title] += 1
    for title in sorted({title for _action, title in counts}):
        print(f"{title} PLAY={counts['PLAY', title]} SKIP={counts['SKIP', title]}")


if __name__ == "__main__":
    main()
