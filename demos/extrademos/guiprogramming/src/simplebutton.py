# This is a simple python program to create a button.

title = "about button"

# importing Tkinter

import Tkinter

# create a class demo for creating a button


class Demo:
    def __init__(self):
        # Create a button

        w = Tkinter.Button(text="I am a button")

        # padx and pady are initialisation options which give the distance from 'x'and 'y' axis

        w.pack(padx=8, pady=8)


######################################################################

# Create demo in root window for testing.

if __name__ == "__main__":
    root = Tkinter.Tk()
    root.title(title)
    widget = Demo()
    root.mainloop()
