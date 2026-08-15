#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Custom QListView


This script demonstrates

 - DND item
 - sort item

Tested environment:
    Mac OS X 10.6.8

Docs

 - http://doc.qt.nokia.com/latest/model-view-programming.html#using-drag-and-drop-with-item-views

 - Qt - QAbstractItemView, PySide - QListView
 - Qt - QAbstractItemModel, PySide - QAbstractItemModel


"""
import glob
import os
import sys

#try:
#    from PySide import QtCore
#    from PySide import QtGui
#except ImportError:
#    from PyQt4 import QtCore
#    from PyQt4 import QtGui

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

    # DND
    def supported_drop_actions(self):
        return QtCore.Qt.MoveAction

    def mime_data(self, idxes):
        super(ListModel, self).mime_data(idxes)

        mime_data = QtCore.QMimeData()

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
        self.set_movement(QtGui.QListView.Free)
        self.set_selection_mode(QtGui.QAbstractItemView.ExtendedSelection)
        self.set_drag_enabled(True)
        self.set_accept_drops(True)

    def drag_enter_event(self, evt):
        if evt.mime_data().has_format('text/plain'):
            print self.child_at(evt.pos())
            
            if evt.source() == self:
                evt.set_drop_action(QtCore.Qt.MoveAction)
                evt.accept()
            else:
                evt.accept_proposed_action()
        else:
            evt.ignore()

    drag_move_event = drag_enter_event

    def drop_event(self, evt):
        evt.accept()
        mime_data = evt.mime_data()

        print mime_data.data('text/plain')


def create_data_source():
    logos = glob.glob('*.png')
    return [(os.path.splitext(i)[0], i) for i in logos]


class ChatWin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ChatWin, self).__init__()
        self.demo = parent

        x, y, w, h = 200, 200, 300, 400
        self.set_geometry(x, y, w, h)

        self.set_accept_drops(True)

    def show_and_raise(self):
        self.show()
        self.raise_()

    def drag_enter_event(self, evt):
        evt.accept()
        if evt.mime_data().has_format('text/plain'):
            evt.accept()
        else:
            evt.ignore()

    def drop_event(self, evt):
        evt.accept()
        mime_data = evt.mime_data()
        
        print mime_data.data('text/plain')

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)


        self.list_view = ListView(self)
        x, y, w, h = 5, 5, 290, 250
        self.list_view.set_geometry(x, y, w, h)

        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.move(5, 260)
        self.lineedit.text_edited.connect(self._lineedit_textEdited)


        self.chat_win = ChatWin(self)
        self.chat_win.show_and_raise()


    def _lineedit_textEdited(self, text):
        if not text:
            self.list_view.clear_selection()
        else:
            self.list_view.keyboard_search(text)
            idx = self.list_view.current_index()

            if idx.is_valid():
                if len(self.list_view.data_sources) - 1 >= idx.row():
                    self.list_view.data_sources.pop(idx.row())
                    self.list_view.update()

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())