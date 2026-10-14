"""Render a scored guess as a text row."""


def render(guess: str, marks: list[str]) -> str:
    """Draw green letters in brackets, yellow in parentheses and grey padded."""
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
