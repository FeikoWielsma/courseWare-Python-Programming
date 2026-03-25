import tkinter as tk

mainWindow = tk.Tk()

def handle_click_left(event):
    print("Left button was clicked!")

def handle_click_right(event):
    print("Right button was clicked!")

btn = tk.Button(mainWindow, text="Click Me")
btn.grid(column=0, row=1)
btn.bind("<Button-1>", handle_click_left)
btn.bind("<Button-3>", handle_click_right)

mainWindow.mainloop()