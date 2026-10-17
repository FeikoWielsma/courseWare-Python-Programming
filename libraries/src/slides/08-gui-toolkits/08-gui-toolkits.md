---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: GUI Toolkits
language: python
---

# GUI Toolkits

- Everything so far has printed to a terminal :
  - Which is the right answer more often than people admit
- Sometimes the audience is not you :
  - A colleague who will not type a command
  - A tool that has to be handed over and used unattended
- Python has a graphical toolkit in the standard library :
  - `tkinter`, which is always present and never has to be installed
- The goal here is recognition, not a finished application


---

# Installing tkinter

- `tkinter` ships with Python, but not with every Python package :
  - The Windows and macOS installers include it
  - Most Linux distributions split it into a separate package
- On Debian and Ubuntu it is one command :

```bash
sudo apt install python3-tk
```

- Check it before writing any code :

```bash
python -c "import tkinter; print(tkinter.TkVersion)"
```


---

# Root Window and Event Loop

- A graphical program has a different shape from a script :
  - A script runs top to bottom and exits
  - A window is created, then waits
- `Tk()` is the root window, and there is exactly one
- `mainloop()` waits for an event, dispatches it, and waits again :
  - It does not return until the window is destroyed
  - Nothing written after it runs before then

```python
root = tk.Tk()
root.title("A window")
root.geometry("420x220")
root.mainloop()
```

> `demo01 · gui_root_window`


---

# Widgets

- Three widgets carry most simple forms :
  - `Label` shows text, `Entry` takes text, `Button` does something
- Prefer the themed `ttk` versions over the plain `tk` ones :
  - Same names, native appearance
- A widget is created with its parent as the first argument
- `command=` takes the function itself, without parentheses

```python
entry = ttk.Entry(root, width=24)
button = ttk.Button(root, text="Look up", command=look_up)
```

> `demo02 · gui_widgets`


---

# Widget Values

- A widget owns its value, and is asked for it rather than tracked :
  - `entry.get()` reads what the user typed
  - `label.configure(text=...)` writes it back
- `configure()` sets any option after construction
- The callback is an ordinary method :
  - It runs when the event happens, not when it is registered

```python
def look_up() -> None:
    name = entry.get().strip()
    if not name:
        result.configure(text="type a hostname first")
        return
    result.configure(text=f"{name} resolved")
```


---

# grid Layout

- Widgets do not place themselves, a geometry manager places them
- `grid` puts a widget in a row and a column :
  - `sticky` takes compass points, so `"e"` pins right and `"ew"` fills
  - `padx` and `pady` add space around the widget
  - `columnspan` lets one widget sit across several columns
- A widget stretches only if its row or column is given a weight :
  - Weight is a share of the spare space, not a yes or no

```python
label.grid(row=row, column=0, sticky="e", padx=(0, 8), pady=4)
entry.grid(row=row, column=1, sticky="ew", pady=4)
form.columnconfigure(1, weight=1)
```

> `demo03 · gui_grid_layout`


---

# Events and Callbacks

- `bind()` maps an event pattern to a callback :
  - `<Key>` is any key, `<Key-a>` is one key, `<Button-1>` is a left click
  - `<Configure>` fires when the widget is resized
- Every bound callback is handed one argument, the event :
  - It carries `x`, `y`, `keysym` and the widget it happened on
- A `Button`'s `command=` is the same idea with the event thrown away

```python
root.bind("<Key>", lambda event: report(f"key {event.keysym}", event))
canvas.bind("<Button-1>", lambda event: report("left click", event))
canvas.bind("<Configure>", lambda event: report("resized", event))
```

> `demo04 · gui_events`


---

# ttk.Treeview

- `ttk.Treeview` is a real table, with headings and columns
- Rows are inserted, and each one gets an identifier back
- Clicking a heading can re-order the rows :
  - `tree.set` reads one cell, `tree.move` re-places a row
- The widget most internal tools need :
  - Most internal tools are a table of something with a filter above it

```python
tree = ttk.Treeview(root, columns=list(COLUMNS), show="headings")
for row in rows:
    tree.insert("", "end", values=[row[name] for name in COLUMNS])
```

> `demo05 · gui_treeview`


---

# Treeview and SQLite

- The same table, filled from SQLite instead of a CSV :
  - Type a filter, press Return, run the query, refill the table
- The user's text is a parameter, never formatted into the SQL :
  - Exactly as in the scraping module

```python
sql = f"SELECT {', '.join(COLUMNS)} FROM servers"
if term:
    sql += " WHERE site LIKE ? OR role LIKE ? OR hostname LIKE ?"
    parameters = (f"%{term}%",) * 3
return connection.execute(sql, parameters).fetchall()
```

> `demo06 · gui_treeview_sqlite`


---

# Choosing a Toolkit

<div class="two-col">
<div>

- `tkinter` :
  - In the standard library
  - Plain, dated, acceptable
  - Small tools and dialogs
- `PySide6`, the Qt binding :
  - A large install
  - Native and modern
  - Real desktop applications

</div>
<div>

- `Streamlit` :
  - Opens a browser tab
  - No event loop, no callbacks
  - Dashboards over data
- Model and view :
  - `tkinter` holds the rows itself
  - Qt asks a model for them
  - Which matters at scale

</div>
</div>


---

# GUI Trade-offs

- A graphical program costs more than it looks :
  - It cannot be run from cron, piped, or driven from a script
  - It needs a display, which rules out most servers
  - It is harder to test than anything else in this course
- Reach for a window when the user is not you :
  - And reach for a command-line tool when the user is
- The command-line tools cover most of the middle ground :
  - A clear `--help`, real exit codes, and a table printed with `rich`


---

# Summary : GUI Toolkits

- A GUI inverts the shape of a program :
  - Build the widgets, then hand control to an event loop
- `tkinter` is in the standard library and always available :
  - `python3-tk` on Debian and Ubuntu
- Three widgets and one geometry manager cover most forms :
  - `Label`, `Entry`, `Button`, placed with `grid`
- `ttk.Treeview` is the widget most internal tools actually need
- Qt and Streamlit are the other two answers, and both are in `reference/gui/`
