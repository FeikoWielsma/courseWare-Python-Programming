#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
QPixmap alpha_channel

Tested environment:
    Mac OS X 10.6.8


Install Oxygen icon on Mac OS X via MacPorts:

    sudo port install oxygen-icons


http://doc.qt.nokia.com/latest/qpixmap.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QPixmap.html#PySide.QtGui.PySide.QtGui.QPixmap.alpha_channel
"""

import sys

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

        if sys.platform == "darwin":
            QtGui.QIcon.set_theme_name("Oxygen")
            QtGui.QIcon.set_theme_search_paths(["/opt/local/share/icons"])

        icon = QtGui.QIcon.from_theme("user-online")
        #        icon = QtGui.QIcon("online.png")

        pix = icon.pixmap(100, 100)
        new_pix = pix.alpha_channel()

        label = QtGui.QLabel(self)
        label.move(10, 10)
        label.set_pixmap(pix)

        label2 = QtGui.QLabel(self)
        label2.move(10, 110)
        label2.set_pixmap(new_pix)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
