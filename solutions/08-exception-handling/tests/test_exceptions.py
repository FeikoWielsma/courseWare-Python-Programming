"""Reference tests for the first student-written exception tests."""

import pytest
from wordle.scoring import InvalidGuess, check_guess

WORDS = ["crane", "slate"]


def test_wrong_length_has_a_specific_reason() -> None:
    with pytest.raises(InvalidGuess, match="five letters"):
        check_guess("cran", WORDS)


def test_non_letters_have_a_specific_reason() -> None:
    with pytest.raises(InvalidGuess, match="letters only"):
        check_guess("cr4ne", WORDS)


def test_unknown_words_have_a_specific_reason() -> None:
    with pytest.raises(InvalidGuess, match="not in the word list"):
        check_guess("zzzzz", WORDS)
