#!/usr/bin/python
# -*- coding: utf-8 -*-

# drawtext.py

import sys
from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.set_geometry(300, 300, 250, 150)
        self.set_window_title("Draw Text")

        self.text = "中文天下"

    def paint_event(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_text(event, qp)
        qp.end()

    def draw_text(self, event, qp):
        qp.set_pen(QtGui.QColor(168, 34, 3))
        qp.set_font(QtGui.QFont("Decorative", 20))
        qp.draw_text(event.rect(), QtCore.Qt.AlignCenter, self.text)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()
