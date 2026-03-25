from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Hello tkinter")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

tab_control.pack(expand=1, fill='both')

window.mainloop()