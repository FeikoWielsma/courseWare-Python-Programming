#!/usr/bin/python
# -*- coding: utf-8 -*-

# slider.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.set_focus_policy(QtCore.Qt.NoFocus)
        slider.set_geometry(30, 40, 100, 30)
        self.connect(slider, QtCore.SIGNAL("value_changed(int)"), self.change_value)

        self.label = QtGui.QLabel(self)
        self.label.set_pixmap(QtGui.QPixmap("mute.png"))
        self.label.set_geometry(160, 40, 80, 30)

        self.set_window_title("Slider")
        self.set_geometry(300, 300, 250, 150)

    def change_value(self, value):
        if value == 0:
            self.label.set_pixmap(QtGui.QPixmap("../icons/mute.png"))
        elif value > 0 and value <= 30:
            self.label.set_pixmap(QtGui.QPixmap("../icons/min.png"))
        elif value > 30 and value < 80:
            self.label.set_pixmap(QtGui.QPixmap("../icons/med.png"))
        else:
            self.label.set_pixmap(QtGui.QPixmap("../icons/max.png"))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
