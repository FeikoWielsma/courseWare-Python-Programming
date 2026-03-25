#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
QSpacerItem demo

Tested environment:
    Mac OS X 10.6.8
"""

import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui


class Demo(QtGui.QDialog):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        ok_btn = QtGui.QPushButton("ok")
        cancel_btn = QtGui.QPushButton("cancel")

        btn_layout = QtGui.QHBoxLayout()

        btn_layout.add_widget(ok_btn)

        btn_layout.add_spacer_item(QtGui.QSpacerItem(50, 50))

        btn_layout.add_widget(cancel_btn)

        layout = QtGui.QGridLayout()

        #        layout.add_layout(btn_layout, int row, int column, int row_span, int column_span, alignment = 0)
        layout.add_layout(btn_layout, 2, 0, 1, 3)

        self.set_layout(layout)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show()

    app.exec_()
