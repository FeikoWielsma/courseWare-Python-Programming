from tkinter import *
from tkinter.ttk import *

main_window = Tk()
main_window.title("Radio Button Demo")
main_window.geometry("500x200")

rad1 = Radiobutton(main_window, text="First", value=1)
rad2 = Radiobutton(main_window, text="Second", value=2)
rad3 = Radiobutton(main_window, text="Third", value=3)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

main_window.mainloop()
