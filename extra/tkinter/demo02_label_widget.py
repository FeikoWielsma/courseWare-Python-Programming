from tkinter import *

window = Tk()

window.title("Hello tkinter")

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

window.mainloop()