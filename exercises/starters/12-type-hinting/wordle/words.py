"""Load the course word list."""

from pathlib import Path


def load_words() -> list[str]:
    """Read the package answer list, independent of the working directory."""
    data_path = Path(__file__).parent / "data" / "words.txt"
    return data_path.read_text(encoding="utf-8").split()


def load_allowed() -> list[str]:
    """Read every allowed guess from the package data folder."""
    data_path = Path(__file__).parent / "data" / "allowed.txt"
    return data_path.read_text(encoding="utf-8").split()


def clean_words(lines: list[str]) -> list[str]:
    """Return unique lowercase five-letter ASCII words in sorted order."""
    kept: set[str] = set()
    for line in lines:
        word = line.strip().lower()
        if len(word) == 5 and word.isascii() and word.isalpha():
            kept.add(word)
    return sorted(kept)
