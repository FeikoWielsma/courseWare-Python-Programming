import tkinter as tk

main_window = tk.Tk()

frame1 = tk.Frame(master=main_window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=main_window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=main_window, width=25, height=25, bg="blue")
frame3.pack()

main_window.mainloop()
