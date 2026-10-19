> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# Slidev core modules package

Recorded 2026-10-18. Native animated slides for modules 01, 02, 04 and 05,
in the style the trainer approved for the Data Structures pilot
([slidev-data-structures.md](slidev-data-structures.md)) : stationary code
with an active line, moving values and references, reversible click steps.
Author checks were kept small on purpose; detailed verification belongs to
Luna and the coordinator.

## What the package adds

Ten native slides, each beside the canonical slide it animates. Every slide
uses the pilot's `DataStructuresRun` shell (code, output, visual, caption,
active line, colour and timing tokens) with one of three new visuals :

| Component | Role |
| --- | --- |
| `CoreNames.vue` | Frames of names (a namespace or one call), arrows to objects; objects in a column, or in a row (`direction="row"`) for a name walking a series of values. Orphaned objects are drawn dashed |
| `CoreLoop.vue` | The items a `for` loop walks, the loop variable as a tag that slides from item to item, each item's fate (`ran`, `skip`, `stop`, `never`) and an end slot that lights when the items run out |
| `CoreStream.vue` | What the `print()` calls wrote, with a mark for each newline and the cursor where the next write continues |

Each component's header comment documents its state schema. Every slide keeps
its data as one JSON object in `<script setup>` (`const run = {...}`), so a
checker reads exactly what is displayed.

## Insertion table

| Module | Insert after (existing title) | Native file (`src/slidev/core/`) | Route | States | Clicks | Demo | Layout |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `01-python-intro` | `Lines and Indentation` | `blocks-and-line-endings.md` | `01-python-intro-17-enhancement` | 6 | 5 | `01-pythonintro/04_lines_and_identation.py` | rows |
| `02-variables-and-data-types` | `Variables` | `binding-and-rebinding.md` | `02-variables-and-data-types-1-enhancement` | 8 | 7 | `02-variablesanddatatypes/01_variables.py` | side |
| `02-variables-and-data-types` | `Multiple Assignment` | `several-names-one-object.md` | `02-variables-and-data-types-3-enhancement` | 6 | 5 | `02-variablesanddatatypes/03_multipleassignment.py` | side |
| `04-control-flow-and-operators` | `while Loop` | `condition-before-each-pass.md` | `04-control-flow-and-operators-7-enhancement` | 7 | 6 | `04-controlflow/05_while.py` | side |
| `04-control-flow-and-operators` | `Looping over a Playlist` | `one-item-per-pass.md` | `04-control-flow-and-operators-10-enhancement` | 5 | 4 | `04-controlflow/07_for.py` | stack |
| `04-control-flow-and-operators` | `break and continue Statements` | `leaving-a-loop-with-break.md` | `04-control-flow-and-operators-13-enhancement` | 5 | 4 | `04-controlflow/09_breakandcontinue.py` | pair |
| `05-functions` | `Passing Object References` | `parameter-shares-the-list.md` | `05-functions-5-enhancement` | 6 | 5 | `05-functions/02_objectreferences.py` | stack |
| `05-functions` | `Overwriting References` | `rebinding-a-parameter.md` | `05-functions-6-enhancement` | 6 | 5 | `05-functions/03_overwritingreferences.py` | stack |
| `05-functions` | `return Statement` | `handing-back-a-result.md` | `05-functions-14-enhancement` | 7 | 6 | `05-functions/11_returnstatement.py` | side |
| `05-functions` | `Example Variable Scope` | `local-and-global-names.md` | `05-functions-16-enhancement` | 9 | 8 | `05-functions/12_variablescope.py` | side |

65 states, 55 clicks. Each target is a different source slide, as the shared
converter requires. Routes were read from a scratch build; they depend only
on source slide positions.

Add to `enrichments` in `build/slidev.config.ts` :

```ts
{ module: '01-python-intro', after: 'Lines and Indentation', file: 'src/slidev/core/blocks-and-line-endings.md' },
{ module: '02-variables-and-data-types', after: 'Variables', file: 'src/slidev/core/binding-and-rebinding.md' },
{ module: '02-variables-and-data-types', after: 'Multiple Assignment', file: 'src/slidev/core/several-names-one-object.md' },
{ module: '04-control-flow-and-operators', after: 'while Loop', file: 'src/slidev/core/condition-before-each-pass.md' },
{ module: '04-control-flow-and-operators', after: 'Looping over a Playlist', file: 'src/slidev/core/one-item-per-pass.md' },
{ module: '04-control-flow-and-operators', after: 'break and continue Statements', file: 'src/slidev/core/leaving-a-loop-with-break.md' },
{ module: '05-functions', after: 'Passing Object References', file: 'src/slidev/core/parameter-shares-the-list.md' },
{ module: '05-functions', after: 'Overwriting References', file: 'src/slidev/core/rebinding-a-parameter.md' },
{ module: '05-functions', after: 'return Statement', file: 'src/slidev/core/handing-back-a-result.md' },
{ module: '05-functions', after: 'Example Variable Scope', file: 'src/slidev/core/local-and-global-names.md' },
```

## How the states map to execution

The pilot's ranges are cumulative (`{1|1-2|1-3}`) because its programs run
straight down. These programs jump (calls, returns, loops), so here **each
range is what executes in that state**, and the last highlighted line is the
active one. Dimmed lines mean "not executing now", not "not run yet".

- Straight-line slides (`binding-and-rebinding`, `several-names-one-object`)
  run one line per state.
- Call slides run in execution order : `def`, the caller's lines, the call,
  the body lines, then the caller again (`{1|5|6|2|3|7}`). The state after
  the call's last body line shows the frame gone. In `handing-back-a-result`
  line 6 appears twice : the call starts there, and after `return` its
  result is bound there.
- Loop slides take one state per pass, highlighting the lines that pass ran :
  `{2-4}` for a `while` pass, `{2-3}` for a `for` pass, `{1-2,4}` for a pass
  that prints and `{1-3}` for the pass that breaks. In
  `leaving-a-loop-with-break`, state 2 is six passes (`o g r a m m`)
  together; its output group has six lines.
- `local-and-global-names` : `{1-2|4,8|12|5|6|13|14|9-10|15}`; state 1 runs
  both `def` statements, state 7 runs `global y` and `y = 2`.

A static checker therefore cannot run the fence prefix by prefix. A tracer
(`sys.settrace` on line events) can map each state to its line events :
state *k* ends after the last line event inside range *k* that follows the
end of state *k-1*. Object identity is CPython's : in particular `x` and `y`
share one `50`, `a` gets the same `1` back in `a, b, c = 1, 2, "john"`, and
the local `x = 2` and the global `y = 2` are one object (`i2`).

### Slide-specific semantics

- `blocks-and-line-endings` : `run.output` lists **finished lines**, as the
  terminal shows them; the open line written by `end=""` is in
  `states[4].writes` (newline `false`). Python's captured stdout after state 4
  contains `hello python` with no newline; compare `writes` with it, and
  `output` with the completed lines.
- `condition-before-each-pass` : the ints `x` leaves behind stay drawn,
  without a name, as a trail (CPython caches small ints, so they do exist).
  Elsewhere an object that loses its last name is drawn dashed for that one
  step, then omitted. Both are display choices; the names and the object a
  name refers to are exact in every state.
- `one-item-per-pass` : in the last state `title` still refers to
  `'Respect'`, as in Python; the end slot lights because the loop ran out.
- `leaving-a-loop-with-break` : after `break`, `letter` still refers to
  `'i'`; the end slot stays unlit and `n`, `g` are marked `never`.
- Function objects are shown as `function` objects with their name, so `def`
  is visibly a binding.

## Design decisions

- **The pilot's convention, unchanged** : same shell, colours (teal for the
  name or object just used or made, amber kept for `continue` in `CoreLoop`
  and not used yet, red for `break`),
  600 ms moves, 300 ms colour, reduced motion instant (component transitions
  are `none` under `prefers-reduced-motion`; the theme also forces 0 ms).
- **One mechanism per slide** : names bind to objects, several names share
  one, the condition is tested before each pass, the loop variable takes each
  item, `break` leaves early, a parameter shares or rebinds, `return` hands
  the object back, local and global scopes. Static, administrative slides in
  module 01 stay static.
- **Fixed geometry** : every frame, name row and object has one place for the
  whole run, computed from all states. A step moves arrows (SVG `d`
  transition), slides the loop tag, shows or hides rows and frames. Moving
  back reverses it.
- **Final states print on their own** : the whole output, the final
  bindings, each loop item's fate and the caption.
- **Code is the demo's** : each fence is an in-order, verbatim excerpt.
  Docstrings are left out of the function excerpts and the two blank lines
  before module-level code are one, as on the canonical slides.
- **Captions** use only terms the slides use (`bind`, `refer to`, `local
  scope`, `global`); one sentence each.

## Author checks (2026-10-18)

Course worktree `t3/cefaa02f` from `4b1ce89`; shared toolchain
`C:/Git/courseWare/_worktrees/presentation-template-slidev` at `faaf6a4`.

```bash
# Outputs : every demo was run and the excerpts with changed blank lines too.
uv run python demos/04-controlflow/09_breakandcontinue.py   # and the other nine
# Provenance : each fence line appears in its demo, in order (one-off script).
# Scratch build : modules 00 to 05 copied to build/slidev/scratch, the ten
# enrichments added to build/slidev.config.ts temporarily, then restored.
PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-slidev \
  bun run build/slidev.ts --slides-dir build/slidev/scratch
bun run build/slidev.ts --check-only
```

- Build : `5 modules, 101 source slides, 124 pages`; the shared check passed
  (`0 failures, 1 upstream warning`).
- Provenance : all ten fences are in-order excerpts; range counts equal the
  state, output and caption counts; no range points past the fence.
- Final state of all ten slides and a middle state of five were opened in
  headless Chromium at 1280 by 800 and looked at; no element of the run
  extends past the content area (measured against `.course-body`).
- Not done, by request : per-state Python comparison, reverse and
  reduced-motion runs, mid-transition frames, PDF and click exports.

## Findings for the coordinator

- **`continue` is not animated.** The demo's two loops print 15 lines; with
  the shell's output panel that does not fit the frame beside the code and a
  two-row visual. Only the `break` loop is animated. Two ways to add the
  `continue` loop : allow two enrichments after one source slide (converter
  change), or an output panel option in `DataStructuresRun` that scrolls or
  uses two columns.
- **Ranges are not cumulative here** (see above); a package checker modelled
  on `check_data_structures.py` needs a tracer rather than prefix runs.
- `blocks-and-line-endings.md` lowers the code font with a slide-scoped
  `<style>` (16 px, as `compactSlides` does for source slides), because the
  demo's comment line is 80 characters.
- The `d` transition on SVG paths animates in Chromium only; other browsers
  jump to the new arrow (as in the pilot's reference arrows).
- Several visuals leave space below them. They are sized for legibility in
  the 1280 by 800 frame, not to fill it; the trainer may want them larger.
- Nothing ships in the student bundle; the release workflow needs no change.
