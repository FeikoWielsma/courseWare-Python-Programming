#!/usr/bin/python
# -*- coding: utf-8 -*-

# points.py

import sys
import random
from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.set_geometry(300, 300, 250, 150)
        self.set_window_title("Points")

    def paint_event(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_points(qp)
        qp.end()

    def draw_points(self, qp):
        qp.set_pen(QtCore.Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.draw_point(x, y)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()
