requested = "Wonderwall"
playlist = ["Imagine", "Yesterday", "Respect"]
for track in playlist:
    if track == requested:
        print(f"Found {requested}")
        break
else:
    print(f"{requested} is not in the playlist")
