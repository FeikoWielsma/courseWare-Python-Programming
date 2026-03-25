from tkinter import *

def clicked():
    lbl.configure(text="Button was clicked !!")

mainWindow = Tk()
mainWindow.title("Hello tkinter")
mainWindow.geometry('350x200')

lbl = Label(mainWindow, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(mainWindow, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

mainWindow.mainloop()