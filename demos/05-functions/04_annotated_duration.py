def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"


def print_playlist(name: str, tracks: list[str]) -> None:
    print(f"Playlist: {name}")
    for number, title in enumerate(tracks, start=1):
        print(f"{number}. {title}")


print(format_duration(222))
print_playlist("Night drive", ["Imagine", "Yesterday"])
