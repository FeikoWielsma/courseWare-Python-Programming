import argparse
import sys
import warnings
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
SAMPLE = DATA / "cli-sample.log"


def with_filetype(argv: list[str]) -> None:
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        parser = argparse.ArgumentParser()
        # "-" means standard input, which is the one genuinely nice thing here.
        parser.add_argument("source", type=argparse.FileType("r", encoding="utf-8"))
        for warning in caught:
            print(f"{warning.category.__name__}: {warning.message}")

    args = parser.parse_args(argv)
    print(f"opened {args.source.name}, first line: {args.source.readline().strip()}")
    # Nothing closed this for you, and nothing would have if parsing had failed
    # after the file was already open.
    args.source.close()


def with_pathlib(argv: list[str]) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    args = parser.parse_args(argv)

    with args.source.open(encoding="utf-8") as stream:
        print(f"opened {args.source.name}, first line: {stream.readline().strip()}")
    # The file is shut here, whatever happened in the block.


if __name__ == "__main__":
    source = sys.argv[1:] or [str(SAMPLE)]
    print("-- argparse.FileType")
    with_filetype(source)
    print("\n-- type=Path and a with statement")
    with_pathlib(source)
