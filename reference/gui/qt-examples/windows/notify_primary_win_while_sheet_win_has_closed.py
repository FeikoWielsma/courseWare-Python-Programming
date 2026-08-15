#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
notify primary window/main thread sheet window has closed

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


class SheetWin(QtGui.QWidget):
    def __init__(self, parent = None):
        super(SheetWin, self).__init__(parent)

        self.set_window_flags(QtCore.Qt.Sheet)


        btn = QtGui.QPushButton("close", self)
        btn.move(10, 10)
        btn.clicked.connect(self.close)

        self._settings = {"name" : "a", "age" : "b"}

    def close_event(self, evt):
        print "close_event"

        self.emit(QtCore.SIGNAL("sheet_win_close( QWidget * )"), self)

        return super(SheetWin, self).close_event(evt)


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        btn = QtGui.QPushButton("btn", self)
        btn.clicked.connect(self.btn_cb)

    def btn_cb(self):
        sw_obj = SheetWin(self)
        sw_obj.show()

        self.connect(sw_obj, QtCore.SIGNAL("sheet_win_close( QWidget * )"), self._sw_cb)

    def _sw_cb(self, sw_obj):
        print "_sw_cb", sw_obj

    def show_and_raise(self):
        self.show()
        self.raise_()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())