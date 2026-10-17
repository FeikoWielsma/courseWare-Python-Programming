"""Render a scored guess as a text row."""

from wordle.scoring import Mark


def render(guess: str, marks: list[Mark]) -> str:
    """Draw green letters in brackets, yellow in parentheses and grey padded."""
    symbols = {
        "green": lambda letter: f"[{letter}]",
        "yellow": lambda letter: f"({letter})",
        "grey": lambda letter: f" {letter} ",
    }
    return "".join(symbols[mark](letter) for letter, mark in zip(guess.upper(), marks, strict=True))
