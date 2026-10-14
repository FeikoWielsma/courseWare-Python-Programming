from tkinter import *
from tkinter import ttk

main_window = Tk()
main_window.title("Tab Demo")
main_window.geometry("500x200")

tab_control = ttk.Notebook(main_window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text="First")
tab_control.add(tab2, text="Second")
tab_control.pack(expand=1, fill="both")

main_window.mainloop()
