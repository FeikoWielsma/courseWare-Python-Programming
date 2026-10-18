def show_playlist(name: str, *tracks: str, **details: str) -> None:
    print(f"Playlist: {name}")
    for track in tracks:
        print(f"- {track}")
    for key, value in details.items():
        print(f"{key}: {value}")


tracks = ["Imagine", "Yesterday"]
details = {"mood": "calm", "owner": "Sam"}
show_playlist("Night drive", *tracks, **details)
