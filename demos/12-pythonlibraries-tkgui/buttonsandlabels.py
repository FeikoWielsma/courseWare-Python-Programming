from tkinter import * # import all tkinter widget classes

class Window(Frame): # new class 'Window' inherits from tkinter class 'Frame'
    
    def __init__(self, parent): # define inherited-class window constructor
        Frame.__init__(self,parent,background="beige")
        self.parent=parent
        self.Interface() # call Interface()
    
    def Interface(self): # define your window container and its widgets
        self.parent.title("Button Test") # window title
        self.pack(fill=BOTH,expand=1) # pack widgets into window
        lbl01=Label(self, # 'Label' widget for label 01
            text="Click either the green or blue button.",
            foreground="blue",background="beige")
        lbl01.place(x=10,y=10) # place label 01
        exitbutton=Button(self, # 'Button' widget for exit button
            text="Exit Program",foreground="blue",background="red",
            command=self.quit) # call built-in tkinter 'quit' function
        exitbutton.place(x=150,y=120) # place exit button
        grnbtn=Button(self, # 'Button' widget for green button
            text="GREEN",foreground="purple",background="green",
            command=self.grnbtn) # call grnbtn()                     
        grnbtn.place(x=10,y=40) # place green button
        blubtn=Button(self, # 'Button' widget for blue button
            text="BLUE",foreground="yellow",background="blue",
            command=self.blubtn) # call blubtn()
        blubtn.place(x=10,y=80) # place blue button
        clrlbls=Button(self, # 'Button' widget for clear-labels reset
            text="Reset",command=self.clrlbls) # call clrlbls()
        clrlbls.place(x=10, y=120) # place clear-labels reset button
    
    def clrlbls(self): # define clear-labels function
        print("You clicked the Reset button.")
        lbl02=Label(self, # 'Label' widget for label 02
            text="                                                   ",
            background="beige") # clears label 02 through wide, empty text
        lbl02.place(x=80,y=40) # place label 02
        lbl03=Label(self, # 'Label' widget for label 03 
            text="                                                   ",
            background="beige") # clears label 03 through wide, empty text
        lbl03.place(x=80,y=80) # place label 03
    
    def grnbtn(self): # define green-button function
        print("Thank you for clicking the GREEN button.")
        lbl02=Label(self,  # 'Label' widget for label 02
            text="You clicked the green button.",
            foreground="blue",background="beige")
        lbl02.place(x=80,y=40) # place label 02
    
    def blubtn(self): # define blue-button function
        print("Thank you for clicking the BLUE button.")
        lbl03=Label(self, # 'Label' widget for label 03
            text="You clicked the blue button.",
            foreground="blue",background="beige")
        lbl03.place(x=80,y=80) # place label 03
def main():
    root=Tk()
    root.geometry("275x160+500+300") # width, height, and x and y 
    app=Window(root)                 # coordinates for window position
    root.mainloop() # wait for user to press a button
    root.destroy() # on exit, close window, but not IDE

if __name__=='__main__':
    main() # call main program 

