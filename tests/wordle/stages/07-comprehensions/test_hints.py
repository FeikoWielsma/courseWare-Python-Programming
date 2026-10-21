"""Checks for the letter hints."""

from wordle.hints import hint, letters_left


def test_letters_left_skips_tried_letters() -> None:
    assert letters_left({"a", "e", "s"})[:4] == ["b", "c", "d", "f"]
    assert len(letters_left(set())) == 26


def test_hint_returns_first_untried_letter() -> None:
    assert hint("crane", {"s", "l", "a", "t", "e"}) == "c"
    assert hint("crane", {"c", "r"}) == "a"
