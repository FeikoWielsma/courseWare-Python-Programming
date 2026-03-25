#!/usr/bin/env python
import findgtk
import gtk

class TwoButtonsGUI:
    def __init__(self, msg1="Hello World", msg2="Hello Again"):
        #Set up the window and the button within.
        self.window=gtk.Window()
        self.box = gtk.VBox()
        self.window.add(self.box)

        self.button1 = gtk.Button(msg1)
        self.button2 = gtk.Button(msg2)
        self.box.pack_start(self.button1)
        self.box.pack_start(self.button2)

        #Show the GUI
        self.button1.show()
        self.button2.show()
        self.box.show()
        self.window.show()

if __name__ == '__main__':    
    TwoButtonsGUI()
    gtk.main()
