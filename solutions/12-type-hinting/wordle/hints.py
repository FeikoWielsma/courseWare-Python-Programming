"""Help the player choose the next guess."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def letters_left(used: set[str]) -> list[str]:
    """Return the letters of the alphabet that have not been tried yet."""
    return [letter for letter in ALPHABET if letter not in used]


def hint(secret: str, used: set[str]) -> str | None:
    """Return the first letter of the secret that has not been tried yet, if any."""
    untried = [letter for letter in secret if letter not in used]
    if not untried:
        return None
    return untried[0]
