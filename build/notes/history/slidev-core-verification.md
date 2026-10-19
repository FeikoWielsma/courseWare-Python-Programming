> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# Core animation verification

Independent verification of the native Slidev additions for modules 01, 02, 04
and 05. The checks cover the ten core slides, 65 states and 55 reveal clicks.

## Result

**Passed.** The displayed code excerpts match their named demos in order. A
single full Python execution per slide, traced at line and return events,
matches the authored state data and output. Browser checks match every state in
both directions, including code highlights, bindings, object values and arrow
targets. The selected final and click PDFs contain all ten final states and all
65 animation states.

No changes to the native slides, shared components, course config or canonical
course content were needed.

## Verification coverage

| Area | Evidence |
| --- | --- |
| Demo provenance | Every displayed Python line is an in-order excerpt from the demo named by the slide pill. |
| Executed line groups | The checker traces each complete program with `sys.settrace`; groups map to executed line, call and return events. Loop and call states are not prefix executions. |
| Names and objects | Every displayed binding matches the Python frame at that checkpoint. Object identity remains stable across states; values and list mutations match. Function frames appear on entry and disappear on return. The return slot matches the actual return value. |
| Local and global scope | `global y` is checked against the compiled function scope. The local `x` remains separate from global `x`; the global `y = 2` binds to the same displayed object as local `x = 2`. |
| Loops | The `for` states match the current filename, per-item status, exhaustion marker and final `filename == "prices.csv"`. The grouped break state prints six passes. After break, `letter == "i"`; later characters remain unreached. |
| Output | Every state’s new output matches traced stdout. `print(end="")` remains an open line in the write panel; the next `print()` completes that same line. The output panel correctly accumulates completed lines. |
| Source highlighting | Every browser state’s highlighted code lines match the slide’s execution group. |
| Browser states | All 65 states match after forward keyboard navigation and after reverse navigation, for 130 settled frames. Visible name/object bindings, object status, reference-arrow targets, loop cursor/status/end slots, output, captions and frame bounds are checked. |
| Motion | One forward and one reverse transition frame per slide were sampled mid-transition; all fit the content frame. Reduced-motion preference was applied on each slide and left no nonzero transition or animation duration. |
| PDF exports | The native exporter produced a 10-page final-state PDF and a 65-page click-state PDF for the ten selected core pages. Every page has nonempty extracted text and the expected slide title. Poppler rendered all 75 pages; final and click contact sheets were visually inspected for legibility, clipping and overlap. |

## Commands and inputs

Static package check and autodiscovery through the existing Python runner:

```powershell
uv run python build/slidev_checks/check_core.py
uv run python build/check-slidev-examples.py
```

The second command discovers and runs `check_core.py` with the existing Data
Structures and tuple checks. Its result was:

```text
Core static check: 10 slides, 65 states; demo provenance and traced Python execution pass.
Data Structures slides: 6 slides, 33 click states match Python.
Slidev examples: 5 list states and 3 tuple states match their demos.
```

The browser app came from the coordinator’s completed 257-page build at
`C:/Git/courseWare/Python-Programming/build/slidev/dist/student`. The manifest
confirmed the ten core headings and routes, 257 total pages and 226 source
topics. The student app and manifest were copied into this worktree’s ignored
`build/slidev/dist/`; the coordinator output and port 4188 were not changed.

```powershell
uv run python -m http.server 53011 --bind 127.0.0.1 --directory build/slidev/dist/student
$env:PRESENTATION_TEMPLATE_DIR='C:/Git/courseWare/_worktrees/presentation-template-slidev'
uv run python build/slidev_checks/check_core.py --browser http://127.0.0.1:53011
```

Browser result:

```text
Core static check: 10 slides, 65 states; demo provenance and traced Python execution pass.
Browser states: 130 forward/reverse frames match; reduced motion and containment pass.
```

The selected page range was `21,27,30,90,94,98,109,111,120,123`, taken from the
integrated manifest. The shared `exportBrowserPdf()` native exporter wrote
`core-final.pdf` with `withClicks=false` and `core-clicks.pdf` with
`withClicks=true` into ignored `build/slidev/core-pdf/`. The app was copied into
that isolated exporter directory; no full-course build was run.

The PDFs had 10 and 65 pages respectively. All page text matched the expected
slide-title grouping. Poppler rendered all pages at 640 pixels wide; the
contact sheets are in ignored `build/slidev/core-pdf/poppler-render/`.

## Remaining limits

- The `break and continue` demo’s `continue` loop remains unanimated. The core
  addition animates the `break` loop, as recorded in the package notes; the
  canonical demo and slide remain intact.
- These selected core PDFs contain no link annotations. This animation review
  checked page content and layout, not selected-export PDF navigation.
- The browser checks use the integrated static app and do not repeat the full
  course build, delivery gate, wheel checks or Mermaid/Pele audit.

## Files

- New package checker: `build/slidev_checks/check_core.py`.
- This verification record: `build/notes/history/slidev-core-verification.md`.
- Generated app copies, PDFs and raster review images remain ignored under
  `build/slidev/`.
