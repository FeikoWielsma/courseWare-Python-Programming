from tkinter import *
from tkinter import ttk

mainWindow = Tk()
mainWindow.title("Tab Demo")
mainWindow.geometry('500x200')

tab_control = ttk.Notebook(mainWindow)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
tab_control.pack(expand=1, fill='both')

mainWindow.mainloop()