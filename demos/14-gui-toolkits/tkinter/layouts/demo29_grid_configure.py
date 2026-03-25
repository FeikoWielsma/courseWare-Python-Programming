import tkinter as tk

main_window = tk.Tk()

for i in range(3):
    main_window.columnconfigure(i, weight=1, minsize=75)
    main_window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(master=main_window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\n_column {j}")
        label.pack(padx=5, pady=5)

main_window.mainloop()
