# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_group.ui'
#
# Created: Thu Jan 26 22:22:29 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.from_utf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Form(object):
    def setup_ui(self, Form):
        Form.set_object_name(_fromUtf8("Form"))
        Form.resize(400, 110)
        Form.set_window_title(
            QtGui.QApplication.translate(
                "Form", "Add Group", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label = QtGui.QLabel(Form)
        self.label.set_geometry(QtCore.QRect(0, 20, 200, 20))
        self.label.set_text(
            QtGui.QApplication.translate(
                "Form", "Enter group name:", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label.set_alignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label.set_object_name(_fromUtf8("label"))
        self.push_button = QtGui.QPushButton(Form)
        self.push_button.set_geometry(QtCore.QRect(290, 60, 90, 32))
        self.push_button.set_text(
            QtGui.QApplication.translate(
                "Form", "Add", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.push_button.set_object_name(_fromUtf8("push_button"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.set_geometry(QtCore.QRect(200, 60, 90, 32))
        self.pushButton_2.set_text(
            QtGui.QApplication.translate(
                "Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.pushButton_2.set_object_name(_fromUtf8("pushButton_2"))
        self.line_edit = QtGui.QLineEdit(Form)
        self.line_edit.set_geometry(QtCore.QRect(210, 20, 144, 22))
        self.line_edit.set_object_name(_fromUtf8("line_edit"))

        self.retranslate_ui(Form)
        QtCore.QMetaObject.connect_slots_by_name(Form)

    def retranslate_ui(self, Form):
        pass
