"""Run one Wordle game."""

from wordle.display import render
from wordle.scoring import InvalidGuess, check_guess, score_guess
from wordle.solver import best_guess, candidates


def play(secret: str, words: list[str], max_guesses: int = 6) -> bool:
    """Play one game and return whether the player found the secret."""
    used_letters = set()
    history = []
    guess_count = 0
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
        try:
            check_guess(guess, words)
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
            return True
    print(f"The word was {secret.upper()}.")
    return False
