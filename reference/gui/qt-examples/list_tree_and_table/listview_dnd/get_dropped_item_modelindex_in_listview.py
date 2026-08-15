#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Get dropped item's ModelIndex in QListView

Tested environment:
    Mac OS X 10.6.8

Docs

 - http://doc.qt.nokia.com/latest/model-view-programming.html#using-drag-and-drop-with-item-views
 - file:///opt/local/share/doc/qt4/html/qabstractitemmodel.html#drop_mime_data
"""
import glob
import os
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, os_list):
        super(ListModel, self).__init__()
        self.os_list = os_list

    def row_count(self, parent):
        return len(self.os_list)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.is_valid():
            return None

        os_name, os_logo_path = self.os_list[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return os_name
        elif role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(os_logo_path)

        return None

    def flags(self, idx):
        if idx.is_valid():
            return QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled |\
                   QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsDropEnabled |\
                   QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    def supported_drop_actions(self):
        return QtCore.Qt.MoveAction

    def drop_mime_data(self, data, action, row, column, parent_idx):
        """
        NOTICE: Although the specified row, column
        and parent indicate the location of an item in the model where the operation ended,
        it is the responsibility of the view to
        provide a suitable location for where the data should be inserted.
        """
#        print data, action, row, column, parent_idx
        return super(ListModel, self).drop_mime_data(data, action, row, column, parent_idx)

    def mime_data(self, idxes):
        # NOTE: create mime data from ancestor method for fixed crash bug on PySide
        mime_data = super(ListModel, self).mime_data(idxes)

        encoded_data = ""

        for idx in idxes:
            if idx.is_valid():
                encoded_data += '\r\n' + self.data(idx, role = QtCore.Qt.DisplayRole)

        mime_data.set_data('text/plain', encoded_data)

        return mime_data



class ListView(QtGui.QListView):
    def __init__(self, parent=None):
        super(ListView, self).__init__(parent)

        self.data_sources = create_data_source()
        list_model = ListModel(self.data_sources)
        self.set_model(list_model)

        # size
        self.set_icon_size(QtCore.QSize(50, 50))
        self.set_spacing(5)
        self.set_uniform_item_sizes(True)

        # view
        self.set_drop_indicator_shown(True)

        # interactive in DND mode
        self.set_selection_mode(QtGui.QAbstractItemView.ExtendedSelection)
        self.set_drag_drop_mode(QtGui.QAbstractItemView.DragDrop)
        self.set_drag_enabled(True)
        self.set_accept_drops(True)

    def drop_event(self, evt):
        mime_data = evt.mime_data()

        if mime_data.has_format('text/plain'):
            buf = mime_data.data('text/plain')
            print "source == self:", evt.source() == self
            print 'mime data:', repr(buf)

            target_idx = self.index_at(evt.pos())
            print "dropped at row:%d, col:%d:" % (target_idx.row(), target_idx.column())

        return super(ListView, self).drop_event(evt)


def create_data_source():
    logos = glob.glob('*.png')
    return [(os.path.splitext(i)[0], i) for i in logos]


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)


        self.list_view = ListView(self)
        x, y, w, h = 5, 5, 290, 250
        self.list_view.set_geometry(x, y, w, h)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())