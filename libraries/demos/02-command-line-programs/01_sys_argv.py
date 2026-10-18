import sys
from pathlib import Path

arguments = sys.argv[1:] or ["tracks.csv", "--genre", "Rock", "--limit", "3"]
print(f"program: {Path(sys.argv[0]).name}")
for position, value in enumerate(arguments, start=1):
    print(f"argv[{position}] = {value!r}")

line = "2026-10-12 08:00:00 INFO PLAY Imagine"
print(line.split(maxsplit=4))
