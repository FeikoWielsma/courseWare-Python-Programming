"""Run one Wordle game."""

from wordle.display import render
from wordle.scoring import is_valid, score_guess


def play(secret: str, words: list[str], max_guesses: int = 6) -> bool:
    """Play one game and return whether the player found the secret."""
    used_letters = set()
    guess_count = 0
    while guess_count < max_guesses:
        guess = input(f"Guess {guess_count + 1}/{max_guesses} : ").strip().lower()
        match guess:
            case "quit":
                break
            case "letters":
                print("Tried :", " ".join(sorted(used_letters)))
                continue
        if not is_valid(guess, words):
            print("That is not a five-letter word I know.")
            continue
        guess_count += 1
        used_letters.update(guess)
        print(render(guess, score_guess(secret, guess)))
        if guess == secret:
            print(f"Got it in {guess_count}!")
            return True
    print(f"The word was {secret.upper()}.")
    return False
