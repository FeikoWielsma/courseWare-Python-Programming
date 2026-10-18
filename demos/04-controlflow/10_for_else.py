requested = "Comet"
playlist = ["Orbit", "Echo", "Pulse"]
for track in playlist:
    if track == requested:
        print(f"Found {requested}")
        break
else:
    print(f"{requested} is not in the playlist")
