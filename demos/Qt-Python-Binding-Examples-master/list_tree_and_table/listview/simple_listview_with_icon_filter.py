#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Custom QListView


This script demonstrates

 - custom icon for item
 - change item data at runtime

Tested environment:
    Mac OS X 10.6.8

Docs
 - http://www.pyside.org/docs/pyside/PySide/QtGui/QAbstractItemView.html
 - http://www.pyside.org/docs/pyside/PySide/QtGui/QListView.html
 - http://doc.qt.nokia.com/latest/model-view-programming.html
"""

import glob
import os
import sys

# try:
#    from PySide import QtCore
#    from PySide import QtGui
# except ImportError:
#    from PyQt4 import QtCore
#    from PyQt4 import QtGui

from PyQt4 import QtCore
from PyQt4 import QtGui


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, os_list):
        super(ListModel, self).__init__()
        self.os_list = os_list

    def row_count(self, parent):
        #        print ">>> row_count"
        #        print 'parent:', parent,
        #        print ', row:', parent.row(),
        #        print ', column:', parent.column(),
        #        print ', internal_pointer:', parent.internal_pointer()

        return len(self.os_list)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        #        print ">>> data"
        #        print 'is_valid:', index.is_valid(),
        #        print ', row:', index.row(),
        #        print ', column:', index.column(),
        #        print ', is Qt.DisplayRole:', role == QtCore.Qt.DisplayRole

        if not index.is_valid():
            return None

        os_name, os_logo_path = self.os_list[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return os_name
        elif role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(os_logo_path)

        return None


def create_data_source():
    logos = glob.glob("*.png")
    return [(os.path.splitext(i)[0], i) for i in logos]


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        self.list_view = QtGui.QListView(self)
        x, y, w, h = 5, 5, 290, 250
        self.list_view.set_geometry(x, y, w, h)

        self.data_sources = create_data_source()
        list_model = ListModel(self.data_sources)
        self.list_view.set_model(list_model)

        # size
        self.list_view.set_icon_size(QtCore.QSize(50, 50))
        self.list_view.set_spacing(5)
        self.list_view.set_uniform_item_sizes(True)

        # view
        #        self.list_view.set_view_mode(QtGui.QListView.IconMode)

        # interactive
        self.list_view.set_selection_mode(QtGui.QAbstractItemView.ExtendedSelection)

        # more advanced controlling on selection
        #        self.selection_model = self.list_view.selection_model()
        #        self.selection_model.current_changed.connect(self._selection_model_currentChanged)

        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.move(5, 260)
        self.lineedit.text_edited.connect(self._lineedit_textEdited)

    def _lineedit_textEdited(self, text):
        if not text:
            self.list_view.clear_selection()
        else:
            self.list_view.keyboard_search(text)
            idx = self.list_view.current_index()
            if idx.is_valid():
                if len(self.data_sources) - 1 >= idx.row():
                    self.data_sources.pop(idx.row())
                    self.list_view.update()

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
