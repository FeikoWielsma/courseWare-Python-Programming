import tkinter as tk

def clearTextInput():
    txt.delete(0,tk.END)

mainWindow = tk.Tk()
mainWindow.title("Demo Delete Text from Entry Control")
mainWindow.geometry("400x240")

txt =tk.Entry(mainWindow, width=30)
txt.pack()

btnRead=tk.Button(mainWindow, height=1, width=10, text="Clear", command=clearTextInput)
btnRead.pack()

mainWindow.mainloop()