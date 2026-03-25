import tkinter as tk

main_window = tk.Tk()

frame1 = tk.Frame(master=main_window, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=main_window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=main_window, height=25, bg="blue")
frame3.pack(fill=tk.X)

main_window.mainloop()
