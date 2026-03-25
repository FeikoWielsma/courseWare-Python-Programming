#!/usr/local/bin/python
from Tkinter import Tk, Button, Toplevel
import calculator
import calculator_plus_ext
import calculator_plus_emb

# demo all 3 calculator flavors at once
# each is a distinct calculator object and window

root = Tk()
calculator.CalcGui(Toplevel())
calculator.CalcGui(Toplevel(), fg="white", bg="purple")
calculator_plus_ext.CalcGuiPlus(Toplevel(), fg="gold", bg="black")
calculator_plus_emb.CalcGuiPlus(fg="black", bg="red")
Button(root, text="Quit Calcs", command=root.quit).pack()
root.mainloop()
