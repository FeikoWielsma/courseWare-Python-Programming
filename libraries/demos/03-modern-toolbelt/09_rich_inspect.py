from rich import inspect


class Track:
    def __init__(self, title: str, duration_s: int) -> None:
        self.title: str = title
        self.duration_s: int = duration_s

    def minutes(self) -> float:
        """Return the duration in minutes."""
        return self.duration_s / 60

song = Track("Imagine", 183)
inspect(song, methods=True, help=True)
