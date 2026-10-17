# INTERACTIVE : this demo opens a window and blocks until you close it

import csv
import tkinter as tk
from pathlib import Path
from tkinter import ttk

DATA = Path(__file__).resolve().parents[2] / "data"

COLUMNS = {
    "hostname": 100,
    "site": 60,
    "role": 100,
    "os": 110,
    "cpu_cores": 70,
    "memory_gb": 80,
    "disk_gb": 80,
    "used_gb": 80,
}

with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))

root = tk.Tk()
root.title("Server inventory")
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
    tree.column(column, width=width, anchor="e" if column.endswith("_gb") else "w")

# Tags let a whole row be styled, which is the Treeview version of the
# colour-coded cell from the rich table in module 3.
tree.tag_configure("full", background="#ffd6d6")
tree.tag_configure("unknown", background="#eeeeee", foreground="#777777")

for row in rows:
    if not row["used_gb"]:
        tag = "unknown"
    elif float(row["used_gb"]) / float(row["disk_gb"]) >= 0.80:
        tag = "full"
    else:
        tag = ""
    # values must be in the same order as the columns list.
    tree.insert("", tk.END, values=[row[column] for column in COLUMNS], tags=(tag,))

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
