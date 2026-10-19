"""Check the native Data Structures slides against Python and their demos.

Each slide in src/slidev/data-structures/ shows one program. Its Python fence
carries cumulative line ranges, one per click state, and its `<script setup>`
holds the JSON `run` object that the components display. This check :

- confirms the fence is an in-order excerpt of the demo named by the slide's pill,
- runs the fence one click state at a time in a single namespace, so object
  identity is real across states,
- compares the printed output of every state with `run.output`,
- compares the displayed collection state, its object identities and the
  selected or changed items with the Python objects after that state.

With `--browser`, it also loads every click state of the built Slidev app and
compares what the components actually rendered with the same Python states.

    uv run python build/slidev_checks/check_data_structures.py
    uv run python build/slidev_checks/check_data_structures.py --browser http://127.0.0.1:4188

The browser check needs the built app served (`build/slidev.ts --serve-only`)
and reads routes from .courseware/fundamentals/student/manifest.json.
"""

from __future__ import annotations

import argparse
import ast
import contextlib
import io
import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SLIDES = ROOT / "src" / "slidev" / "data-structures"
DEMOS = ROOT / "demos" / "03-datastructures"

# Slide file, the component that draws its state, and the kind of state it holds.
PACKAGE = {
    "indexing-and-slicing.md": ("DataStructuresSlicing", "slicing"),
    "replacing-and-deleting.md": ("DataStructuresSequence", "sequence"),
    "shared-and-separate-rows.md": ("DataStructuresReferences", "references"),
    "lists-as-stacks.md": ("DataStructuresSequence", "sequence"),
    "set-operations.md": ("DataStructuresSets", "sets"),
    "updating-a-dictionary.md": ("DataStructuresDict", "dict"),
}


@dataclass
class Slide:
    file: str
    title: str
    component: str
    kind: str
    demo: Path
    code: list[str]
    ends: list[int]
    run: dict[str, Any]
    expected: list[dict[str, Any]] = field(default_factory=list)


def fail(slide: str, message: str) -> None:
    raise AssertionError(f"{slide}: {message}")


def parse(file: str) -> Slide:
    component, kind = PACKAGE[file]
    text = (SLIDES / file).read_text(encoding="utf-8")
    front = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not front:
        fail(file, "no frontmatter")
    title = re.search(r"^title: (.+)$", front[1], re.MULTILINE)
    heading = re.search(r"^# (.+)$", text, re.MULTILINE)
    if not title or not heading or title[1] != heading[1]:
        fail(file, "frontmatter title and heading differ")
    pill = re.search(r'pills: \["demo(\d\d) · (\w+)"\]', front[1])
    if not pill:
        fail(file, "no demo pill")
    demo = DEMOS / f"{pill[1]}_{pill[2]}.py"
    if not demo.is_file():
        fail(file, f"pill names a missing demo {demo.name}")
    fences = re.findall(r"^```python \{([^}]*)\}\n(.*?)^```$", text, re.MULTILINE | re.DOTALL)
    if len(fences) != 1:
        fail(file, "expected exactly one ranged Python fence")
    ranges, body = fences[0]
    code = body.splitlines()
    ends = []
    for part in ranges.split("|"):
        match = re.fullmatch(r"1(?:-(\d+))?", part)
        if not match:
            fail(file, f"range {part!r} is not cumulative from line 1")
        ends.append(int(match[1] or 1))
    if ends != sorted(set(ends)) or ends[-1] != len(code):
        fail(file, f"ranges {ranges} must grow and end at line {len(code)}")
    script = re.search(r"<script setup>\nconst run = (\{.*?\})\n</script>", text, re.DOTALL)
    if not script:
        fail(file, "no `const run = {...}` JSON in <script setup>")
    run = json.loads(script[1])
    if '<DataStructuresRun :run="run"' not in text or f'<{component} :run="run"' not in text:
        fail(file, f"run is not passed to DataStructuresRun and {component}")
    for key in ("states", "output", "captions"):
        if len(run[key]) != len(ends):
            fail(file, f"{len(run[key])} {key} for {len(ends)} click states")
    return Slide(file, title[1], component, kind, demo, code, ends, run)


def check_provenance(slide: Slide) -> None:
    """The fence is the demo's own lines, in the demo's order."""
    demo = slide.demo.read_text(encoding="utf-8").splitlines()
    position = 0
    for line in slide.code:
        try:
            position = demo.index(line, position) + 1
        except ValueError:
            fail(slide.file, f"line not found in order in {slide.demo.name}: {line}")


class KeyOf:
    """Stands in for a list to recover the index or slice an expression uses."""

    def __getitem__(self, key: object) -> object:
        return key


def execute(slide: Slide) -> list[tuple[dict[str, Any], list[str], dict[str, Any], int]]:
    """Run each click state's lines in one namespace; keep output and snapshots."""
    namespace: dict[str, Any] = {}
    results = []
    start = 0
    for end in slide.ends:
        before = snapshot(namespace)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(compile("\n".join(slide.code[start:end]), slide.file, "exec"), namespace)
        results.append((snapshot(namespace), output.getvalue().splitlines(), before, end))
        start = end
    return results


def snapshot(namespace: dict[str, Any]) -> dict[str, Any]:
    """The namespace, and each collection's items as the objects themselves."""
    collections = (list, dict, set)
    state: dict[str, Any] = {"__ns__": namespace}
    for name, value in namespace.items():
        if isinstance(value, collections):
            state[name] = {
                "id": id(value),
                "items": list(value.items()) if isinstance(value, dict) else list(value),
                "inner": [(id(item), list(item)) for item in value if isinstance(item, list)]
                if isinstance(value, list)
                else [],
            }
    return state


class Identity:
    """Data ids must stand for the same Python objects in every state."""

    def __init__(self, slide: str) -> None:
        self.slide = slide
        self.forward: dict[str, int] = {}
        self.backward: dict[int, str] = {}

    def bind(self, data_id: str, python_id: int) -> None:
        if self.forward.setdefault(data_id, python_id) != python_id:
            fail(self.slide, f"data id {data_id!r} stands for two different objects")
        if self.backward.setdefault(python_id, data_id) != data_id:
            fail(self.slide, f"one object is shown as {self.backward[python_id]!r} and {data_id!r}")


def check(slide: Slide) -> None:
    check_provenance(slide)
    results = execute(slide)
    identity = Identity(slide.file)
    printed: list[str] = []
    for k, (state, output, before, end) in enumerate(results):
        if output != slide.run["output"][k]:
            fail(slide.file, f"state {k} prints {output}, the slide shows {slide.run['output'][k]}")
        printed += output
        shown = slide.run["states"][k]
        last_line = slide.code[end - 1]
        namespace = state["__ns__"]
        expected: dict[str, Any] = {"output": list(printed)}
        if slide.kind == "slicing":
            expected |= check_slicing(slide, k, shown, namespace, last_line)
        elif slide.kind == "sequence":
            expected |= check_sequence(slide, k, shown, state, before, last_line, identity)
        elif slide.kind == "references":
            expected |= check_references(slide, k, shown, state, results, identity)
        elif slide.kind == "sets":
            expected |= check_sets(slide, k, shown, namespace, last_line)
        elif slide.kind == "dict":
            expected |= check_dict(slide, k, shown, state, namespace, output, identity)
        slide.expected.append(expected)


def check_slicing(slide, k, shown, namespace, line) -> dict[str, Any]:
    listing = slide.run["list"]
    values = namespace[listing["name"]]
    if listing["values"] != [repr(item) for item in values]:
        fail(slide.file, f"state {k} shows {listing['values']}")
    if shown["expr"] is None:
        if shown["picked"]:
            fail(slide.file, f"state {k} selects items without an expression")
        return {"values": listing["values"], "result": []}
    if shown["expr"] not in line:
        fail(slide.file, f"state {k} expression {shown['expr']} is not on line {line!r}")
    actual = eval(shown["expr"], namespace)
    key = eval(shown["expr"].replace(listing["name"], "KeyOf()"), {"KeyOf": KeyOf})
    indexes = list(range(len(values)))[key]
    if isinstance(key, slice):
        expected_key = {"start": key.start, "stop": key.stop, "step": key.step}
        picked, kind, items = indexes, "list", actual
    else:
        expected_key = {"index": key}
        picked, kind, items = [indexes], "item", [actual]
    if shown["key"] != expected_key or shown["picked"] != picked or shown["result"] != kind:
        fail(slide.file, f"state {k} selection differs from {shown['expr']}")
    return {"values": listing["values"], "result": [repr(item) for item in items]}


def check_sequence(slide, k, shown, state, before, line, identity) -> dict[str, Any]:
    name = slide.run["name"]
    items = state[name]["items"]
    displayed = [slide.run["objects"][data_id] for data_id in shown["items"]]
    if displayed != [repr(item) for item in items]:
        fail(slide.file, f"state {k} shows {displayed}, Python has {items}")
    for data_id, item in zip(shown["items"], items, strict=True):
        identity.bind(data_id, id(item))
    returned = None
    if ".pop()" in line:
        returned = repr(before[name]["items"][-1])
    shown_returned = shown.get("returned")
    if (slide.run["objects"][shown_returned] if shown_returned else None) != returned:
        fail(slide.file, f"state {k} returned item differs from Python ({returned})")
    if shown_returned:
        identity.bind(shown_returned, id(before[name]["items"][-1]))
    if shown.get("active") and shown["active"] not in shown["items"]:
        fail(slide.file, f"state {k} marks an item that is not in the list")
    return {"items": [repr(item) for item in items], "returned": returned}


def canonical(refs: list[int]) -> list[int]:
    order: list[int] = []
    for ref in refs:
        if ref not in order:
            order.append(ref)
    return [order.index(ref) for ref in refs]


def check_references(slide, k, shown, state, results, identity) -> dict[str, Any]:
    expected = {}
    for name in slide.run["names"]:
        refs = shown["refs"].get(name)
        if name not in state:
            if refs:
                fail(slide.file, f"state {k} draws {name} before it exists")
            continue
        if refs is None:
            fail(slide.file, f"state {k} omits {name}")
        inner = state[name]["inner"]
        for data_id, (python_id, values) in zip(refs, inner, strict=True):
            identity.bind(data_id, python_id)
            if shown["objects"][data_id] != [repr(value) for value in values]:
                fail(slide.file, f"state {k} shows {data_id} as {shown['objects'][data_id]}")
        expected[name] = {
            "targets": canonical([python_id for python_id, _ in inner]),
            "values": [[repr(value) for value in values] for _, values in inner],
        }
    changed = shown.get("changed")
    if changed:
        previous = results[k - 1][0]
        old = next(v for n in slide.run["names"] if n in previous for i, v in previous[n]["inner"]
                   if identity.forward.get(changed["object"]) == i)
        new = shown["objects"][changed["object"]]
        if repr(old[changed["index"]]) == new[changed["index"]]:
            fail(slide.file, f"state {k} marks an unchanged cell")
    return {"names": expected}


def check_sets(slide, k, shown, namespace, line) -> dict[str, Any]:
    for side in ("left", "right"):
        data = slide.run["sets"][side]
        if set(data["members"]) != namespace[data["name"]]:
            fail(slide.file, f"{data['name']} members differ from Python")
    if shown["expr"] is None:
        return {"on": []}
    if shown["expr"] not in line:
        fail(slide.file, f"state {k} expression {shown['expr']} is not on line {line!r}")
    value = eval(shown["expr"], namespace)
    if isinstance(value, bool):
        tested = ast.literal_eval(ast.parse(shown["expr"], mode="eval").body.left)
        right = ast.parse(shown["expr"], mode="eval").body.comparators[0].id
        if not value or shown.get("test") != tested or shown.get("within") != right:
            fail(slide.file, f"state {k} membership test differs from Python")
        return {"on": [tested]}
    if shown["result"] != sorted(value):
        fail(slide.file, f"state {k} result {shown['result']} differs from {sorted(value)}")
    return {"on": sorted(value)}


def check_dict(slide, k, shown, state, namespace, output, identity) -> dict[str, Any]:
    pairs = state[slide.run["name"]]["items"]
    rows = [[row["key"], row["value"]] for row in shown["rows"]]
    if rows != [[repr(key), repr(value)] for key, value in pairs]:
        fail(slide.file, f"state {k} shows {rows}, Python has {pairs}")
    for row, (key, _) in zip(shown["rows"], pairs, strict=True):
        identity.bind(row["id"], id(key))
    if output:
        active = next(row for row in shown["rows"] if row["id"] == shown["active"])
        looked_up = namespace[slide.run["name"]][ast.literal_eval(active["key"])]
        if output != [str(looked_up)]:
            fail(slide.file, f"state {k} highlights {active['key']}, which is not the lookup")
    return {"rows": rows}


# Reads what each component rendered for every click state, from the built app.
BROWSER_SCRIPT = r"""
import { browserTimeoutMs, withBrowser, withPage } from %(browser)s;
import { animationRate, onPages, settle } from %(animation)s;
const [origin, plan] = [process.argv[2], JSON.parse(process.argv[3])];
const results = {}, unsettled = {};
const readRoute = async (page, { route, states, kind }) => {
  {
    results[route] = [];
    unsettled[route] = [];
    for (let k = 0; k < states; k++) {
      const url = `${origin}/slidev/?r=${Date.now()}#/${route}?clicks=${k}`;
      await page.goto(url, { waitUntil: 'networkidle0', timeout: browserTimeoutMs });
      await page.waitForSelector(
        `[data-source-id="${route}"] .ds-run`,
        { timeout: browserTimeoutMs },
      );
      await page.evaluate(() => document.fonts.ready);
      // Read once the opening transitions have ended, played fast.
      await animationRate(page, 10);
      const problem = await settle(page, route, k);
      if (problem) unsettled[route].push(problem);
      results[route].push(await page.evaluate((route, kind) => {
        const frame = document.querySelector(`[data-source-id="${route}"]`);
        const text = el => el.textContent.trim();
        const box = el => el.getBoundingClientRect();
        const shown = el => parseFloat(getComputedStyle(el).opacity) > .5;
        const out = {
          step: Number(frame.querySelector('.ds-run').dataset.dsStep),
          output: [...frame.querySelectorAll('[data-ds-output]')].map(text),
          caption: text(frame.querySelector('[data-ds-caption]')),
          overflow: [...frame.querySelectorAll('.ds-run *')].filter(el => {
            const r = box(el), body = box(frame.querySelector('.course-body'));
            return shown(el) && r.width && (r.right > body.right + 2 || r.bottom > body.bottom + 2);
          }).length,
        };
        if (kind === 'slicing') {
          out.values = [...frame.querySelectorAll('.cell[data-ds-value]:not(.copy)')].map(text);
          out.result = [...frame.querySelectorAll('.copy')].filter(shown)
            .sort((a, b) => box(a).left - box(b).left).map(text);
        } else if (kind === 'sequence') {
          const present = [...frame.querySelectorAll('[data-ds-status="present"]')];
          const stack = frame.querySelector('.ds-sequence.stack');
          present.sort((a, b) => stack ? box(b).top - box(a).top : box(a).left - box(b).left);
          out.items = present.map(text);
          const returned = frame.querySelector('[data-ds-status="returned"]');
          out.returned = returned && shown(returned) ? text(returned) : null;
        } else if (kind === 'references') {
          out.names = {};
          for (const panel of frame.querySelectorAll('[data-ds-name]')) {
            if (!shown(panel)) continue;
            const objects = [...panel.querySelectorAll('[data-ds-object]')].filter(shown);
            const ends = [...panel.querySelectorAll('path.ref')].map(path => {
              const end = path.getPointAtLength(path.getTotalLength());
              const svg = box(path.ownerSVGElement);
              return svg.top + end.y;
            });
            const middle = o => box(o).top + box(o).height / 2;
            const targets = ends.map(y => objects.findIndex(o => Math.abs(middle(o) - y) < 4));
            const order = [];
            for (const t of targets) if (!order.includes(t)) order.push(t);
            out.names[panel.dataset.dsName] = {
              targets: targets.map(t => order.indexOf(t)),
              values: targets.map(t => t < 0
                ? null : [...objects[t].querySelectorAll('[data-ds-value]')].map(text)),
            };
          }
        } else if (kind === 'sets') {
          out.on = [...frame.querySelectorAll('.chip.on')].map(el => el.dataset.dsMember).sort();
        } else if (kind === 'dict') {
          const cells = ['[data-ds-key]', '.item[data-ds-value]'];
          out.rows = [...frame.querySelectorAll('[data-ds-status="present"]')]
            .sort((a, b) => box(a).top - box(b).top)
            .map(row => cells.map(css => row.querySelector(css)))
            .map(found => found.map(text));
        }
        return out;
      }, route, kind));
    }
  }
};
await withBrowser({ origin }, session => onPages(session, withPage, plan, readRoute));
console.log(JSON.stringify({ results, unsettled }));
"""


def check_browser(slides: list[Slide], origin: str) -> int:
    """Compare each rendered click state with the Python state."""
    template = Path(subprocess.run(
        [shutil.which("bun") or "bun", str(ROOT / "build/toolchain.ts"), "--path"],
        stdout=subprocess.PIPE, text=True, check=True,
    ).stdout.strip())
    page_map = ROOT / ".courseware/fundamentals/student/manifest.json"
    manifest = json.loads(page_map.read_text(encoding="utf-8"))
    native = [page for page in manifest["pages"] if page["kind"] == "enrichment"]
    pages = {page["title"]: page["sourceId"] for page in native}
    plan = []
    for slide in slides:
        if slide.title not in pages:
            fail(slide.file, "not in the built deck; add it to build/slidev.config.ts enrichments")
        plan.append({"route": pages[slide.title], "states": len(slide.ends), "kind": slide.kind})
    browser = json.dumps((template / "build/browser.ts").as_posix())
    with tempfile.TemporaryDirectory() as folder:
        script = Path(folder) / "read-states.ts"
        animation = json.dumps((Path(__file__).parent / "browser_support.ts").as_posix())
        script.write_text(
            BROWSER_SCRIPT % {"browser": browser, "animation": animation},
            encoding="utf-8", newline="\n",
        )
        result = subprocess.run(
            [shutil.which("bun") or "bun", str(script), origin, json.dumps(plan)],
            capture_output=True, text=True, encoding="utf-8", check=False,
        )
    if result.returncode:
        raise RuntimeError(result.stderr[-3000:])
    reported = json.loads(result.stdout.strip().splitlines()[-1])
    rendered = reported["results"]
    checked = 0
    for slide, item in zip(slides, plan, strict=True):
        if reported["unsettled"][item["route"]]:
            fail(slide.file, "; ".join(reported["unsettled"][item["route"]]))
        states = zip(rendered[item["route"]], slide.expected, strict=True)
        for k, (dom, expected) in enumerate(states):
            if dom["step"] != k:
                fail(slide.file, f"click {k} renders step {dom['step']}")
            if dom["overflow"]:
                fail(slide.file, f"click {k} draws {dom['overflow']} elements outside the frame")
            caption = slide.run["captions"][k].replace("`", "")
            if dom["caption"] != caption:
                fail(slide.file, f"click {k} caption {dom['caption']!r}")
            for key, value in expected.items():
                if dom.get(key) != value:
                    fail(slide.file, f"click {k} renders {key}={dom.get(key)}, Python has {value}")
            checked += 1
    return checked


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--browser", metavar="ORIGIN", help="served app, e.g. http://127.0.0.1:4188")
    args = parser.parse_args()
    slides = [parse(file) for file in PACKAGE]
    for slide in slides:
        check(slide)
    states = sum(len(slide.ends) for slide in slides)
    print(f"Data Structures slides: {len(slides)} slides, {states} click states match Python.")
    if args.browser:
        checked = check_browser(slides, args.browser.rstrip("/"))
        print(f"Rendered states: {checked} click states match Python in the browser.")


if __name__ == "__main__":
    main()
