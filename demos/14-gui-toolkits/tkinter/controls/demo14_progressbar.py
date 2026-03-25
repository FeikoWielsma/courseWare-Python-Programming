from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

def clicked():
    print(bar['value'])
    bar['value'] += 10

mainWindow = Tk()
mainWindow.title("Progressbar Demo")
mainWindow.geometry('500x200')

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(mainWindow, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 20
bar.grid(column=0, row=0)

btn = Button(mainWindow, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

mainWindow.mainloop()