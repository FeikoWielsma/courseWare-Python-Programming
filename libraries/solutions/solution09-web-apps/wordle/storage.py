"""Save and restore an unfinished game in JSON format."""

import json
from pathlib import Path

from wordle.scoring import Mark

SAVE_PATH = Path(__file__).resolve().parents[1] / "save.json"


def save_game(
    secret: str, history: list[tuple[str, list[Mark]]], max_guesses: int, hard: bool
) -> None:
    """Write the secret, the scored guesses and the game's settings to the save file."""
    data = {"secret": secret, "history": history, "max_guesses": max_guesses, "hard": hard}
    SAVE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_saved_game() -> tuple[str, list[tuple[str, list[Mark]]], int, bool] | None:
    """Read a saved game, returning None when no save exists."""
    if not SAVE_PATH.exists():
        return None
    data = json.loads(SAVE_PATH.read_text(encoding="utf-8"))
    history = [(word, marks) for word, marks in data["history"]]
    return data["secret"], history, data["max_guesses"], data["hard"]


def clear_saved_game() -> None:
    """Remove the save after a game is complete."""
    SAVE_PATH.unlink(missing_ok=True)
