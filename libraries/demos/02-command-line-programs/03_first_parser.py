import argparse
import sys


def main(argv: list[str]) -> None:

    parser = argparse.ArgumentParser(description="Print the square of a number.")
    parser.add_argument("number", type=int, help="the number to square")
    parser.add_argument("number2", type=int, help="the number to add")
    args = parser.parse_args(argv)

    print(f"{args.number} squared is {args.number**2 + args.number2}")


if __name__ == "__main__":
    # A sample argument list stands in when the file is run bare, so that the
    # demo shows its output instead of a usage error.
    main(sys.argv[1:] or ["12"])
