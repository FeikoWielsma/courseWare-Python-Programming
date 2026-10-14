from tkinter import *
from tkinter.ttk import *

main_window = Tk()
main_window.title("Combobox Demo")
main_window.geometry("500x200")

combo = Combobox(main_window)
combo["values"] = (1, 2, 3, 4, 5, "Text")
combo.current(1)  # set the selected item
combo.grid(column=0, row=0)

main_window.mainloop()
