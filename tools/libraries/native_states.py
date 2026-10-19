"""Generate native slides from demo excerpts and Python-executed checkpoints.

Run with --check to compare the checked-in slide payloads with fresh execution.
The renderer components are reused from the fundamentals; ArrayGrid adds only
the array/frame cells required by these examples.
"""

import ast
import contextlib
import copy
import io
import json
import re
import sys
import textwrap
from pathlib import Path

import numpy as np
import pandas as pd
from sqlalchemy import inspect

ROOT = Path(__file__).resolve().parents[2] / "libraries"


def excerpt(demo: str, start: str, end: str | None = None) -> tuple[str, str, Path]:
    path = ROOT / "demos" / demo
    source = path.read_text(encoding="utf-8")
    offset = source.index(start)
    stop = source.index(end, offset) if end else len(source)
    return source[:offset], source[offset:stop].strip(), path


def namespace(setup: str, path: Path) -> dict:
    values = {"__file__": str(path), "__name__": "__native__"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(setup, str(path), "exec"), values)
    return values


def grid(name: str, values, columns, labels=None, selected=()) -> dict:
    return {
        "name": name,
        "values": values,
        "columns": columns,
        "labels": labels,
        "selected": [[int(row), int(column)] for row, column in selected],
    }


def frame_grid(name: str, frame: pd.DataFrame, selected=()) -> dict:
    frame = frame.fillna("NA")
    return grid(
        name,
        frame.values.tolist(),
        frame.columns.tolist(),
        ["NA" if pd.isna(value) else value for value in frame.index],
        selected,
    )


def cells(array) -> list:
    return np.asarray(array, dtype=float).round(3).tolist()


def ordinary(
    demo, start, render, captions, *, end=None, base=None, layout="side", discard=()
) -> dict:
    setup, code, path = excerpt(demo, start, end)
    values = namespace(setup, path)
    for name in discard:
        values.pop(name, None)
    states, output, ranges = [], [], []
    for index, node in enumerate(ast.parse(code).body):
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), "exec"), values)
        states.append(copy.deepcopy(render(values, index)))
        output.append(captured.getvalue().splitlines())
        ranges.append(f"1-{node.end_lineno}")
    assert len(captions) == len(states), (demo, len(captions), len(states))
    return {
        "demo": demo,
        "code": code,
        "ranges": ranges,
        "layout": layout,
        "run": (base or {}) | {"states": states, "output": output, "captions": captions},
    }


def lookup() -> dict:
    def render(values, index):
        classes = values["Mage"].__mro__
        owners = [
            classes[0],
            next(cls for cls in classes if "attack" in cls.__dict__),
            values["Character"],
            *[classes[-1]] * 2,
        ]
        return {
            "attrs": {
                cls.__name__: {
                    "attack": "yes" if "attack" in cls.__dict__ else "-",
                    "__str__": "yes" if "__str__" in cls.__dict__ else "-",
                }
                for cls in classes
            },
            "active": [owners[index].__name__],
        }

    return ordinary(
        "01-inheritance/04_overriding.py",
        'jaina = Mage("Jaina")',
        render,
        [
            "Jaina's class is Mage.",
            "Mage supplies the first attack implementation in the MRO.",
            "The explicit Character call uses the base implementation.",
            "The method resolution order includes Mage, Character and object.",
            "Neither course class defines __str__; the inherited method belongs to object.",
        ],
        base={
            "boxes": [
                {"id": name, "label": name, "tag": "class", "x": index * 290, "y": 0, "width": 260}
                for index, name in enumerate(["Mage", "Character", "object"])
            ]
        },
        layout="pair",
    )


def constructor() -> dict:
    setup, code, path = excerpt("01-inheritance/03_super_init.py", "class Mage")
    values = namespace(setup, path)
    nodes = ast.parse(code).body
    exec(compile(ast.Module(body=[nodes[0]], type_ignores=[]), str(path), "exec"), values)
    attributes = [{}]

    def trace(frame, event, _arg):
        if frame.f_code.co_filename == str(path) and frame.f_code.co_name == "__init__":
            obj = frame.f_locals.get("self")
            if obj is not None and isinstance(obj, values["Mage"]):
                current = vars(obj).copy()
                if current != attributes[-1]:
                    attributes.append(current)
        return trace

    previous = sys.gettrace()
    try:
        sys.settrace(trace)
        exec(compile(ast.Module(body=[nodes[1]], type_ignores=[]), str(path), "exec"), values)
    finally:
        sys.settrace(previous)
    assert [list(item) for item in attributes] == [
        [],
        ["name"],
        ["name", "health"],
        ["name", "health", "mana"],
    ]
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        exec(compile(ast.Module(body=[nodes[2]], type_ignores=[]), str(path), "exec"), values)
    states = [
        {
            "attrs": {
                "base": {"sets": "name, health"},
                "mage": {key: repr(value) for key, value in attrs.items()},
            },
            "active": ["base" if index in {1, 2} else "mage"],
        }
        for index, attrs in enumerate(attributes)
    ]
    return {
        "demo": "01-inheritance/03_super_init.py",
        "code": code,
        "ranges": ["1-4", "1-3", "1-3", f"1-{len(code.splitlines())}"],
        "layout": "stack",
        "run": {
            "boxes": [
                {
                    "id": "base",
                    "label": "Character.__init__",
                    "tag": "",
                    "x": 0,
                    "y": 0,
                    "width": 330,
                },
                {
                    "id": "mage",
                    "label": "jaina",
                    "tag": "Mage object",
                    "x": 380,
                    "y": 0,
                    "width": 330,
                },
            ],
            "states": states,
            "output": [[], [], [], captured.getvalue().splitlines()],
            "captions": [
                "The subclass initialiser starts with an empty instance.",
                "Character.__init__ stores name on that same instance.",
                "The base initialiser also stores health.",
                "The subclass stores mana after super returns.",
            ],
        },
    }


def tree() -> dict:
    def render(values, index):
        price = values["price"]
        pod = price.find_parent("article")
        tags = [price, price.parent, pod, pod.select_one("h3 a"), price.find_next_sibling("p")]
        ids = ["price", "container", "book", "title", "stock"]
        return {
            "names": {"selection": {"cursor": ids[index]}},
            "objects": {
                key: {"type": key, "value": tag.name} for key, tag in zip(ids, tags, strict=True)
            },
            "active": ["selection.cursor"],
        }

    return ordinary(
        "04-web-scraping/05_walking_the_tree.py",
        'price = soup.select_one("p.price_color")',
        render,
        [
            "Select the price paragraph in the fixture.",
            "parent is the surrounding div.",
            "find_parent walks up to the containing article.",
            "select_one finds the title link below the article.",
            "find_next_sibling finds the stock paragraph beside the price.",
        ],
        end="image = pod.select_one",
        base={"frames": [{"id": "selection", "label": "Tree cursor"}]},
        layout="stack",
    )


def session() -> dict:
    setup, code, path = excerpt(
        "05-sqlalchemy/07_session_and_persistence.py",
        "with Session(engine)",
        "    # The session tracks",
    )
    # The excerpt owns a context manager. Execute its body in an equivalent
    # session so every statement can be inspected before the context closes.
    values = namespace(setup, path)
    values["session"] = values["Session"](values["engine"])
    body = ast.parse(textwrap.dedent(code.split("\n", 1)[1])).body
    states, output, ranges, captions = [], [], [], []
    committed = False
    try:
        for node in body:
            captured = io.StringIO()
            with contextlib.redirect_stdout(captured):
                exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), "exec"), values)
            if ast.unparse(node).startswith("session.commit("):
                committed = True
            obj = inspect(values["first"])
            phase = (
                "committed"
                if committed
                else "pending"
                if obj.pending
                else "flushed"
                if obj.persistent
                else "transient"
            )
            identifier = obj.identity[0] if obj.identity else None
            states.append(
                {
                    "attrs": {phase: {"title": "Sharp Objects", "id": str(identifier)}},
                    "active": [phase],
                }
            )
            output.append(captured.getvalue().splitlines())
            ranges.append(f"1-{node.end_lineno + 1}")
            captions.append(
                {
                    "transient": "Constructed objects have not yet been added to the session.",
                    "pending": "Added objects are pending; no generated id is available yet.",
                    "flushed": "Flush assigns ids, but the transaction is still open.",
                    "committed": "Commit makes the transaction permanent.",
                }[phase]
            )
    finally:
        values["session"].close()
        values["engine"].dispose()
    return {
        "demo": "05-sqlalchemy/07_session_and_persistence.py",
        "code": code,
        "ranges": ranges,
        "layout": "pair",
        "run": {
            "boxes": [
                {
                    "id": phase,
                    "label": phase.title(),
                    "tag": "book",
                    "x": index * 285,
                    "y": 0,
                    "width": 250,
                }
                for index, phase in enumerate(["transient", "pending", "flushed", "committed"])
            ],
            "states": states,
            "output": output,
            "captions": captions,
        },
    }


def views() -> dict:
    def render(values, _index):
        photo = values["photo"]
        view = values["crop"]
        detached = values.get("detached")
        return {
            "grids": [
                grid(
                    "photo red channel",
                    cells(photo[12:14, 16:19, 0]),
                    ["16", "17", "18"],
                    ["12", "13"],
                    [(0, 0)],
                ),
                grid(
                    "crop red channel",
                    cells(view[:2, :3, 0]),
                    ["0", "1", "2"],
                    ["0", "1"],
                    [(0, 0)],
                ),
                grid(
                    "copy red channel",
                    cells(detached[:2, :3, 0])
                    if detached is not None
                    else [["", "", ""], ["", "", ""]],
                    ["0", "1", "2"],
                    ["0", "1"],
                    [(0, 0)],
                ),
            ]
        }

    return ordinary(
        "06-numpy/09_views_and_copies.py",
        "crop = photo",
        render,
        [
            "Slicing creates a view of the photo buffer.",
            "copy allocates an independent buffer.",
            "Writing red through the view changes the photo.",
            "The photo contains the new pixel.",
            "The independent copy retains the original pixel.",
            "The view shares memory with the photo.",
            "The copy does not share the buffer.",
            "Advanced indexing also creates a copy.",
        ],
    )


def broadcasting() -> dict:
    def render(values, index):
        photo, factors = values["photo"], values["factors"]
        result = np.broadcast_shapes(photo.shape, factors.shape)
        return {
            "grids": [
                grid(
                    "Shapes align from the right",
                    [
                        list(photo.shape),
                        ["", "", factors.shape[0]],
                        list(result) if index else ["", "", ""],
                    ],
                    ["height", "width", "channels"],
                    ["photo", "factors", "result"],
                    [(0, 2), (1, 2), (2, 2)],
                ),
                grid("Channel multipliers", [cells(factors)], ["red", "green", "blue"], ["factor"]),
            ]
        }

    return ordinary(
        "06-numpy/13_broadcasting.py",
        "factors = np.array",
        render,
        [
            "A length-three factor vector aligns with the channel dimension.",
            "Every pixel receives the same three factors, followed by clipping.",
            "The result keeps the photo's height, width and channel count.",
            "broadcast_shapes confirms the compatible result shape.",
        ],
        end="print(np.broadcast_shapes((3, 1)",
        layout="stack",
    )


def axes() -> dict:
    def render(values, index):
        plays = values["plays"]
        return {
            "grids": [
                grid(
                    "Days by hours", cells(plays), ["08", "09", "10", "11"], ["Mon", "Tue", "Wed"]
                ),
                grid(
                    "axis=0 removes days",
                    [cells(plays.sum(axis=0))] if index >= 2 else [["", "", "", ""]],
                    ["08", "09", "10", "11"],
                    ["sum"],
                ),
                grid(
                    "axis=1 removes hours",
                    [[int(value)] for value in plays.sum(axis=1)]
                    if index >= 3
                    else [[""], [""], [""]],
                    ["sum"],
                    ["Mon", "Tue", "Wed"],
                ),
            ]
        }

    return ordinary(
        "06-numpy/15_the_axis_argument.py",
        "plays = np.array",
        render,
        [
            "Each row is one day; each column is one selected hour.",
            "Without an axis, all twelve counts reduce to one total.",
            "axis=0 adds down the days and leaves four hour totals.",
            "axis=1 adds across hours and leaves three day totals.",
            "keepdims retains a size-one column dimension.",
        ],
        end="photo = image",
    )


def selections() -> dict:
    def render(values, index):
        frame = values["frame"]
        selected = [[], [(1, 1)], [(0, 1)], [(0, 1), (1, 1)]][index]
        return {"grids": [frame_grid("Same table, two selectors", frame, selected)]}

    return ordinary(
        "07-pandas/10_iloc_by_position.py",
        "frame = tracks.iloc",
        render,
        [
            "The three-row sample has title labels and zero-based positions.",
            "loc selects Yesterday by its label.",
            "iloc selects the first row by position.",
            "The label slice includes both Imagine and Yesterday.",
        ],
    )


def grouping() -> dict:
    def render(values, index):
        sample = values["sample"]
        labels = list(sample.groupby("genre").groups)
        totals = sample.groupby("genre")["plays"].sum()
        selected = (
            [
                (position, 0)
                for positions in sample.groupby("genre").indices.values()
                for position in positions
            ]
            if index >= 1
            else []
        )
        return {
            "grids": [
                frame_grid("Input tracks", sample, selected),
                grid(
                    "One sum per genre",
                    [[int(totals[label])] for label in labels]
                    if index >= 2
                    else [[""] for _ in labels],
                    ["plays"],
                    labels,
                ),
            ]
        }

    return ordinary(
        "07-pandas/16_groupby_agg.py",
        "sample = tracks.iloc",
        render,
        [
            "The input contains three tracks and their fictional play counts.",
            "groupby assigns rows with the same genre to a group.",
            "sum applies to each group's plays and combines the results by genre.",
            "The result has one indexed value per genre.",
        ],
    )


def joins() -> dict:
    def render(values, _index):
        tracks, artists = values["tracks"], values["artists"]
        keys = list(dict.fromkeys([*tracks["artist"], *artists["artist"]]))
        titles = dict(zip(tracks["artist"], tracks["title"], strict=True))
        countries = dict(zip(artists["artist"], artists["country"], strict=True))
        inputs = [[titles.get(key, "NA"), countries.get(key, "NA")] for key in keys]
        input_grid = grid(
            "Input keys",
            inputs,
            ["track title", "country"],
            keys,
            [
                (i, j)
                for i, row in enumerate(inputs)
                for j, value in enumerate(row)
                if value == "NA"
            ],
        )
        input_grid["labelWidth"] = 160
        result = next(values[key] for key in ["outer", "right", "left", "inner"] if key in values)
        return {
            "grids": [input_grid, frame_grid("Join result", result.set_index("title")[["country"]])]
        }

    return ordinary(
        "07-pandas/19_merge_how.py",
        'inner = tracks.merge(artists, on="artist", how="inner")',
        render,
        [
            "Inner keeps only the two matching artists.",
            "The inner join has two rows.",
            "Left also keeps Imagine, with a missing country.",
            "The left join has three rows.",
            "Right also keeps Fleetwood Mac, with no track title.",
            "The right join has three rows.",
            "Outer keeps both unmatched keys as well as the matches.",
            "The outer join has four rows.",
        ],
        discard=("inner", "left", "right", "outer"),
    )


DEFINITIONS = [
    ("lookup", "01-inheritance", "Overriding Methods", "Method Lookup", "StatefulObjects", lookup),
    (
        "constructor",
        "01-inheritance",
        "Extending with super",
        "Initialising One Mage",
        "StatefulObjects",
        constructor,
    ),
    ("tree", "04-web-scraping", "Navigating the Tree", "Traversing a Book Card", "CoreNames", tree),
    (
        "session",
        "05-sqlalchemy",
        "Session",
        "A Book Through a Transaction",
        "StatefulObjects",
        session,
    ),
    ("views", "06-numpy", "Views and Copies", "A View Shares the Photo Buffer", "ArrayGrid", views),
    (
        "broadcasting",
        "06-numpy",
        "Broadcasting",
        "Three Factors for Every Pixel",
        "ArrayGrid",
        broadcasting,
    ),
    ("axes", "06-numpy", "axis Argument", "Reducing Days and Hours", "ArrayGrid", axes),
    ("selections", "07-pandas", "loc and iloc", "Labels and Positions", "ArrayGrid", selections),
    ("grouping", "07-pandas", "groupby", "Summing Each Genre", "ArrayGrid", grouping),
    ("joins", "07-pandas", "Join Types", "Keeping Unmatched Artists", "ArrayGrid", joins),
]


def markdown(title: str, component: str, spec: dict) -> str:
    number, slug = Path(spec["demo"]).stem.split("_", 1)
    data = json.dumps(spec["run"], indent=2, ensure_ascii=False)
    options = (
        ' direction="row" :cell-width="100" :frame-width="170" :pitch="110" :gap="65"'
        if component == "CoreNames"
        else ""
    )
    return (
        f'---\nlayout: default\ntitle: {title}\npills: ["demo{number} · {slug}"]\n---\n\n'
        f"# {title}\n\n<script setup>\nconst run = {data}\n</script>\n\n"
        f'<DataStructuresRun :run="run" layout="{spec["layout"]}" output-width="300px">\n\n'
        f"```python {{{'|'.join(spec['ranges'])}}}\n{spec['code']}\n```\n\n"
        f'<template #visual="{{ step }}">\n<{component} :run="run" :step="step"{options} />\n'
        "</template>\n</DataStructuresRun>\n"
    )


def main() -> None:
    total = 0
    for name, _module, _after, title, component, build in DEFINITIONS:
        spec = build()
        path = ROOT / "src" / "slidev" / "native" / f"{name}.md"
        expected = markdown(title, component, spec)
        if "--check" in sys.argv:
            actual = path.read_text(encoding="utf-8")
            match = re.search(r"const run = (.*?)\n</script>", actual, re.DOTALL)
            assert match and json.loads(match[1]) == spec["run"], f"{name}: displayed state drift"
            assert actual == expected, f"{name}: demo excerpt or choreography drift"
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
        total += len(spec["run"]["states"])
        print(f"{name}: {len(spec['run']['states'])} executed states")
    print(f"Ten native slides, {total} states match their demo programs.")


if __name__ == "__main__":
    main()
