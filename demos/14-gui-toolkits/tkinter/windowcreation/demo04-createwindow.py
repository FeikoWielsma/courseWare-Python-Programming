# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
mainWindow = Tk()

# sets the geometry of main
# root window
mainWindow.geometry("500x200")


# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(mainWindow)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("500x200+500+300")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()

label = Label(mainWindow,
              text="This is the main window")
label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(mainWindow,
             text="Open a new window",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()