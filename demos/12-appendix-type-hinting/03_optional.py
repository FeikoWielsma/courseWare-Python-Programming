def find_duration(title: str, durations: dict[str, int]) -> int | None:
    return durations.get(title)


def parse_seconds(value: str | int) -> int:
    return int(value)


durations = {"Imagine": 183, "Yesterday": 125}
seconds = find_duration("Wonderwall", durations)
if seconds is None:
    print("Track not found")
else:
    print(f"Track length: {seconds} seconds")
print(parse_seconds("222"))
