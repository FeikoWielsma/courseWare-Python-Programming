from tkinter import ttk
import tkinter as tk
import sqlite3


def connect():
    con1 = sqlite3.connect("cars.db")
    cur1 = con1.cursor()
    cur1.execute(
        "CREATE TABLE IF NOT EXISTS (id INTEGER PRIMARY KEY, Name TEXT, Price INT)"
    )
    con1.commit()
    con1.close()


def View():
    con1 = sqlite3.connect("cars.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM cars")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()


# connect to the database
# connect()

main_window = tk.Tk()

tree = ttk.Treeview(main_window, column=("c1", "c2", "c3"), show="headings")
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="ID")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="NAME")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="PRICE")
tree.pack()

button1 = tk.Button(text="Display data", command=View)
button1.pack(pady=10)

main_window.mainloop()
