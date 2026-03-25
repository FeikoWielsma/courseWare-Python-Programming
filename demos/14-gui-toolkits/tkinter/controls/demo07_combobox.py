from tkinter import *
from tkinter.ttk import *

mainWindow = Tk()
mainWindow.title("Combobox Demo")
mainWindow.geometry('500x200')

combo = Combobox(mainWindow)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)

mainWindow.mainloop()