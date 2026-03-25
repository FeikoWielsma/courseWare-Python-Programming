from tkinter import *


def select_item(i):
    index = int(i.widget.curselection()[0])
    value = i.widget.get(index)
    print("You selected item ", index, value)


main_window = Tk()
main_window.title("Listbox Demo")
main_window.geometry("500x200")

Lb1 = Listbox(main_window)
Lb1.bind("<<ListboxSelect>>", select_item)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
main_window.mainloop()
