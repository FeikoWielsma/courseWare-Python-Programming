from tkinter import *
import tkinter as tk

def clicked():
    res = "Welcome to " + txt.get()
    txt.delete(0, tk.END)
    lbl.configure(text=res)

mainWindow = Tk()
mainWindow.title("Demo Text to Label")
mainWindow.geometry('350x200')

lbl = Label(mainWindow, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(mainWindow, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

txt = Entry(mainWindow, width=20)
txt.grid(column=0, row=2)

mainWindow.mainloop()