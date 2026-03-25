#!/usr/bin/env python
import findgtk
import gtk.glade
class TwoButtonsGUI:
    def __init__(self):
        self.window = gtk.glade.XML('GladeTwoButtonsGUI.glade', 'window1')

if __name__ == '__main__':
    TwoButtonsGUI()
    gtk.main()
