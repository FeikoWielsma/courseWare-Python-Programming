"""Checks for cleaning the raw word list."""

from wordle.words import clean_words


def test_clean_words_lowercases_filters_and_sorts() -> None:
    assert clean_words(["Crane", "crane", "slate", "two", "12345", "café", ""]) == [
        "crane",
        "slate",
    ]
