"""Store and summarize completed games in SQLite."""

import sqlite3
from datetime import datetime


def connect(path: str = "wordle.db") -> sqlite3.Connection:
    """Open a database and create the games table when needed."""
    connection = sqlite3.connect(path)
    connection.execute(
        """CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            played_at TEXT,
            secret TEXT,
            guesses INTEGER,
            won INTEGER
        )"""
    )
    return connection


def record_game(connection: sqlite3.Connection, secret: str, guesses: int, won: bool) -> None:
    """Insert one game using a parameterized statement; the caller commits."""
    played_at = datetime.now().isoformat(timespec="seconds")
    connection.execute(
        "INSERT INTO games (played_at, secret, guesses, won) VALUES (?, ?, ?, ?)",
        (played_at, secret, guesses, int(won)),
    )


def summary(connection: sqlite3.Connection) -> dict:
    """Return totals, guess distribution and the current winning streak."""
    played, won = connection.execute(
        "SELECT COUNT(*), COALESCE(SUM(won), 0) FROM games"
    ).fetchone()
    rows = connection.execute(
        "SELECT guesses, COUNT(*) FROM games WHERE won = 1 GROUP BY guesses ORDER BY guesses"
    ).fetchall()
    distribution = dict(rows)
    streak = 0
    for (game_won,) in connection.execute("SELECT won FROM games ORDER BY id DESC"):
        if not game_won:
            break
        streak += 1
    percentage = won / played * 100 if played else 0.0
    return {
        "played": played,
        "won": won,
        "win_percentage": percentage,
        "distribution": distribution,
        "streak": streak,
    }
