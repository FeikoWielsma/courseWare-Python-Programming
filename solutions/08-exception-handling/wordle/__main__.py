"""Start Wordle when run as a module."""

from wordle.game import play
from wordle.words import load_words


def main() -> None:
    """Load the words and play one game."""
    try:
        words = load_words()
        print(
            "Guess the five-letter word. Type 'quit' to give up, "
            "'letters' for the letters tried."
        )
        secret = "crane"
        play(secret, words)
    except (KeyboardInterrupt, EOFError):
        print("\nGame stopped.")


if __name__ == "__main__":
    main()
