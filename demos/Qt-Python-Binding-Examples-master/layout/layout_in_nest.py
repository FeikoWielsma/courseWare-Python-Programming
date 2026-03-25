#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
layout in nest

Tested environment:
    Mac OS X 10.6.8

"""

import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui


class BeNestWidget(QtGui.QWidget):
    def __init__(self, container):
        super(BeNestWidget, self).__init__()

        container.add_widget(self)

        hbox = QtGui.QHBoxLayout(self)

        a_btn = QtGui.QPushButton("d", self)
        hbox.add_widget(a_btn)

        b_tn = QtGui.QPushButton("e", self)
        hbox.add_widget(b_tn)

        c_btn = QtGui.QPushButton("f", self)
        hbox.add_widget(c_btn)

        self.set_layout(hbox)


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        vbox = QtGui.QVBoxLayout(self)

        a_btn = QtGui.QPushButton("a", self)
        vbox.add_widget(a_btn)

        b_tn = QtGui.QPushButton("b", self)
        vbox.add_widget(b_tn)

        c_btn = QtGui.QPushButton("c", self)
        vbox.add_widget(c_btn)

        self.bn_widget = BeNestWidget(container=vbox)

        self.set_layout(vbox)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
