#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import web

try:
    from PySide import QtCore
    from PySide import QtGui
    from PySide import QtWebKit
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


buf = '<msg id="2825" type="0" show-once="0"> <validity begin="2010-12-25 16:00:00.000" end="2015-10-26 15:59:59.000"/> <content type="text/plain">尊敬的用户，您的手机已停机，这将影响您使用飞信的部分功能。为了您的正常使用，请尽快充值。</content> <url style="auto:0;">http://space.fetion.com.cn/redirection/count/203</url> </msg>'

DEFAULT_STYLE = """
* {
font-family: Monaco;
font-size: 12px;
}
"""


class Foo(QtGui.QWidget):
    def __init__(self):
        super(Foo, self).__init__()

        x, y, w, h = 100, 100, 900, 600
        self.set_geometry(x, y, w, h)

        self.source = QtGui.QTextEdit(self)
        #        self.preview = QtWebKit.QWebView(self)
        self.preview = QtGui.QTextEdit(self)
        self.preview.set_read_only(True)
        self.preview.set_frame_shape(QtGui.QFrame.NoFrame)

        qd = QtGui.QTextDocument()
        qd.set_default_style_sheet(DEFAULT_STYLE)

        self.preview.set_document(qd)

        self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.add_widget(self.source)
        self.splitter.add_widget(self.preview)

        #        widget = self.splitter.widget(0)
        #        policy = widget.size_policy()
        #        policy.set_horizontal_stretch(1)
        #        policy.set_vertical_stretch(1)
        #        widget.set_size_policy(policy)

        self.hbox = QtGui.QHBoxLayout(self)
        self.hbox.set_contents_margins(0, 0, 0, 0)
        self.hbox.set_spacing(0)
        self.hbox.add_widget(self.splitter)
        self.set_layout(self.hbox)

        self.font = QtGui.QFont("Monaco", 12)
        self.set_font(self.font)

        self.source.text_changed.connect(self.source_text_changed)

        self.source.set_text(web.safeunicode(buf))

    def source_text_changed(self):
        buf = self.source.to_plain_text()
        #        import markdown
        #        buf = markdown.markdown(buf)
        self.preview.set_html(buf)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    foo = Foo()
    foo.show()
    sys.exit(app.exec_())
