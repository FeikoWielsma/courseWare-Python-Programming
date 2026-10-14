import sys
import argparse
import pandas as pd

from PySide2.QtCore import (
    QDateTime,
    QTimeZone,
    Slot,
)
from PySide2.QtWidgets import (
    QAction,
    QApplication,
    QMainWindow,
)


def transform_date(utc, timezone=None):
    utc_fmt = "yyyy-MM-dd_thh:mm:ss.zzz_z"
    new_date = QDateTime().from_string(utc, utc_fmt)
    if timezone:
        new_date.set_time_zone(timezone)
    return new_date


def read_data(fname):
    # Read the CSV content
    df = pd.read_csv(fname)

    # Remove wrong magnitudes
    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]

    # My local timezone
    timezone = QTimeZone(b"Europe/Berlin")

    # Get timestamp transformed to our timezone
    times = df["time"].apply(lambda x: transform_date(x, timezone))

    return times, magnitudes


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.set_window_title("Eartquakes information")

        # Menu
        self.menu = self.menu_bar()
        self.file_menu = self.menu.add_menu("File")

        ## Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.set_shortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.add_action(exit_action)

        # Status Bar
        self.status = self.status_bar()
        self.status.show_message("Data loaded and plotted")

        # Window dimensions
        geometry = app.desktop().available_geometry(self)
        self.set_fixed_size(geometry.width() * 0.8, geometry.height() * 0.7)

    @Slot()
    def exit_app(self, checked):
        sys.exit()


if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)

    # Qt Application
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
