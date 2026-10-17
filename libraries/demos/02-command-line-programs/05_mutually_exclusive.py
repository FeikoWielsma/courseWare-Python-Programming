import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Raise a base to an exponent.")
    # Asking for both --verbose and --quiet is refused before any code runs.
    loudness = parser.add_mutually_exclusive_group()
    loudness.add_argument("-v", "--verbose", action="store_true", help="explain the answer")
    loudness.add_argument("-q", "--quiet", action="store_true", help="print the answer only")
    parser.add_argument("base", type=int, help="the base")
    parser.add_argument("exponent", type=int, help="the exponent")
    return parser


def main(argv: list[str]) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    answer = args.base**args.exponent

    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.base} to the power {args.exponent} equals {answer}")
    else:
        print(f"{args.base}^{args.exponent} == {answer}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["2", "10", "--quiet"])
