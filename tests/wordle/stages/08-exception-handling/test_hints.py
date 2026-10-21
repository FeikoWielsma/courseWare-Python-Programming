"""Checks for the letter hints."""

from wordle.hints import hint, letter_counts, letters_left, most_common_first


def test_letters_left_skips_tried_letters() -> None:
    assert letters_left({"a", "e", "s"})[:4] == ["b", "c", "d", "f"]
    assert len(letters_left(set())) == 26


def test_letter_counts_count_every_occurrence() -> None:
    counts = letter_counts(["geese", "crane"])
    assert counts["e"] == 4
    assert counts["z"] == 0


def test_most_common_first_sorts_by_count() -> None:
    assert most_common_first(["c", "e", "z"], ["geese", "crane"]) == ["e", "c", "z"]


def test_hint_returns_first_untried_letter() -> None:
    assert hint("crane", {"s", "l", "a", "t", "e"}) == "c"
    assert hint("crane", {"c", "r"}) == "a"
