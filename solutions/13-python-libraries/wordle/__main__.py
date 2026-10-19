"""Start Wordle when run as a module."""

import sys
from contextlib import closing
from datetime import date

from wordle.game import play
from wordle.stats import connect, record_game
from wordle.storage import load_saved_game
from wordle.words import load_words


def main() -> None:
    """Load the words and play one game."""
    try:
        words = load_words()
        options = set(sys.argv[1:])
        saved = load_saved_game()
        if saved is not None:
            secret, history, max_guesses, hard = saved
            print("Resuming your saved game.")
        else:
            history = []
            if "--daily" in options:
                day_number = (date.today() - date(2026, 1, 1)).days
                secret = words[day_number % len(words)]
            else:
                secret = "crane"
            max_guesses = 10 if "--easy" in options else 6
            hard = "--hard" in options
        print(
            "Guess the five-letter word. Type 'quit', 'letters', "
            "'hint' or 'stats'."
        )
        guesses, won = play(secret, words, max_guesses, hard, history)
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
