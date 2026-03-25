from tkinter import *
from tkinter import Menu

def add_item():
    print("Add Item Clicked")

def exit_app():
    print("Exit Application")
    mainWindow.destroy()

mainWindow = Tk()
mainWindow.title("Menu Demo")
mainWindow.geometry('500x200')

menu = Menu(mainWindow )

new_item = Menu(menu)
new_item.add_command(label='New', command=add_item)
new_item.add_command(label='Edit')
new_item.add_separator()
new_item.add_command(label='Exit', command=exit_app)

menu.add_cascade(label='File', menu=new_item)

mainWindow.config(menu=menu)

mainWindow.mainloop()