"""Checks for the Game object."""

import pytest
from wordle.game import Game
from wordle.scoring import InvalidGuess

WORDS = ["crane", "slate", "raise"]


def test_guess_records_marks_and_updates_properties() -> None:
    game = Game("crane", WORDS, max_guesses=2)
    assert game.guesses_left == 2
    assert not game.is_won
    assert not game.is_over
    assert game.guess("slate") == ["grey", "grey", "green", "grey", "green"]
    assert game.guesses_left == 1
    assert game.guess("crane") == ["green"] * 5
    assert game.is_won
    assert game.is_over
    assert "[C][R][A][N][E]" in str(game)


def test_max_guesses_is_validated() -> None:
    game = Game("crane", WORDS)
    game.max_guesses = 10
    with pytest.raises(ValueError):
        game.max_guesses = 0
    with pytest.raises(ValueError):
        Game("crane", WORDS, max_guesses=11)


def test_invalid_guess_does_not_change_history() -> None:
    game = Game("crane", WORDS)
    with pytest.raises(InvalidGuess):
        game.guess("wrong")
    assert game.history == []


def test_game_is_over_when_the_limit_drops_below_the_history() -> None:
    game = Game("crane", WORDS, max_guesses=3)
    game.guess("slate")
    game.guess("raise")
    game.max_guesses = 1
    assert game.guesses_left == -1
    assert game.is_over
