from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI(title="Playlist")
genres = {"Imagine": "Rock", "Respect": "Soul", "Jolene": "Country"}


@app.get("/genre/{title}")
def genre(title: str) -> dict[str, str]:
    if title not in genres:
        raise HTTPException(status_code=404, detail="Unknown track")
    return {"title": title, "genre": genres[title]}


# The client calls the application directly; no server and no network are involved.
client = TestClient(app)

response = client.get("/genre/Jolene")
print(response.status_code, response.json())

response = client.get("/genre/Toxic")
print(response.status_code, response.json())


def test_known_track() -> None:
    response = client.get("/genre/Respect")
    assert response.status_code == 200
    assert response.json()["genre"] == "Soul"
