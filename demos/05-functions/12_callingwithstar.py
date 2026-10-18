def show_playlist(name: str, *tracks: str, **details: str) -> None:
    print(f"Playlist: {name}")
    for track in tracks:
        print(f"- {track}")
    for key, value in details.items():
        print(f"{key}: {value}")


tracks = ["Orbit", "Echo"]
details = {"mood": "calm", "owner": "Nova"}
show_playlist("Night drive", *tracks, **details)
