from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk


def clicked():
    print(bar["value"])
    bar["value"] += 10


main_window = Tk()
main_window.title("Progressbar Demo")
main_window.geometry("500x200")

style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background="black")

bar = Progressbar(main_window, length=200, style="black.Horizontal.TProgressbar")
bar["value"] = 20
bar.grid(column=0, row=0)

btn = Button(main_window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

main_window.mainloop()
