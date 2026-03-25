import tkinter as tk

mainWindow = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
mainWindow.bind("<Key>", handle_keypress)

mainWindow.mainloop()
