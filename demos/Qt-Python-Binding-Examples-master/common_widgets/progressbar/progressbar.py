#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.set_geometry(30, 40, 200, 25)
        self.pbar.set_maximum(0)
        self.pbar.set_minimum(0)
        self.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    assert ex != None
    app.exec_()
