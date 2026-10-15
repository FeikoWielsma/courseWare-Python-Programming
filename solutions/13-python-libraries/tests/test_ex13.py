"""The Exercise 13 tests written from scratch."""

import pytest
from wordle.game import follows_hints
from wordle.scoring import Mark
from wordle.solver import best_guess
from wordle.words import clean_words


@pytest.mark.parametrize("line", ["crane", "slate", "raise"])
def test_clean_words_keeps_lowercase_five_letter_words(line: str) -> None:
    assert clean_words([line, line.upper()]) == [line]


def test_best_guess_returns_none_for_no_candidates() -> None:
    assert best_guess([]) is None


def test_follows_hints_keeps_green_letters_and_uses_yellow_letters() -> None:
    history: list[tuple[str, list[Mark]]] = [
        ("crane", ["green", "grey", "yellow", "grey", "grey"])
    ]
    assert follows_hints("caper", history)
    assert not follows_hints("paper", history)
