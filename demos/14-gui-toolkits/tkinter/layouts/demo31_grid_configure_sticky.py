import tkinter as tk

mainWindow = tk.Tk()
mainWindow.columnconfigure(0, minsize=250)
mainWindow.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="n")

mainWindow.mainloop()
