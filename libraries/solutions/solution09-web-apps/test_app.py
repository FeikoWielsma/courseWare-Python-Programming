"""Play the web game without a browser: run with `uv run pytest`."""

from fastapi.testclient import TestClient

from app import app, game

client = TestClient(app)


def test_home_shows_an_empty_board() -> None:
    game.history.clear()
    response = client.get("/")
    assert response.status_code == 200
    assert response.text.count('class="tile"') == 30


def test_guess_draws_a_row() -> None:
    game.history.clear()
    response = client.post("/guess", data={"word": "slate"})
    assert '<span class="tile green">A</span>' in response.text


def test_unknown_word_shows_the_reason() -> None:
    game.history.clear()
    response = client.post("/guess", data={"word": "xxxxx"})
    assert "That word is not in the word list." in response.text
