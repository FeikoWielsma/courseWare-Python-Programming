"""Checks for the text display."""

from wordle.display import render


def test_render_marks_each_letter() -> None:
    marks = ["yellow", "yellow", "green", "yellow", "grey"]
    assert render("react", marks) == "(R)(E)[A](C) T "
