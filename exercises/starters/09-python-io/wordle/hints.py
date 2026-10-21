"""Help the player choose the next guess."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def letters_left(used: set[str]) -> list[str]:
    """Return the letters of the alphabet that have not been tried yet."""
    return [letter for letter in ALPHABET if letter not in used]


def letter_counts(words: list[str]) -> dict[str, int]:
    """Count how often each letter of the alphabet occurs in the words."""
    text = "".join(words)
    return {letter: text.count(letter) for letter in ALPHABET}


def most_common_first(letters: list[str], words: list[str]) -> list[str]:
    """Sort the letters so that the ones used most in the words come first."""
    counts = letter_counts(words)
    return sorted(letters, key=lambda letter: counts[letter], reverse=True)


def hint(secret: str, used: set[str]) -> str:
    """Return the first letter of the secret that has not been tried yet."""
    untried = [letter for letter in secret if letter not in used]
    return untried[0]
