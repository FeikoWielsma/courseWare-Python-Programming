from pathlib import Path

text = Path("tracks.txt").read_text(encoding="utf-8")
tracks = text.split()
print(tracks)
print(len(tracks))
