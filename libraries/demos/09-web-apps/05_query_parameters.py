# INTERACTIVE : this demo starts a web server; open http://127.0.0.1:8000/tracks?genre=Soul

import csv
from pathlib import Path

import uvicorn
from fastapi import FastAPI

DATA = Path(__file__).resolve().parents[2] / "data"
with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    tracks = list(csv.DictReader(handle))

app = FastAPI(title="Playlist")


@app.get("/tracks")
def list_tracks(genre: str | None = None, limit: int = 5) -> list[str]:
    found = [row for row in tracks if genre is None or row["genre"] == genre]
    return [row["title"] for row in found[:limit]]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
