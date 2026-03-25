#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
lay out in Gird demo

Tested environment:
    Mac OS X 10.6.8
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

        title = QtGui.QLabel("Title")
        author = QtGui.QLabel("Author")
        review = QtGui.QLabel("Review")

        title_edit = QtGui.QLineEdit()
        author_edit = QtGui.QLineEdit()
        review_edit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.set_spacing(10)

        grid.add_widget(title, 1, 0)
        grid.add_widget(title_edit, 1, 1)

        grid.add_widget(author, 2, 0)
        grid.add_widget(author_edit, 2, 1)

        grid.add_widget(review, 3, 0)
        grid.add_widget(review_edit, 3, 1, 5, 1)

        self.set_layout(grid)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
