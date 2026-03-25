#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
collect data for analysing user behaves

Tested environment:
    Mac OS X 10.6.8
    
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

    def show_and_raise(self):
        self.show()
        self.raise_()

        
def last_window_closed():
    print "last_window_closed"


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    QtGui.QWidget.connect(app, QtCore.SIGNAL("last_window_closed()"), last_window_closed)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())