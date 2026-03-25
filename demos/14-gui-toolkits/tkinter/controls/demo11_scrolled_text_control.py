from tkinter import *

from tkinter import scrolledtext

mainWindow = Tk()
mainWindow.title("Scrolled Text Control Demo")
mainWindow.geometry('500x200')

txt = scrolledtext.ScrolledText(mainWindow, width=40, height=10)
txt.grid(column=0, row=0)

mainWindow.mainloop()