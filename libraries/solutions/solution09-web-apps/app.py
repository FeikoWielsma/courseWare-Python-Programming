"""Play Wordle in the browser: press Play on this file, then open http://127.0.0.1:8000."""

import random
from pathlib import Path
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from wordle.game import Game
from wordle.words import load_allowed, load_words

app = FastAPI(title="Wordle")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
game = Game("crane", load_allowed())


def page(request: Request, message: str = "") -> HTMLResponse:
    """Draw the board, with an optional message about the last guess."""
    rows = [list(zip(word.upper(), marks, strict=True)) for word, marks in game.history]
    return templates.TemplateResponse(
        request, "index.html", {"game": game, "rows": rows, "message": message},
    )


@app.get("/")
def home(request: Request) -> HTMLResponse:
    return page(request)


@app.post("/guess")
def guess(request: Request, word: Annotated[str, Form()]) -> HTMLResponse:
    try:
        game.guess(word.strip().lower())
    except ValueError as error:
        return page(request, str(error))
    return page(request)


@app.post("/new")
def new_game(request: Request) -> HTMLResponse:
    game.secret = random.choice(load_words())
    game.history.clear()
    return page(request)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
