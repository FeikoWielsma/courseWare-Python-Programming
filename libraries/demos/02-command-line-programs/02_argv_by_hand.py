import sys


def parse_by_hand(argv: list[str]) -> tuple[str | None, int, bool]:
    filename: str | None = None
    limit = 10
    verbose = False

    index = 0
    while index < len(argv):
        item = argv[index]
        if item == "--verbose":
            verbose = True
        elif item == "--limit":
            index += 1
            limit = int(argv[index])  # IndexError when --limit ends the line
        else:
            filename = item
        index += 1

    return filename, limit, verbose


def try_it(argv: list[str]) -> None:
    try:
        print(f"{argv} -> {parse_by_hand(argv)}")
    except (IndexError, ValueError) as error:
        print(f"{argv} -> {type(error).__name__}: {error}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try_it(sys.argv[1:])
    else:
        try_it(["--limit", "3", "hosts.txt"])  # this one works
        try_it(["--limit"])  # the value is missing
        try_it(["--limit", "many", "hosts.txt"])  # the value is not a number
        try_it(["--lmit", "3", "hosts.txt"])  # a typo silently becomes a filename
        try_it(["--help"])  # nobody wrote any help
