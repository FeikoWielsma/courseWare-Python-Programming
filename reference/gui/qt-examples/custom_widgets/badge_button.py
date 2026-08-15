#!/usr/bin/env python
"""
Qt Notification Badge

References

 - http://th30z.blogspot.com/2008/10/cocoa-notification-badge_127.html
 - http://khertan.net/blog/qbadgebutton_a_qpushbutton_with_a_badge_counter

origin version it here
http://khertan.net/blog/qbadgebutton_a_qpushbutton_with_a_badge_counter
"""

import sys

try:
    from PySide import QtGui, QtCore
except ImportError:
    from PyQt4 import QtGui, QtCore


class QBadgeButton(QtGui.QPushButton):
    def __init__(self, icon=None, text=None, parent=None):
        if icon:
            QtGui.QPushButton.__init__(self, icon, text, parent)
        elif text:
            QtGui.QPushButton.__init__(self, text, parent)
        else:
            QtGui.QPushButton.__init__(self, parent)

        self.badge_counter = 0
        self.badge_size = 50

        self.red_gradient = QtGui.QRadialGradient(
            0.0, 0.0, 17.0, self.badge_size - 3, self.badge_size - 3
        )
        self.red_gradient.set_color_at(0.0, QtGui.QColor(0xE0, 0x84, 0x9B))
        self.red_gradient.set_color_at(0.5, QtGui.QColor(0xE9, 0x34, 0x43))
        self.red_gradient.set_color_at(1.0, QtGui.QColor(0xDC, 0x0C, 0x00))

    def set_size(self, size):
        self.badge_size = size

    def set_counter(self, counter):
        self.badge_counter = counter
        self.update()

    def paint_event(self, event):
        QtGui.QPushButton.paint_event(self, event)
        p = QtGui.QPainter(self)
        p.set_render_hint(QtGui.QPainter.TextAntialiasing)
        p.set_render_hint(QtGui.QPainter.Antialiasing)

        if self.badge_counter > 0:
            point = self.rect().top_right()
            self.draw_badge(
                p,
                point.x() - self.badge_size - 1,
                point.y() + 1,
                self.badge_size,
                str(self.badge_counter),
                QtGui.QBrush(self.red_gradient),
            )

    def fill_ellipse(self, painter, x, y, size, brush):
        path = QtGui.QPainterPath()
        path.add_ellipse(x, y, size, size)
        painter.fill_path(path, brush)

    def draw_badge(self, painter, x, y, size, text, brush):
        painter.set_font(QtGui.QFont(painter.font().family(), 11, QtGui.QFont.Bold))

        while (size - painter.font_metrics().width(text)) < 10:
            point_size = painter.font().point_size() - 1
            weight = QtGui.QFont.Normal if (point_size < 8) else QtGui.QFont.Bold
            painter.set_font(
                QtGui.QFont(
                    painter.font().family(), painter.font().point_size() - 1, weight
                )
            )

        shadow_color = QtGui.QColor(0, 0, 0, size)
        self.fill_ellipse(painter, x + 1, y, size, shadow_color)
        self.fill_ellipse(painter, x - 1, y, size, shadow_color)
        self.fill_ellipse(painter, x, y + 1, size, shadow_color)
        self.fill_ellipse(painter, x, y - 1, size, shadow_color)

        painter.set_pen(QtGui.QPen(QtCore.Qt.white, 2))
        self.fill_ellipse(painter, x, y, size - 3, brush)
        painter.draw_ellipse(x, y, size - 3, size - 3)

        painter.set_pen(QtGui.QPen(QtCore.Qt.white, 1))
        painter.draw_text(x, y, size - 2, size - 2, QtCore.Qt.AlignCenter, text)


class QToolBadgeButton(QtGui.QToolButton):
    def __init__(self, parent=None):
        QtGui.QToolButton.__init__(self, parent)

        self.badge_counter = 0
        self.badge_size = 25

        self.red_gradient = QtGui.QRadialGradient(
            0.0, 0.0, 17.0, self.badge_size - 3, self.badge_size - 3
        )
        self.red_gradient.set_color_at(0.0, QtGui.QColor(0xE0, 0x84, 0x9B))
        self.red_gradient.set_color_at(0.5, QtGui.QColor(0xE9, 0x34, 0x43))
        self.red_gradient.set_color_at(1.0, QtGui.QColor(0xDC, 0x0C, 0x00))

    def set_size(self, size):
        self.badge_size = size

    def set_counter(self, counter):
        self.badge_counter = counter

    def paint_event(self, event):
        QtGui.QToolButton.paint_event(self, event)
        p = QtGui.QPainter(self)
        p.set_render_hint(QtGui.QPainter.TextAntialiasing)
        p.set_render_hint(QtGui.QPainter.Antialiasing)
        if self.badge_counter > 0:
            point = self.rect().top_right()
            self.draw_badge(
                p,
                point.x() - self.badge_size,
                point.y(),
                self.badge_size,
                str(self.badge_counter),
                QtGui.QBrush(self.red_gradient),
            )

    def fill_ellipse(self, painter, x, y, size, brush):
        path = QtGui.QPainterPath()
        path.add_ellipse(x, y, size, size)
        painter.fill_path(path, brush)

    def draw_badge(self, painter, x, y, size, text, brush):
        painter.set_font(QtGui.QFont(painter.font().family(), 11, QtGui.QFont.Bold))

        while (size - painter.font_metrics().width(text)) < 10:
            point_size = painter.font().point_size() - 1
            weight = QtGui.QFont.Normal if (point_size < 8) else QtGui.QFont.Bold
            painter.set_font(
                QtGui.QFont(
                    painter.font().family(), painter.font().point_size() - 1, weight
                )
            )

        shadow_color = QtGui.QColor(0, 0, 0, size)
        self.fill_ellipse(painter, x + 1, y, size, shadow_color)
        self.fill_ellipse(painter, x - 1, y, size, shadow_color)
        self.fill_ellipse(painter, x, y + 1, size, shadow_color)
        self.fill_ellipse(painter, x, y - 1, size, shadow_color)

        painter.set_pen(QtGui.QPen(QtCore.Qt.white, 2))
        self.fill_ellipse(painter, x, y, size - 3, brush)
        painter.draw_ellipse(x, y, size - 2, size - 2)

        painter.set_pen(QtGui.QPen(QtCore.Qt.white, 1))
        painter.draw_text(x, y, size - 2, size - 2, QtCore.Qt.AlignCenter, text)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = QtGui.QMainWindow()

    toolbar = QtGui.QToolBar("Toolbar")
    win.add_tool_bar(QtCore.Qt.BottomToolBarArea, toolbar)
    b = QToolBadgeButton(win)
    b.set_text("test")
    b.set_counter(22)
    toolbar.add_widget(b)

    w = QBadgeButton(parent=win)
    w.set_text("test")
    w.set_counter(22)
    win.set_central_widget(w)
    win.show()

    sys.exit(app.exec_())
