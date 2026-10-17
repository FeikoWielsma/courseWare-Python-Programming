from tkinter import *

from tkinter.ttk import *


def clicked():
    print(selected.get())


main_window = Tk()
main_window.title("Demo Click Radio Button")

selected = IntVar()
rad1 = Radiobutton(main_window, text="First", value=1, variable=selected)
rad2 = Radiobutton(main_window, text="Second", value=2, variable=selected)
rad3 = Radiobutton(main_window, text="Third", value=3, variable=selected)

btn = Button(main_window, text="Click Me", command=clicked)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)

main_window.mainloop()
