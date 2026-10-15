"""Validate and score guesses."""

WORD_LENGTH = 5


def is_valid(guess: str, words: list[str]) -> bool:
    """Return whether guess is a five-letter word in the list."""
    return len(guess) == WORD_LENGTH and guess.isalpha() and guess in words


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
