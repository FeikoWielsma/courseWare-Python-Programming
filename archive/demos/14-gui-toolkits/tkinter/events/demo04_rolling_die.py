import random
import tkinter as tk


def roll():
    lbl_result["text"] = str(random.randint(1, 6))


main_window = tk.Tk()
main_window.columnconfigure(0, minsize=150)
main_window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Roll", command=roll)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

main_window.mainloop()
