import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
LOG = DATA / "listening.log"
LEVELS = ("INFO", "WARN", "ERROR")
TIMEOUT = 5.0


def require(program: str) -> None:
    if shutil.which(program) is None:
        print(f"{program} is not installed or not on PATH", file=sys.stderr)
        raise SystemExit(1)


def count_matches(pattern: str, path: Path) -> int:
    found = subprocess.run(
        ["grep", "-c", pattern, str(path)],
        capture_output=True,
        text=True,
        check=False,
        timeout=TIMEOUT,
    )
    if found.returncode > 1:
        raise RuntimeError(f"grep failed: {found.stderr.strip()}")
    return int(found.stdout.strip() or 0)


def tally_with_commands(path: Path) -> Counter[str]:
    matched = subprocess.run(
        ["grep", "-o", "-E", "|".join(LEVELS), str(path)],
        capture_output=True,
        text=True,
        check=False,
        timeout=TIMEOUT,
    )
    if matched.returncode > 1:
        raise RuntimeError(f"grep failed: {matched.stderr.strip()}")

    ordered = subprocess.run(
        ["sort"], input=matched.stdout, capture_output=True, text=True, check=True, timeout=TIMEOUT
    )
    summary = subprocess.run(
        ["uniq", "-c"],
        input=ordered.stdout,
        capture_output=True,
        text=True,
        check=True,
        timeout=TIMEOUT,
    )

    tally: Counter[str] = Counter()
    for line in summary.stdout.strip().splitlines():
        count, level = line.split()
        tally[level] = int(count)
    return tally


def tally_with_python(path: Path) -> Counter[str]:
    text = path.read_text(encoding="utf-8")
    return Counter(level for line in text.splitlines() for level in LEVELS if level in line)


def show_timeout() -> None:
    sleeper = [sys.executable, "-c", "import time; time.sleep(30)"]
    try:
        subprocess.run(sleeper, timeout=1.0, check=True)
    except subprocess.TimeoutExpired as error:
        print(f"timed out after {error.timeout} seconds, as intended")


def main() -> int:
    require("grep")
    require("sort")
    require("uniq")

    print("errors, via grep -c :", count_matches("ERROR", LOG))
    print()

    commands = tally_with_commands(LOG)
    python = tally_with_python(LOG)

    print(f"{'level':<8}{'commands':>10}{'python':>10}")
    for level in LEVELS:
        print(f"{level:<8}{commands[level]:>10}{python[level]:>10}")

    print()
    print("agree :", commands == python)
    print()
    show_timeout()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
