from tkinter import *

mainWindow = Tk()
mainWindow.title("Spinbox Demo")
mainWindow.geometry('500x200')

spin = Spinbox(mainWindow, from_=0, to=100, width=5)
spin.grid(column=0, row=0)

mainWindow.mainloop()