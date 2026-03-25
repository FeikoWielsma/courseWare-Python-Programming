from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
import sqlite3
import csv

mainWindow = Tk()
mainWindow.columnconfigure(0, minsize=250)
mainWindow.rowconfigure([0, 0], minsize=200)

tree = ttk.Treeview(mainWindow, column=("c1", "c2", "c3", "c4"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="NAME")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="DURATION")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="LOCATION")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="PRICE")
# tree.pack()
tree.grid(row=0, column=0)

mainWindow.title("Training Application")
mainWindow.geometry('900x500')

menu = Menu(mainWindow)

new_item = Menu(menu)

def OpenFile():
    file = filedialog.askopenfilename(initialdir=".", title="Select file",
                               filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))
    # tkinter.messagebox.showinfo("Opening File" + file)
    print(file)

def ReadCourses():
    # courses = []
    with open('courses.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for course in csv_reader:
            print(type(course))
            if line_count == 0:
                print(f'{course[0]:10}{course[1]:10}{course[2]:15}{course[3]}')
                line_count += 1
            else:
                tree.insert("", tk.END, values=course)
                print(f'{course[0]:10}{course[1]:10}{course[2]:15}{course[3]}')
                line_count += 1
                # courses.append(course)
        print()
        print(f'Processed {line_count} courses.')
        LoadCourses()

def AddCourse():
    print("Adding a new course")

def EditCourse():
    print("Editing a new course")
    treerow = tree.item(tree.focus())
    print(treerow['values'])

def ExitApplication():
    print("Exit application")
    mainWindow.destroy()

def LoadCourses():
    con1 = sqlite3.connect("courses.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM courses")
    rows = cur1.fetchall()
    print(type(rows))
    for row in rows:
        print(type(row))
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()

def Clicked(event):
    print("Table Clicked")
    treerow = tree.item(tree.focus())
    # name = treerow.values[0]

    # duration = treerow.values[1]
    # location = treerow.values[2]
    # price = treerow.values[3]
    print(treerow['values'])
    print(treerow.keys())
    print(treerow.values())
    print(type(treerow.values()))
    # rclicked = tree.  get_row_clicked(event)
    # cclicked = tree.get_col_clicked(event)
    # clicks = (rclicked, cclicked)
    # print('clicks:', clicks)

new_item.add_command(label='Open', command=OpenFile)
new_item.add_command(label='LoadDB', command=LoadCourses)
new_item.add_command(label='New', command=AddCourse)
new_item.add_command(label='Edit', command=EditCourse)
new_item.add_command(label='ReadCSV', command=ReadCourses)
new_item.add_separator()
new_item.add_command(label='Exit', command=ExitApplication)

menu.add_cascade(label='File', menu=new_item)

mainWindow.bind('<Button-1>', Clicked)
mainWindow.config(menu=menu)

mainWindow.mainloop()