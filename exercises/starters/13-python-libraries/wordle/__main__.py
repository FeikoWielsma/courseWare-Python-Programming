"""Start Wordle when run as a module."""

import os
import random
from contextlib import closing

from wordle.game import play
from wordle.stats import connect, record_game
from wordle.words import load_words


def main() -> None:
    """Load the words and play one game."""
    try:
        words = load_words()
        print(
            "Guess the five-letter word. Type 'quit', 'letters', "
            "'hint' or 'stats'."
        )
        secret = os.environ.get("WORDLE_SECRET", random.choice(words))
        guesses, won = play(secret, words)
        with closing(connect()) as connection, connection:
            record_game(connection, secret, guesses, won)
    except FileNotFoundError:
        print(
            "A word list is missing. Restore wordle/data/words.txt "
            "and wordle/data/allowed.txt and try again."
        )
    except (KeyboardInterrupt, EOFError):
        print("\nGame stopped.")


if __name__ == "__main__":
    main()
