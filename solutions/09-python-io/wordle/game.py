"""Run one Wordle game."""

import csv
from pathlib import Path

from rich.console import Console

from wordle.display import colour_row
from wordle.hints import hint, letters_left, most_common_first
from wordle.scoring import InvalidGuess, check_guess, score_guess
from wordle.words import load_allowed

console = Console()


def play(secret: str, words: list[str], max_guesses: int = 6) -> bool:
    """Play one game and return whether the player found the secret."""
    used_letters = set()
    guess_count = 0
    allowed_words = load_allowed()
    while guess_count < max_guesses:
        guess = input(f"Guess {guess_count + 1}/{max_guesses} : ").strip().lower()
        match guess:
            case "quit":
                break
            case "letters":
                print("Tried :", " ".join(sorted(used_letters)))
                left = most_common_first(letters_left(used_letters), words)
                print("Not tried, most common first :", " ".join(left))
                continue
            case "hint":
                print(f"The word contains the letter {hint(secret, used_letters).upper()}.")
                continue
            case "stats":
                print_stats()
                continue
        try:
            check_guess(guess, allowed_words)
        except InvalidGuess as error:
            print(error)
            continue
        guess_count += 1
        used_letters.update(guess)
        console.print(colour_row(guess, score_guess(secret, guess)))
        if guess == secret:
            print(f"Got it in {guess_count}!")
            record_history(secret, guess_count, True)
            return True
    print(f"The word was {secret.upper()}.")
    record_history(secret, guess_count, False)
    return False


def history_path() -> Path:
    """Return the history file beside the project package."""
    return Path(__file__).resolve().parents[1] / "history.txt"


def record_history(secret: str, guesses: int, won: bool) -> None:
    """Append one finished game to the CSV history file."""
    with history_path().open("a", encoding="utf-8", newline="") as history_file:
        csv.writer(history_file).writerow([secret, guesses, int(won)])


def print_stats() -> None:
    """Read the CSV history and print game and win totals."""
    path = history_path()
    if not path.exists():
        print("Games played: 0; won: 0.")
        return
    with path.open(encoding="utf-8", newline="") as history_file:
        rows = list(csv.reader(history_file))
    wins = sum(row[2] == "1" for row in rows)
    print(f"Games played: {len(rows)}; won: {wins}.")
