# INTERACTIVE : this demo starts a web server; open http://127.0.0.1:8000 and press Ctrl+C to stop

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Playlist")


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Hello from the playlist"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
