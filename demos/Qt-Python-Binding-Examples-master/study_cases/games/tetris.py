#!/usr/bin/python

# tetris.py

import sys
import random
from PyQt4 import QtCore, QtGui


class Tetris(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.set_geometry(300, 300, 180, 380)
        self.set_window_title("Tetris")
        self.tetrisboard = Board(self)

        self.set_central_widget(self.tetrisboard)

        self.statusbar = self.status_bar()
        self.connect(
            self.tetrisboard,
            QtCore.SIGNAL("message_to_statusbar(QString)"),
            self.statusbar,
            QtCore.SLOT("show_message(QString)"),
        )

        self.tetrisboard.start()
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screen_geometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2
        )


class Board(QtGui.QFrame):
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)

        self.timer = QtCore.QBasicTimer()
        self.is_waiting_after_line = False
        self.cur_piece = Shape()
        self.next_piece = Shape()
        self.cur_x = 0
        self.cur_y = 0
        self.num_lines_removed = 0
        self.board = []

        self.set_focus_policy(QtCore.Qt.StrongFocus)
        self.is_started = False
        self.is_paused = False
        self.clear_board()

        self.next_piece.set_random_shape()

    def shape_at(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]

    def set_shape_at(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape

    def square_width(self):
        return self.contents_rect().width() / Board.BoardWidth

    def square_height(self):
        return self.contents_rect().height() / Board.BoardHeight

    def start(self):
        if self.is_paused:
            return

        self.is_started = True
        self.is_waiting_after_line = False
        self.num_lines_removed = 0
        self.clear_board()

        self.emit(
            QtCore.SIGNAL("message_to_statusbar(QString)"), str(self.num_lines_removed)
        )

        self.new_piece()
        self.timer.start(Board.Speed, self)

    def pause(self):
        if not self.is_started:
            return

        self.is_paused = not self.is_paused
        if self.is_paused:
            self.timer.stop()
            self.emit(QtCore.SIGNAL("message_to_statusbar(QString)"), "paused")
        else:
            self.timer.start(Board.Speed, self)
            self.emit(
                QtCore.SIGNAL("message_to_statusbar(QString)"),
                str(self.num_lines_removed),
            )

        self.update()

    def paint_event(self, event):
        painter = QtGui.QPainter(self)
        rect = self.contents_rect()

        board_top = rect.bottom() - Board.BoardHeight * self.square_height()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shape_at(j, Board.BoardHeight - i - 1)
                if shape != Tetrominoes.NoShape:
                    self.draw_square(
                        painter,
                        rect.left() + j * self.square_width(),
                        board_top + i * self.square_height(),
                        shape,
                    )

        if self.cur_piece.shape() != Tetrominoes.NoShape:
            for i in range(4):
                x = self.cur_x + self.cur_piece.x(i)
                y = self.cur_y - self.cur_piece.y(i)
                self.draw_square(
                    painter,
                    rect.left() + x * self.square_width(),
                    board_top + (Board.BoardHeight - y - 1) * self.square_height(),
                    self.cur_piece.shape(),
                )

    def key_press_event(self, event):
        if not self.is_started or self.cur_piece.shape() == Tetrominoes.NoShape:
            QtGui.QWidget.key_press_event(self, event)
            return

        key = event.key()
        if key == QtCore.Qt.Key_P:
            self.pause()
            return

        if self.is_paused:
            return
        elif key == QtCore.Qt.Key_Left:
            self.try_move(self.cur_piece, self.cur_x - 1, self.cur_y)
        elif key == QtCore.Qt.Key_Right:
            self.try_move(self.cur_piece, self.cur_x + 1, self.cur_y)
        elif key == QtCore.Qt.Key_Down:
            self.try_move(self.cur_piece.rotated_right(), self.cur_x, self.cur_y)
        elif key == QtCore.Qt.Key_Up:
            self.try_move(self.cur_piece.rotated_left(), self.cur_x, self.cur_y)
        elif key == QtCore.Qt.Key_Space:
            self.drop_down()
        elif key == QtCore.Qt.Key_D:
            self.one_line_down()
        else:
            QtGui.QWidget.key_press_event(self, event)

    def timer_event(self, event):
        if event.timer_id() == self.timer.timer_id():
            if self.is_waiting_after_line:
                self.is_waiting_after_line = False
                self.new_piece()
            else:
                self.one_line_down()
        else:
            QtGui.QFrame.timer_event(self, event)

    def clear_board(self):
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoes.NoShape)

    def drop_down(self):
        new_y = self.cur_y
        while new_y > 0:
            if not self.try_move(self.cur_piece, self.cur_x, new_y - 1):
                break
            new_y -= 1

        self.piece_dropped()

    def one_line_down(self):
        if not self.try_move(self.cur_piece, self.cur_x, self.cur_y - 1):
            self.piece_dropped()

    def piece_dropped(self):
        for i in range(4):
            x = self.cur_x + self.cur_piece.x(i)
            y = self.cur_y - self.cur_piece.y(i)
            self.set_shape_at(x, y, self.cur_piece.shape())

        self.remove_full_lines()

        if not self.is_waiting_after_line:
            self.new_piece()

    def remove_full_lines(self):
        num_full_lines = 0

        rows_to_remove = []

        for i in range(Board.BoardHeight):
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shape_at(j, i) == Tetrominoes.NoShape:
                    n = n + 1

            if n == 10:
                rows_to_remove.append(i)

        rows_to_remove.reverse()

        for m in rows_to_remove:
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.set_shape_at(l, k, self.shape_at(l, k + 1))

            num_full_lines = num_full_lines + len(rows_to_remove)

            if num_full_lines > 0:
                self.num_lines_removed = self.num_lines_removed + num_full_lines
                self.emit(
                    QtCore.SIGNAL("message_to_statusbar(QString)"),
                    str(self.num_lines_removed),
                )
                self.is_waiting_after_line = True
                self.cur_piece.set_shape(Tetrominoes.NoShape)
                self.update()

    def new_piece(self):
        self.cur_piece = self.next_piece
        self.next_piece.set_random_shape()
        self.cur_x = Board.BoardWidth / 2 + 1
        self.cur_y = Board.BoardHeight - 1 + self.cur_piece.min_y()

        if not self.try_move(self.cur_piece, self.cur_x, self.cur_y):
            self.cur_piece.set_shape(Tetrominoes.NoShape)
            self.timer.stop()
            self.is_started = False
            self.emit(QtCore.SIGNAL("message_to_statusbar(QString)"), "Game over")

    def try_move(self, new_piece, new_x, new_y):
        for i in range(4):
            x = new_x + new_piece.x(i)
            y = new_y - new_piece.y(i)
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False
            if self.shape_at(x, y) != Tetrominoes.NoShape:
                return False

        self.cur_piece = new_piece
        self.cur_x = new_x
        self.cur_y = new_y
        self.update()
        return True

    def draw_square(self, painter, x, y, shape):
        color_table = [
            0x000000,
            0xCC6666,
            0x66CC66,
            0x6666CC,
            0xCCCC66,
            0xCC66CC,
            0x66CCCC,
            0xDAAA00,
        ]

        color = QtGui.QColor(color_table[shape])
        painter.fill_rect(
            x + 1, y + 1, self.square_width() - 2, self.square_height() - 2, color
        )

        painter.set_pen(color.light())
        painter.draw_line(x, y + self.square_height() - 1, x, y)
        painter.draw_line(x, y, x + self.square_width() - 1, y)

        painter.set_pen(color.dark())
        painter.draw_line(
            x + 1,
            y + self.square_height() - 1,
            x + self.square_width() - 1,
            y + self.square_height() - 1,
        )
        painter.draw_line(
            x + self.square_width() - 1,
            y + self.square_height() - 1,
            x + self.square_width() - 1,
            y + 1,
        )


class Tetrominoes(object):
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):
    coords_table = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1)),
    )

    def __init__(self):
        self.coords = [[0, 0] for i in range(4)]
        self.piece_shape = Tetrominoes.NoShape

        self.set_shape(Tetrominoes.NoShape)

    def shape(self):
        return self.piece_shape

    def set_shape(self, shape):
        table = Shape.coords_table[shape]
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.piece_shape = shape

    def set_random_shape(self):
        self.set_shape(random.randint(1, 7))

    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def set_x(self, index, x):
        self.coords[index][0] = x

    def set_y(self, index, y):
        self.coords[index][1] = y

    def min_x(self):
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

    def max_x(self):
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def min_y(self):
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def max_y(self):
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    def rotated_left(self):
        if self.piece_shape == Tetrominoes.SquareShape:
            return self

        result = Shape()
        result.piece_shape = self.piece_shape
        for i in range(4):
            result.set_x(i, self.y(i))
            result.set_y(i, -self.x(i))

        return result

    def rotated_right(self):
        if self.piece_shape == Tetrominoes.SquareShape:
            return self

        result = Shape()
        result.piece_shape = self.piece_shape
        for i in range(4):
            result.set_x(i, -self.y(i))
            result.set_y(i, self.x(i))

        return result


app = QtGui.QApplication(sys.argv)
tetris = Tetris()
tetris.show()
sys.exit(app.exec_())
