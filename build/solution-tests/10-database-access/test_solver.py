"""Checks for the Wordle candidate solver."""

from wordle.scoring import score_guess
from wordle.solver import best_guess, candidates, consistent, letter_counts


def test_consistent_reuses_scoring_rules() -> None:
    marks = score_guess("crane", "slate")
    assert consistent("crane", "slate", marks)
    assert not consistent("crane", "raise", marks)


def test_candidates_match_all_history() -> None:
    history = [("slate", score_guess("crane", "slate"))]
    assert candidates(["crane", "slate", "trace"], history) == ["crane"]


def test_letter_counts_count_words_containing_letters() -> None:
    assert letter_counts(["cacao", "crane"]) == {
        "c": 2,
        "a": 2,
        "o": 1,
        "r": 1,
        "n": 1,
        "e": 1,
    }


def test_best_guess_uses_distinct_letters() -> None:
    assert best_guess(["crane", "cacao"]) == "crane"
