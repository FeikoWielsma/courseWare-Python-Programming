import tkinter as tk

main_window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(master=main_window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\n_column {j}")
        label.pack()

main_window.mainloop()
