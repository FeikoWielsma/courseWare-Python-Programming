from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
import sqlite3
import csv

mainWindow = Tk()
mainWindow.columnconfigure(0, minsize=150)
mainWindow.rowconfigure([0, 0], minsize=15)

tree = ttk.Treeview(mainWindow, column=("c1", "c2", "c3", "c4"), show='headings')

tree.heading(column="c1", anchor=tk.W)
tree.heading(column="c2", anchor=tk.W)
tree.heading(column="c3", anchor=tk.W)
tree.heading(column="c4", anchor=tk.W)

tree.column("#1", anchor=tk.W)
tree.heading("#1", text="NAME")
tree.column("#2", anchor=tk.W)
tree.heading("#2", text="DURATION")
tree.column("#3", anchor=tk.W)
tree.heading("#3", text="LOCATION")
tree.column("#4", anchor=tk.W)
tree.heading("#4", text="PRICE")

lbl_form_title = tk.Label(master=mainWindow, text="List of Courses")
lbl_form_title.config(font=("Arial", 12, 'bold'))
lbl_form_title.grid(row=0, column=0, sticky="w", ipadx=10, ipady=15)

tree.grid(row=1, column=0, sticky="e", ipadx=100, ipady=15)

mainWindow.title("Training Application")
mainWindow.geometry('900x500')

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
    def Cancel():
        print("Cancel Clicked")
        newWindow.destroy()

    def CourseToAdd():
        print("Adding a new course")
        print(ent_course_name.get())
        print(ent_course_duration.get())
        print(ent_course_location.get())
        print(ent_course_price.get())

        conn = sqlite3.connect('courses.db')
        c = conn.cursor()
        with conn:
            conn.execute("INSERT INTO courses VALUES( ?, ?, ?, ?)",
            (ent_course_name.get(), ent_course_duration.get(), ent_course_location.get(), ent_course_price.get()))
        # clear fields for new entry
        ent_course_name.delete(0, 'end')
        ent_course_duration.delete(0, 'end')
        ent_course_location.delete(0, 'end')
        ent_course_price.delete(0, 'end')
        LoadCourses()

    print("Showing new course screen")

    newWindow = Toplevel(mainWindow)
    newWindow.title("Add Course")

    newWindow.geometry("500x200+500+200")

    newWindow.columnconfigure(0, minsize=150)
    newWindow.rowconfigure([6, 0], minsize=25)

    lbl_form_title = tk.Label(master=newWindow, text="Add Course Details:")
    lbl_form_title.config(font=("Arial", 12, 'bold'))
    lbl_form_title.grid(row=0, column=0, sticky="w", ipadx=10, ipady=15)

    lbl_course_name = tk.Label(master=newWindow, text="Course Name:")
    lbl_course_name.grid(row=1, column=0, sticky="w", ipadx=10, ipady=1)
    ent_course_name = tk.Entry(master=newWindow, width=40)
    ent_course_name.grid(row=1, column=1, sticky="w", ipadx=10, ipady=1)

    lbl_course_duration = tk.Label(master=newWindow, text="Course Duration:")
    lbl_course_duration.grid(row=2, column=0, sticky="w", ipadx=10, ipady=1)
    ent_course_duration = tk.Entry(master=newWindow, width=40)
    ent_course_duration.grid(row=2, column=1, sticky="w", ipadx=10, ipady=1)

    lbl_course_location = tk.Label(master=newWindow, text="Course Location:")
    lbl_course_location.grid(row=3, column=0, sticky="w", ipadx=10, ipady=1)
    ent_course_location = tk.Entry(master=newWindow, width=40)
    ent_course_location.grid(row=3, column=1, sticky="w", ipadx=10, ipady=1)

    lbl_course_price = tk.Label(master=newWindow, text="Course Price:")
    lbl_course_price.grid(row=4, column=0, sticky="w", ipadx=10, ipady=1)
    ent_course_price = tk.Entry(master=newWindow, width=40)
    ent_course_price.grid(row=4, column=1, sticky="w", ipadx=10, ipady=1)

    btn_cancel_add = tk.Button(master=newWindow, text="Cancel", command=Cancel)
    btn_cancel_add.grid(row=5, column=0, sticky="w", ipadx=10, ipady=1)

    btn_add_course = tk.Button(master=newWindow, text="Add Course", command = CourseToAdd)
    btn_add_course.grid(row=5, column=1, sticky="e", ipadx=10, ipady=1)

def EditCourse():
    print("Editing a new course")
    treerow = tree.item(tree.focus())
    print(treerow['values'])
    course = treerow['values']
    print(type(treerow['values']))
    coursename = course[0]
    courseduration =  course[1]
    courselocation = course[2]
    courseprice = course[3]
    print(coursename)
    print(courseduration)
    print(courselocation)
    print(courseprice)

    def Cancel():
        print("Cancel Clicked")
        newWindow.destroy()

    def CourseToUpdate():
        print("Updating a new course")
        print(ent_course_name.get())
        print(ent_course_duration.get())
        print(ent_course_location.get())
        print(ent_course_price.get())

        conn = sqlite3.connect('courses.db')
        with conn:
            cur = conn.cursor()
            cur.execute("UPDATE courses SET duration=?, location=?, price=? WHERE name=? ",
                        (ent_course_duration.get(), ent_course_location.get(),
                         ent_course_price.get(), ent_course_name.get()))
            conn.commit()

        print("Cancel Clicked")
        newWindow.destroy()
        LoadCourses()

    print("Showing edit course screen")

    newWindow = Toplevel(mainWindow)
    newWindow.title("Edit Course")

    newWindow.geometry("500x200+500+200")

    newWindow.columnconfigure(0, minsize=150)
    newWindow.rowconfigure([6, 0], minsize=25)

    lbl_form_title = tk.Label(master=newWindow, text="Add Course Details:")
    lbl_form_title.config(font=("Arial", 12, 'bold'))
    lbl_form_title.grid(row=0, column=0, sticky="w", ipadx=10, ipady=15)

    lbl_course_name = tk.Label(master=newWindow, text="Course Name:")
    lbl_course_name.grid(row=1, column=0, sticky="w", ipadx=10, ipady=1)
    ent_course_name = tk.Entry(master=newWindow, width=40)
    ent_course_name.insert(0, coursename)
    ent_course_name.grid(row=1, column=1, sticky="w", ipadx=10, ipady=1)

    lbl_course_duration = tk.Label(master=newWindow, text="Course Duration:")
    lbl_course_duration.grid(row=2, column=0, sticky="w", ipadx=10, ipady=1)
    ent_course_duration = tk.Entry(master=newWindow, width=40)
    ent_course_duration.insert(0, courseduration)
    ent_course_duration.grid(row=2, column=1, sticky="w", ipadx=10, ipady=1)

    lbl_course_location = tk.Label(master=newWindow, text="Course Location:")
    lbl_course_location.grid(row=3, column=0, sticky="w", ipadx=10, ipady=1)
    ent_course_location = tk.Entry(master=newWindow, width=40)
    ent_course_location.insert(0, courselocation)
    ent_course_location.grid(row=3, column=1, sticky="w", ipadx=10, ipady=1)

    lbl_course_price = tk.Label(master=newWindow, text="Course Price:")
    lbl_course_price.grid(row=4, column=0, sticky="w", ipadx=10, ipady=1)
    ent_course_price = tk.Entry(master=newWindow, width=40)
    ent_course_price.insert(0, courseprice)

    ent_course_price.grid(row=4, column=1, sticky="w", ipadx=10, ipady=1)

    btn_cancel_add = tk.Button(master=newWindow, text="Cancel", command=Cancel)
    btn_cancel_add.grid(row=5, column=0, sticky="w", ipadx=10, ipady=1)

    btn_add_course = tk.Button(master=newWindow, text="Update Course", command=CourseToUpdate)
    btn_add_course.grid(row=5, column=1, sticky="e", ipadx=10, ipady=1)

def ExitApplication():
    print("Exit application")
    mainWindow.destroy()

def LoadCourses():
    con1 = sqlite3.connect("courses.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM courses")
    rows = cur1.fetchall()
    print(type(rows))

    for i in tree.get_children():
        tree.delete(i)

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

menu = Menu(mainWindow)

filemenu = Menu(menu)
coursemenu = Menu(menu)
aboutmenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=OpenFile)
filemenu.add_command(label='ReadCSV', command=ReadCourses)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=ExitApplication)

menu.add_cascade(label='Load', menu=coursemenu)
coursemenu.add_command(label='LoadDB', command=LoadCourses)
coursemenu.add_command(label='Add', command=AddCourse)
coursemenu.add_command(label='Edit', command=EditCourse)

menu.add_cascade(label='About', menu=aboutmenu)

mainWindow.bind('<Button-1>', Clicked)
mainWindow.config(menu=menu)

mainWindow.mainloop()