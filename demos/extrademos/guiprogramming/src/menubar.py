#this is program that creates a menubar using Tkinter widgets.
# a menubar is just a frame that holds menus.
#We will then pass menubar to all of the subsequent menus we'll define
#(File, Edit, Help, etc.) as the parent function.
#A menu in Tk is a combination of a Menubutton (the title of the menu) and
#the Menu (what drops down when the Menubutton is pressed)

from Tkinter import *

class mywidgets:
    def __init__(self,root):
        frame = Frame(root)
        self.makeMenuBar(frame)
        frame.pack()
        return


    def makeMenuBar(self,frame):
        menubar = Frame(frame,relief=RAISED,borderwidth=1)
        menubar.pack()
        
        #A menu in Tk is a combination of a Menubutton (the title of the
        #menu) and the Menu (what drops down when the Menubutton is pressed)
               
        mb_file = Menubutton(menubar,text='file')
        mb_file.pack(side=LEFT)
        mb_file.menu = Menu(mb_file)
        
        #Once we've specified the menubutton and the menu, we can add
        #different commands to the menu
        
        mb_file.menu.add_command(label='open')
        mb_file.menu.add_command(label='close')
        
        mb_edit = Menubutton(menubar,text='edit')
        mb_edit.pack(side=LEFT)
        mb_edit.menu = Menu(mb_edit)
        mb_edit.menu.add_command(label='copy')
        mb_edit.menu.add_command(label='paste')
        
        mb_help = Menubutton(menubar,text='help')
        mb_help.pack(padx=25,side=RIGHT)
        
        mb_file['menu'] = mb_file.menu
        mb_edit['menu'] = mb_edit.menu
        return 

def main():
    root = Tk()
    k=mywidgets(root)
    root.title('menu bar')
    root.mainloop()
main()

