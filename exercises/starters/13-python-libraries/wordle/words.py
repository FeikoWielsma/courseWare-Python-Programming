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
    return sorted(
        {
            line.strip().lower()
            for line in lines
            if len(line.strip()) == 5
            and line.strip().isascii()
            and line.strip().isalpha()
        }
    )
