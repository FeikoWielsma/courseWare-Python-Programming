def find_duration(title: str, durations: dict[str, int]) -> int | None:
    return durations.get(title)


def parse_seconds(value: str | int) -> int:
    return int(value)


durations = {"Orbit": 222, "Echo": 185}
seconds = find_duration("Comet", durations)
if seconds is None:
    print("Track not found")
else:
    print(f"Track length: {seconds} seconds")
print(parse_seconds("222"))
