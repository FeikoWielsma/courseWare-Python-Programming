2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Hello tkinter")

selected = IntVar()

rad1 = Radiobutton(window, text='First', value=1, variable=selected)

rad2 = Radiobutton(window, text='Second', value=2, variable=selected)

rad3 = Radiobutton(window, text='Third', value=3, variable=selected)


def clicked():
    print(selected.get())


btn = Button(window, text="Click Me", command=clicked)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)

btn.grid(column=3, row=0)

window.mainloop()