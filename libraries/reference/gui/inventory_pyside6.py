"""The server inventory as a Qt application, for comparison with tkinter demo 05.

Not part of the course environment. Install it first :

    uv pip install PySide6
    python reference/gui/inventory_pyside6.py

INTERACTIVE : opens a window and blocks until you close it.

The point of reading this next to demos/08-gui/05_gui_treeview.py is the
difference in shape. tkinter's Treeview stores the rows itself, so you fill it
and empty it. Qt separates the data (a model) from the display (a view), so
sorting and filtering happen in the model and the table just redraws. That is
more code for a small table and much less code for a large one.
"""

import csv
import sys
from pathlib import Path

from PySide6.QtCore import QAbstractTableModel, QModelIndex, QSortFilterProxyModel, Qt
from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QTableView,
    QVBoxLayout,
    QWidget,
)

DATA = Path(__file__).resolve().parents[2] / "data"

COLUMNS: tuple[str, ...] = ("hostname", "site", "role", "os", "disk_gb", "used_gb")


def load() -> list[dict[str, str]]:
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


class ServerModel(QAbstractTableModel):
    """A model answers four questions: how many rows, how many columns, what
    is in a cell, and what is in a header. The view asks; it never stores."""

    def __init__(self, rows: list[dict[str, str]]) -> None:
        super().__init__()
        self._rows = rows

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return len(self._rows)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return len(COLUMNS)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> object:
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        return self._rows[index.row()][COLUMNS[index.column()]]

    def headerData(  # noqa: N802
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> object:
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return COLUMNS[section].replace("_", " ").title()
        return section + 1


class InventoryWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Inventory (Qt)")
        self.resize(760, 400)

        model = ServerModel(load())

        # A proxy model sits between the data and the view and filters or
        # sorts it. Nothing in ServerModel knows this is happening.
        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(model)
        self.proxy.setFilterKeyColumn(-1)  # search every column
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        search = QLineEdit()
        search.setPlaceholderText("Filter...")
        search.textChanged.connect(self.proxy.setFilterFixedString)

        table = QTableView()
        table.setModel(self.proxy)
        table.setSortingEnabled(True)  # clickable headers, no code of your own
        table.resizeColumnsToContents()

        layout = QVBoxLayout()
        layout.addWidget(search)
        layout.addWidget(table)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.statusBar().showMessage(f"{model.rowCount()} hosts")


def main() -> int:
    app = QApplication(sys.argv)
    window = InventoryWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
