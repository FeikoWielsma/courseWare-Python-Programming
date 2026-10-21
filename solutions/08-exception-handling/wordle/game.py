"""Run one Wordle game."""

from rich.console import Console

from wordle.display import colour_row
from wordle.hints import hint, letters_left, most_common_first
from wordle.scoring import InvalidGuess, check_guess, score_guess

console = Console()


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
                left = most_common_first(letters_left(used_letters), words)
                print("Not tried, most common first :", " ".join(left))
                continue
            case "hint":
                print(f"The word contains the letter {hint(secret, used_letters).upper()}.")
                continue
        try:
            check_guess(guess, words)
        except InvalidGuess as error:
            print(error)
            continue
        guess_count += 1
        used_letters.update(guess)
        console.print(colour_row(guess, score_guess(secret, guess)))
        if guess == secret:
            print(f"Got it in {guess_count}!")
            return True
    print(f"The word was {secret.upper()}.")
    return False
