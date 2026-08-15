"""
add custom theme name and search path for fix icon file not found on Mac OS X

Install Oxygen icon on Mac OS X via MacPorts:

    sudo port install oxygen-icons

"""

import sys

try:
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui


__all__ = [
    "config_theme_path",
]


def config_theme_path():
    if sys.platform != "darwin":
        return

    theme_name = str(QtGui.QIcon.theme_name())

    if theme_name != "Oxygen":
        QtGui.QIcon.set_theme_name("Oxygen")

    search_paths = list(QtGui.QIcon.theme_search_paths())

    custom_path = "/opt/local/share/icons"
    if custom_path not in search_paths:
        search_paths.append(custom_path)

    QtGui.QIcon.set_theme_search_paths(search_paths)
