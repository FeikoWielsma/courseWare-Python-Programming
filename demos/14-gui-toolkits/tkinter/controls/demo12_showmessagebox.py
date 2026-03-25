from tkinter import *
from tkinter import messagebox

def clicked():
    messagebox.showinfo('Message title', 'Message content')

mainWindow = Tk()
mainWindow.title("MessageBox Demo")
mainWindow.geometry('500x200')

btn = Button(mainWindow, text='Click here', command=clicked)
btn.grid(column=0, row=0)

mainWindow.mainloop()