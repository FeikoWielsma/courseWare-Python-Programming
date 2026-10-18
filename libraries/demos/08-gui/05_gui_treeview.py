# INTERACTIVE : this demo opens a window and blocks until you close it

import csv
import tkinter as tk
from pathlib import Path
from tkinter import ttk

DATA = Path(__file__).resolve().parents[2] / "data"

COLUMNS = {
    "title": 220,
    "artist": 160,
    "genre": 90,
    "year": 70,
    "duration_s": 90,
    "plays": 70,
}

with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))

root = tk.Tk()
root.title("Playlist")
root.geometry("820x360")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# show="headings" hides the tree column on the left, which is what turns a
# Treeview from an outline widget into a plain table.
tree = ttk.Treeview(root, columns=list(COLUMNS), show="headings", selectmode="browse")
tree.grid(row=0, column=0, sticky="nsew")


def sort_by(column: str, descending: bool) -> None:
    def key(pair: tuple[str, str]) -> tuple[int, float, str]:
        text = pair[0]
        if not text:
            return (2, 0.0, "")
        try:
            return (0, float(text), "")
        except ValueError:
            return (1, 0.0, text.lower())

    ordered = sorted(
        ((tree.set(item, column), item) for item in tree.get_children("")),
        key=key,
        reverse=descending,
    )
    for index, (_value, item) in enumerate(ordered):
        tree.move(item, "", index)
    tree.heading(column, command=lambda: sort_by(column, not descending))


for column, width in COLUMNS.items():
    # The heading is what the user reads; the column is how it behaves.
    tree.heading(
        column,
        text=column.replace("_", " ").title(),
        command=lambda c=column: sort_by(c, False),
    )
    anchor = "e" if column in {"year", "duration_s", "plays"} else "w"
    tree.column(column, width=width, anchor=anchor)

# Tags let a whole row be styled, which is the Treeview version of the
# colour-coded cell from the rich table in module 3.
tree.tag_configure("favourite", background="#dceeff")
tree.tag_configure("never", background="#eeeeee")

for row in rows:
    tag = "never" if not row["last_played"] else ""
    if int(row["plays"]) >= 50:
        tag = "favourite"
    tree.insert("", tk.END, values=[row[name] for name in COLUMNS], tags=(tag,))

# A Treeview does not scroll itself; it is wired to a Scrollbar by hand.
scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.grid(row=0, column=1, sticky="ns")

selected = ttk.Label(root, text="select a row", padding=6)
selected.grid(row=1, column=0, columnspan=2, sticky="ew")
tree.bind(
    "<<TreeviewSelect>>",
    lambda _event: selected.configure(text=" | ".join(tree.item(tree.focus(), "values"))),
)

root.bind("<Escape>", lambda _event: root.destroy())

root.mainloop()
