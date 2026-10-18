# Slidev rollout and teaching examples

Current integration record, 2026-10-18. Supersedes the stopping points and counts
in the earlier foundation, parity-audit and Functions reports. Scope and trainer
decisions: [adoption plan](slidev-migration-plan.md) and
[example map](engaging-examples.md).

## Delivered content

Music and photos recur through the fundamentals; SQLite uses a film watchlist
and Classes uses game characters. Functions starts with formatting a track's
duration, calls and returned values; annotations and docstrings follow those
concrete examples. IO introduces `with` before manual resource management.
The exercise solutions and starter contracts remain the Wordle spine. Two hint
descriptions were adjusted to match the new collection and character demos.

The canonical Markdown stays in `src/slides/`. There are 229 source topics and
294 canonical code/output fences: 242 Marp pages, or 275 Slidev pages including
33 native additions. The separate `libraries/` companion remains outside this
migration. Claude Opus 5.5 authored the native packages; the coordinator
integrated and retargeted them. Further Luna rounds were stopped at the
trainer's request.

| Module | Native slides | Authored states |
| --- | ---: | ---: |
| 01 Introduction | 1 | 6 |
| 02 Variables and Data Types | 2 | 14 |
| 03 Data Structures | 8 | 41 |
| 04 Control Flow | 3 | 17 |
| 05 Functions | 4 | 31 |
| 06 Modules | 2 | 12 |
| 07 Comprehensions | 2 | 13 |
| 08 Exceptions | 2 | 9 |
| 09 IO | 2 | 15 |
| 10 Database Access | 2 | 15 |
| 11 Classes | 3 | 22 |
| 12 Type Hinting | 1 | 7 |
| 13 Libraries | 1 | 5 |
| Total | 33 | 207 |

Insertion titles and files are in `build/slidev.config.ts`. Package notes:
[pilot](slidev-data-structures.md), [core](slidev-core.md),
[middle](slidev-middle.md), [stateful](slidev-stateful.md) and
[appendices](slidev-appendices.md). Code stays stationary while the active line,
values, references and output change; steps are reversible and respect reduced
motion. The original two Magic Move additions remain available.

## Verification

- Ordinary `bun run --cwd build build` builds and checks 275 frames with zero
  failures; canonical Marp layout lint also passes. The one known upstream
  FloatingVue patch warning remains. Fonts and assets load with external HTTP
  blocked during the browser check.
- All nine canonical Mermaid fences pass the Pele 1.6.0 audit: cache/version,
  source labels, nodes/edges, SVG geometry, rendered fonts and slide containment.
  No placeholders or missing images. Minimum diagram text is 11.5px on the
  normalized 1280px canvas.
- Existing static animation checks pass 68 traced core states, 33 Data
  Structures states and eight legacy snapshots. Middle programs match their
  demo excerpts and executed output; the stateful and appendix authors checked
  their displayed programs and output. This is not an independent Python trace
  audit of every authored middle/stateful checkpoint.
- A focused browser pass checks all 98 states in the six middle, seven stateful
  and two appendix additions: output, caption, stationary code geometry,
  forward/backward navigation, identical restored visual state and reduced
  motion. No page exceptions. Earlier live review inspected moving values and
  references; final review includes character health and the JSON round trip.
- The final `check:delivery` command passes against the packaged student app:
  136 forward/reverse core frames, reduced motion and containment; all 33 Data
  Structures states match Python in the browser; ordinary reveals and physical
  wheel forward/reverse, quick gestures, momentum, guards and slide boundaries
  pass. The student launcher on port 4188 also serves the fresh deck.
- The full PDF has 275 pages and 945 valid internal link destinations. A native
  click export includes all 33 additions and 207 states; a smaller 26-state
  review export covers return values, computed properties and both appendices.
  Poppler render review covers the filename-cleaning slide, Function Syntax,
  returned duration, read-only property, optional lookup and JSON round trip.
  File-position, watchlist transaction and character pages were also reviewed.
- Executed demo checks include the coordinator's 93 changed main demos
  (92 execute; the endless input example compiles), all stateful author demos,
  both appendix animation programs and the eight later collection refinements.
  Ruff is at zero; 544 Python fences parse or are classified snippets; all
  exercise slide references resolve. Seven appendix pytest cases pass, the
  deliberate broken formatter produces the quoted failure, and mypy reports
  the two intended type errors.
- All 13 Wordle stages pass tests, required type checks and scripted games;
  all 12 generated starters are current; 39 quiz questions / 25 code examples
  pass. The offline exercise site builds and its 13 module links, module-specific
  presentation helper and embedded hint preview work under `file://`.
  The new default wrapper also builds the exercises PDF/HTML successfully with
  `build -- --exercises --skip-lint`.
- Shared TypeScript and 14 converter/PDF/wheel/UnoCSS tests pass. Two unrelated
  courses retained identical PDF page counts and per-page text; details are in
  the shared worktree's `docs/slidev-regression.md`.

The browser checks found and fixed a wide stack return chip and a property error
message that resized the code column. Future output now reserves its final
layout from the first state. Build output is explicitly cleaned so obsolete
compiled chunks do not enter delivery. The fresh ZIP has 421 files, its PDF is
byte-identical to the canonical course PDF, and it contains no trainer notes,
comparison material or authoring sources.

After the full delivery gate, stack headings were moved above their columns.
The default build/layout check and 207-state native export were regenerated;
all five stack states pass forward/reverse and reduced-motion checks, a live
render confirms separated labels, and the physical wheel probe passes again.

Generated evidence is ignored under `build/slidev/`: `default-build.log`,
`final-delivery.log`, `media-browser.log`, `native-clicks.log`, QA images and
`dist/validation.json`. The final packaged-navigation result is also recorded in
the integration log.

## Default delivery and limits

`build` now routes to `build/course.ts`: public Slidev app, canonical final-state
PDF and `build/dist/Python-Programming-slides.zip`. `serve` starts native Slidev
development on port 3030. `build:marp` creates the named fallback PDF and HTML;
exercise and companion-course builds retain their existing paths. The student
launcher needs Python only and serves port 4188; Codespaces forwards that port.
The exercise site's primary module buttons point to the animated presentation;
embedded hint previews retain their direct-from-disk behavior.

Mermaid syntax currently goes through shared build-time Pele into inline SVG,
giving both engines the same offline diagrams. Slidev itself also supports
native Mermaid fences, options, configuration and a custom renderer hook;
switching to that hook adds no benefit to the present static diagram inventory.
The research and primary links are in [the audit](slidev-parity-diagrams.md).
Wheel navigation is the shared course component, not a community add-on: 18px
accumulation, 120ms quiet period, immediate reversal and one step per momentum
gesture, with scrollable/editable/control-wheel guards.

The release workflow is wired for this delivery, but no remote release, push or
production-template merge was performed. Shared changes are on
`feature/slidev-foundation` in `../_worktrees/presentation-template-slidev`;
Presentation-Template main is untouched. That shared feature must reach main
before the course release, because CI clones main and checks for the delivery
toolchain. Basic presenter/notes behavior and native authoring were checked in
the integration log; multi-display drawing and every presenter control were
not exhaustively exercised. Student builds strip notes; trainer builds remain
separate. These are the concrete remaining limits, not pending authoring work.

## Optional libraries migration

The companion course now also defaults to Slidev, with a Marp fallback and its
own student presentation ZIP. Its 168 pages preserve all 145 original fences;
offline browser validation reports zero failures. The earlier statement that
`libraries/` is outside the migration describes the fundamentals rollout only.
Commands, comparison review and delivery evidence are in
[the libraries Phase 1 record](libraries-slidev-phase1.md).

Phase 2 replaces the inventory and employee examples with music, photos and WoW
characters, while retaining the book dataset. Ten native additions have 55
states checked against executed Python. The final deck has 179 Slidev pages;
the Marp fallback has 169. Both build with no layout failures and lint is within
budget. Phase 3 reviewed nine Slidev module sheets plus the preamble sheet, a Marp spot check,
the exercise PDF and all 55 native click-export pages; tested reduced-motion
behavior in Chromium; exercised all six interactive Tk demos under WSLg; and
verified a fresh extraction of the 302-entry student ZIP. Details and exact
commands are in [the Phase 3 delivery record](libraries-slidev-phase3.md).
