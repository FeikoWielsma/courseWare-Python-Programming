#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.set_geometry(0, 0, 200, 25)
        self.pbar.set_maximum(100)
        self.pbar.set_minimum(0)

        self.button = QtGui.QPushButton("Start", self)
        self.button.set_focus_policy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)

        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.do_action)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

        self.set_window_title("ProgressBar")
        self.set_geometry(300, 300, 250, 150)
        self.show()

    def timer_event(self, event):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.pbar.set_value(self.step)

    def do_action(self):
        if self.timer.is_active():
            self.timer.stop()
            self.button.set_text("Start")
        else:
            self.timer.start(100, self)
            self.button.set_text("Stop")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    assert ex != None
    app.exec_()
