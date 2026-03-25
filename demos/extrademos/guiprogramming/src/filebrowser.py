# this is a program that uses askopenfilename function to open files.
# this function is imported from tkFileDialog
# you can specify the filetypes of your choice
# there is an other function called LoadFileDialog which also
# performs the same function.
from Tkinter import *
from tkFileDialog import askopenfilename


def main():
    root = Tk()
    filename = askopenfilename(filetypes=[("allfiles", "*"), ("pythonfiles", "*.py")])


main()
