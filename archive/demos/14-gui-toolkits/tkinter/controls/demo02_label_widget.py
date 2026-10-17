from tkinter import *

main_window = Tk()
main_window.title("Hello tkinter")

lbl = Label(main_window, text="Hello")
lbl.grid(column=0, row=0)

main_window.mainloop()
