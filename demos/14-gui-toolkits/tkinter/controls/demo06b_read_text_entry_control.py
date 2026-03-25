from tkinter import *
import tkinter as tk


def clicked():
    res = "Welcome to " + txt.get()
    txt.delete(0, tk.END)
    lbl.configure(text=res)


main_window = Tk()
main_window.title("Demo Text to Label")
main_window.geometry("350x200")

lbl = Label(main_window, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(main_window, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

txt = Entry(main_window, width=20)
txt.grid(column=0, row=2)

main_window.mainloop()
