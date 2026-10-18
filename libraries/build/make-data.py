"""Rebuild the teaching datasets offline, from the attributed source catalogue.

Song editions and lengths: ../data/track-catalogue.json (Apple catalogue URLs).
Seconds are rounded up from the catalogue's millisecond lengths.
Years describe original track releases.
Listening counts, events and hourly patterns are fictional personal data.
"""

import csv
import io
import json
import re
import shutil
import sqlite3
import struct
import sys
import tempfile
import zlib
from contextlib import closing
from datetime import datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

import matplotlib.image as image
import numpy as np
import pandas as pd
from matplotlib.figure import Figure

DATA = Path(__file__).resolve().parents[1] / "data"
FIRST = [
    "Imagine", "Yesterday", "Respect", "Toxic", "Thriller", "Hey Jude",
    "Let It Be", "Jolene", "Wonderwall", "Bohemian Rhapsody",
]


def write_csv(name: str, rows: list[dict]) -> None:
    with (DATA / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_workbook(tracks: pd.DataFrame, name: str = "tracks.xlsx") -> None:
    """Normalize workbook properties and ZIP metadata so repeated builds agree."""
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as workbook:
        tracks.to_excel(workbook, sheet_name="tracks", index=False)
        if name == "tracks-report.xlsx":
            tracks.groupby("genre", as_index=False)["plays"].sum().to_excel(
                workbook, sheet_name="per genre", index=False,
            )
        workbook.book.properties.created = datetime(2026, 10, 12)
        workbook.book.properties.modified = datetime(2026, 10, 12)
    with ZipFile(buffer) as source, ZipFile(DATA / name, "w") as target:
        for name in sorted(source.namelist()):
            contents = source.read(name)
            if name == "docProps/core.xml":
                contents = re.sub(
                    rb"(<dcterms:modified[^>]*>).*?(</dcterms:modified>)",
                    rb"\g<1>2026-10-12T00:00:00Z\2", contents,
                )
            entry = ZipInfo(name, (2026, 10, 12, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            target.writestr(entry, contents)


def write_photo() -> None:
    """Encode a 64 by 48 RGB crop of the attributed NASA composite as a PNG."""
    original = image.imread(DATA / "photo-source.jpg")
    pixels = original[256:1792:32, ::32, :3].astype(np.uint8)
    assert pixels.shape == (48, 64, 3)

    def chunk(kind: bytes, contents: bytes) -> bytes:
        return (
            struct.pack(">I", len(contents)) + kind + contents
            + struct.pack(">I", zlib.crc32(kind + contents))
        )

    rows = b"".join(b"\0" + row.tobytes() for row in pixels)
    (DATA / "photo.png").write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", 64, 48, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b"")
    )


def main() -> None:
    catalogue = json.loads((DATA / "track-catalogue.json").read_text(encoding="utf-8"))
    catalogue.sort(key=lambda row: FIRST.index(row["title"]) if row["title"] in FIRST else 40)
    rows = []
    for index, track in enumerate(catalogue):
        rows.append({
            **{key: track[key] for key in ("title", "artist", "year", "genre", "duration_s")},
            "plays": (index * 17 + 11) % 97,
            "last_played": "" if index in {5, 12, 19} else f"2026-10-{12 + index % 7:02d}",
        })
    # Import defects are deliberate and confined to a separate input file.
    write_csv("tracks.csv", rows)
    imported = [row.copy() for row in rows] + [rows[0].copy()]
    imported[12]["duration_s"] = ""
    write_csv("tracks-import.csv", imported)
    tracks = pd.DataFrame(rows)
    write_workbook(tracks)
    artists = [
        {"artist": artist, "country": country, "formed": formed, "members": members}
        for artist, country, formed, members in [
            ("The Beatles", "UK", 1960, 4), ("Queen", "UK", 1970, 4),
            ("Daft Punk", "France", 1993, 2), ("Oasis", "UK", 1991, 5),
            ("Aretha Franklin", "USA", "", 1), ("Britney Spears", "USA", "", 1),
            ("Michael Jackson", "USA", "", 1), ("Dolly Parton", "USA", "", 1),
            ("Adele", "UK", "", 1), ("Fleetwood Mac", "UK", 1967, 5),
        ]
    ]
    write_csv("artists.csv", artists)
    hours = np.array([
        [0 if hour < 6 else (hour * 3 + day * 2) % 13 for hour in range(24)]
        for day in range(7)
    ])
    hours[5, 22] = 18
    write_csv("plays-hourly.csv", [
        {"day": day, **{f"h{hour:02d}": int(value) for hour, value in enumerate(values)}}
        for day, values in zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], hours,
                               strict=True)
    ])
    levels = ["INFO"] * 11 + ["WARN"] * 4 + ["ERROR"] * 3
    lines = []
    for index, level in enumerate(levels):
        action = ["PLAY", "SKIP", "PAUSE"][index % 3]
        if level == "WARN":
            action = "MISSING_FILE" if index % 2 else "SLOW_STREAM"
        elif level == "ERROR":
            action = "READ_ERROR"
        lines.append(
            f"2026-10-12 {8 + index // 6:02d}:{index % 6 * 10:02d}:00 {level} "
            f"{action} {rows[index % len(rows)]['title']}"
        )
    (DATA / "listening.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
    with tempfile.TemporaryDirectory() as directory:
        database = Path(directory) / "tracks.db"
        with closing(sqlite3.connect(database)) as connection:
            tracks.to_sql("tracks", connection, index=False)
        (DATA / "tracks.db").write_bytes(database.read_bytes())
    tracks.sort_values("plays", ascending=False).to_csv(DATA / "tracks-report.csv", index=False)
    report = tracks.sort_values("plays", ascending=False)
    report.to_csv(DATA / "tracks-report.tsv", sep="\t", index=False)
    write_workbook(report, "tracks-report.xlsx")
    np.savetxt(DATA / "plays-hourly-mean.csv", hours.mean(axis=0), delimiter=",", fmt="%.2f")
    per_decade = tracks.groupby(tracks["year"] // 10 * 10)["plays"].sum()
    figure = Figure(figsize=(7, 4))
    axes = figure.subplots()
    axes.bar([str(value) for value in per_decade.index], per_decade)
    axes.set_title("Fictional plays by decade")
    axes.set_ylabel("plays")
    figure.tight_layout()
    figure.savefig(DATA / "tracks-plot.png", dpi=120)
    write_photo()
    print(f"Generated {len(rows)} tracks, {len(artists)} artist rows, a {hours.shape} plays grid.")


if __name__ == "__main__":
    if "--check" in sys.argv:
        source = DATA
        with tempfile.TemporaryDirectory() as directory:
            DATA = Path(directory)
            for name in ("track-catalogue.json", "photo-source.jpg"):
                shutil.copyfile(source / name, DATA / name)
            main()
            for name in (
                "tracks.csv", "tracks-import.csv", "tracks.xlsx", "artists.csv",
                "plays-hourly.csv", "listening.log", "photo.png", "tracks-report.csv",
                "tracks-report.tsv", "tracks-report.xlsx", "tracks-plot.png",
                "plays-hourly-mean.csv",
            ):
                assert (source / name).read_bytes() == (DATA / name).read_bytes(), name
        print("Twelve checked-in data artifacts reproduce byte-for-byte.")
    else:
        main()
