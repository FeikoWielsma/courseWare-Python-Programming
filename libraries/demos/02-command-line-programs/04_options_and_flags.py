import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Raise a base to an exponent.")
    parser.add_argument("base", type=int, help="the base")
    parser.add_argument("exponent", type=int, nargs="?", default=2, help="the exponent")
    parser.add_argument("--dry-run", action="store_true", help="say what would happen")
    # count lets the flag be repeated, so -vv is more verbose than -v.
    parser.add_argument("-v", "--verbose", action="count", default=0, help="repeat for more detail")
    # choices rejects anything not in the list, and lists them in the help.
    parser.add_argument(
        "--format", choices=["dec", "hex", "bin"], default="dec", help="how to print the answer"
    )
    return parser


def render(value: int, style: str) -> str:
    return {"dec": str(value), "hex": hex(value), "bin": bin(value)}[style]


def main(argv: list[str]) -> None:
    args = build_parser().parse_args(argv)
    # A dashed option name becomes an underscored attribute: --dry-run is dry_run.
    if args.dry_run:
        print(f"would raise {args.base} to the power {args.exponent}")
        return

    answer = args.base**args.exponent
    if args.verbose >= 2:
        print(f"{args.base} to the power {args.exponent} equals {render(answer, args.format)}")
    elif args.verbose == 1:
        print(f"{args.base}^{args.exponent} == {render(answer, args.format)}")
    else:
        print(render(answer, args.format))


if __name__ == "__main__":
    main(sys.argv[1:] or ["2", "10", "-vv", "--format", "hex"])
