#!/usr/bin/python
# -*- coding: utf-8 -*-

# brushes.py

import sys
from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.set_geometry(300, 300, 355, 280)
        self.set_window_title("Brushes")

    def paint_event(self, e):
        qp = QtGui.QPainter()

        qp.begin(self)
        self.draw_brushes(qp)
        qp.end()

    def draw_brushes(self, qp):
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        qp.set_brush(brush)
        qp.draw_rect(10, 15, 90, 60)

        brush.set_style(QtCore.Qt.Dense1Pattern)
        qp.set_brush(brush)
        qp.draw_rect(130, 15, 90, 60)

        brush.set_style(QtCore.Qt.Dense2Pattern)
        qp.set_brush(brush)
        qp.draw_rect(250, 15, 90, 60)

        brush.set_style(QtCore.Qt.Dense3Pattern)
        qp.set_brush(brush)
        qp.draw_rect(10, 105, 90, 60)

        brush.set_style(QtCore.Qt.DiagCrossPattern)
        qp.set_brush(brush)
        qp.draw_rect(10, 105, 90, 60)

        brush.set_style(QtCore.Qt.Dense5Pattern)
        qp.set_brush(brush)
        qp.draw_rect(130, 105, 90, 60)

        brush.set_style(QtCore.Qt.Dense6Pattern)
        qp.set_brush(brush)
        qp.draw_rect(250, 105, 90, 60)

        brush.set_style(QtCore.Qt.HorPattern)
        qp.set_brush(brush)
        qp.draw_rect(10, 195, 90, 60)

        brush.set_style(QtCore.Qt.VerPattern)
        qp.set_brush(brush)
        qp.draw_rect(130, 195, 90, 60)

        brush.set_style(QtCore.Qt.BDiagPattern)
        qp.set_brush(brush)
        qp.draw_rect(250, 195, 90, 60)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()
