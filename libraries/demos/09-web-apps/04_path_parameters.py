# INTERACTIVE : this demo starts a web server; open http://127.0.0.1:8000/tracks/1

import csv
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException

DATA = Path(__file__).resolve().parents[2] / "data"
with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    tracks = list(csv.DictReader(handle))

app = FastAPI(title="Playlist")


@app.get("/tracks/{number}")
def track(number: int) -> dict[str, str]:
    if not 1 <= number <= len(tracks):
        raise HTTPException(status_code=404, detail=f"No track {number}")
    row = tracks[number - 1]
    return {"title": row["title"], "artist": row["artist"]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
