#!/usr/bin/env python
import time
from threading import Thread

import findgtk
import gtk
from gui_queue import Queued

class CountUpGUI(Queued):
    """Does counting in a separate thread. To be safe, the other
    thread puts calls to threads_enter() and threads_leave() around
    all GTK code."""

    START = "Click me to start counting up."
    STOP = "I've counted to %s (click me to stop)."

    def __init__(self):
        Queued.__init__(self)
        self.window=gtk.Window()        
        self.button=gtk.Button(self.START)
        self.button.timesClicked = 0        
        self.window.add(self.button)
        self.thread = None


        #Call the toggleCount method when the button is clicked.
        self.button.connect("clicked", self.toggleCount)

        #Quit the program when the window is destroyed.
        self.window.connect("destroy", self.destroy)

        #Show the GUI
        self.button.show()
        self.window.show()

    def destroy(self, window):
        "Remove the window and quit the program."
        window.hide()
        gtk.main_quit()

    def toggleCount(self, button):
        if self.thread and self.thread.doCount:
            #Stop counting.
            self.thread.doCount = False
        else:
            #Start counting.
            self.thread = self.CountingThread(self, self.button)
            self.thread.start()

    def incrementCount(self, button, count):
        button.set_label(self.STOP % count)

    def resetCount(self, button):
        button.set_label(self.START)

    class CountingThread(Thread):
        """Increments a counter once per second and updates the button
        label accordingly. Updates the button label by putting an
        event on the GUI queue, rather than manipulating the GUI
        directly."""
        def __init__(self, gui, button):
            self.gui = gui
            Thread.__init__(self)
            self.button = button
            self.doCount = False
            self.count = 0
            self.setDaemon(True)
            
        def run(self):
            self.doCount = True
            while self.doCount:
                self.gui.gui_queue_append("incrementCount",
                                          [self.button, self.count])
                self.count += 1
                time.sleep(1)
            self.gui.gui_queue_append("resetCount", [self.button])
            self.count = 0

if __name__ == '__main__':    
    CountUpGUI()
    try:
        gtk.threads_init()
    except:
        print "No threading was enabled when you compiled pyGTK!"
        import sys
        sys.exit(1)
    gtk.threads_enter()
    gtk.main()
    gtk.threads_leave()
