tracks: list[str] = ["Orbit", "Echo", "Pulse"]
favourites: set[str] = {"Orbit", "Echo"}
durations: dict[str, int] = {"Orbit": 222, "Echo": 185}

photo_size: tuple[int, int] = (1920, 1080)
track: tuple[str, int] = ("Orbit", 222)
album_lengths: tuple[int, ...] = (222, 185, 204)

print(tracks)
print(durations)
print(photo_size, track, album_lengths)
