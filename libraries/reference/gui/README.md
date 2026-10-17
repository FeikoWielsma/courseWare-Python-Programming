# Bonus GUI examples

The course itself uses **tkinter**, because it ships with Python and therefore
cannot fail to install at half past four in the afternoon. These four files are
the other two answers to the same question, written against the same
`data/servers.csv` as `demos/08-gui/05_gui_treeview.py`, so that they can be
read side by side.

Nothing here is needed to complete the course. None of it is installed by
`uv sync`, and none of it is checked by the course's `ruff` or `compileall`
runs. Install what you want to try, and delete the rest.

---

## `hello_pyside6.py` — Qt, the smallest version

The PySide6 equivalent of `demos/08-gui/01_gui_root_window.py`. A root object
that owns an event loop, a window, one label.

```bash
uv pip install PySide6
python reference/gui/hello_pyside6.py
```

Read it next to the tkinter file and the differences are: Qt is class-based
rather than function-based, its method names are camelCase because the API is
a binding onto a C++ library, and a `QMainWindow` arrives with menus, toolbars
and a status bar already built in.

## `inventory_pyside6.py` — Qt, the inventory table

The PySide6 equivalent of `demos/08-gui/05_gui_treeview.py`, with sorting and
a live filter box.

```bash
uv pip install PySide6
python reference/gui/inventory_pyside6.py
```

This is the file worth reading, because it shows the one structural idea Qt
has that tkinter does not: **model and view are separate**. A tkinter
`Treeview` holds the rows itself, so you fill it and empty it by hand. In Qt
you write a model that answers questions about your data, hand it to a view,
and sorting, filtering and redrawing are somebody else's problem. That is more
code for fourteen rows and far less code for fourteen thousand.

PySide6 is the official Qt binding, LGPL licensed, from The Qt Company. PyQt6
is a different binding to the same toolkit under a stricter licence. The older
`PySide2` you may find in examples online is Qt 5 and is no longer maintained.

## `inventory_streamlit.py` — the same data as a web app

```bash
uv pip install streamlit
streamlit run reference/gui/inventory_streamlit.py
```

Opens a browser tab instead of a window. There is no event loop, no callback
and no widget object to keep hold of: the script runs from top to bottom again
on every interaction, and each widget function returns whatever the user has
currently chosen. `st.dataframe` turns a pandas DataFrame into a sortable,
scrollable table in one line, which is why data teams reach for it.

The trade-off is that it is a web server. It is excellent for a dashboard your
colleagues open in a browser, and the wrong tool for a program that has to run
on one machine with no network.

---

## Choosing between the three

| | tkinter | PySide6 / Qt | Streamlit |
|---|---|---|---|
| Install | none, in the standard library | ~100 MB | pip, plus a browser |
| Looks | plain, dated, acceptable | native, modern | a web page |
| Best at | small tools, dialogs, anything internal | real desktop applications | dashboards over data |
| Learning cost | an afternoon | weeks | an afternoon |
| Licence | Python's own | LGPL, or commercial | Apache 2.0 |

On Debian and Ubuntu, tkinter itself needs one extra package that is not
installed with Python by default :

```bash
sudo apt install python3-tk
```
