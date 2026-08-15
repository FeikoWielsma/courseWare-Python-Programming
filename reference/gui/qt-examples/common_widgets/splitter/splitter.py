#!/usr/bin/python
# -*- coding: utf-8 -*-

# ZetCode PyQt4 tutorial
#
# This example shows
# how to use QSplitter widget.
#
# author: Jan Bodnar
# website: zetcode.com
# last edited: December 2010


from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        hbox = QtGui.QHBoxLayout(self)

        topleft = QtGui.QFrame(self)
        topleft.set_frame_shape(QtGui.QFrame.StyledPanel)

        topright = QtGui.QFrame(self)
        topright.set_frame_shape(QtGui.QFrame.StyledPanel)

        bottom = QtGui.QFrame(self)
        bottom.set_frame_shape(QtGui.QFrame.StyledPanel)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.add_widget(topleft)
        splitter1.add_widget(topright)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.add_widget(splitter1)
        splitter2.add_widget(bottom)

        hbox.add_widget(splitter2)
        self.set_layout(hbox)

        self.set_window_title("QSplitter")
        QtGui.QApplication.set_style(QtGui.QStyleFactory.create("Cleanlooks"))
        self.set_geometry(250, 200, 350, 250)


def main():
    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == "__main__":
    main()
