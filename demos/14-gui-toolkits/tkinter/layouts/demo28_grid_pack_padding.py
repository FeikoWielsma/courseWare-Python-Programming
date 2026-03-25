import tkinter as tk

mainWindow = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=mainWindow,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

mainWindow.mainloop()