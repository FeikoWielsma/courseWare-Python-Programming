# Slidev stateful modules package

Recorded 2026-10-18. Native animated slides for modules 09, 10 and 11, in the
style the trainer approved for the Data Structures pilot
([slidev-data-structures.md](slidev-data-structures.md)), as in the core and
middle packages ([slidev-core.md](slidev-core.md),
[slidev-middle.md](slidev-middle.md)) : stationary code with an active line,
moving values, records and objects, reversible click steps. Author checks were
kept small on purpose; detailed verification belongs to Luna and the
coordinator. Work started before a quota pause; the WIP commit `aa47245`
holds the first four slides, which were finished and fixed afterwards.

## What the package adds

Six native slides, two per module, each beside the canonical slide it
animates. All use the pilot's `DataStructuresRun` shell and one new visual per
module :

| Component | Role |
| --- | --- |
| `StatefulFile.vue` | One file on disk as a row of cells; each file object a box with its mode and `open` / `closed`. An open file object's position is a marker between two cells. Text written but not flushed sits, dashed amber, in the file object's buffer lane; closing moves the same cells up into the file. Cells a read covers turn teal |
| `StatefulRecords.vue` | Name boxes (`con`, `cur`, `row`, `lid`) with a short description of their value, and the rows of one table or query result. A fetched row moves from its slot into the `row` box (same object), leaving a dashed empty slot; a `next` marker shows where the cursor reads next. Uncommitted rows are dashed amber with `not committed`; an open transaction is a badge on `con` |
| `StatefulObjects.vue` | A class box and instance boxes, each listing its own attributes, with a `class` arrow from each instance to its class. A read lights the attribute where Python finds it, and the arrow when it is found on the class. A note beside an attribute shows a property's computed value or the refused assignment |

Each component's header comment documents its state schema. Every slide keeps
its data as one JSON object in `<script setup>` (`const run = {...}`), with
explicit geometry where the component takes it.

## Insertion table

| Module | Insert after (existing title) | Native file (`src/slidev/stateful/`) | States | Clicks | Demo | Layout | Visual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `09-python-io` | `Using with` | `closing-when-with-ends.md` | 7 | 6 | `09-python-io/08_usingwith.py` | stack | `StatefulFile` |
| `09-python-io` | `File Positions` | `moving-the-file-position.md` | 7 | 6 | `09-python-io/09_file_positions.py` | stack | `StatefulFile` |
| `10-python-database-access` | `Last inserted row id` | `inserts-wait-for-the-commit.md` | 7 | 6 | `10-python-database-access/05_lastinsertedrowid.py` | stack | `StatefulRecords` |
| `10-python-database-access` | `Fetching Rows` | `one-row-per-fetch.md` | 8 | 7 | `10-python-database-access/09_fetchone.py` (table from `04_preparedstatements.py`) | side | `StatefulRecords` |
| `11-python-classes` | `Class Attributes and Instance Attributes` | `object-first-then-class.md` | 9 | 8 | `11-python-classes/03_classattributes.py` | stack | `StatefulObjects` |
| `11-python-classes` | `A Computed Attribute` | `computed-on-every-read.md` | 6 | 5 | `11-python-classes/06_computedproperty.py` | side | `StatefulObjects` |

44 states, 38 clicks. Each target is a different source slide. Module 09 and
10 both have a slide titled `Using with`; the module slug disambiguates. In the
scratch build (preamble and modules 09 to 11 only) the routes were
`09-python-io-13-enhancement`, `09-python-io-14-enhancement`,
`10-python-database-access-7-enhancement`,
`10-python-database-access-11-enhancement`,
`11-python-classes-8-enhancement`, `11-python-classes-11-enhancement`.

Add to `enrichments` in `build/slidev.config.ts` :

```ts
{ module: '09-python-io', after: 'Using with', file: 'src/slidev/stateful/closing-when-with-ends.md' },
{ module: '09-python-io', after: 'File Positions', file: 'src/slidev/stateful/moving-the-file-position.md' },
{ module: '10-python-database-access', after: 'Last inserted row id', file: 'src/slidev/stateful/inserts-wait-for-the-commit.md' },
{ module: '10-python-database-access', after: 'Fetching Rows', file: 'src/slidev/stateful/one-row-per-fetch.md' },
{ module: '11-python-classes', after: 'Class Attributes and Instance Attributes', file: 'src/slidev/stateful/object-first-then-class.md' },
{ module: '11-python-classes', after: 'A Computed Attribute', file: 'src/slidev/stateful/computed-on-every-read.md' },
```

## Provenance and code

- Module 09 slides show their demo file whole, verbatim (`diff` clean).
- Module 10 and 11 slides quote the canonical slide fence of the slide they
  follow, verbatim (checked as a substring of the module source). Those fences
  are the demo without its blank lines (10) or with the demo's `try` around the
  last line removed (`computed-on-every-read`, as on the canonical slide, so the
  last state shows the uncaught `AttributeError` line the canonical slide shows).
- Type hints are kept as in the fences.

## How the states map to execution

As in the earlier packages, **each range is what executes in that state** and
the last highlighted line is the active one; ranges repeat when one line does
more than one thing (a `with` line also ends its block). Traced with
`sys.settrace` : CPython 3.14 reports a `with` block's exit on the `with` line.

- `closing-when-with-ends` `{1|2|1|4|6|7|6}` : open `fw` (file created empty,
  position 0); `write` (9 cells in `fw`'s buffer, disk still empty, position at
  the end); block exit (buffer flushed to disk, `fw` closed); `print(fw.closed)`;
  open `fr` (position 0); `read()` (all cells read, position at the end);
  block exit (`fr` closed). Probe : `os.path.getsize("foo.txt")` is 0 after
  `write` and nonzero after the block; `fw.closed` is `True`.
- `moving-the-file-position` `{1-2|4|5|6|7|8|4}` : state 0 is the whole first
  block (write and close); open `fr` at 0; `read(2)` to 2; `tell()`; `seek(0)`;
  `read(2)` to 2 again; block exit. Marker labels give the byte position.
- `inserts-wait-for-the-commit` `{1-2|3-5|6|7-9|10|11|3}` : connect; cursor and
  `CREATE TABLE` (empty table, no transaction); first `INSERT` (row 1 pending,
  `lastrowid` 1, transaction open); three more (rows 2 to 4 pending,
  `lastrowid` 4); `lid`; print; block exit commits (rows committed, badge gone).
  Probe : `con.in_transaction` is `False` after `CREATE TABLE`, `True` after the
  first `INSERT`, `False` after the block; `lastrowid` 1 then 4.
- `one-row-per-fetch` `{1-2|3-5|6-7|8,10|6-8,10|6-8,10|6-7|8-9}` : connect;
  cursor and `execute` (8 result rows, `next` before row 1); first `fetchone`
  (row 1 moves to `row`); test and print; second iteration (row 2 replaces it,
  row 1 gone); iterations 3 to 8 in one state (six output lines); `fetchone`
  returns `None`; `break`. Row identity : each row id is one tuple; the state
  where `row` holds it is the tuple `fetchone` returned.
- `object-first-then-class` `{1-3|6|7|8|9|10|11|12|13}` : class body (`wheels`,
  `__init__`); `a`; `b`; plates read on the objects; `wheels` read through the
  class arrow for both; `Car.wheels = 6` (changed); both read the class again;
  `a.wheels = 3` (new row on `a`); final reads (`a` own, `b` via class, `Car`
  direct). Probe : `vars(a)` is `{'plate': 'ABC 111', 'wheels': 3}`, `vars(b)`
  is `{'plate': 'XYX 123'}`.
- `computed-on-every-read` `{1-5|8|9|10|11|12}` : class (`__init__`, `area`
  property); `Square(5)` (only `length` stored); `sq.area` (found on the class,
  getter reads `length`, note `5 * 5 = 25`); `sq.length = 6`; `sq.area`
  (`6 * 6 = 36`); `sq.area = 50` refused (`no setter`). Probe : `vars(sq)` is
  `{'length': 6}`.

Expected output, from running each demo or fence with `uv run python` (in a
temporary directory; `cars.db` made by `04_preparedstatements.py` first, so
Audi is 52642, not the 62300 `10_parameterizedqueries.py` writes) :

| Slide | Output (state) |
| --- | --- |
| `closing-when-with-ends` | `True` (3), `one line` (5) |
| `moving-the-file-position` | `b'AB'` (2), `2` (3), `b'AB'` (5) |
| `inserts-wait-for-the-commit` | `The last Id of the inserted row is 4` (5) |
| `one-row-per-fetch` | `1 Audi 52642` (3), `2 Mercedes 57127` (4), rows 3 to 8 (5) |
| `object-first-then-class` | `ABC 111 XYX 123` (3), `4 4` (4), `6 6` (6), `3 6 6` (8) |
| `computed-on-every-read` | `25` (2), `36` (4), `AttributeError: property 'area' of 'Square' object has no setter` (5) |

## Display choices

- Text-mode positions are opaque (the canonical slide says so) : the text slide
  shows the marker without a number; on Windows `foo.txt` holds `\r\n` and
  `tell()` is 10, not 9. The newline is drawn as one `\n` cell, as written.
- The result of a query is drawn as all its rows, waiting in the cursor. SQLite
  steps through the result as rows are fetched; the caption only says the
  cursor stands before the first row.
- The implicit transaction (sqlite3 opens one before the first `INSERT`) is
  shown as a badge, without new terms in the captions.
- Names and class objects are drawn as labelled boxes, not name-to-object
  arrows : each name refers to one object here, and references were taught in
  modules 02 and 05.
- Colours keep the pilot's meanings : teal for active, read or made; amber for
  changed, buffered or uncommitted; red for refused.

## Author checks (2026-10-18)

Course worktree `t3/54be0d52` from `2d7cdef` (WIP `aa47245`); shared
toolchain `C:/Git/courseWare/_worktrees/presentation-template-slidev` at
`f4f9ca1`.

```bash
# Outputs, in a temporary directory with copies of the demos
uv run python 08_usingwith.py; uv run python 09_file_positions.py
uv run python 04_preparedstatements.py; uv run python 09_fetchone.py
uv run python 05_lastinsertedrowid.py; uv run python 03_classattributes.py
uv run python sq.py   # the computed-property fence, as on the slide
# plus throwaway probes for buffer size, in_transaction, lastrowid, vars()
# Scratch build : 00-preamble and 09 to 11 copied to build/slidev/scratch,
# build/slidev.config.ts enrichments temporarily replaced by the six above,
# then restored (no diff) and the scratch folder removed.
PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-slidev \
  bun run build/slidev.ts --slides-dir build/slidev/scratch
bun run build/slidev.ts --check-only
```

- Build : `3 modules, 56 source slides, 65 pages, 74 original code/output
  fences`; check `65 pages, 56 topics, 0 failures, 1 upstream warning`.
- One throwaway headless pass at 1280 by 800 visited all 44 states :
  `data-ds-step` matched the click, the rendered output matched the table
  above, and after one geometry fix no visible element left `.course-body`.
  Final frames of all six and a few middle frames were looked at.
- Not done, by request : per-state Python comparison, reverse and
  reduced-motion runs, PDF and click exports, a package checker.

## Findings for the coordinator

- `one-row-per-fetch` folds iterations 3 to 8 into one state (six output
  lines at once) to keep the click count down.
- `computed-on-every-read` ends on an uncaught exception, as the canonical
  slide does; the demo file itself catches it and prints only the message.
- The validating setter (`07_validatingsetter.py`) was not animated : its
  canonical fence has no calling code, and the demo file is too long to show
  whole beside a visual.
- Nothing ships in the student bundle; the release workflow needs no change.
