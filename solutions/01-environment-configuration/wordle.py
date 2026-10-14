"""Read the word list handed out in Exercise 1."""

from pathlib import Path


def main() -> None:
    """Print the number of characters in the word list."""
    words = Path("words.txt").read_text(encoding="utf-8")
    print(f"The word list contains {len(words)} characters.")


if __name__ == "__main__":
    main()
