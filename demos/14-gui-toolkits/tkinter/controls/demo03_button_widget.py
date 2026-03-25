from tkinter import *

mainWindow = Tk()
mainWindow.title("Hello tkinter")
mainWindow.geometry('350x200')

lbl = Label(mainWindow, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(mainWindow, text="Click Me")
btn.grid(column=0, row=1)

mainWindow.mainloop()