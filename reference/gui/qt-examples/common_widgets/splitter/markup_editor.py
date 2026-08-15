#!/usr/bin/env python
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
    from PySide import QtWebKit
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui
    from PyQt4 import QtWebKit


class Foo(QtGui.QWidget):
    def __init__(self):
        super(Foo, self).__init__()

        x, y, w, h = 100, 100, 900, 600
        self.set_geometry(x, y, w, h)

        self.source = QtGui.QTextEdit(self)
        self.preview = QtWebKit.QWebView(self)

        self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.add_widget(self.source)
        self.splitter.add_widget(self.preview)

        self.hbox = QtGui.QHBoxLayout(self)
        self.hbox.add_widget(self.splitter)
        self.set_layout(self.hbox)

        self.font = QtGui.QFont("Monaco", 13)
        self.set_font(self.font)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    foo = Foo()
    foo.show()
    sys.exit(app.exec_())
