import tkinter as tk

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

mainWindow = tk.Tk()
mainWindow.rowconfigure(0, minsize=50, weight=1)
mainWindow.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=mainWindow, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=mainWindow, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=mainWindow, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

mainWindow.mainloop()
