#!/usr/bin/python
# -*- coding: utf-8 -*-

# penstyles.py

import sys
from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.set_geometry(300, 300, 280, 270)
        self.set_window_title("penstyles")

    def paint_event(self, e):
        qp = QtGui.QPainter()

        qp.begin(self)
        self.do_drawing(qp)
        qp.end()

    def do_drawing(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        qp.set_pen(pen)
        qp.draw_line(20, 40, 250, 40)

        pen.set_style(QtCore.Qt.DashLine)
        qp.set_pen(pen)
        qp.draw_line(20, 80, 250, 80)

        pen.set_style(QtCore.Qt.DashDotLine)
        qp.set_pen(pen)
        qp.draw_line(20, 120, 250, 120)

        pen.set_style(QtCore.Qt.DotLine)
        qp.set_pen(pen)
        qp.draw_line(20, 160, 250, 160)

        pen.set_style(QtCore.Qt.DashDotDotLine)
        qp.set_pen(pen)
        qp.draw_line(20, 200, 250, 200)

        pen.set_style(QtCore.Qt.CustomDashLine)
        pen.set_dash_pattern([1, 4, 5, 4])
        qp.set_pen(pen)
        qp.draw_line(20, 240, 250, 240)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()
