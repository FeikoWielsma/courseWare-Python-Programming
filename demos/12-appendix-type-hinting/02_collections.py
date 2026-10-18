tracks: list[str] = ["Imagine", "Yesterday", "Respect"]
favourites: set[str] = {"Imagine", "Yesterday"}
durations: dict[str, int] = {"Imagine": 183, "Yesterday": 125}

photo_size: tuple[int, int] = (1920, 1080)
track: tuple[str, int] = ("Imagine", 183)
album_lengths: tuple[int, ...] = (183, 125, 149)

print(tracks)
print(durations)
print(photo_size, track, album_lengths)
