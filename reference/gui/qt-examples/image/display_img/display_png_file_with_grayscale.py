#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
display png file with GrayScaled feature

Tested environment:
    Mac OS X 10.6.8
"""

import os
import sys
from PySide import QtGui

PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)
IM_RES_PATH = os.path.join(os.path.dirname(parent_path), "image_resources")


def to_grayscaled(path):
    origin = QtGui.QPixmap(path)

    img = origin.to_image()
    for i in xrange(origin.width()):
        for j in xrange(origin.height()):
            col = img.pixel(i, j)
            gray = QtGui.q_gray(col)
            img.set_pixel(i, j, QtGui.q_rgb(gray, gray, gray))

    dst = origin.from_image(img)
    return dst


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        online_path = os.path.join(IM_RES_PATH, "online-50x50.png")
        self.label = QtGui.QLabel("online", self)
        pix = QtGui.QPixmap(online_path)
        self.label.set_pixmap(pix)
        self.label.move(10, 10)

        offline_path = os.path.join(IM_RES_PATH, "offline-50x50.png")
        self.label = QtGui.QLabel("offline", self)
        pix = QtGui.QPixmap(offline_path)
        self.label.set_pixmap(pix)
        self.label.move(10, 70)

        online_grayscale_path = os.path.join(IM_RES_PATH, "online-50x50.png")
        self.label = QtGui.QLabel("offline", self)
        pix = to_grayscaled(online_grayscale_path)
        self.label.set_pixmap(pix)
        self.label.move(10, 130)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
