import sys
from pathlib import Path


def describe(argv: list[str]) -> None:
    print(f"program : {Path(argv[0]).name}")
    print(f"count   : {len(argv) - 1} argument(s) after the program name")
    for index, value in enumerate(argv[1:], start=1):
        print(f"  argv[{index}] = {value!r}")


if __name__ == "__main__":
    # Running the file bare would show an empty list, which teaches nothing, so
    # a sample command line stands in when no arguments are given.
    sample = [sys.argv[0], "report", "--limit", "5", "hosts.txt"]
    describe(sys.argv if len(sys.argv) > 1 else sample)
