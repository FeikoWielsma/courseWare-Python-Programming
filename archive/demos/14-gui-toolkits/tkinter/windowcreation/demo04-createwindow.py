# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
main_window = Tk()

# sets the geometry of main
# root window
main_window.geometry("500x200")


# function to open a new window
# on a button click
def open_new_window():
    # Toplevel object which will
    # be treated as a new window
    new_window = Toplevel(main_window)

    # sets the title of the
    # Toplevel widget
    new_window.title("New Window")

    # sets the geometry of toplevel
    new_window.geometry("500x200+500+300")

    # A Label widget to show in toplevel
    Label(new_window, text="This is a new window").pack()


label = Label(main_window, text="This is the main window")
label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(main_window, text="Open a new window", command=open_new_window)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()
