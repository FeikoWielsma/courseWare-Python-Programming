import os
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"


def log(message: str) -> None:
    print(message, file=sys.stderr)


def emit(path: Path) -> int:
    log(f"reading {path.name}")
    log(f"stdout is a terminal: {sys.stdout.isatty()}")

    written = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        service = line.split()[3].rstrip(":")
        print(service)
        written += 1
    log(f"wrote {written} lines")
    return written


def main() -> int:
    try:
        emit(DATA / "cli-sample.log")
    except BrokenPipeError:
        # `...
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        log("downstream stopped reading, which is normal")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
