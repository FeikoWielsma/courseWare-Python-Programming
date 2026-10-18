def print_playlist(name, tracks):
    print(f"Playlist: {name}")
    for number, title in enumerate(tracks, start=1):
        print(f"{number}. {title}")


print_playlist("Night drive", ["Imagine", "Yesterday"])
