from tkinter import *

mainWindow = Tk()
mainWindow.title("Hello tkinter")

lbl = Label(mainWindow, text="Hello")
lbl.grid(column=0, row=0)

mainWindow.mainloop()