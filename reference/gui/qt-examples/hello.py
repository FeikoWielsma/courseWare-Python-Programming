# /usr/bin/env python
import sys

from PySide import QtGui

app = QtGui.QApplication(sys.argv)

hello = QtGui.QLabel("hello Qt")
hello.show()
x, y, w, h = 100, 100, 100, 100
hello.set_geometry(x, y, w, h)

sys.exit(app.exec_())
