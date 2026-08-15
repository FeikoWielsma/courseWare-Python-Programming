#!/usr/bin/env python
"""
DND file into window

Tested environment:
    Mac OS X 10.6.8
"""

import sys
import logging
from PySide import QtGui

logging.get_logger().set_level(logging.DEBUG)


def print_data(mime_data, msg_prefix=""):
    if mime_data.has_image():
        msg = repr(mime_data.image_data())
    elif mime_data.has_html():
        msg = repr(mime_data.html())
    elif mime_data.has_text():
        msg = repr(mime_data.text())
    elif mime_data.has_urls():
        msg = repr(mime_data.urls())
    else:
        raise Exception("unexpected mime data")

    logging.info(msg_prefix + msg)


class DropArea(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(DropArea, self).__init__(*args, **kwargs)
        self.set_accept_drops(True)

    def drag_enter_event(self, evt):
        #        mime_data = evt.mime_data()
        #        print_data(mime_data)

        evt.accept_proposed_action()

    def drag_move_event(self, evt):
        #        mime_data = evt.mime_data()
        #        print_data(mime_data)

        evt.accept_proposed_action()

    def drop_event(self, evt):
        mime_data = evt.mime_data()
        print_data(mime_data, msg_prefix="drop ")

        evt.accept_proposed_action()

    def drag_leave_event(self, evt):
        #        mime_data = evt.mime_data()
        #        print_data(mime_data)

        evt.accept()

    def main(self):
        self.show()
        self.raise_()


app = QtGui.QApplication(sys.argv)

win = DropArea()
win.main()

sys.exit(app.exec_())
