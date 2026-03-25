#This sample program is written as a class. The constructor(the ___init__
#method) is called with a parent widget, to which it adds a
#number of child widgets. The constructor starts by creating a Frame widget.
#A frame is a simple container, and is in this case used to hold the
#button and entry widgets.


from Tkinter import *


class App:
    def __init__(self,parent):
        #The frame instance is stored in a local variable 'f'.
        #After creating the widget, we immediately call the 
        #pack method to make the frame visible.

        f = Frame(parent)
        f.pack(padx=15,pady=15)
        
        #we then create an entry widget,pack it and then 
        #create two more button widgets as children to the frame.
    
        self.entry = Entry(f,text="enter your choice")
        self.entry.pack(side= TOP,padx=10,pady=12)
        
        #this time, we pass a number of options to the
        # constructor, as keyword arguments. The first button
        # is labelled "exit"and the second is labelled "Hello". 
        #Both buttons also take a command option. This option 
        #specifies a function, or (as in this
        #case) a bound method, which will be called when the button is clicked.
        
        self.button = Button(f, text="print",command=self.print_this)
        self.button.pack(side=BOTTOM,padx=10,pady=10)

        self.exit = Button(f, text="exit", command=f.quit)
        self.exit.pack(side=BOTTOM,padx=10,pady=10)

    def print_this(self):
        print "this is to be printed"

        #Finally, we provide some script level code that creates
        # a Tk root widget,and one instance of the App class using 
        #the root widget as its parent:

        #The last call is to the mainloop method on the root widget. It enters the
        #Tk event loop, in which the application will stay until the quit method is
        #called (just click the exit button), or the window is closed.


root = Tk()
root.title('Tkwidgets application')
app = App(root)

root.mainloop()

