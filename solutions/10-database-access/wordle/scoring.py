"""Validate and score guesses."""

WORD_LENGTH = 5


class InvalidGuess(ValueError):  # noqa: N818  # Contracted name from plan section 4.
    """Raised when a guess is not an allowed five-letter word."""


def check_guess(guess: str, words: list[str]) -> None:
    """Raise InvalidGuess with a reason when guess cannot be played."""
    if len(guess) != WORD_LENGTH:
        raise InvalidGuess("A guess must have five letters.")
    if not guess.isalpha():
        raise InvalidGuess("A guess must contain letters only.")
    if guess not in words:
        raise InvalidGuess("That word is not in the word list.")


def is_valid(guess: str, words: list[str]) -> bool:
    """Return whether guess is valid, for compatibility with Exercise 6."""
    try:
        check_guess(guess, words)
    except InvalidGuess:
        return False
    return True


def score_guess(secret: str, guess: str) -> list[str]:
    """Return Wordle marks while counting each secret letter only once."""
    marks = ["grey"] * WORD_LENGTH
    unmatched = []
    for position, letter in enumerate(guess):
        if letter == secret[position]:
            marks[position] = "green"
        else:
            unmatched.append(secret[position])
    for position, letter in enumerate(guess):
        if marks[position] != "green" and letter in unmatched:
            marks[position] = "yellow"
            unmatched.remove(letter)
    return marks
