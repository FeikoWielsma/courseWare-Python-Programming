"""Listing the photos in an album directory."""

from pathlib import Path

here = Path.cwd()
album = here / "holiday"
album.mkdir(exist_ok=True)
for name in ["beach.jpg", "sunset.jpg", "notes.txt"]:
    (album / name).touch()

print("contents   :", sorted(p.name for p in album.iterdir()))
print("only photos:", sorted(p.name for p in album.glob("*.jpg")))

photo = album / "sunset.jpg"
print("name       :", photo.name)
print("stem       :", photo.stem)
print("suffix     :", photo.suffix)
print("parent     :", photo.parent.name)

for leftover in album.iterdir():
    leftover.unlink()
album.rmdir()
print("still there:", album.exists())
