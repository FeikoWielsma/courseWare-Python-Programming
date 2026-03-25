#!/usr/bin/env python
import findgtk        
import gtk,gtk.glade
import pygtk
pygtk.require("2.0")
import gtk

class ClickCountGUI:
    "When you click, it increments the label."
    
    CLICK_COUNT = 'Click count: %d'

    def __init__(self):
        "Set up the window and the button within."
        self.window=gtk.Window()        
        self.button=gtk.Button(self.CLICK_COUNT % 0)
        self.button.timesClicked = 0        
        self.window.add(self.button)

        #Call the buttonClicked method when the button is clicked.
        self.button.connect("clicked", self.buttonClicked)

        #Quit the program when the window is destroyed.
        self.window.connect("destroy", self.destroy)

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
    gtk.main()
