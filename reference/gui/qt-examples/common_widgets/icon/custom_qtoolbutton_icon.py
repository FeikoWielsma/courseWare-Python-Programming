#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
custom QToolButton icon

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

        path = "mic-64x64.png"
        pix = QtGui.QPixmap(path)

        label = QtGui.QLabel(self)
        label.move(10, 10)
        label.set_pixmap(pix)

        btn = QtGui.QToolButton(self)
        btn.move(10, 100)
        btn.set_icon_size(QtCore.QSize(64, 64))

        # way A
        #        btn.set_icon(pix)

        # way B
        icon = QtGui.QIcon(pix)
        act = QtGui.QAction(icon, "Send", self)
        btn.set_default_action(act)

        style = "QLabel, QToolButton { border : 1px solid red; }"
        self.set_style_sheet(style)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
