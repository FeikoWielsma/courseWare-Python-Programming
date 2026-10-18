def add_encore(tracks: list[str]) -> None:
    tracks.append("Let It Be")
    print(f"Inside: {tracks}")

queue = ["Imagine", "Yesterday"]
add_encore(queue)
print(f"After call: {queue}")
