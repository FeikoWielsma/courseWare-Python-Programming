from tkinter import *

main_window = Tk()
main_window.title("Table Demo")
main_window.geometry("500x200")

rows = []

for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=GROOVE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, "%d.%d" % (i, j))
        cols.append(e)
    rows.append(cols)

main_window.mainloop()
