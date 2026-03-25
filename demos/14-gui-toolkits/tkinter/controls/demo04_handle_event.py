from tkinter import *


def clicked():
    lbl.configure(text="Button was clicked !!")


main_window = Tk()
main_window.title("Hello tkinter")
main_window.geometry("350x200")

lbl = Label(main_window, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(main_window, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

main_window.mainloop()
