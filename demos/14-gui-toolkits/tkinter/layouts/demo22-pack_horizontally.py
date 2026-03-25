import tkinter as tk

mainWindow = tk.Tk()

frame1 = tk.Frame(master=mainWindow, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=mainWindow, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=mainWindow, height=25, bg="blue")
frame3.pack(fill=tk.X)

mainWindow.mainloop()
