"""Filter possible answers and suggest a useful next guess."""

from wordle.scoring import Mark, score_guess


def consistent(word: str, guess: str, marks: list[Mark]) -> bool:
    """Return whether word would produce the observed marks for guess."""
    return score_guess(word, guess) == marks


def candidates(words: list[str], history: list[tuple[str, list[Mark]]]) -> list[str]:
    """Return words consistent with every guess and its marks."""
    return [
        word
        for word in words
        if all(consistent(word, guess, marks) for guess, marks in history)
    ]


def letter_counts(words: list[str]) -> dict[str, int]:
    """Count how many candidate words contain each letter."""
    letters = {letter for word in words for letter in word}
    return {letter: sum(letter in word for word in words) for letter in letters}


def best_guess(words: list[str]) -> str | None:
    """Choose the word with the most frequently occurring distinct letters."""
    if not words:
        return None
    counts = letter_counts(words)
    return max(words, key=lambda word: sum(counts[letter] for letter in set(word)))
