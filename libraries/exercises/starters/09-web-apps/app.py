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

# Step 1 : add the function page and the route for "/" here.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
