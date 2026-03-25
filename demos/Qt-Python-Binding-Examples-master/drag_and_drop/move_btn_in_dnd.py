#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
move a button in DND I

Tested environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/dnd.html
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class DragWidget(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(DragWidget, self).__init__('DND me', parent)

    def mouse_press_event(self, evt):
        if evt.button() == QtCore.Qt.MouseButton.LeftButton:
            mime_data = QtCore.QMimeData()
            mime_data.set_text(self.text())

            drag = QtGui.QDrag(self)
            drag.set_mime_data(mime_data)
            drag.exec_(QtCore.Qt.MoveAction)


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        self.btn = DragWidget(self)
        self.btn.move(10, 10)

        self.set_accept_drops(True)

    def show_and_raise(self):
        self.show()
        self.raise_()

    def drag_enter_event(self, drag_enter_evt):
        mime_data = drag_enter_evt.mime_data()
        if mime_data.has_format('text/plain'):
            drag_enter_evt.accept_proposed_action()

    def drag_move_event(self, evt):
        print 'drag_move_event', evt.pos()

        self.btn.move(evt.pos())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())