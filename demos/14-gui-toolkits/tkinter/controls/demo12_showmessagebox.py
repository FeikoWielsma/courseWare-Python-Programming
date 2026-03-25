from tkinter import *
from tkinter import messagebox


def clicked():
    messagebox.showinfo("Message title", "Message content")


main_window = Tk()
main_window.title("MessageBox Demo")
main_window.geometry("500x200")

btn = Button(main_window, text="Click here", command=clicked)
btn.grid(column=0, row=0)

main_window.mainloop()
