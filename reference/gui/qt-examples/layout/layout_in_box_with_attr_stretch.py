#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
layout in box with attribute stretch demo

Tested environment:
    Mac OS X 10.6.8
"""

import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui


class Demo(QtGui.QDialog):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        vbox = QtGui.QVBoxLayout()

        hbox1 = QtGui.QHBoxLayout()
        vbox.add_layout(hbox1)

        a_btn = QtGui.QPushButton("A")
        hbox1.add_widget(a_btn)

        b_btn = QtGui.QPushButton("B")
        hbox1.add_widget(b_btn)

        hbox2 = QtGui.QHBoxLayout()
        vbox.add_layout(hbox2)

        #        使用 QHBoxLayout 布局，默认是左右平均分布放置
        #        设置 Stretch 属性后，两个按钮会靠右放置，而且随着窗口大小的改变，也是靠右
        hbox2.add_stretch()

        c_btn = QtGui.QPushButton("C")
        hbox2.add_widget(c_btn)

        d_btn = QtGui.QPushButton("D")
        hbox2.add_widget(d_btn)

        self.set_layout(vbox)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show()

    app.exec_()
