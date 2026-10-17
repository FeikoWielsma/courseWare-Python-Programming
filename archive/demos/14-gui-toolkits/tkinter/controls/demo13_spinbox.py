from tkinter import *

main_window = Tk()
main_window.title("Spinbox Demo")
main_window.geometry("500x200")

spin = Spinbox(main_window, from_=0, to=100, width=5)
spin.grid(column=0, row=0)

main_window.mainloop()
