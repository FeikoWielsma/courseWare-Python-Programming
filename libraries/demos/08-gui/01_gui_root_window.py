# INTERACTIVE : this demo opens a window and blocks until you close it

import tkinter as tk

root = tk.Tk()
root.title("Playlist")

# "widthxheight+x+y" in pixels. Leave the position off and the window manager
# decides where to put it.
# root.geometry("420x220+300+200")
# root.minsize(300, 150)

message = tk.Label(
    root,
    text="Playlist editor\n\nPress Escape to close.",
    font=("TkDefaultFont", 12),
    justify="center",
)
message.pack(expand=True)

root.bind("<Escape>", lambda _event: root.destroy())

print("before mainloop()")
root.mainloop()
print("after mainloop()")
