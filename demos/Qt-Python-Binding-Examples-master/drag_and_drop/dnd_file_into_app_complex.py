#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
DND file into application

Tested environment:
    Mac OS X 10.6.8

This script copy from official PySide/PyQt examples.
"""

import sys

# PWD = os.path.dirname(os.path.realpath(__file__))
# parent_path = os.path.dirname(PWD)
# if parent_path not in sys.path:
#    sys.path.insert(0, parent_path)


from PySide import QtCore
from PySide import QtGui


class DropArea(QtGui.QLabel):
    def __init__(self, parent):
        super(DropArea, self).__init__(parent)

        self.set_minimum_size(200, 200)
        #        self.set_frame_style(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        #        self.set_alignment(QtCore.Qt.AlignCenter)
        self.set_accept_drops(True)
        self.set_auto_fill_background(True)
        self.clear()

    def drag_enter_event(self, evt):
        self.set_text("<drop content>")
        self.set_background_role(QtGui.QPalette.Highlight)

        evt.accept_proposed_action()
        #        self.emit changed(evt.mime_data())
        self.emit(QtCore.SIGNAL("changed( QString )"), evt.mime_data())

    def drag_move_event(self, evt):
        evt.accept_proposed_action()

    def drop_event(self, evt):
        mime_data = evt.mime_data()

        if mime_data.has_image():
            self.set_pixmap(mime_data.image_data())
        elif mime_data.has_html():
            self.set_text(mime_data.html())
            self.set_text_format(QtCore.Qt.RichText)
        elif mime_data.has_text():
            self.set_text(mime_data.text())
            self.set_text_format(QtCore.Qt.PlainText)
        elif mime_data.has_urls():
            urls = mime_data.urls()

            text = ""

            for url in urls:
                text += url + " "

            self.set_text(text)

        else:
            self.set_text("Cannot display data")

        self.set_background_role(QtGui.QPalette.Dark)
        evt.accept_proposed_action()

    def drag_leave_event(self, evt):
        self.clear()
        evt.accept()

    def clear(self):
        self.set_text("<drop content>")
        self.set_background_role(QtGui.QPalette.Dark)
        self.emit(QtCore.SIGNAL("changed()"))


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        buf = (
            "This example accepts drags from other applications "
            + "and displays the MIME types provided by the drag object."
        )
        lab = QtGui.QLabel(buf, self)
        lab.set_word_wrap(True)
        lab.adjust_size()

        drop_area = DropArea(self)
        self.connect(
            drop_area, QtCore.SIGNAL("changed(mime_data)"), self.update_formats_table
        )

        self.formats_table = QtGui.QTableWidget(self)
        self.formats_table.set_column_count(2)
        self.formats_table.set_edit_triggers(QtGui.QAbstractItemView.NoEditTriggers)
        labels = ("Format", "Content")
        self.formats_table.set_horizontal_header_labels(labels)
        self.formats_table.horizontal_header().set_stretch_last_section(True)

        clear_button = QtGui.QPushButton("Clear")
        quit_button = QtGui.QPushButton("Quit")

        button_box = QtGui.QDialogButtonBox()
        button_box.add_button(clear_button, QtGui.QDialogButtonBox.ActionRole)
        button_box.add_button(quit_button, QtGui.QDialogButtonBox.RejectRole)

        quit_button.pressed.connect(self.close)
        self.connect(
            clear_button, QtCore.SIGNAL("pressed()"), drop_area, QtCore.SLOT("clear()")
        )

        main_layout = QtGui.QVBoxLayout(self)
        main_layout.add_widget(lab)
        main_layout.add_widget(drop_area)
        main_layout.add_widget(self.formats_table)
        main_layout.add_widget(button_box)
        self.set_layout(main_layout)

        self.set_window_title("Drop Site")
        self.set_minimum_size(350, 500)

    def update_formats_table(self, mime_data):
        self.formats_table.set_row_count(0)

        if not mime_data:
            return

        for format in mime_data.formats():
            format_item = QtGui.QTableWidgetItem(format)
            format_item.set_flags(QtCore.Qt.ItemIsEnabled)
            format_item.set_text_alignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

            if format == "text/plain":
                text = mime_data.text().simplified()
            elif format == "text/html":
                text = mime_data.html().simplified()
            elif format == "text/uri-list":
                text = ""
                for i in mime_data.urls():
                    text += " " + i
            else:
                text = "binary data"

            row = self.formats_table.row_count()
            self.formats_table.insert_row(row)
            self.formats_table.set_item(row, 0, QtGui.QTableWidgetItem(format))
            self.formats_table.set_item(row, 1, QtGui.QTableWidgetItem(text))

        self.formats_table.resize_columns_to_contents(0)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
