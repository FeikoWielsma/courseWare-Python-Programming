"""The smallest possible PySide6 window, for comparison with tkinter demo 01.

Not part of the course environment. Install it first :

    uv pip install PySide6
    python reference/gui/hello_pyside6.py

INTERACTIVE : opens a window and blocks until you close it.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class HelloWindow(QMainWindow):
    """Qt is class-based all the way down; you subclass rather than configure."""

    def __init__(self) -> None:
        super().__init__()
        # Qt methods are camelCase, because the API is a binding onto C++.
        self.setWindowTitle("Hello PySide6")
        self.resize(420, 220)

        label = QLabel("This is Qt.\nSame idea as tkinter, a much bigger toolkit.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # A QMainWindow has one central widget, plus optional menus, toolbars,
        # docks and a status bar. tkinter has none of that built in.
        self.setCentralWidget(label)
        self.statusBar().showMessage("Ready")


def main() -> int:
    # QApplication is Qt's equivalent of the Tk root object: exactly one per
    # process, and it owns the event loop.
    app = QApplication(sys.argv)
    window = HelloWindow()
    window.show()
    # app.exec() is Qt's mainloop(). It returns the process exit code.
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
