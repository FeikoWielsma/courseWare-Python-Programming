from tkinter import * # import (bind to) the standard Tk widgets 
from tkinter import ttk # also import the more-recent Themed Tk widgets

def texter(*args): # texter() 
    try:           # = GUI function to retrieve and display text
        copytxt=txtin.get() # get() = retrieve input
        txtout.set(copytxt) # set() = display output
    except ValueError:
        pass
def adder(*args): # adder()
    try:          # = GUI function to retrieve and add "a" and "b"
        a_in=a.get()
        b_in=b.get()
        total.set(a_in+b_in)
    except ValueError:
        pass

root=Tk()
root.title("Entering Text and Numeric Values") # window title
window=ttk.Frame(root,padding="12 12 12 12") # window setup
window.grid(column=0,row=0,sticky=(N,W,E,S))
window.columnconfigure(0,weight=1) # adjust window size
window.rowconfigure(0,weight=1)    # automatically
# variable type definitions
txtin=StringVar() # - text string
txtout=StringVar() 
a=DoubleVar() # - floating numerical value
b=DoubleVar()
total=DoubleVar()
# plan a ttk grid, and then set up your window according to that grid 
# - row and column numbers determine grid positions
ttk.Label(window,text="Entering Text").grid(row=1,column=2,sticky=(W,E))
# enter text through row 2, ttk Label and Entry widgets to enter text
ttk.Label(window,text="Type text here: ").grid(row=2,column=1,sticky=E)
txt_entry=ttk.Entry(window,width=7,textvariable=txtin)
txt_entry.grid(row=2,column=2,sticky=(W,E))
# display text through row 3, ttk Label and Button widgets to display text
ttk.Label(window,text="Text = ").grid(row=3,column=1,sticky=E)
ttk.Label(window,textvariable=txtout).grid(row=3,column=2,sticky=(W,E))
ttk.Button(window,text="Display Text",command=texter).grid(row=3,
column=3,sticky=E) # ttk Button widget calls texter() function
# to save horizontal space split ttk code lines only after commas
ttk.Label(window,text="Entering Numeric Values").grid(row=4,
column=2,sticky=(W,E))
# enter value a through row 5, ttk Label and Entry widgets to enter "a"
ttk.Label(window,text="a = ").grid(row=5,column=1,sticky=E)
a_entry=ttk.Entry(window,width=7,textvariable=a)
a_entry.grid(row=5,column=2,sticky=(W,E))
# enter value b through row 7, ttk Label and Entry widgets to enter "b"
ttk.Label(window, text="b = ").grid(row=6,column=1,sticky=E)
b_entry=ttk.Entry(window,width=7,textvariable=b)
b_entry.grid(row=6,column=2,sticky=(W,E))
# display total through row 7, ttk Label widget for "total" row
ttk.Label(window,text="total = ").grid(row=7,column=1,sticky=E)
ttk.Label(window,textvariable=total).grid(row=7,column=2,sticky=(W,E))
ttk.Button(window,text="Add a and b",command=adder).grid(row=7,
column=3,sticky=E) # ttk Button widget calls adder() function
ttk.Button(window,text="Exit Program",command=window.quit).grid(row=8,
column=3,sticky=E) # window 'quit' provides clean exit
# padx and pady pad widgets (children) to avoid crowding
for child in window.winfo_children():child.grid_configure(padx=5,pady=5)
txt_entry.focus() # places cursor intially within text-entry field
root.bind('<F12>',texter) # F12 also calls texter() function
root.bind('<Return>',adder) # Return also calls adder() function
root.mainloop() # wait for input
root.destroy() # provides clean exit

