"""Run one Wordle game."""

from contextlib import closing

from wordle.display import render
from wordle.scoring import InvalidGuess, check_guess, score_guess
from wordle.solver import best_guess, candidates
from wordle.stats import connect, summary
from wordle.words import load_allowed


def play(secret: str, words: list[str], max_guesses: int = 6) -> tuple[int, bool]:
    """Play one game and return the guesses used and whether the secret was found."""
    used_letters = set()
    history = []
    guess_count = 0
    allowed_words = load_allowed()
    while guess_count < max_guesses:
        guess = input(f"Guess {guess_count + 1}/{max_guesses} : ").strip().lower()
        match guess:
            case "quit":
                break
            case "letters":
                print("Tried :", " ".join(sorted(used_letters)))
                continue
            case "hint":
                possible = candidates(words, history)
                print(f"{len(possible)} words left, try {best_guess(possible).upper()}")
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
        marks = score_guess(secret, guess)
        history.append((guess, marks))
        print(render(guess, marks))
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
