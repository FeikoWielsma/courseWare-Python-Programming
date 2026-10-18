albums = ["Night drive", "Warm-up"]
play_counts = dict.fromkeys(albums, 0)
print(play_counts)
playlists: dict[str, list[str]] = {name: [] for name in albums}
playlists["Night drive"].append("Orbit")
print(playlists)
