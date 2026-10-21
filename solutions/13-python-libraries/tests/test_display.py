"""Checks for the text and colour display."""

from wordle.display import colour_row, render


def test_render_marks_each_letter() -> None:
    marks = ["yellow", "yellow", "green", "yellow", "grey"]
    assert render("react", marks) == "(R)(E)[A](C) T "


def test_colour_row_keeps_the_text_of_render() -> None:
    marks = ["yellow", "yellow", "green", "yellow", "grey"]
    row = colour_row("react", marks)
    assert row.plain == render("react", marks)
    assert len(row.spans) == 5
