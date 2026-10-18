def with_encore(tracks: list[str]) -> list[str]:
    tracks = tracks + ["Let It Be"]
    return tracks

queue = ["Imagine", "Yesterday"]
extended = with_encore(queue)
print(f"Original: {queue}")
print(f"With encore: {extended}")
