#!/usr/bin/python
# -*- coding: utf-8 -*-

# colors.py

import sys
from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.set_geometry(300, 300, 350, 280)
        self.set_window_title("Colors")

    def paint_event(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)

        self.draw_rectangles(qp)

        qp.end()

    def draw_rectangles(self, qp):
        color = QtGui.QColor(0, 0, 0)
        color.set_named_color("#d4d4d4")
        qp.set_pen(color)

        qp.set_brush(QtGui.QColor(255, 0, 0, 80))
        qp.draw_rect(10, 15, 90, 60)

        qp.set_brush(QtGui.QColor(255, 0, 0, 160))
        qp.draw_rect(130, 15, 90, 60)

        qp.set_brush(QtGui.QColor(255, 0, 0, 255))
        qp.draw_rect(250, 15, 90, 60)

        qp.set_brush(QtGui.QColor(10, 163, 2, 55))
        qp.draw_rect(10, 105, 90, 60)

        qp.set_brush(QtGui.QColor(160, 100, 0, 255))
        qp.draw_rect(130, 105, 90, 60)

        qp.set_brush(QtGui.QColor(60, 100, 60, 255))
        qp.draw_rect(250, 105, 90, 60)

        qp.set_brush(QtGui.QColor(50, 50, 50, 255))
        qp.draw_rect(10, 195, 90, 60)

        qp.set_brush(QtGui.QColor(50, 150, 50, 255))
        qp.draw_rect(130, 195, 90, 60)

        qp.set_brush(QtGui.QColor(223, 135, 19, 255))
        qp.draw_rect(250, 195, 90, 60)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()
