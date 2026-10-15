"""Start Wordle when run as a module."""

import os
import random

from wordle.game import play
from wordle.words import load_words


def main() -> None:
    """Load the words and play one game."""
    words = load_words()
    print("Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.")
    play(os.environ.get("WORDLE_SECRET", random.choice(words)), words)


if __name__ == "__main__":
    main()
