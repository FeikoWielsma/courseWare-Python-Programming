from tkinter import *
from tkinter.ttk import *

mainWindow = Tk()
mainWindow.title("Radio Button Demo")
mainWindow.geometry('500x200')

rad1 = Radiobutton(mainWindow, text='First', value=1)
rad2 = Radiobutton(mainWindow, text='Second', value=2)
rad3 = Radiobutton(mainWindow, text='Third', value=3)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

mainWindow.mainloop()