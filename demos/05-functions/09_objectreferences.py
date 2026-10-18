def add_encore(tracks: list[str]) -> None:
    tracks.append("Encore")
    print(f"Inside: {tracks}")

queue = ["Orbit", "Echo"]
add_encore(queue)
print(f"After call: {queue}")
