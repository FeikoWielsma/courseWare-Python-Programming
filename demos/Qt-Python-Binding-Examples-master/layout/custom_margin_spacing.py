#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Custom margin and spacing of box layout

Tested environment:
    Mac OS X 10.6.8


http://doc.qt.nokia.com/latest/layout.html
http://doc.qt.nokia.com/latest/qlayout.html

http://www.pyside.org/docs/pyside/PySide/QtGui/QLayout.html
"""

import os
import sys

PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        vbox = QtGui.QVBoxLayout(self)

        chat_history = QtGui.QTextEdit(self)
        w, h = 100, 100
        chat_history.set_minimum_size(w, h)
        vbox.add_widget(chat_history)

        input_win = QtGui.QTextEdit(self)
        w, h = 100, 100
        input_win.set_minimum_size(w, h)
        vbox.add_widget(input_win)

        vbox.set_spacing(0)
        vbox.set_contents_margins(0, 0, 0, 0)

        self.set_layout(vbox)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
