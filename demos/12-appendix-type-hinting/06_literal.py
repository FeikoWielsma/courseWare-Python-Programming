from typing import Literal

type PlaybackMode = Literal["normal", "repeat"]


def next_index(index: int, mode: PlaybackMode) -> int:
    if mode == "repeat":
        return index
    return index + 1


print(next_index(0, "repeat"))
print(next_index(0, "shuffle"))  # Deliberate checker error.
