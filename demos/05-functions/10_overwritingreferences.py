def with_encore(tracks: list[str]) -> list[str]:
    tracks = tracks + ["Encore"]
    return tracks

queue = ["Orbit", "Echo"]
extended = with_encore(queue)
print(f"Original: {queue}")
print(f"Encore mix: {extended}")
