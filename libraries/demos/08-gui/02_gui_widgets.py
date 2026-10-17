# INTERACTIVE : this demo opens a window and blocks until you close it

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widgets")
root.geometry("420x180")

ttk.Label(root, text="Hostname :").grid(row=0, column=0, padx=8, pady=8, sticky="e")

entry = ttk.Entry(root, width=24)
entry.grid(row=0, column=1, padx=8, pady=8, sticky="w")
entry.focus()

result = ttk.Label(root, text="nothing yet", foreground="grey")
result.grid(row=2, column=0, columnspan=2, padx=8, pady=12)


def look_up() -> None:
    name = entry.get().strip()
    if not name:
        result.configure(text="type a hostname first", foreground="red")
        return
    result.configure(text=f"{name} is at rack 4, site AMS", foreground="black")
    entry.delete(0, tk.END)


# command= takes the function itself, without parentheses.
ttk.Button(root, text="Look up", command=look_up).grid(row=1, column=1, padx=8, pady=4, sticky="w")

root.bind("<Return>", lambda _event: look_up())
root.bind("<Escape>", lambda _event: root.destroy())

root.mainloop()
