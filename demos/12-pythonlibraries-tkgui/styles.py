from tkinter import *  # import (bind to) the standard Tk widgets
from tkinter import ttk  # also import the more-recent Themed Tk widgets


def stoogenum(*args):  # stoogenum()
    try:  # = GUI function to retrieve and process "a"
        a_in = a.get()
        if a_in == 3.0:  # txta and txtb = result
            txta.set("Excellent work, Moe!")
            txtb.set("You are correct!")
        elif 3.0001 < a_in < 4.0001:
            txta.set("Good work, Larry!")
            txtb.set("You are close!")
        elif 1.9999 < a_in < 2.9999:
            txta.set("Good work, Larry!")
            txtb.set("You are close!")
        elif a_in > 4.0001:
            txta.set("Nice try, Curly!")
            txtb.set("But no cigar!")
        elif a_in < 2.9999:
            txta.set("Nice try, Curly!")
            txtb.set("But no cigar!")
    except ValueError:
        pass


def chicken(*args):  # chicken()
    try:  # = GUI function to weed out scaredy cats
        txta.set("You are a big")  # txta and txtb = result
        txtb.set("chicken!")
    except ValueError:
        pass


def reset(*args):  # reset()
    try:  # = GUI function to reset input "a" and its result
        a.set(0.0)
        txta.set("")  # txta and txtb = result
        txtb.set("")
    except ValueError:
        pass


root = Tk()
root.title("Ttk Widgets With Styles")  # window title
window = ttk.Frame(root, padding="12 12 12 12")  # window setup
window.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)  # adjust window size
window.rowconfigure(0, weight=1)  # automatically
# variable type definitions
txta = StringVar()  # - text string
txtb = StringVar()
a = DoubleVar()  # - floating numerical value
# define ttk widget styles
ttk.Style().configure(
    "TFrame", padding=1, relief="solid", background="beige"
)  # new default style for frame (window)
ttk.Style().configure(
    "TLabel",  # new default style for Label widgets
    background="beige",
    foreground="blue",
)
ttk.Style().configure(
    "TEntry",  # new default style for Entry widgets
    background="beige",
    foreground="black",
)
ttk.Style().configure(
    "TButton",  # new default style for Button widets
    padding=6,
    relief="raised",
    background="green",
    foreground="blue",
)
ttk.Style().configure(
    "Exit.TButton",  # custom stye for Exit-button widget
    padding=6,
    relief="solid",
    background="#afd",
    foreground="red",
)
# plan a ttk grid, and then set up your window according to that grid
# - row and column numbers determine grid positions
ttk.Label(window, text="How many stooges in").grid(row=1, column=1, sticky=E)
ttk.Label(window, text="The Three Stooges?").grid(row=1, column=2, sticky=W)
# enter value a through row 2, ttk Label and Entry widgets to enter "a"
ttk.Label(window, text="Enter a numeric value: ").grid(row=2, column=1, sticky=E)
a_entry = ttk.Entry(window, width=7, textvariable=a)
a_entry.grid(row=2, column=2, sticky=(W, E))
ttk.Button(window, text="Click if not so sure.", command=chicken).grid(
    row=3, column=1, sticky=W
)  # ttk Button widget calls stoogenum() function
ttk.Button(window, text="Click if sure.", command=stoogenum).grid(
    row=3, column=2, sticky=E
)  # ttk Button widget calls stoogenum() function
# display answer through row 4, columns 1 and 2
ttk.Label(window, textvariable=txta).grid(row=4, column=1, sticky=E)
ttk.Label(window, textvariable=txtb).grid(row=4, column=2, sticky=W)
ttk.Button(window, text="Reset", command=reset).grid(
    row=5, column=1, sticky=W
)  # ttk Button widget calls reset() function
ttk.Button(window, text="Exit Program", style="Exit.TButton", command=window.quit).grid(
    row=5, column=2, sticky=E
)  # window 'quit' provides clean exit
# padx and pady pad widgets (children) to avoid crowding
for child in window.winfo_children():
    child.grid_configure(padx=1, pady=5)
root.bind("<F12>", reset)  # F12 also calls reset() function
root.bind("<Return>", stoogenum)  # Return also calls stoogenum() function
root.mainloop()  # wait for input
root.destroy()  # provides clean exit
