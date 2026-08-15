from tkinter import *

window = Tk()

window.title("Hello tkinter")

window.geometry('350x200')

spin = Spinbox(window, from_=0, to=100, width=5)

spin.grid(column=0, row=0)

window.mainloop()