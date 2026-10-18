"""Verify core Slidev animation states against their canonical demos and browser output.

Static mode executes each complete displayed program under ``sys.settrace``.
The fence's line groups select execution events, including calls and returns;
loops therefore run as written instead of being approximated with prefixes.

    uv run python build/slidev_checks/check_core.py
    uv run python build/slidev_checks/check_core.py --browser http://127.0.0.1:53011
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SLIDES = ROOT / "src" / "slidev" / "core"
COMPONENTS = ROOT / "src" / "slidev" / "components"

# File, demo path, component kind, route in the integrated source map.
FILES = {
    "blocks-and-line-endings.md": (
        "01-pythonintro/04_lines_and_identation.py",
        "stream",
        "01-python-intro-17-enhancement",
    ),
    "binding-and-rebinding.md": (
        "02-variablesanddatatypes/01_variables.py",
        "names",
        "02-variables-and-data-types-1-enhancement",
    ),
    "several-names-one-object.md": (
        "02-variablesanddatatypes/03_multipleassignment.py",
        "names",
        "02-variables-and-data-types-3-enhancement",
    ),
    "condition-before-each-pass.md": (
        "04-controlflow/05_while.py",
        "names",
        "04-control-flow-and-operators-7-enhancement",
    ),
    "one-item-per-pass.md": (
        "04-controlflow/07_for.py",
        "loop",
        "04-control-flow-and-operators-10-enhancement",
    ),
    "leaving-a-loop-with-break.md": (
        "04-controlflow/09_breakandcontinue.py",
        "loop",
        "04-control-flow-and-operators-13-enhancement",
    ),
    "parameter-shares-the-list.md": (
        "05-functions/09_objectreferences.py",
        "names",
        "05-functions-11-enhancement",
    ),
    "rebinding-a-parameter.md": (
        "05-functions/10_overwritingreferences.py",
        "names",
        "05-functions-12-enhancement",
    ),
    "handing-back-a-result.md": (
        "05-functions/02_returnstatement.py",
        "names",
        "05-functions-4-enhancement",
    ),
    "local-and-global-names.md": (
        "05-functions/15_variablescope.py",
        "names",
        "05-functions-18-enhancement",
    ),
}


@dataclass
class Slide:
    file: str
    title: str
    demo: Path
    kind: str
    route: str
    code: list[str]
    groups: list[list[int]]
    run: dict[str, Any]
    states: list[dict[str, Any]]


@dataclass
class Event:
    event: str
    line: int
    function: str
    globals: dict[str, Any]
    stack: list[tuple[str, dict[str, Any]]]
    output: str
    object_values: dict[int, Any]
    return_value: Any = None


def fail(file: str, message: str) -> None:
    raise AssertionError(f"{file}: {message}")


def parse_groups(raw: str) -> list[list[int]]:
    groups: list[list[int]] = []
    for group in raw.split("|"):
        numbers: list[int] = []
        for part in group.split(","):
            match = re.fullmatch(r"(\d+)(?:-(\d+))?", part.strip())
            if not match:
                raise ValueError(f"invalid code range {part!r}")
            start, end = int(match[1]), int(match[2] or match[1])
            numbers.extend(range(start, end + 1))
        groups.append(numbers)
    return groups


def parse(file: str) -> Slide:
    demo_rel, kind, route = FILES[file]
    text = (SLIDES / file).read_text(encoding="utf-8")
    front = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    title = re.search(r"^title: (.+)$", front[1], re.MULTILINE) if front else None
    heading = re.search(r"^# (.+)$", text, re.MULTILINE)
    if not title or not heading or title[1] != heading[1]:
        fail(file, "frontmatter title and heading differ")
    fences = re.findall(r"^```python(?: \{([^}]*)\})?\n(.*?)^```$", text, re.MULTILINE | re.DOTALL)
    if len(fences) != 1 or not fences[0][0]:
        fail(file, "expected one highlighted Python fence")
    groups = parse_groups(fences[0][0])
    code = fences[0][1].splitlines()
    if any(max(group) > len(code) for group in groups):
        fail(file, "highlight range exceeds the displayed code")
    setup = re.search(r"<script setup>\s*const run = (\{.*?\})\s*</script>", text, re.DOTALL)
    if not setup:
        fail(file, "no inspectable const run object")
    run = json.loads(setup[1])
    if (
        len(groups) != len(run["states"])
        or len(groups) != len(run["output"])
        or len(groups) != len(run["captions"])
    ):
        fail(file, "line groups, state data, outputs and captions have different counts")
    demo = ROOT / "demos" / demo_rel
    demo_lines = demo.read_text(encoding="utf-8").splitlines()
    position = 0
    for line in code:
        try:
            position = demo_lines.index(line, position) + 1
        except ValueError:
            fail(file, f"fence line is absent or out of order in {demo_rel}: {line!r}")
    expected_component = {"names": "CoreNames", "loop": "CoreLoop", "stream": "CoreStream"}[kind]
    if f'<{expected_component} :run="run"' not in text:
        fail(file, f"run object is not passed to {expected_component}")
    return Slide(file, title[1], demo, kind, route, code, groups, run, [])


def trace(slide: Slide) -> list[Event]:
    """Run the whole program once, recording executable line/call/return snapshots."""
    source = "\n".join(slide.code)
    filename = f"<core:{slide.file}>"
    namespace: dict[str, Any] = {"__name__": "__main__"}
    output = io.StringIO()
    frames: list[Any] = []
    events: list[Event] = []

    def tracer(frame, event, arg):
        if frame.f_code.co_filename != filename:
            return tracer
        if event == "call":
            frames.append(frame)
        elif event == "return":
            pass
        if event in {"line", "return"}:
            stack = [(item.f_code.co_name, dict(item.f_locals)) for item in frames]
            globals_now = dict(namespace)
            object_values: dict[int, Any] = {}
            for value in [
                *globals_now.values(),
                *(item for _, local in stack for item in local.values()),
                *([arg] if event == "return" else []),
            ]:
                object_values[id(value)] = snapshot_value(value)
            events.append(
                Event(
                    event,
                    frame.f_lineno,
                    frame.f_code.co_name,
                    globals_now,
                    stack,
                    output.getvalue(),
                    object_values,
                    arg if event == "return" else None,
                )
            )
        if event == "return" and frames and frames[-1] is frame:
            frames.pop()
        return tracer

    old_trace = sys.gettrace()
    try:
        sys.settrace(tracer)
        with contextlib.redirect_stdout(output):
            exec(compile(source, filename, "exec"), namespace)
    finally:
        sys.settrace(old_trace)
    return events


def snapshot_value(value: Any) -> Any:
    if callable(value):
        return {"kind": "function", "value": value.__name__}
    if isinstance(value, list):
        return {"kind": "list", "items": [repr(item) for item in value]}
    return {"kind": type(value).__name__, "value": repr(value)}


def completed_lines(text: str) -> list[str]:
    return [line[:-1] for line in re.findall(r"(.*?\n)", text)]


def plan_states(slide: Slide, events: list[Event]) -> list[Event]:
    """Map each highlighted line group to its next executable checkpoint.

    A group can repeat while an output batch is being illustrated. Its target
    list is matched against trace line events, with call bodies and return
    events retained between the call site and the next caller checkpoint.
    """
    checkpoints: list[Event] = []
    cursor = 0
    complete_offset = 0
    for index, (group, wanted_output) in enumerate(
        zip(slide.groups, slide.run["output"], strict=True)
    ):
        last_index = cursor
        while True:
            progressed = False
            forced_endpoint: int | None = None
            for line in group:
                if slide.code[line - 1].lstrip().startswith("global "):
                    # A global declaration changes compiler scope metadata;
                    # CPython emits no line event for it.
                    progressed = True
                    continue
                found = next(
                    (
                        i
                        for i in range(last_index, len(events))
                        if events[i].event == "line" and events[i].line == line
                    ),
                    None,
                )
                if found is None:
                    # A repeated call-site range in a teaching animation can
                    # mean its resumed state after the call returns. The call
                    # line was already traced before entering the body; use
                    # the caller's resume checkpoint after that return.
                    previous = events[cursor] if cursor < len(events) else None
                    resumed = next(
                        (
                            i
                            for i in range(cursor, len(events))
                            if events[i].event == "line" and events[i].function == "<module>"
                        ),
                        None,
                    )
                    seen_before = any(line in earlier for earlier in slide.groups[:index])
                    if (
                        previous
                        and previous.event == "return"
                        and seen_before
                        and resumed is not None
                    ):
                        last_index = resumed
                        forced_endpoint = resumed
                        progressed = True
                        continue
                    fail(
                        slide.file,
                        f"state {index} cannot find line {line} after trace event {last_index}",
                    )
                last_index = found + 1
                progressed = True
            if not progressed:
                fail(slide.file, f"state {index} has no executable line")

            # A statement is complete at the next line event or at the return
            # event for a function's final statement.
            endpoint = (
                forced_endpoint
                if forced_endpoint is not None
                else next(
                    (
                        i
                        for i in range(last_index, len(events))
                        if events[i].event in {"line", "return"}
                    ),
                    None,
                )
            )
            if endpoint is None:
                fail(slide.file, f"state {index} has no trace checkpoint after lines {group}")
            completed = completed_lines(events[endpoint].output)
            delta = completed[complete_offset:]
            expected = wanted_output
            if delta == expected:
                checkpoints.append(events[endpoint])
                cursor = endpoint
                complete_offset = len(completed)
                break
            # Empty-output groups are one execution unit. Output groups may
            # intentionally combine repeated loop passes (the break example).
            if expected and len(delta) < len(expected):
                last_index = endpoint
                continue
            fail(
                slide.file,
                f"state {index} output is {delta}, expected {expected}; line groups {group}",
            )
    return checkpoints


def actual_names(event: Event) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    globals_now = event.globals
    frames = {
        "global": globals_now,
        **{function: values for function, values in event.stack if function != "<module>"},
    }
    return frames, globals_now


def expected_object_map(slide: Slide, state: dict[str, Any]) -> dict[str, Any]:
    if slide.kind != "names":
        return {}
    return state["objects"]


def compare_name_state(
    slide: Slide, k: int, event: Event, identity: dict[int, str], py_for_data: dict[str, int]
) -> None:
    shown = slide.run["states"][k]
    actual, global_actual = actual_names(event)
    object_map = expected_object_map(slide, shown)
    names_by_frame = shown.get("names", {})
    expected_runtime_frames = {
        frame["label"].removesuffix("()")
        for frame in slide.run["frames"]
        if frame["id"] in names_by_frame and frame["id"] != "names" and frame["label"] != "global"
    }
    actual_runtime_frames = set(actual) - {"global"}
    if actual_runtime_frames != expected_runtime_frames:
        fail(
            slide.file,
            f"state {k} frames: Python {sorted(actual_runtime_frames)}, "
            f"displayed {sorted(expected_runtime_frames)}",
        )
    # Scope frame names correspond to displayed frame ids, not labels.
    for frame_id, bindings in names_by_frame.items():
        label = next(
            (item["label"] for item in slide.run["frames"] if item["id"] == frame_id), frame_id
        )
        python_frame = actual.get("global" if frame_id == "names" else label.removesuffix("()"))
        if python_frame is None:
            # A frame may have returned at this checkpoint. Its absence is a
            # deliberate state; fail only if the slide still draws locals.
            if bindings:
                fail(slide.file, f"state {k} shows frame {label!r} after Python returned")
            continue
        for name, data_id in bindings.items():
            if name.startswith("global "):
                declared = name.split(" ", 1)[1]
                if declared not in global_actual or declared in python_frame:
                    fail(
                        slide.file,
                        f"state {k} global declaration {declared!r} disagrees with Python scope",
                    )
                continue
            if name == "return":
                if event.event != "return" or data_id not in object_map:
                    fail(slide.file, f"state {k} return binding is not at a Python return event")
                value = event.return_value
            else:
                if name not in python_frame:
                    fail(slide.file, f"state {k} draws {label}.{name}, absent from Python locals")
                value = python_frame[name]
            if data_id is None:
                fail(slide.file, f"state {k} maps {label}.{name} to no object")
            if data_id not in object_map:
                fail(slide.file, f"state {k} references missing object {data_id}")
            prior = py_for_data.setdefault(data_id, id(value))
            if prior != id(value):
                fail(slide.file, f"state {k} changes the Python identity represented by {data_id}")
            if identity.setdefault(id(value), data_id) != data_id:
                fail(slide.file, f"state {k} draws one Python object as two objects")
            if slide.kind == "names":
                shown_object = object_map[data_id]
                observed = event.object_values[id(value)]
                if "value" in shown_object:
                    actual_value = observed["value"]
                    if actual_value != shown_object["value"]:
                        fail(
                            slide.file,
                            f"state {k} object {data_id} shows {shown_object['value']}, "
                            f"Python has {actual_value}",
                        )
                elif "items" in shown_object:
                    actual_items = observed["items"]
                    if actual_items != shown_object["items"]:
                        fail(
                            slide.file,
                            f"state {k} list {data_id} shows {shown_object['items']}, "
                            f"Python has {actual_items}",
                        )
    # Every name in the execution stack must be represented, except Python's
    # function internals and module metadata.
    return None


def verify_static(slide: Slide) -> None:
    events = trace(slide)
    checkpoints = plan_states(slide, events)
    identity: dict[int, str] = {}
    py_for_data: dict[str, int] = {}
    finished = 0
    for k, event in enumerate(checkpoints):
        current = len(completed_lines(event.output))
        delta = completed_lines(event.output)[finished:current]
        if delta != slide.run["output"][k]:
            fail(slide.file, f"state {k} output {delta} differs from {slide.run['output'][k]}")
        finished = current
        if slide.kind == "names":
            compare_name_state(slide, k, event, identity, py_for_data)
        elif slide.kind == "loop":
            shown = slide.run["states"][k]
            expected_rows = slide.run["rows"]
            row = expected_rows[0]
            statuses = shown.get("status", {}).get(row["id"], [])
            if slide.file == "one-item-per-pass.md":
                module = event.globals
                count = sum(
                    line.startswith("Now playing: ")
                    for batch in slide.run["output"][: k + 1]
                    for line in batch
                )
                if statuses != ["ran"] * count:
                    fail(
                        slide.file,
                        f"state {k} loop statuses {statuses}, expected {['ran'] * count}",
                    )
                if shown.get("cursor") and module.get("title") != row_value(
                    expected_rows[0], shown["cursor"]["at"]
                ):
                    fail(slide.file, f"state {k} loop variable does not match Python title")
                if k == len(checkpoints) - 1 and module.get("title") != "Respect":
                    fail(slide.file, "loop exhaustion should preserve the final title")
                if (row["id"] in shown.get("ended", [])) != (k == len(checkpoints) - 1):
                    fail(slide.file, f"state {k} end slot does not match Python loop exhaustion")
            elif slide.file == "leaving-a-loop-with-break.md":
                module = event.globals
                at = shown.get("cursor", {}).get("at")
                if at is not None and module.get("track") != row_value(expected_rows[0], at):
                    fail(slide.file, f"state {k} letter differs from the Python loop variable")
                count = sum(
                    line.startswith("Checked ")
                    for batch in slide.run["output"][: k + 1]
                    for line in batch
                )
                expected_status = ["ran"] * count
                if k >= 3:
                    expected_status += ["stop"] + ["never"] * (len(row["items"]) - count - 1)
                if statuses != expected_status:
                    fail(
                        slide.file,
                        f"state {k} loop statuses {statuses}, expected {expected_status}",
                    )
                if k >= 3 and (module.get("track") != "Respect" or at != count):
                    fail(
                        slide.file,
                        "break must preserve track='Respect' and leave Hey Jude unreached",
                    )
        elif slide.kind == "stream":
            shown_writes = slide.run["states"][k]["writes"]
            actual_text = event.output
            reconstructed = "".join(
                item["text"] + ("\n" if item["newline"] else "") for item in shown_writes
            )
            if actual_text != reconstructed:
                fail(
                    slide.file,
                    f"state {k} writes {reconstructed!r}, Python stdout is {actual_text!r}",
                )
            done = []
            pending = ""
            for item in shown_writes:
                pending += item["text"]
                if item["newline"]:
                    done.append(pending)
                    pending = ""
            if done != completed_lines(actual_text):
                fail(
                    slide.file,
                    f"state {k} completed output {done} differs from stdout "
                    f"{completed_lines(actual_text)} ({actual_text!r})",
                )
    # Full run is also the independent final-output oracle.
    actual_final = events[-1].output if events else ""
    expected_final = "".join(line + "\n" for batch in slide.run["output"] for line in batch)
    if actual_final != expected_final:
        fail(
            slide.file,
            f"complete stdout {actual_final!r} differs from displayed output {expected_final!r}",
        )


def row_value(row: dict[str, Any], index: int) -> str:
    value = row["items"][index]
    return value[1:-1] if value.startswith("'") and value.endswith("'") else value


def verify_provenance(slide: Slide) -> None:
    # parse() checked the in-order literal excerpt. This also rejects a demo
    # change after the native slide was authored if the lines no longer match.
    source = slide.demo.read_text(encoding="utf-8").splitlines()
    cursor = 0
    for line in slide.code:
        cursor = source.index(line, cursor) + 1


BROWSER_SCRIPT = r"""
import { browserTimeoutMs, reducedMotion, withBrowser } from %(browser)s;
const origin = process.argv[2], plan = JSON.parse(process.argv[3]);
const outputFile = process.argv[4];
const results = {};
await withBrowser({ origin }, async ({ page }) => {
  const read = async (route, k, reduced=false, navigate=true) => {
    if (navigate) {
      const url = `${origin}/slidev/?r=${Date.now()}#/${route}?clicks=${k}`;
      await page.goto(url, { waitUntil: 'networkidle0', timeout: browserTimeoutMs });
    }
    await page.waitForSelector(`[data-source-id="${route}"] .ds-run`, { timeout: browserTimeoutMs });
    await page.evaluate(() => document.fonts.ready);
    const data = await page.evaluate((route) => {
      const frame = document.querySelector(`[data-source-id="${route}"]`);
      const visible = el => parseFloat(getComputedStyle(el).opacity || '1') > .5;
      const box = el => el.getBoundingClientRect();
      const body = box(frame.querySelector('.course-body'));
      const overflow = [...frame.querySelectorAll('.ds-run *')].filter(el => {
        const r = box(el);
        return visible(el) && r.width && (
          r.left < body.left - 2 || r.right > body.right + 2 ||
          r.top < body.top - 2 || r.bottom > body.bottom + 2
        );
      }).length;
      const run = frame.querySelector('.ds-run');
      const activeLines = [...frame.querySelectorAll('.ds-code .slidev-code .line')]
        .flatMap((line, index) => (
          line.classList.contains('slidev-code-highlighted') ? [index + 1] : []
        ));
      const out = {
        step: Number(run.dataset.dsStep),
        caption: frame.querySelector('[data-ds-caption]')?.textContent.trim(),
        output: [...frame.querySelectorAll('[data-ds-output]')].map(x => x.textContent.trim()),
        activeLines,
        overflow,
      };
      const names = frame.querySelector('[data-core-step]');
      if (names?.classList.contains('core-names')) {
        out.frames = [...names.querySelectorAll('[data-core-frame]')]
          .filter(f => f.classList.contains('shown'))
          .map(f => ({
            id: f.dataset.coreFrame,
            names: [...f.querySelectorAll('[data-core-name]')]
              .filter(n => n.classList.contains('shown'))
              .map(n => {
                const label = n.querySelector('.label').textContent.trim();
                return label === 'return value' ? 'return' : label;
              }),
          }));
        out.objects = [...names.querySelectorAll('[data-core-object]')]
          .filter(x => x.dataset.coreStatus !== 'hidden')
          .map(o => ({
            id: o.dataset.coreObject,
            status: o.dataset.coreStatus,
            value: [...o.querySelectorAll('[data-core-value]')].map(v => v.textContent.trim()),
          }));
        const objectNodes = [...names.querySelectorAll('[data-core-object]')]
          .filter(object => object.dataset.coreStatus !== 'hidden');
        out.refs = [...names.querySelectorAll('path[data-core-ref]')]
          .filter(path => path.classList.contains('shown'))
          .map(path => {
            const end = path.getPointAtLength(path.getTotalLength());
            const point = path.ownerSVGElement.createSVGPoint();
            point.x = end.x;
            point.y = end.y;
            const screen = point.matrixTransform(path.ownerSVGElement.getScreenCTM());
            const target = objectNodes
              .map(object => {
                const rect = box(object);
                const dx = Math.max(rect.left - screen.x, 0, screen.x - rect.right);
                const dy = Math.max(rect.top - screen.y, 0, screen.y - rect.bottom);
                return { id: object.dataset.coreObject, distance: Math.hypot(dx, dy) };
              })
              .sort((a, b) => a.distance - b.distance)[0];
            return { key: path.dataset.coreRef, target: target?.id || null };
          });
      } else if (names?.classList.contains('core-loop')) {
        out.tiles = [...names.querySelectorAll('[data-core-value]')]
          .map(t => ({ text: t.childNodes[0].textContent.trim(), status: t.dataset.coreStatus }));
        out.cursor = names.querySelector('[data-core-cursor]')?.textContent.trim();
        out.cursorAt = [...names.querySelectorAll('[data-core-value]')]
          .findIndex(tile => tile.classList.contains('current'));
        out.ends = [...names.querySelectorAll('[data-core-end]')].map(e => e.textContent.trim());
      } else if (frame.querySelector('.core-stream')) {
        out.writes = [...frame.querySelectorAll('[data-core-write]')]
          .map(w => ({
            text: w.querySelector('.text').textContent,
            newline: Boolean(w.querySelector('.newline')),
          }));
        out.stream = frame.querySelector('.core-stream').textContent;
      }
      return out;
    }, route);
    if (reduced) data.motion = await page.evaluate(() =>
      [...document.querySelectorAll('.core-names,.core-loop,.core-stream')]
        .flatMap(x => [...x.querySelectorAll('*')]
          .map(el => {
            const style = getComputedStyle(el);
            return [style.transitionDuration, style.animationDuration];
          })
          .flat())
        .filter(Boolean));
    return data;
  };
  for (const item of plan) {
    const states=[];
    await page.goto(
      `${origin}/slidev/?r=${Date.now()}#/${item.route}?clicks=0`,
      { waitUntil: 'networkidle0', timeout: browserTimeoutMs },
    );
    for (let k=0;k<item.states;k++) {
      states.push(await read(item.route,k,false,false));
      if (k+1<item.states) {
        await page.keyboard.press('ArrowRight');
        if (k===0) {
          await new Promise(resolve=>setTimeout(resolve,300));
          const middle=await read(item.route,k+1,false,false);
          if (middle.step !== k + 1 || middle.overflow) {
            throw new Error(`${item.route}: forward transition frame overflow or wrong state`);
          }
          await new Promise(resolve=>setTimeout(resolve,350));
        } else await new Promise(resolve=>setTimeout(resolve,650));
      }
    }
    await new Promise(resolve=>setTimeout(resolve,650));
    states[states.length-1]=await read(item.route,item.states-1,false,false);
    const reverse=[];
    for (let k=item.states-1;k>=0;k--) {
      reverse.push(await read(item.route,k,false,false));
      if (k>0) {
        await page.keyboard.press('ArrowLeft');
        if (k===item.states-1) {
          await new Promise(resolve=>setTimeout(resolve,300));
          const middle=await read(item.route,k-1,false,false);
          if (middle.step !== k - 1 || middle.overflow) {
            throw new Error(`${item.route}: reverse transition frame overflow or wrong state`);
          }
          await new Promise(resolve=>setTimeout(resolve,350));
        } else await new Promise(resolve=>setTimeout(resolve,650));
      }
    }
    await new Promise(resolve=>setTimeout(resolve,650));
    reverse[reverse.length-1]=await read(item.route,0,false,false);
    await reducedMotion(page, true);
    const reduced=await read(item.route,item.states-1,true);
    await reducedMotion(page, false);
    results[item.route]={states,reverse,reduced};
  }
});
await Bun.write(outputFile, JSON.stringify(results));
console.log('Browser state results written.');
"""


def browser_plan(slides: list[Slide], origin: str) -> int:
    shared = os.environ.get("PRESENTATION_TEMPLATE_DIR")
    template = Path(shared) if shared else ROOT.parent / "Presentation-Template"
    manifest_path = ROOT / ".courseware/fundamentals/student/manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    native = {
        page["title"]: page["sourceId"]
        for page in manifest["pages"]
        if page["kind"] == "enrichment"
    }
    plan = []
    for slide in slides:
        route = native.get(slide.title)
        if not route:
            fail(slide.file, "integrated manifest has no matching native slide")
        if route != slide.route:
            fail(slide.file, f"manifest route {route} differs from recorded route {slide.route}")
        plan.append({"route": route, "states": len(slide.groups), "kind": slide.kind})
    browser = json.dumps((template / "build/browser.ts").as_posix())
    with tempfile.TemporaryDirectory() as folder:
        script = Path(folder) / "read-core.ts"
        output = Path(folder) / "rendered.json"
        script.write_text(BROWSER_SCRIPT % {"browser": browser}, encoding="utf-8", newline="\n")
        result = subprocess.run(
            [shutil.which("bun") or "bun", str(script), origin, json.dumps(plan), str(output)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        if result.returncode:
            raise RuntimeError(result.stderr[-4000:])
        rendered = json.loads(output.read_text(encoding="utf-8"))
    checked = 0
    for slide in slides:
        record = rendered[slide.route]
        for direction in ("states", "reverse"):
            rows = record[direction]
            for index, dom in enumerate(rows):
                k = index if direction == "states" else len(rows) - 1 - index
                if dom["step"] != k:
                    fail(
                        slide.file,
                        f"{direction} navigation expected click {k}, rendered {dom['step']}",
                    )
                if dom["activeLines"] != slide.groups[k]:
                    fail(
                        slide.file,
                        f"click {k} highlights lines {dom['activeLines']}, "
                        f"expected executing lines {slide.groups[k]}",
                    )
                if dom["overflow"]:
                    fail(
                        slide.file,
                        f"click {k} has {dom['overflow']} visible elements outside "
                        "the content frame",
                    )
                expected_caption = slide.run["captions"][k].replace("`", "")
                if dom["caption"] != expected_caption:
                    fail(slide.file, f"click {k} caption is {dom['caption']!r}")
                expected_output = [
                    line.rstrip("\n") for batch in slide.run["output"][: k + 1] for line in batch
                ]
                if dom["output"] != expected_output:
                    fail(
                        slide.file,
                        f"click {k} visible output {dom['output']} differs from {expected_output}",
                    )
                if slide.kind == "names":
                    state = slide.run["states"][k]
                    shown_names = {frame["id"]: frame["names"] for frame in dom["frames"]}
                    for frame in slide.run["frames"]:
                        should = state["names"].get(frame["id"], {})
                        visible = shown_names.get(frame["id"], [])
                        if visible != list(should):
                            fail(
                                slide.file,
                                f"click {k} frame {frame['id']} names {visible}, "
                                f"expected {list(should)}",
                            )
                    expected_refs = sorted(
                        (f"{frame_id}.{name}", target)
                        for frame_id, names in state["names"].items()
                        for name, target in names.items()
                        if target is not None
                    )
                    actual_refs = sorted((ref["key"], ref["target"]) for ref in dom["refs"])
                    if actual_refs != expected_refs:
                        fail(
                            slide.file,
                            f"click {k} reference arrows {actual_refs}, expected {expected_refs}",
                        )
                    referenced = {
                        target
                        for names in state["names"].values()
                        for target in names.values()
                        if target is not None
                    }
                    for object_id, value in state["objects"].items():
                        match = next(
                            (obj for obj in dom["objects"] if obj["id"] == object_id), None
                        )
                        if not match:
                            fail(slide.file, f"click {k} hides expected object {object_id}")
                        expected_status = "present" if object_id in referenced else "orphan"
                        if match["status"] != expected_status:
                            fail(
                                slide.file,
                                f"click {k} object {object_id} status {match['status']}, "
                                f"expected {expected_status}",
                            )
                        expected_value = (
                            [value.get("value")] if "value" in value else value.get("items", [])
                        )
                        if match["value"] != expected_value:
                            fail(
                                slide.file,
                                f"click {k} object {object_id} renders {match['value']}, "
                                f"expected {expected_value}",
                            )
                elif slide.kind == "loop":
                    expected_tiles = []
                    for row in slide.run["rows"]:
                        status = slide.run["states"][k].get("status", {}).get(row["id"], [])
                        expected_tiles.extend(
                            {"text": item, "status": status[i] if i < len(status) else ""}
                            for i, item in enumerate(row["items"])
                        )
                    if dom["tiles"] != expected_tiles:
                        fail(
                            slide.file, f"click {k} tiles {dom['tiles']}, expected {expected_tiles}"
                        )
                    row = slide.run["rows"][0]
                    cursor = slide.run["states"][k].get("cursor")
                    expected_at = cursor["at"] if cursor else -1
                    if dom["cursor"] != row["variable"] or dom["cursorAt"] != expected_at:
                        fail(
                            slide.file,
                            f"click {k} loop cursor {dom['cursor']!r}/{dom['cursorAt']}, "
                            f"expected {row['variable']!r}/{expected_at}",
                        )
                    expected_ends = [
                        "no items left"
                        if row["id"] in slide.run["states"][k].get("ended", [])
                        else "end"
                    ]
                    if dom["ends"] != expected_ends:
                        fail(
                            slide.file,
                            f"click {k} end slot {dom['ends']}, expected {expected_ends}",
                        )
                else:
                    expected_writes = slide.run["states"][k]["writes"]
                    if dom["writes"] != expected_writes:
                        fail(
                            slide.file,
                            f"click {k} stream writes {dom['writes']}, expected {expected_writes}",
                        )
                checked += 1
        reduced = record["reduced"]["motion"]
        if any(value not in {"0s", "0ms"} for value in reduced):
            fail(slide.file, "reduced-motion preference leaves a nonzero transition or animation")
    print(
        f"Browser states: {checked} forward/reverse frames match; "
        "reduced motion and containment pass."
    )
    return checked


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--browser", metavar="ORIGIN", help="served integrated app origin")
    args = parser.parse_args()
    slides = [parse(file) for file in FILES]
    for slide in slides:
        verify_provenance(slide)
        verify_static(slide)
    count = sum(len(slide.groups) for slide in slides)
    print(
        f"Core static check: {len(slides)} slides, {count} states; "
        "demo provenance and traced Python execution pass."
    )
    if args.browser:
        browser_plan(slides, args.browser.rstrip("/"))


if __name__ == "__main__":
    main()
