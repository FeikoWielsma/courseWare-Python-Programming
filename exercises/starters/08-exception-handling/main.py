"""Start a game of Wordle: press Play on this file, or run `uv run python main.py`."""

from wordle.game import play
from wordle.words import load_words


def main() -> None:
    """Load the words and play one game."""
    words = load_words()
    print("Guess the five-letter word. Type 'quit', 'letters' or 'hint'.")
    secret = "crane"
    play(secret, words)


if __name__ == "__main__":
    main()
