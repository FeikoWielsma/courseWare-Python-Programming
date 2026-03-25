from tkinter import *
from tkinter.ttk import *

mainWindow = Tk()
mainWindow.title("Checkbox Demo")
mainWindow.geometry('500x200')

chk_state = BooleanVar()
chk_state.set(True)  # set check state
chk = Checkbutton(mainWindow, text='Choose', var=chk_state)
chk.grid(column=0, row=0)

mainWindow.mainloop()