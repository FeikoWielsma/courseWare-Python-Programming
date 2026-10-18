def reverse_playlist(tracks: list[str]) -> list[str]:
    reversed_tracks = tracks[::-1]
    assert len(reversed_tracks) == len(tracks), "Reversing must preserve every track"
    return reversed_tracks


print(reverse_playlist(["Imagine", "Yesterday", "Respect"]))
