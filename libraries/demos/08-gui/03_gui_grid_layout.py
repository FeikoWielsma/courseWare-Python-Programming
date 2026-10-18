# INTERACTIVE : this demo opens a window and blocks until you close it

import tkinter as tk
from tkinter import ttk

FIELDS = ["Title", "Artist", "Genre", "Duration", "Plays"]

root = tk.Tk()
root.title("grid layout")
root.geometry("480x260")

form = ttk.Frame(root, padding=12)
form.grid(row=0, column=0, sticky="nsew")

# A widget only stretches if its row and column are told they may.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
form.columnconfigure(1, weight=1)

entries: dict[str, ttk.Entry] = {}
for row, field in enumerate(FIELDS):
    # sticky is compass points.
    ttk.Label(form, text=f"{field} :").grid(row=row, column=0, sticky="e", padx=(0, 8), pady=4)
    entry = ttk.Entry(form)
    entry.grid(row=row, column=1, sticky="ew", pady=4)
    entries[field] = entry

buttons = ttk.Frame(form)
# columnspan lets one widget sit across both columns of the grid.
buttons.grid(row=len(FIELDS), column=0, columnspan=2, sticky="e", pady=(12, 0))
ttk.Button(buttons, text="Cancel", command=root.destroy).grid(row=0, column=0, padx=4)
ttk.Button(
    buttons,
    text="Save",
    command=lambda: print({name: field.get() for name, field in entries.items()}),
).grid(row=0, column=1)

entries["Title"].focus()
root.bind("<Escape>", lambda _event: root.destroy())

root.mainloop()
