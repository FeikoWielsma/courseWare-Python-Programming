# INTERACTIVE : this demo starts a web server; open http://127.0.0.1:8000

from pathlib import Path
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Playlist")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
playlist: list[dict[str, str]] = []


@app.get("/")
def show_playlist(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "playlist.html", {"playlist": playlist})


@app.post("/")
def add_track(
    request: Request, title: Annotated[str, Form()], artist: Annotated[str, Form()],
) -> HTMLResponse:
    playlist.append({"title": title, "artist": artist})
    return templates.TemplateResponse(request, "playlist.html", {"playlist": playlist})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
