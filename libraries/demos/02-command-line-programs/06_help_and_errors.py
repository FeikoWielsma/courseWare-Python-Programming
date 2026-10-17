import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="squares",
        description="Print the square of a number.",
        epilog="Exits 0 on success and 2 when the command line is wrong.",
    )
    parser.add_argument("number", type=int, help="the number to square")
    parser.add_argument("-v", "--verbose", action="store_true", help="explain the answer")
    return parser


def run(argv: list[str]) -> int:
    print(f"$ squares {' '.join(argv)}")
    try:
        args = build_parser().parse_args(argv)
    except SystemExit as stop:
        print(f"[argparse exited with status {stop.code}]\n")
        return int(stop.code or 0)
    print(f"{args.number**2}\n")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1:])
    else:
        run(["--help"])  # generated from the add_argument calls, free of charge
        run([])  # a required argument is missing
        run(["seven"])  # not an int, so type=int refuses it
        run(["--colour"])  # an option nobody defined
        run(["9", "--verbose"])  # and finally one that works
