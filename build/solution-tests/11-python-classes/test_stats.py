"""Checks for the game statistics."""

import sqlite3

from wordle.stats import connect, record_game, summary


def make_db(results: list[tuple[int, bool]]) -> sqlite3.Connection:
    """Return an in-memory database holding one game per result."""
    connection = connect(":memory:")
    for guesses, won in results:
        record_game(connection, "crane", guesses, won)
    return connection


def test_summary_counts_games_and_wins() -> None:
    totals = summary(make_db([(2, True), (6, False), (4, True), (3, True)]))
    assert totals["played"] == 4
    assert totals["won"] == 3
    assert totals["win_percentage"] == 75.0


def test_summary_of_an_empty_database() -> None:
    totals = summary(connect(":memory:"))
    assert totals["played"] == 0
    assert totals["win_percentage"] == 0.0


def test_distribution_counts_wins_per_guess_count() -> None:
    totals = summary(make_db([(2, True), (4, True), (4, True), (6, False)]))
    assert totals["distribution"] == {2: 1, 4: 2}


def test_streak_counts_wins_since_the_last_loss() -> None:
    assert summary(make_db([(6, False), (3, True), (4, True)]))["streak"] == 2
    assert summary(make_db([(3, True), (6, False)]))["streak"] == 0
    assert summary(make_db([]))["streak"] == 0
