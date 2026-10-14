"""Wordle, as it stands at the end of Exercise 5."""

import os
import random
from pathlib import Path

WORD_LENGTH = 5


def load_words(path: str = "words.txt") -> list[str]:
    """Read the word list, one word per line."""
    return Path(path).read_text(encoding="utf-8").split()


def is_valid(guess: str, words: list[str]) -> bool:
    """A guess must be a known word of the right length."""
    return len(guess) == WORD_LENGTH and guess.isalpha() and guess in words


def score_guess(secret: str, guess: str) -> list[str]:
    """Mark each letter of guess as "green", "yellow" or "grey".

    A letter is yellow only while the secret still has an unmatched copy of it,
    so one E in the secret cannot make two E's in the guess yellow.
    """
    marks = ["grey"] * WORD_LENGTH
    unmatched: list[str] = []

    # First pass : exact matches. Whatever the secret has left over is
    # available to be found elsewhere.
    for position, letter in enumerate(guess):
        if letter == secret[position]:
            marks[position] = "green"
        else:
            unmatched.append(secret[position])

    # Second pass : right letter, wrong place, each copy used at most once.
    for position, letter in enumerate(guess):
        if marks[position] != "green" and letter in unmatched:
            marks[position] = "yellow"
            unmatched.remove(letter)

    return marks


def render(guess: str, marks: list[str]) -> str:
    """[A] is in the right place, (A) is in the word elsewhere, A is not in it."""
    row = ""
    for position, letter in enumerate(guess.upper()):
        match marks[position]:
            case "green":
                row += f"[{letter}]"
            case "yellow":
                row += f"({letter})"
            case _:
                row += f" {letter} "
    return row


def play(secret: str, words: list[str], max_guesses: int = 6) -> bool:
    """Play one game. Returns True when the word was found."""
    used_letters: set[str] = set()
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


def main() -> None:
    words = load_words()
    print("Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.")
    secret = os.environ.get("WORDLE_SECRET", random.choice(words))
    play(secret, words)


if __name__ == "__main__":
    main()
