"""Checks for Exercise 5. Run them with :  uv run pytest"""

from wordle import is_valid, render, score_guess

WORDS = ["crane", "speed", "geese", "error", "react"]


def test_a_correct_guess_is_all_green() -> None:
    assert score_guess("crane", "crane") == ["green"] * 5


def test_letters_not_in_the_word_are_grey() -> None:
    assert score_guess("crane", "solid") == ["grey"] * 5


def test_right_letters_in_the_wrong_place_are_yellow() -> None:
    assert score_guess("crane", "react") == ["yellow", "yellow", "green", "yellow", "grey"]


def test_one_r_in_the_secret_cannot_make_three_rs_coloured() -> None:
    # CRANE has one R. ERROR has three, and only the one in the right place counts.
    assert score_guess("crane", "error") == ["yellow", "green", "grey", "grey", "grey"]


def test_repeated_letters_are_matched_once_each() -> None:
    # SPEED has two E's, so GEESE may colour two of its three, and no more.
    assert score_guess("speed", "geese") == ["grey", "yellow", "green", "yellow", "grey"]


def test_is_valid_accepts_a_known_word() -> None:
    assert is_valid("crane", WORDS)


def test_is_valid_rejects_the_wrong_length() -> None:
    assert not is_valid("cran", WORDS)
    assert not is_valid("cranes", WORDS)


def test_is_valid_rejects_an_unknown_word() -> None:
    assert not is_valid("zzzzz", WORDS)


def test_render_marks_each_letter() -> None:
    assert render("react", ["yellow", "yellow", "green", "yellow", "grey"]) == "(R)(E)[A](C) T "
