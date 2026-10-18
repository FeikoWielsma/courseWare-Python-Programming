# Slidev integration evidence

Continuation of [the adoption plan](slidev-migration-plan.md), 2026-10-18.

## Initial Luna audit

Merged `1e5967b` from `t3/audit-slidev-mermaid-parity`. The
[audit](slidev-parity-diagrams.md) describes its original 241-page baseline;
subsequent fixes are recorded here rather than rewriting those observations.

## Diagram and PDF fixes

- `Unexpected Errors` now has an explicit compact grid in course config/CSS.
  Original prose, Mermaid source and the single source-page boundary remain.
  Luna's diagram check measures the minimum label at 14.1px, previously 5.5px.
- Shared validation measures Pele text after its SVG screen transform,
  normalized to the 1280px canvas. Sub-10px labels and render placeholders fail.
- PDF export collects visible anchor rectangles from each native printed frame
  and maps semantic/numeric slide routes to PDF destinations. Range/click PDFs
  use their actual exported page order, link to the first included state, and
  omit destinations outside the selected range. Web links retain URI actions.
- Two regression tests cover semantic/numeric routes, coordinates, external
  URLs, serialization and selected/click-state destination handling.

Executed against shared feature worktree:

```powershell
bun run --cwd ../_worktrees/presentation-template-slidev/build typecheck
bun test --cwd ../_worktrees/presentation-template-slidev/build/slidev convert.test.ts pdf.test.ts
$env:PRESENTATION_TEMPLATE_DIR='C:/Git/courseWare/_worktrees/presentation-template-slidev'
bun run --cwd build slidev --pdf --check
bun build/slidev_checks/check_diagrams.ts
```

Results: TypeScript and seven tests pass; 241 pages, 226 source topics, 299
original code/output fences, zero browser validation failures, nine diagrams
passing. The known upstream FloatingVue warning remains recorded.

Independent `pypdf` inspection of the rebuilt full PDF found 874 link annotations,
all 874 destinations belonging to actual PDF pages, and preserved outlines.
The eight-state exception-slide PDF was regenerated; its final page contains all
exception labels. Poppler rendered page 143 at 1280px, and the resulting image
was visually inspected for legibility and overlap. Generated evidence remains
under ignored `build/slidev/`; the PDF is `dist/course-slidev.pdf`.

These checks establish the fixes above. The complete course animation rollout,
default build/release cutover, authoring integration and final acceptance remain
open. Shared production checkout remains unchanged.

## Live authoring

Added opt-in `bun run --cwd build slidev:dev` over shared `--dev`. It starts
native Slidev on port 3030 and watches canonical/native sources, source assets,
course config and the shared template. Generated source synchronization changes
only differing files and removes stale managed component/layout/setup files.
Authoring manifests are separate from the static delivery manifest; trainer
notes are available locally and the static student build retains its existing
note stripping.

A copied tiny fixture was served in the T3 browser. Editing a canonical title
updated the visible title without a manual reload. Adding a native slide and
setting an accent in course config added its route and changed the computed
accent. Editing its Vue component updated the visible 1280 by 800 slide live.
The first probe exposed a restart caused by removing unchanged setup files;
changed-only synchronization fixed it and the probes above then passed.
The fixture/server were isolated from course sources and the server was stopped.
TypeScript and seven converter/PDF regression tests pass after this change.

## Data Structures pilot integration

Merged Opus `e5c5f9d` from `t3/data-structures-slidev-pilot` and applied its six
insertion specs. The integrated deck has 247 pages, 226 source topics and the
same 299 original fences. The main Python snapshot command now discovers the
package checks. Reference-arrow marker IDs use Vue instance IDs so simultaneously
printed click states cannot share marker IDs.

Executed: `uv run python build/check-slidev-examples.py`, Ruff, course fence and
reference checks, `slidev --pdf --check`, and the package's `--browser` check
against the served integrated app. All pass; all 33 package states match Python
in the actual browser. Full PDF has 247 pages and 886 internal links. Exported a
six-page final-state pilot PDF and a 33-page click-state pilot PDF and checked
their page counts. Poppler-rendered pilot pages were inspected. A real T3 browser
recording exercises list replacement/deletion, shared/separate rows and stack
operations, including reverse clicks; each recorded forward step was read back
from the component's click state.

The rendered gallery, recording and PDFs were prepared for the trainer's style
review before any remaining-module authors were started. The review is the
prototype checkpoint in the shared orchestration guide. Release packaging work
can proceed independently while that preference is pending.

## Delivery preparation before the default switch

Prepared `build/course.ts`, deliberately not yet wired to the ordinary package
scripts. It builds/checks the public Slidev deck, preserves exercise routing,
provides explicit Marp routing and custom PDF output, and uses the shared
student-package helper. `--serve` selects source watching. Trainer builds remain
an explicit separate command so they cannot enter student packaging.

The portable package allowlists the built app, local licences, launcher and
instructions. Its zip contains `slides/` plus the course PDF. A custom-output
probe built the 247-page PDF and a 13.6 MiB zip; all 5,716 zip entries matched
their source hashes, CRC checks passed, and no Markdown, source manifest or Marp
comparison files entered it. The packaged `serve.py` then served the copied app,
and all 33 pilot states passed against that delivery origin. The explicit Marp
route independently built its 239-page PDF and HTML. No ordinary script,
release workflow or student README default has been switched yet.

## Approved rollout and shared-build regression

The trainer approved the pilot style for the remaining modules. Opus authors do
animation implementation and basic output/syntax checks; Luna/coordinator own
detailed verification. One Opus author runs at a time to conserve quota. The
middle package was cancelled during inspection and remains queued.

Built two unrelated courses with the production template, then the Slidev
feature worktree, using `build/build.ts --skip-lint --no-html --force --out
build/dist/slidev-regression-{before,after}.pdf`. Python `pypdf` extracted text
from every page and compared exact strings, without whitespace normalization:

| Course | Production pages | Feature pages | Pages with changed text |
| --- | --- | --- | --- |
| GitLab CI/CD | 161 | 161 | 0 |
| C# Programming | 273 | 273 | 0 |

All four PDF builds passed. JSON evidence is in ignored
`build/slidev/shared-regression.json`. Production checkout and both unrelated
course sources were not edited by this work (unrelated existing changes were
left alone). Regression PDFs are retained under ignored `build/slidev/regression/`.
This satisfies the documented shared
before/after PDF comparison gate; no production merge or push was performed.

## Wheel responsiveness

The trainer requested snappier wheel navigation. The original handler required
24px movement, 180ms quiet and a 700ms fixed lockout; a new gesture inside the
lockout was consumed without navigation. Shared `f4f9ca1` replaces that lockout
with one movement per gesture, an 18px threshold and 120ms gesture separation.
Reversing by 18px responds immediately. Small opposite recoil does not rearm
momentum. Scrollable content, editable controls, horizontal scrolling and
Ctrl/Command-wheel retain their exclusions.

Executed 13 shared converter/PDF/wheel tests and TypeScript checking; all pass.
Rebuilt and restaged the public app, then ran the physical CDP delivery probe
against its packaged launcher on 4188. Quick consecutive gestures under 700ms,
immediate reversal, ordinary navigation, momentum grouping, zoom/control/scroll
exclusions and forward/reverse slide boundaries all pass. The check reads actual
navigation after 60ms, before visual transitions finish. The public preview was
reloaded to use the rebuilt JavaScript. PDF content was unchanged; no new export
was necessary for this interaction-only change.

## Core package integration

Merged Opus `f2a0eba` and integrated ten insertion points in `25941da`. A fresh
full build/export/check passed: 257 pages, 226 original topics, 299 original
fences, zero layout failures and the same known upstream warning. The full PDF
has 906 link annotations. Restaged the public app with this fresh PDF. Rendered
PDF pages 27, 94 and 120 (binding/rebinding, for-loop traversal and return values)
were inspected by the coordinator; code, output and reference arrows are readable.
The return-value final caption's phrase "Only total remains" should be made
more precise because the global function binding also remains.

Luna round `slidev-20261018-luna-core-verification-r4` owns all 65 detailed
state checks, reverse/reduced-motion and selected exports. The sole Opus task
`slidev-20261018-opus-middle-animations-r2` authors modules 06/07/08. Stateful
modules 09/10/11 and appendices 12/13 remain queued. Named Marp fallback and
animation/delivery check scripts are now available; ordinary default build and
release routing still wait for full acceptance.

Release workflow changes are staged on this feature branch: install the isolated
Slidev dependencies, run animation/delivery gates, build the named Marp fallback,
copy the public `student/` allowlist as `slides/`, and publish the animated zip,
default PDF and explicit fallback. They depend on the final ordinary-build switch
and on merging the shared feature into template main first; the workflow reports
that prerequisite explicitly. No remote workflow or publishing step was run.

## Middle package integration

Merged Opus `986c3db` and six insertion points in `2d7cdef`. The fresh full build,
PDF export and layout check passed: 263 pages, 226 original topics, 299 original
fences, zero failures and the known upstream warning. The PDF has 918 link
annotations. Coordinator inspected rendered final pages 136, 146 and 174
(package imports, filtered comprehension and finally propagation); text and
state diagrams are readable. The public preview/package was restaged with this
fresh app and PDF. All 34 detailed states still need independent Luna checks.

The sole Opus task `slidev-20261018-opus-stateful-animations-r1` now authors
09/10/11. Appendices 12/13 remain queued; Luna's core verification is still active.

## Practical Functions examples and focused acceptance

Trainer feedback superseded the unchanged-source requirement for module 05.
Committed `a747bf6` replaces the abstract syntax and toy examples with delivery
pricing, receipts, CSV export columns, dispatch details and order sorting.
Annotations and docstrings follow concrete calls and return values. Fifteen
main demos are numbered in teaching order; the four native animations retain
the approved design and now use these examples. Wordle contracts are unchanged.

The new source baseline is 228 topics, 297 code/output fences and 241 Marp pages.
The full comparison build, PDF export and layout check pass with 265 Slidev
pages, zero failures and the previously known FloatingVue warning. The PDF
contains 924 internal links. The public student folder and zip were restaged.

All 15 Functions demos run, all 16 Python fences match their demo excerpts, and
the existing core trace checker passes all 67 states. Ruff, fence/reference
checks and Functions Marp layout lint pass. The focused browser checker for the
four changed animations passes 60 forward/reverse frames, reduced motion and
containment against the packaged launcher on port 4188. Its first pass exposed
a caption overflow; an explicit 16px code layout fixes it. Wider name boxes
preserve complete function names. Label encoding was repaired before rebuilding.

Coordinator inspected newly rendered PDF pages 105, 109, 116 and 118: first
function syntax, receipt, mutation and returned-list examples. No clipping,
overlap or corrupted labels remain. These focused checks replace further Luna
rounds at the trainer's request. Stateful authoring remains saved, unintegrated
WIP awaiting the scheduled Claude quota reset; appendices and final cutover
remain open.

## Completed rollout and media examples

The trainer's subsequent instruction to use music/photos, game characters and
a film watchlist supersedes the delivery-pricing examples and pending-work
statements above. Stateful authoring `9af38f8` and appendix authoring `b054bcc`
are integrated. There are 229 canonical topics, 294 canonical fences and
242 Marp pages, plus 33 native additions for 275 Slidev pages and 207 native
states. [The current rollout record](slidev-rollout.md) has the full inventory,
commands, verification granularity, delivery behavior and remaining limits.

The ordinary Slidev build and canonical layout lint pass. All nine Pele diagrams
pass, the full PDF has 275 pages and 945 valid internal links, and all 207 native
click states export. Six latest PDF pages and live character/JSON frames were
visually reviewed. The 98 middle/stateful/appendix states pass a focused browser
run including reverse navigation, restored visual state, output and reduced
motion. Existing static core, Data Structures and legacy snapshot checks pass.

Final `bun run --cwd build check:delivery` exits zero against the public package:
136 core forward/reverse frames, reduced motion and containment; all 33 Data
Structures states match Python in the browser; physical wheel rapid gestures,
immediate reversal, momentum grouping, exclusions, scrollable controls and
forward/reverse slide boundaries pass. A popped stack value was moved inside the
frame, and output now reserves its final layout to prevent code/diagram shifts.
The stack labels were subsequently placed above their columns for legibility.

`build` and `serve` use the Slidev wrapper; named Marp fallback, exercise build,
portable inline exercise previews, release allowlists and Codespaces are wired.
The public ZIP contains only 421 current files and the canonical PDF, with no
trainer notes or authoring sources. Shared `e1b1c63` clears stale output chunks;
shared TypeScript and 14 focused tests pass. Two unrelated-course PDF regression
comparisons passed earlier. No further Luna rounds were used.

Shared production main is untouched. The shared feature must be merged before
a remote course release; the prepared CI workflow explicitly checks for its
delivery toolchain. No push, PR, remote release or production merge was made.
