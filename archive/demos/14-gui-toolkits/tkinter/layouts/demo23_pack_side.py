import tkinter as tk

main_window = tk.Tk()

frame1 = tk.Frame(master=main_window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=main_window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=main_window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

main_window.mainloop()
