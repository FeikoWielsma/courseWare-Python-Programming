#!/usr/bin/python
# -*- coding: utf-8 -*-

# calendar.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.set_grid_visible(True)
        self.cal.move(20, 20)
        self.connect(self.cal, QtCore.SIGNAL("selection_changed()"), self.show_date)

        self.label = QtGui.QLabel(self)
        date = self.cal.selected_date()
        self.label.set_text(str(date.to_py_date()))
        self.label.move(130, 260)

        self.set_window_title("Calendar")
        self.set_geometry(300, 300, 350, 300)

    def show_date(self):
        date = self.cal.selected_date()
        self.label.set_text(str(date.to_py_date()))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
