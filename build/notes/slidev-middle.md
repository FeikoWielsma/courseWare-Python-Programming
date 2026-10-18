# Slidev middle modules package

Recorded 2026-10-18. Native animated slides for modules 06, 07 and 08, in the
style the trainer approved for the Data Structures pilot
([slidev-data-structures.md](slidev-data-structures.md)) and used by the core
package ([slidev-core.md](slidev-core.md)) : stationary code with an active
line, moving values and references, reversible click steps. Author checks were
kept small on purpose; detailed verification belongs to Luna and the
coordinator.

## What the package adds

Six native slides, two per module, each beside the canonical slide it
animates. All use the pilot's `DataStructuresRun` shell. Module 06 reuses
`CoreNames`; two new visuals serve 07 and 08 :

| Component | Role |
| --- | --- |
| `MiddleComprehension.vue` | The source list (one row, or inner lists inside an outer one), the loop variable as a tag over its item (and a second tag over the inner list for two `for` clauses), the `True`/`False` result of the `if` under each tested item, and the new list. An added item moves from its source cell into the next slot : the same object, now in two lists |
| `MiddleExceptions.vue` | Frames (`<module>`, one call) listing the clauses of their `try` statement; the exception object as one card beside the clause it has reached. The card moves clause to clause and up to the caller when a call ends; clauses show `raised`, `matches`, `not checked` or `skipped` on their border |

Each component's header comment documents its state schema. Every slide keeps
its data as one JSON object in `<script setup>` (`const run = {...}`).

## Insertion table

| Module | Insert after (existing title) | Native file (`src/slidev/middle/`) | States | Clicks | Demo | Layout | Visual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `06-modules` | `import Statement` | `importing-a-module.md` | 6 | 5 | `06-modules/01_importmodule.py` | side | `CoreNames` |
| `06-modules` | `Importing Names from a Package` | `importing-a-package.md` | 6 | 5 | `06-modules/07_implicitimport.py` (+ `reports/__init__.py`, `reports/shipping.py`) | side | `CoreNames` |
| `07-comprehensions` | `Filtered List Comprehension` | `filtering-into-a-new-list.md` | 6 | 5 | `07_comprehensions/demo02_comprehension_with_predicate.py` | stack | `MiddleComprehension` |
| `07-comprehensions` | `Flattening a List of Lists` | `two-for-clauses.md` | 7 | 6 | `07_comprehensions/demo03_nested_comprehensions.py` | stack | `MiddleComprehension` |
| `08-exception-handling` | `Typed Exception Handling` | `first-matching-handler.md` | 3 | 2 | `08-exceptionhandling/03_typedexceptionhandling.py` | side | `MiddleExceptions` |
| `08-exception-handling` | `Example try-finally` | `finally-while-propagating.md` | 6 | 5 | `08-exceptionhandling/07_tryfinally.py` | side | `MiddleExceptions` |

34 states, 28 clicks. Each target is a different source slide. Pages in the
scratch build (preamble and modules 06 to 08 only) : 6, 14, 24, 27, 45, 52 of
58; routes follow the shared `<module>-<n>-enhancement` scheme.

Add to `enrichments` in `build/slidev.config.ts` :

```ts
{ module: '06-modules', after: 'import Statement', file: 'src/slidev/middle/importing-a-module.md' },
{ module: '06-modules', after: 'Importing Names from a Package', file: 'src/slidev/middle/importing-a-package.md' },
{ module: '07-comprehensions', after: 'Filtered List Comprehension', file: 'src/slidev/middle/filtering-into-a-new-list.md' },
{ module: '07-comprehensions', after: 'Flattening a List of Lists', file: 'src/slidev/middle/two-for-clauses.md' },
{ module: '08-exception-handling', after: 'Typed Exception Handling', file: 'src/slidev/middle/first-matching-handler.md' },
{ module: '08-exception-handling', after: 'Example try-finally', file: 'src/slidev/middle/finally-while-propagating.md' },
```

## Provenance and code

- `importing-a-module`, `importing-a-package`, `finally-while-propagating`
  and `first-matching-handler` show their demo file whole, verbatim.
- `filtering-into-a-new-list` is lines 1, 8 and 9 of demo02;
  `two-for-clauses` is lines 1, 11 and 12 of demo03. Both are in-order,
  verbatim excerpts (the loop forms are on the canonical slide).
- Module 06 demos run from `demos/06-modules` (they import `shipping` and
  `reports` from there). `first-matching-handler` needs `somefile` to be
  absent from the working directory, as in the demo.

## How the states map to execution

As in the core package, **each range is what executes in that state** and the
last highlighted line is the active one; ranges repeat while one line does
several things. A checker needs trace semantics (line events, or the
comprehension's iterations), not prefix execution.

- `importing-a-module` `{1|1|3|4|6|8}` : state 0 is `shipping.py` running
  (its namespace filled), state 1 the binding of `shipping`. State 4 binds
  `delivery` to the same module object; `shipping.py` does not run again.
- `importing-a-package` `{1|1|1|3|5|7}` : state 0 is `reports/shipping.py`
  running inside the import in `__init__.py`; state 1 is `__init__.py`
  finishing, with `shipping` (the submodule, set by the import system) and
  `delivery_cost` in the package namespace; state 2 binds `reports`.
  Checked : `[n for n in vars(reports) if not n.startswith('__')]` is
  `['shipping', 'delivery_cost']` and all three `delivery_cost` names are one
  function object.
- `filtering-into-a-new-list` `{1|2|2|2|2|3}` : states 1 to 3 are one
  iteration each (`tested` holds the condition's result); state 4 binds the
  finished list. `csv_files[1] is filenames[2]` is `True`.
- `two-for-clauses` `{1|2|2|2|2|2|3}` : states 1 to 4 are one innermost
  iteration each, `cursor.row` and `cursor.item` the two loop variables;
  state 5 binds `flat`. `flat[2] is readings[1][0]` is `True`.
- `finally-while-propagating` `{8-9|2-3|4-5|9|10|11}` : state 0 enters the
  `try` and calls; state 1 is the division raising; state 2 the `finally`
  block (it prints); state 3 the call ending, the exception now at line 9 of
  the caller; state 4 the handler match; state 5 its block.
- `first-matching-handler` `{1-2|3|4}` : the raise, the first handler
  matching, its block. `OSError` would match too (`isinstance` is `True`);
  it is shown `not checked`.

Expected output, from running each demo (or excerpt) with `uv run python` :

| Slide | Output (per state with output) |
| --- | --- |
| `importing-a-module` | `4.95` (2), `0.0` (3), `50.0` (5) |
| `importing-a-package` | `4.95` (3), `0.0` (5) |
| `filtering-into-a-new-list` | `['sales.csv', 'stock.csv']` (5) |
| `two-for-clauses` | `[18.2, 19.6, 20.1, 21.8]` (6) |
| `first-matching-handler` | `The file does not exist` (2) |
| `finally-while-propagating` | `This always runs` (2), `Cannot divide by zero` (5) |

## Display choices

- A module object is drawn only once a name refers to it (states 0 of both
  module slides omit it, although it exists while its file runs), so it is
  never drawn dashed as if orphaned.
- The namespace of a module is a `CoreNames` frame labelled `module <name>`;
  the module object is a separate box, as in Python (object and namespace).
- Comprehension loop variables disappear when the list is bound : they are
  not visible after the comprehension. The caption does not dwell on it.
- In `finally-while-propagating` the `divide()` frame fades out when the call
  ends, so the final state shows only the module frame.
- Colours keep the pilot's meanings : teal for active or matching, red for
  where an exception was raised and for the exception card, dashed and muted
  for what does not run. A handled exception turns teal.

## Author checks (2026-10-18)

Course worktree `t3/cc400833` from `25941da`; shared toolchain
`C:/Git/courseWare/_worktrees/presentation-template-slidev` at `f4f9ca1`.

```bash
# Outputs and identities
cd demos/06-modules && uv run python 01_importmodule.py && uv run python 07_implicitimport.py
cd demos/08-exceptionhandling && uv run python 07_tryfinally.py && uv run python 03_typedexceptionhandling.py
# (excerpts of demo02 and demo03 run inline, with the `is` checks above)
# Scratch build : 00-preamble and 06 to 08 copied to build/slidev/scratch,
# build/slidev.config.ts enrichments temporarily replaced by the six above,
# then restored (no diff).
PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-slidev \
  bun run build/slidev.ts --slides-dir build/slidev/scratch
bun run build/slidev.ts --check-only
```

- Build : `3 modules, 49 source slides, 58 pages, 50 original code/output
  fences`; check `58 pages, 49 topics, 0 failures, 1 upstream warning`.
- One throwaway headless pass at 1280 by 800 visited every state of the six
  slides : `data-ds-step` matched the click, and no visible element left
  `.course-body`. Final frames of three slides were looked at.
- Not done, by request : per-state Python comparison, reverse and
  reduced-motion runs, PDF and click exports, a package checker.

## Findings for the coordinator

- `first-matching-handler` has three states : the demo has one raise and
  one handler. `05_multipleexceptions.py` (two exceptions, one tuple handler)
  could become a third 08 slide if wanted.
- Running a module directly (`__name__`) was not animated : it needs two runs
  of one file side by side, which the shell does not show.
- Several visuals leave space below them (most on `importing-a-module`).
- Nothing ships in the student bundle; the release workflow needs no change.
