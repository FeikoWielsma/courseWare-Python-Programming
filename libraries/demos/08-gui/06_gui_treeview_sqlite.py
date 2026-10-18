# INTERACTIVE : this demo opens a window and blocks until you close it

import csv
import sqlite3
import tkinter as tk
from pathlib import Path
from tkinter import ttk

DATA = Path(__file__).resolve().parents[2] / "data"
DB = DATA / "gui-playlist.db"

COLUMNS = ("title", "artist", "genre", "year", "duration_s", "plays")

if not DB.exists():
    with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    connection = sqlite3.connect(DB)
    connection.execute(
        "CREATE TABLE tracks ("
        "title TEXT PRIMARY KEY, artist TEXT, genre TEXT, year INTEGER, "
        "duration_s REAL, plays REAL)"
    )
    connection.executemany(
        "INSERT INTO tracks VALUES (:title, :artist, :genre, :year, :duration_s, :plays)",
        [{key: row[key] or None for key in COLUMNS} for row in rows],
    )
    connection.commit()
    connection.close()
    print(f"created {DB.name} with {len(rows)} rows")


def query(term: str) -> list[tuple[str, ...]]:
    # The column names are a constant in this file, so formatting them in is
    # safe. The user's text is not, and goes in as a ? parameter below.
    sql = f"SELECT {', '.join(COLUMNS)} FROM tracks"
    parameters: tuple[str, ...] = ()
    if term:
        sql += " WHERE artist LIKE ? OR genre LIKE ? OR title LIKE ?"
        parameters = (f"%{term}%",) * 3
    sql += " ORDER BY title"
    connection = sqlite3.connect(DB)
    found = connection.execute(sql, parameters).fetchall()
    connection.close()
    return found


root = tk.Tk()
root.title("Playlist")
root.geometry("760x400")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

bar = ttk.Frame(root, padding=8)
bar.grid(row=0, column=0, sticky="ew")
bar.columnconfigure(1, weight=1)
ttk.Label(bar, text="Filter :").grid(row=0, column=0, padx=(0, 6))

filter_entry = ttk.Entry(bar)
filter_entry.grid(row=0, column=1, sticky="ew")
filter_entry.focus()

tree = ttk.Treeview(root, columns=COLUMNS, show="headings")
tree.grid(row=1, column=0, sticky="nsew", padx=8)
for column in COLUMNS:
    tree.heading(column, text=column.replace("_", " ").title())
    tree.column(column, width=110, anchor="e" if column in {"year", "duration_s", "plays"} else "w")

status = ttk.Label(root, padding=6)
status.grid(row=2, column=0, sticky="ew")


def refresh() -> None:
    term = filter_entry.get().strip()
    # A Treeview is not a data store; you empty it and refill it.
    tree.delete(*tree.get_children())
    found = query(term)
    for row in found:
        tree.insert("", tk.END, values=["" if value is None else value for value in row])
    status.configure(text=f"{len(found)} row(s) matching {term or 'anything'}")
    print(f"query({term!r}) returned {len(found)} rows")


ttk.Button(bar, text="Search", command=refresh).grid(row=0, column=2, padx=6)

root.bind("<Return>", lambda _event: refresh())
root.bind("<Escape>", lambda _event: root.destroy())

refresh()
root.mainloop()
