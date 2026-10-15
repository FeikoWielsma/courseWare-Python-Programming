"""Load the course word list."""

from pathlib import Path


def load_words(path: str = "words.txt") -> list[str]:
    """Read the word list, one word per line."""
    return Path(path).read_text(encoding="utf-8").split()
