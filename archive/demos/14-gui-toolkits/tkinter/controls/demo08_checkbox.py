from tkinter import *
from tkinter.ttk import *

main_window = Tk()
main_window.title("Checkbox Demo")
main_window.geometry("500x200")

chk_state = BooleanVar()
chk_state.set(True)  # set check state
chk = Checkbutton(main_window, text="Choose", var=chk_state)
chk.grid(column=0, row=0)

main_window.mainloop()
