"""Draw a scored guess as a row, in plain text or in colour."""

from rich.text import Text

SYMBOLS = {
    "green": lambda letter: f"[{letter}]",
    "yellow": lambda letter: f"({letter})",
    "grey": lambda letter: f" {letter} ",
}

COLOURS = {
    "green": "bold white on green",
    "yellow": "bold black on yellow",
    "grey": "white on grey35",
}


def render(guess: str, marks: list[str]) -> str:
    """Draw green letters in brackets, yellow in parentheses and grey padded."""
    return "".join(SYMBOLS[mark](letter) for letter, mark in zip(guess.upper(), marks, strict=True))


def colour_row(guess: str, marks: list[str]) -> Text:
    """Draw the same row as render, with a background colour for each mark."""
    return Text("").join(
        Text(SYMBOLS[mark](letter), style=COLOURS[mark])
        for letter, mark in zip(guess.upper(), marks, strict=True)
    )
