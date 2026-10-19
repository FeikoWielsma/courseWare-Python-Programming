> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# Slidev Data Structures pilot

Recorded 2026-10-18. Package for stage 2 of the
[migration plan](slidev-migration-plan.md): six native slides for module 03,
added beside the canonical pages, ready for the trainer's style review.

## What the pilot adds

Each slide shows one program from an existing demo. The code fence uses
Slidev's own line highlighting with cumulative ranges (`{1|1-2|1-3}`), so every
click runs one more line. Lines that have not run are dimmed, and the last line
that ran is marked. Beside the code there are three parts :

- **Output** : the lines printed so far, with the newest one marked. Its height
  is reserved for the whole run, so nothing below it shifts.
- **Visual** : the data after the current line. Every object is drawn once and
  keeps its element across the run. Moving between states moves that element;
  moving back reverses it.
- **Caption** : one sentence on the current step, using only taught terms.

| Slide (native file) | Insert after | Demo | States | What moves |
| --- | --- | --- | --- | --- |
| Indexing and Slicing a List (`indexing-and-slicing.md`) | `Lists` | `01_lists.py` | 4 | Copies leave their cells to build the result; the slice bracket marks `start` and `stop`; `[::-1]` reorders the same copies |
| Replacing and Deleting Items (`replacing-and-deleting.md`) | `Delete List Elements` | `02_updatinglists.py` | 6 | The replaced and deleted items drop to a struck-through *removed* row; later items slide left under fixed index labels |
| Shared and Separate Rows (`shared-and-separate-rows.md`) | `Multidimensional Lists` | `03_multidimensionallists.py` | 6 | References drawn as arrows : two slots to one list, then two slots to two lists; the changed cell and the path used are marked |
| A List as a Stack (`lists-as-stacks.md`) | `List Operations` | `04_listsasstacks.py` | 5 | Items drop onto the top; `pop()` moves the top item out to *returned*; the `top` marker follows the last index |
| Set Operations by Region (`set-operations.md`) | `Set Operations` | `09_setsandfrozensets.py` | 6 | Each name sits in its Venn region; `in` rings one set, each operator fills the regions in its result |
| Updating a Dictionary (`updating-a-dictionary.md`) | `Accessing Values in Dictionary` | `10_dictionaries.py` | 6 | New pairs append; a lookup marks its row; a new value replaces the old in place (old value struck out beside it); `del` drops the row |

States are click states including the initial one, so clicks per slide are
states minus one : 3, 5, 5, 4, 5 and 5, 27 clicks in all, 33 states.

Pages in the integrated deck (with the existing two native slides) : 52, 56,
58, 60, 71 and 74 of 247.

### Components

All in `src/slidev/components/`, styles scoped :

| Component | Role |
| --- | --- |
| `DataStructuresRun.vue` | Layout (`stack`, `pair`, `side`, `rows`), output, caption, active-line marker, shared colour and timing tokens |
| `DataStructuresSlicing.vue` | Index, negative index, slice bracket and result copies |
| `DataStructuresSequence.vue` | A list with stable items, as a row or a stack; ghost and returned states |
| `DataStructuresReferences.vue` | Names, outer slots, reference arrows and inner lists |
| `DataStructuresSets.vue` | Two-set Venn with region fills and member chips |
| `DataStructuresDict.vue` | Key and value rows in insertion order |

Each slide's data is one JSON object in `<script setup>` (`const run = {...}`),
passed to `DataStructuresRun` and to the visual, so the checker reads exactly
what the components display.

## Design decisions

- **One convention, six subjects.** Code above or beside, output next to it,
  visual, caption. The line marker, colours and timings are the same on every
  slide, so the room learns the convention once.
- **Colour has one meaning each** : teal for the selected or newly placed item,
  amber for a changed value, red and struck through for what was removed.
  Everything else stays in the course's blue-grey.
- **States stay readable in print.** A removed item stays visible, struck
  through, for the step that removed it, and `pop()` keeps the returned item
  on screen, so each click page of the PDF explains itself. The final state is
  the whole program, its whole output and the data after it.
- **Motion is restrained** : 600 ms with an ease-out curve for moves, 300 ms for
  colour. No looping, no decoration of static facts. With
  `prefers-reduced-motion` every state is reached instantly (measured :
  transition durations `0s`, a ghost at its final position after 60 ms).
- **Fixed geometry.** No automatic fitting. Every slide was checked in the
  1280 by 800 frame, and the browser check fails if a visible element leaves
  the content area.
- **Code is the demo's.** Each fence is an in-order excerpt of its demo, kept
  verbatim with its comments. The examples stay neutral (no Wordle).
- **Titles** are noun phrases within 40 characters; captions are single
  sentences with inline code in backticks.

Dimmed lines use opacity `.36` in place of Slidev's `.3` so the initial-state
print page stays legible.

## Checks

```powershell
# Static : provenance, executed output, displayed state, object identity.
uv run python build/slidev_checks/check_data_structures.py

# Rendered : every click state of the built app against Python.
$env:PRESENTATION_TEMPLATE_DIR = 'C:/Git/courseWare/_worktrees/presentation-template-slidev'
bun run build/slidev.ts --serve-only --port 4188
uv run python build/slidev_checks/check_data_structures.py --browser http://127.0.0.1:4188
```

The static check runs each slide's fence one click state at a time in one
namespace and compares :

- the fence with the demo named by the pill (lines in order, verbatim);
- the ranges with the number of states, outputs and captions;
- printed output per state with `run.output`;
- displayed items with the Python objects, by `repr`;
- data ids with Python object identity across all states (a data id must
  always stand for one object, and one object for one data id). This is what
  proves `shared` has one inner list and `rows` two;
- selections : the index or slice recovered from the expression, the picked
  indexes, the set operation's result, the membership test, the dictionary
  lookup and the value returned by `pop()`;
- each expression appears on the line that ran in that state.

The browser check loads `#/<route>?clicks=k` for each of the 33 states and
reads what was rendered : cell texts in visual order, result copies, the
inner list each arrow ends at (by its rendered end point), lit set members,
dictionary rows by position, output lines, caption and step. It compares them
with the Python states, and fails on elements outside the frame.

Both checks were shown to fail on deliberate errors : a changed dictionary
value, a reference pointing at the wrong list, a wrong list item, a wrong
slice selection, an edited code line, a range removed, a wrong set result, and
a component that drew the list in reverse order.

## Evidence (2026-10-18)

Course worktree branch `t3/data-structures-slidev-pilot` from `77a1478`;
shared toolchain `C:/Git/courseWare/_worktrees/presentation-template-slidev`
at `c7ec5ce` with uncommitted changes from another session in `build.ts`,
`prepare.ts` and a new `dev.ts`.

- Static check : 6 slides, 33 click states match Python.
- Browser check : 33 click states match Python (scratch module-03 build and the
  full-course build).
- Full build with the insertions below, `--pdf --check` : 247 pages (241 + 6),
  226 topics, no geometry issues, full PDF 247 pages with 886 internal links.
  One failure, outside this package : *Diagram labels below 10px* on
  `08-exception-handling-1`, raised by the shared checker's new label test
  (`c7ec5ce`). The coordinator's branch fixes it in `53d3e2d`, which this
  worktree's base predates.
- Click export, `--with-clicks --range 52,56,58,60,71,74` : 33 pages, one per
  state. All 33 and the six final-state pages of the full PDF were rasterised
  and inspected.
- Browser frames : every state forwards and backwards was captured, and a
  frame 260 ms into each forward click. All final states, and mid-click frames
  for the deletion, stack and dictionary moves, were inspected by eye. Reverse navigation returns
  each state exactly (`data-ds-step` read back on every step).
- `uv run ruff check .` : clean.
- Known upstream console warning only : `Failed to patch FloatingVue`.

## Insertion spec for the coordinator

Add to `enrichments` in `build/slidev.config.ts`. The order in the list does
not matter; each targets a different source slide, which the shared converter
requires because the route is `<topic>-enhancement`.

```ts
{ module: '03-data-structures', after: 'Lists', file: 'src/slidev/data-structures/indexing-and-slicing.md' },
{ module: '03-data-structures', after: 'Delete List Elements', file: 'src/slidev/data-structures/replacing-and-deleting.md' },
{ module: '03-data-structures', after: 'Multidimensional Lists', file: 'src/slidev/data-structures/shared-and-separate-rows.md' },
{ module: '03-data-structures', after: 'List Operations', file: 'src/slidev/data-structures/lists-as-stacks.md' },
{ module: '03-data-structures', after: 'Set Operations', file: 'src/slidev/data-structures/set-operations.md' },
{ module: '03-data-structures', after: 'Accessing Values in Dictionary', file: 'src/slidev/data-structures/updating-a-dictionary.md' },
```

Routes : `03-data-structures-2-enhancement`, `-4-`, `-5-`, `-6-`, `-15-` and
`-17-enhancement`. Keep the existing `compactSlides` list.

Global checker integration : run `build/slidev_checks/check_data_structures.py`
beside `build/check-slidev-examples.py`; the `--browser` mode needs a served
build and `PRESENTATION_TEMPLATE_DIR`. The release workflow needs no change for
this package (nothing here ships in the student bundle).

## Findings for coordinator-owned files

- `src/slidev/list-mutation.md` uses the shared `CollectionState`, which keys
  items by `String(value)`. A list holding a repeated value would collapse two
  objects into one element. The pilot's `DataStructuresSequence` keys by object
  and could replace it; the slide would then match this pilot's convention
  (output panel, active line, captions).
- `list-mutation.md` and `tuple-unpacking.md` use Magic Move growth while the
  pilot uses cumulative line highlighting. Pick one for the module after the
  style review; the highlighting form keeps code still, so the eye follows the
  data rather than the code.
- `build/check-slidev-examples.py` checks code lines are in the demo but not
  their order; the pilot's checker also checks order and identity.
- The shared converter allows one enrichment per source slide. A second
  addition after `Accessing Lists` would need a converter change.

## Limitations

- The JSON in each slide is written by hand and checked, not generated from
  Python; a change to a demo needs the JSON updated, and the check says where.
- The motion was reviewed as frame sequences, not as a recording.
- Presenter mode, notes and wheel navigation were not exercised on these
  slides beyond ordinary arrow-key navigation.
