from tkinter import *

from tkinter import scrolledtext

main_window = Tk()
main_window.title("Scrolled Text Control Demo")
main_window.geometry("500x200")

txt = scrolledtext.ScrolledText(main_window, width=40, height=10)
txt.grid(column=0, row=0)

main_window.mainloop()
