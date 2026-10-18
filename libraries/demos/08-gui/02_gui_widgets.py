# INTERACTIVE : opens a window until it is closed

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Add a track")
playlist: list[tuple[str, str]] = []
ttk.Label(root, text="Title :").grid(row=0, column=0, padx=8, pady=8)
entry = ttk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=8, pady=8)
ttk.Label(root, text="Genre :").grid(row=1, column=0, padx=8)
genre = ttk.Combobox(root, values=["Rock", "Pop", "Soul", "Country", "Electronic"],
                     state="readonly")
genre.set("Rock")
genre.grid(row=1, column=1, padx=8)
result = ttk.Label(root, text="No tracks added")
result.grid(row=3, column=0, columnspan=2, pady=8)


def add_track() -> None:
    title = entry.get().strip()
    if not title:
        result.configure(text="Enter a title first")
        return
    playlist.append((title, genre.get()))
    result.configure(text=f"{title}: {genre.get()} ({len(playlist)} tracks)")
    entry.delete(0, tk.END)


ttk.Button(root, text="Add", command=add_track).grid(row=2, column=1, pady=8)
root.bind("<Return>", lambda _event: add_track())
root.bind("<Escape>", lambda _event: root.destroy())
entry.focus()
root.mainloop()
