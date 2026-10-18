
def parse_by_hand(argv: list[str]) -> tuple[str | None, int]:
    genre: str | None = None
    limit = 5
    index = 0
    while index < len(argv):
        if argv[index] == "--genre":
            index += 1
            genre = argv[index]
        elif argv[index] == "--limit":
            index += 1
            limit = int(argv[index])
        else:
            raise ValueError(f"Unknown option: {argv[index]}")
        index += 1
    return genre, limit


for sample in (["--genre", "Soul"], ["--limit"], ["--limit", "many"], ["--lmit", "3"]):
    try:
        print(sample, parse_by_hand(sample))
    except (IndexError, ValueError) as error:
        print(type(error).__name__, error)
