#!/usr/bin/env python
import time
import findgtk
import gtk

from gui_queue import Queued

class ClickCountGUI(Queued):
    "When you click, it increments the label."

    CLICK_COUNT = 'Click count: %d'

    def __init__(self):
        Queued.__init__(self)
        self.window=gtk.Window()        
        self.button=gtk.Button(self.CLICK_COUNT % 0)
        self.button.timesClicked = 0        
        self.window.add(self.button)

        #Call the toggleCount method when the button is clicked.
        self.button.connect("clicked",
                            lambda(x): self.gui_queue_append("buttonClicked",
                                                             [x]))

        #Quit the program when the window is destroyed.
        self.window.connect("destroy",
                            lambda(x): self.gui_queue_append("destroy",
                                                             [x]))

        #Show the GUI
        self.button.show()
        self.window.show()

    def buttonClicked(self, button):
        "This button was clicked; increment the message on its label."
        button.timesClicked += 1
        button.set_label(self.CLICK_COUNT % button.timesClicked)

    def destroy(self, window):
        "Remove the window and quit the program."
        window.hide()
        gtk.main_quit()

if __name__ == '__main__':    
    ClickCountGUI()
    try:
        gtk.threads_init()
    except:
        print "No threading was enabled when you compiled pyGTK!"
        import sys
        sys.exit(1)
    gtk.threads_enter()
    gtk.main()
    gtk.threads_leave()
