"""Run one Wordle game."""

from contextlib import closing

from rich.console import Console

from wordle.display import colour_row
from wordle.hints import hint, letters_left, most_common_first
from wordle.scoring import InvalidGuess, check_guess, score_guess
from wordle.stats import connect, summary
from wordle.words import load_allowed

console = Console()


def play(secret: str, words: list[str], max_guesses: int = 6) -> tuple[int, bool]:
    """Play one game and return the guesses used and whether the secret was found."""
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
            return guess_count, True
    print(f"The word was {secret.upper()}.")
    return guess_count, False


def print_stats() -> None:
    """Print database totals, a guess chart and the current winning streak."""
    with closing(connect()) as connection:
        totals = summary(connection)
    print(
        f"Games played: {totals['played']}; won: {totals['won']}; "
        f"win rate: {totals['win_percentage']:.1f}%."
    )
    chart = " ".join(
        f"{guesses}: {'#' * count}"
        for guesses, count in totals["distribution"].items()
    )
    print(f"Wins by guesses: {chart or 'none'}")
    print(f"Current streak: {totals['streak']}")
