# WP8b : factual slide corrections

Completed on 2026-10-17. Branch: `t3/fix-slide-factual-errors`.
Implementation model: GPT-6-astra. Base: `65dbee6`.
Read `AGENTS.md`, `build/plan.md`, `build/tasks.md` and `build/notes/wp5.md`.
Only slides, demos and this report changed. No push or merge.

## Findings and commits

| Finding | Commit | Resolution |
|---|---|---|
| F07, F19 | `86ee554` | Module 02 uses names bound to objects, including Multiple Assignment and Python Numbers. Rebinding does not necessarily allocate an object; `del` removes bindings. Removed the cross-language aliasing wording. Slice `[2:5]` is third through fifth in slide and demo; `sqrt` accepts zero. Logarithm domains remain strictly positive. |
| F08, F09 | `7d756a5` | Module 03 describes `pop(index=-1)` and keyword-only sort options. Dictionary keys and tuple keys are explained through hashability, with a tuple containing a list as the counterexample. The tuple-deletion explanation also distinguishes binding removal from object lifetime. |
| F17 | `d90c3d8` | Module 05 says rebinding a global name requires `global`; mutation such as `append` does not. |
| F10 | `6ec33a6` | Module 06 diagram and summary distinguish script-directory lookup from current-directory lookup in REPL and `-m`. PYTHONPATH follows the first directory. Windows command explicitly labelled CMD; removed trailing empty path component. Diagram retains rectangular outer nodes. |
| Optional exception testing | `4a13ab7` | Module 08 adds Testing an Expected Exception with demo11. It explains the block and failure conditions, uses annotated neutral division, and tests `ZeroDivisionError`. |
| F18 | `11bbc38` | Module 09 says buffering zero is binary-only and line buffering is for text mode. |
| F05 | `6c30dea` | One SQL slide after Retrieving Data, with matching demo07, covers COUNT, SUM, COALESCE, WHERE, GROUP BY, ORDER BY and a bound `?` parameter against Cars. It closes the connection in `finally`. Former demos07–11 and their pills are now08–12. |
| F26 | `b9e14a7` | Module 12 says annotations can go stale without runtime enforcement; mypy detects contradictions. |
| F11, F12 | `d2e7756` | Module 13 separates third-party pytest and the Exercise 5 install command from standard-library modules. Summary distinguishes isoformat formatting from fromisoformat parsing, retaining strftime/strptime. Matching functions include fullmatch, with identical new demo/slide examples. |

## Python 3.14 verification

`uv sync` created the locked environment with CPython 3.14.3, pytest 9.1.1,
ruff 0.16.3 and mypy 2.3.1. Ran assertions and subprocess probes under that
interpreter, not an older system Python.

- F07: `a=[]; b=a; del a` leaves `b == []`. Rebinding one integer alias leaves the other binding unchanged.
- F19: `"Hello World!"[2:5]` prints `llo`; `math.sqrt(0)` returns `0.0`.
- F08: `[10,20,30].pop(1)` returns20; default pop returns the last item. Out-of-range pop raises `IndexError: pop index out of range`. Positional sort options raise `TypeError: sort() takes no positional arguments`. Keyword sorting by length in reverse yields `['bbb', 'cc', 'a']`.
- F09: tuple key lookup returns2341; `hash(("Albert", []))` raises `TypeError: unhashable type: 'list'`.
- F17: a function mutates a module list without `global`; a second function rebinds it with `global`.
- F10: subprocess script in a subdirectory reports that subdirectory as `sys.path[0]`; `-m sub.probe` reports cwd; interactive `-i` reports the empty string, which represents cwd.
- F18: unbuffered text raises `ValueError: can't have unbuffered text I/O`; unbuffered binary returns a FileIO and reads bytes. Text buffering1 reports `line_buffering == True`.
- F05: created the existing Cars table with demo03, then ran demo07. Exact output:

```text
('Bentley', 1, 350000)
('Mercedes', 1, 57127)
('Audi', 1, 52642)
```

An ungrouped aggregate with no qualifying rows returns `(0, None, 0)` for
`COUNT(*)`, `SUM(Price)`, `COALESCE(SUM(Price), 0)`. A grouped query with no
qualifying groups returns no rows; COALESCE does not manufacture a group.
All twelve Module 10 demos also executed in numeric order in a fresh temporary
directory, with exit code0. Pills and filenames were checked as gap-free01–12.

- F11: pytest is absent from `sys.stdlib_module_names`; the environment imports the separately installed pytest9.1.1.
- F12: `datetime(2026,8,15,12,30).isoformat()` returns `2026-08-15T12:30:00`; `fromisoformat` round-trips it. Fullmatch examples print `True` for `hello` and `False` for `hello!`.
- F26: `price: float = "free"` runs and prints `free`; mypy exits1 with an incompatible-assignment diagnostic.
- Optional demo: `uv run pytest -q demos/08-exceptionhandling/11_pytest_raises.py` gives `1 passed`.
- Ran changed string and regex demos; their output matches the comments. Compared both new full slide code fences byte-for-byte with their demo files.

Scratch verification scripts remain at `%TEMP%/wp8b-verify.py` and
`%TEMP%/wp8b-artifacts.py`. Temporary databases and drift fixtures were isolated
outside the repository. An initial artifact-check invocation used Windows'
default text encoding and failed to find the middle-dot pills; rerunning with
explicit UTF-8 passed. This was a verification-harness issue, not a deck issue.

## Gates

All final gates passed:

- `uv sync`.
- `uv run python build/check-fences.py`:380 fences,336 complete modules,44 snippets; no problems.
- `uv run ruff check .`:all checks passed.
- `uv run python -m compileall -q demos/02-variablesanddatatypes demos/08-exceptionhandling demos/10-python-database-access demos/13-appendix-libraries`:exit0.
- From this worktree's `build/`, with `PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/Presentation-Template`, `bun run C:/Git/courseWare/Presentation-Template/build/build.ts --skip-lint`:PDF/HTML/bookmarks generated,235 authored slides.
- Then separately `bun run C:/Git/courseWare/Presentation-Template/build/lint-slides.ts`:All slides within budget. No lint warnings.
- All ten Mermaid root SVG viewBoxes start with `3 3`. The changed diagram is `mermaid-0f877e477878b53a1a4493fcac40873724662ef7.svg`, viewBox `3 3 1158.4375 88`.
- `git diff --check`:clean.

The PDF exporter emits its normal warning that local file access is enabled.
Generated PDF, HTML, caches and `build/site/dist/` are not committed.

## Coordinator-only changes

None required. No `ruff.toml` changes or new dependencies are needed. Existing
module directories already belong to the release allowlist. The coordinator can
mark these findings complete in shared tracking notes; those files were not edited.
