"""Checks for the Wordle scoring functions."""

from wordle.scoring import is_valid, score_guess

WORDS = ["crane", "speed", "geese", "error", "react"]


def test_correct_guess_is_all_green() -> None:
    assert score_guess("crane", "crane") == ["green"] * 5


def test_duplicate_letters_are_not_overcounted() -> None:
    assert score_guess("crane", "error") == ["yellow", "green", "grey", "grey", "grey"]


def test_is_valid_checks_length_and_membership() -> None:
    assert is_valid("crane", WORDS)
    assert not is_valid("cran", WORDS)
    assert not is_valid("zzzzz", WORDS)
