#this is a simple program demonstrating the 'frame' widgets.frame
#widgets are containers for other widgets.
#frames can be used as a master for a group of widgets which will be
#handled by a geometry manager.

title='creating a frame'
from Tkinter import *
root = Tk()

# the appearance of the frame can be modified choosing a relief type and
# applying appropriate bandwidth.

Frame(root,borderwidth=2,relief=SUNKEN).pack(side=LEFT,padx=5,pady=5)
Label(root,text='I am a frame').pack(side=LEFT)

root.title(title)
root.mainloop()


