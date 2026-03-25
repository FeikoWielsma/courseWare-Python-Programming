#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Provides a dialog widget for selecting a file

Tested environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QFileDialog.html
"""
import os
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        
        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        
        self.text_edit = QtGui.QTextEdit()
        self.set_central_widget(self.text_edit)
        self.status_bar()
        self.set_focus()
        
#        open_file_action = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        open_file_action = QtGui.QAction('Open', self)
        open_file_action.set_shortcut('Ctrl+O') # `command + O` on Mac OS X 
        open_file_action.set_status_tip('Open new File')
        open_file_action.triggered.connect(self._open_file_cb)

        menubar = self.menu_bar()
        file_menu = menubar.add_menu('&File')
        file_menu.add_action(open_file_action)
        
    def _open_file_cb(self):
        filename, filter = QtGui.QFileDialog.get_open_file_name(parent=self,
                                                             caption='Open file',
                                                             dir=os.getenv("HOME"))
        print 'filename:', filename
        print 'filter:', filter
        
        if os.path.exists(filename):
            buf = open(filename).read()
            self.text_edit.set_text(buf)

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
    