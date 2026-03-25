import tkinter as tk

mainWindow = tk.Tk()

frame1 = tk.Frame(master=mainWindow, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=mainWindow, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=mainWindow, width=25, height=25, bg="blue")
frame3.pack()

mainWindow.mainloop()
