#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
popup menu in QTreeView

Tested environment:
    Mac OS X 10.6.8

http://developer.qt.nokia.com/doc/qt-4.8/qmenu.html#details
http://diotavelli.net/PyQtWiki/Handling%20context%20menus
"""
import sys

try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui


datas = [
    "a",
    "b",
    "c",
]

class Demo(QtGui.QWidget):
    def __init__(self):

        QtGui.QWidget.__init__(self)

        self.tree_view = QtGui.QTreeView()
        self.model = QtGui.QStandardItemModel()
        for name in datas:
            item = QtGui.QStandardItem(name)
            self.model.append_row(item)
        self.tree_view.set_model(self.model)

        self.model.set_horizontal_header_labels([self.tr("Object")])

        layout = QtGui.QVBoxLayout()
        layout.add_widget(self.tree_view)
        self.set_layout(layout)


        self.popup_menu = QtGui.QMenu(self)

        # menu item
        self.item_add_act = QtGui.QAction("Add", self)
        self.item_add_act.triggered.connect(self.add_cb)
        self.popup_menu.add_action(self.item_add_act)

    def add_cb(self):
        print "add callback"

    def context_menu_event(self, event):
        point = self.map_to_global(event.pos())
        widget = QtGui.QApplication.widget_at(point)
        print "widget:", widget

        act = self.popup_menu.exec_(point)

        if act == self.item_add_act:
            print "item add clicked"

        return super(Demo, self).context_menu_event(event)

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())