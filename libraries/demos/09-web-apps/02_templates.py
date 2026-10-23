# INTERACTIVE : this demo starts a web server; open http://127.0.0.1:8000

import csv
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

DATA = Path(__file__).resolve().parents[2] / "data"
with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    tracks = list(csv.DictReader(handle))

app = FastAPI(title="Playlist")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/")
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "tracks.html", {"tracks": tracks})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
