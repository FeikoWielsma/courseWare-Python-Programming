# INTERACTIVE : this demo opens a window and blocks until you close it

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Events")
root.geometry("520x320")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

status = ttk.Label(root, text="waiting for an event", padding=8)
status.grid(row=0, column=0, sticky="ew")

canvas = tk.Frame(root, background="#dddddd", width=480, height=200)
canvas.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)


def report(what: str, event: tk.Event) -> None:
    status.configure(text=f"{what}  at ({event.x}, {event.y})")
    print(f"{what:<14} x={event.x:<4} y={event.y:<4} keysym={event.keysym!r}")


root.bind("<Key>", lambda event: report(f"key {event.keysym}", event))
canvas.bind("<Button-1>", lambda event: report("left click", event))
canvas.bind("<Button-3>", lambda event: report("right click", event))
canvas.bind("<Motion>", lambda event: report("mouse moved", event))

# <Configure> fires when the widget is resized, which is how a program notices
# the user has dragged the window edge.
canvas.bind("<Configure>", lambda event: report("resized", event))

# A Button's command= is the same idea with the event thrown away, which is why
# a command callback takes no arguments and a bind callback takes exactly one.
ttk.Button(root, text="Quit", command=root.destroy).grid(row=2, column=0, pady=8)

root.bind("<Escape>", lambda _event: root.destroy())

root.mainloop()
