import tkinter as tk

main_window = tk.Tk()
main_window.columnconfigure(0, minsize=250)
main_window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="n")

main_window.mainloop()
