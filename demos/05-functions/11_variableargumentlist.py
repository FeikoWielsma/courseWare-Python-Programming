def show_playlist(name: str, *tracks: str, **details: str) -> None:
    print(f"Playlist: {name}")
    for track in tracks:
        print(f"- {track}")
    for key, value in details.items():
        print(f"{key}: {value}")


show_playlist("Night drive", "Imagine", "Yesterday", mood="calm", owner="Sam")
show_playlist("Warm-up", "Respect", mood="energetic")
