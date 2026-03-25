from tkinter import *
import tkinter.messagebox
from tkinter import Menu
from tkinter import filedialog

window = Tk()

window.title("Training Application")
window.geometry('900x500')

menu = Menu(window)

new_item = Menu(menu)

def OpenFile():
    file = filedialog.askopenfilename(initialdir=".", title="Select file",
                               filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))
    # tkinter.messagebox.showinfo("Opening File" + file)
    print(file)

def AddCourse():
    print("Adding a new course")

def EditCourse():
    print("Editing a new course")

def ExitApplication():
    print("Exit application")
    window.destroy()

new_item.add_command(label='Open', command=OpenFile)
new_item.add_command(label='New', command=AddCourse)
new_item.add_command(label='Edit', command=EditCourse)
new_item.add_separator()
new_item.add_command(label='Exit', command=ExitApplication)

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

window.mainloop()