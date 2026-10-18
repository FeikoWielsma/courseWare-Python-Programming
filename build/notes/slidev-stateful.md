# Slidev stateful modules package

Recorded 2026-10-18. Canonical example rewrite of modules 09, 10 and 11 and
their native animated slides, under the trainer-approved scope in
[engaging-examples.md](engaging-examples.md) and the current
`build/slidev-agent-brief.md`. Those supersede the unchanged-canonical and Luna
instructions of the earlier rounds (WIP `aa47245`, first finish `e5e6aa3`),
which were merged and whose components and geometry fixes are reused.

Themes : music and photos for files (09), one film watchlist for SQLite (10),
game characters for classes (11). Slide titles are unchanged, so exercise
references and enrichment targets still resolve. Native slides follow the
approved Data Structures pilot : stationary code with an active line, moving
values, records and references, reversible click steps, reduced motion.

## Canonical changes

### 09 Python IO

The module now teaches `with` and useful text reading before manual `close`
and the io layers. Slide order, demos renumbered (stems kept) :

| # | Title | Demo | Was |
| --- | --- | --- | --- |
| 1 | Input and Output | `01_readinput.py` | `01_readinput.py` |
| 2 | Opening Files | | slide 3 |
| 3 | File Open Modes | | slide 4 |
| 4 | Using with | `02_usingwith.py` | `08_usingwith.py`, slide 13 |
| 5 | Reading Text Files | `03_readtextfile.py` (new) | slide 11, no demo |
| 6 | Writing Text Files | `04_writetextfile.py` | `07_writetextfile.py`, slide 10 |
| 7 | Closing Files | | slide 12 |
| 8 | File Object Attributes | `05_fileioobject.py` | `03_fileioobject.py`, slide 6 |
| 9 | IO Module | | slide 2 |
| 10 | Result of Calling open | `06_openfile.py` | `02_openfile.py`, slide 5 |
| 11 | Bytes and Byte Arrays | `07_bytesandbytesarrays.py` | `04_...` |
| 12 | Reading Binary Files | `08_readbinaryfile.py` | `05_...` |
| 13 | Writing Binary Files | `09_writebinaryfile.py` | `06_...` |
| 14 | File Positions | `10_file_positions.py` | `09_...` |
| 15 | The csv Module | `11_csv_module.py` | `10_...` |
| 16 | Reading CSV Rows by Name | `12_csv_dictionary.py` | `11_...` |
| 17 | Paths with pathlib | | |
| 18 | Paths Relative to a Module | | |
| 19 | Renaming and Deleting Files | `13_renaming_files.py` | `12_...` |
| 20 | Creating and Removing Directories | `14_creatingandremoving_directories.py` | `13_...` |
| 21 | Directory Contents | `15_directorymethods.py` | `14_...` |
| 22 | Summary : Python IO | | |

Supplied data : `playlist.txt` and `listening_history.csv` (new), the existing
`trilobyte.jpg`. Removed : `test.txt`, `test_02.txt`, `textfilepolish.txt`
(no longer read). Examples : last played track, a playlist read by line, a
road-trip playlist written and appended with UTF-8 titles, the photo's JPEG
signature and `JFIF` marker by position, a resumable player state packed with
`struct`, listening history totals with `DictReader`, photo rename, album
folders and `glob("*.jpg")`. The `FileIO` repr now shows `closefd=True`, as
Python 3.14 prints it.

### 10 Python Database Access

Same 16 slides in the same order; every demo keeps its file name. One table,
`films(id INTEGER PRIMARY KEY, title, year, minutes, watched DEFAULT 0, rating)`
in `watchlist.db`, six films with generated ids. Demo03/04 create it (literal
SQL, then `executemany`); 05 uses `:memory:` and `lastrowid`; 06 to 09 and 11
read it; 07 groups minutes per year from 2010; 10 marks film 3 watched and
rated with `?`, then adds `Howl's Moving Castle` with named placeholders;
12 `save_ratings` commits a valid batch and rolls back a batch with an invalid
rating. The first query (demo01) is five lines without error handling;
the `try`/`except`/`rollback` now lives in Committing Data where it is the
lesson.

### 11 Python Classes

Same 17 slides in the same order. `02_employee.py` is renamed
`03_character.py` (pill `demo03 · character`); other names unchanged.
`Character` with independent `health`, `take_damage`, `heal` and
`show_status` comes before the class attribute (`max_health`, slide 8, with
a game-wide change and a per-character override). Plain `health`, the
computed `is_alive` property, then a validating `health` setter (0 to 100)
with unchanged calling code. `_gold` and `__save_key` for internal names,
`Wizard(Character)` as the one introductory inheritance example.

## Insertion table

| Module | Insert after (existing title) | Native file (`src/slidev/stateful/`) | States | Clicks | Demo | Layout | Visual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `09-python-io` | `Using with` | `closing-when-with-ends.md` | 7 | 6 | `09-python-io/02_usingwith.py` (whole) | stack | `StatefulFile` |
| `09-python-io` | `File Positions` | `moving-the-file-position.md` | 8 | 7 | `09-python-io/10_file_positions.py` (whole) | stack | `StatefulFile` |
| `10-python-database-access` | `Last inserted row id` | `inserts-wait-for-the-commit.md` | 7 | 6 | `10-python-database-access/05_lastinsertedrowid.py` (slide fence) | stack | `StatefulRecords` |
| `10-python-database-access` | `Fetching Rows` | `one-row-per-fetch.md` | 8 | 7 | `10-python-database-access/09_fetchone.py` (slide fence; table from demo03/04) | side | `StatefulRecords` |
| `11-python-classes` | `Creating and Using Objects` | `each-object-has-its-own-health.md` (new) | 7 | 6 | `11-python-classes/03_character.py` (calling lines, verbatim) | side | `StatefulObjects` |
| `11-python-classes` | `Class Attributes and Instance Attributes` | `object-first-then-class.md` | 9 | 8 | `11-python-classes/04_classattributes.py` (slide fence) | stack | `StatefulObjects` |
| `11-python-classes` | `A Computed Attribute` | `computed-on-every-read.md` | 6 | 5 | `11-python-classes/07_computedproperty.py` (slide fence) | side | `StatefulObjects` |

52 states, 45 clicks. Module 09 and 10 both have a slide titled `Using with`;
the module slug disambiguates. Scratch-build routes (preamble and 09 to 11
only) : `09-python-io-4-enhancement`, `09-python-io-14-enhancement`,
`10-python-database-access-7-enhancement`,
`10-python-database-access-11-enhancement`, `11-python-classes-6-enhancement`,
`11-python-classes-8-enhancement`, `11-python-classes-11-enhancement`.

Enrichments for `build/slidev.config.ts` :

```ts
{ module: '09-python-io', after: 'Using with', file: 'src/slidev/stateful/closing-when-with-ends.md' },
{ module: '09-python-io', after: 'File Positions', file: 'src/slidev/stateful/moving-the-file-position.md' },
{ module: '10-python-database-access', after: 'Last inserted row id', file: 'src/slidev/stateful/inserts-wait-for-the-commit.md' },
{ module: '10-python-database-access', after: 'Fetching Rows', file: 'src/slidev/stateful/one-row-per-fetch.md' },
{ module: '11-python-classes', after: 'Creating and Using Objects', file: 'src/slidev/stateful/each-object-has-its-own-health.md' },
{ module: '11-python-classes', after: 'Class Attributes and Instance Attributes', file: 'src/slidev/stateful/object-first-then-class.md' },
{ module: '11-python-classes', after: 'A Computed Attribute', file: 'src/slidev/stateful/computed-on-every-read.md' },
```

## Components

Unchanged from `e5e6aa3`; each header comment documents its state schema.
Every slide keeps its data as one JSON object (`const run = {...}`).

| Component | Role |
| --- | --- |
| `StatefulFile.vue` | One file as a row of cells; each file object a box with mode and `open` / `closed`; position marker between cells; unflushed text dashed amber in the object's buffer lane, moved up into the file on close; read cells teal |
| `StatefulRecords.vue` | Name boxes and the rows of a table or result; a fetched row moves into `row`; `next` marker; uncommitted rows dashed amber with an open-transaction badge on `con`. `inserts-wait-for-the-commit` passes `:label-width="96"` for `film_id` |
| `StatefulObjects.vue` | Class and instance boxes with their own attributes and `class` arrows; a read lights where Python finds the attribute (and the arrow when found on the class); a note shows a computed value, the `self` of a method call, or a refused assignment |

## How the states map to execution

Each range is what executes in that state; the last highlighted line is the
active one. A `with` line repeats when the block ends.

- `closing-when-with-ends` `{1|2|1|4|6|7|6}` : open `fw` (empty file); `write`
  (8 cells `So What\n` in `fw`'s buffer, disk empty); block exit (flushed,
  `fw` closed); `print(fw.closed)`; open `fr` at 0; `read()` to the end;
  block exit closes `fr`.
- `moving-the-file-position` `{1|2|3|4|5|6|7|1}` : the first ten bytes of
  `trilobyte.jpg` (`ff d8 ff e0 00 10 J F I F`, then `...`); open at 0;
  `read(2)` to 2; `tell()`; `seek(6)`; `read(4)` to 10 (`JFIF`); `seek(0)`;
  `read(2)` to 2; block exit.
- `inserts-wait-for-the-commit` `{1-2|3-5|6|7-8|9|10|3}` : connect; cursor and
  `CREATE TABLE` (no transaction); first `INSERT` (id 1 pending, transaction
  open); two more (ids 2 and 3 pending, `lastrowid` 3); `film_id`; print;
  block exit commits.
- `one-row-per-fetch` `{1-2|3-5|6-7|8,10|6-8,10|6-8,10|6-7|8-9}` : connect;
  `execute` (6 rows, `next` before row 1); first `fetchone`; test and print;
  second pass; passes 3 to 6 in one state (four output lines); `fetchone`
  returns `None`; `break`.
- `each-object-has-its-own-health` `{1|2|4|5|6|8|9}` : `hero` (Aria, 100);
  `troll` (Grok, 60); `troll.take_damage(25)` found on the class with
  `self is troll` (60 to 35); `hero.take_damage(10)` (100 to 90);
  `hero.heal(5)` (95); `hero.show_status()`; `troll.show_status()`.
- `object-first-then-class` `{1-3|6|7|8|9|10|11|12|13}` : class body
  (`max_health`, `__init__`); `hero`; `mage`; names read on the objects;
  `max_health` read through the class arrow; `Character.max_health = 120`;
  both read 120; `hero.max_health = 150` (new row on `hero`); final reads.
- `computed-on-every-read` `{1-7|9|10|11|12|13}` : class (`__init__`,
  `is_alive` property); `hero` (only `name` and `health` stored); `is_alive`
  found on the class (`30 > 0 is True`); `hero.health = 0`; read again
  (`0 > 0 is False`); assignment refused (`no setter`).

## Expected output

From running each demo with `uv run python` in a temporary directory
(`watchlist.db` made by `04_preparedstatements.py` first) :

| Slide | Output (state) |
| --- | --- |
| `closing-when-with-ends` | `True` (3), `So What` (5) |
| `moving-the-file-position` | `ffd8` (1), `2` (2), `b'JFIF'` (4), `ffd8` (6) |
| `inserts-wait-for-the-commit` | `Paddington 2 was added with id 3` (5) |
| `one-row-per-fetch` | `1 Spirited Away 125` (3), `2 Amélie 122` (4), rows 3 to 6 (5) |
| `each-object-has-its-own-health` | `Aria : 95 health` (5), `Grok : 35 health` (6) |
| `object-first-then-class` | `Aria Lumi` (3), `100 100` (4), `120 120` (6), `150 120 120` (8) |
| `computed-on-every-read` | `True` (2), `False` (4), `AttributeError: property 'is_alive' of 'Character' object has no setter` (5) |

`computed-on-every-read` ends on the uncaught exception, as the canonical
slide fence does; the demo file catches it and prints only the message.

## Author checks (2026-10-18)

Branch `t3/slidev-canonical-examples-rewrite` from `7c1766a`, with `aa47245`
and `e5e6aa3` merged; shared toolchain
`C:/Git/courseWare/_worktrees/presentation-template-slidev` at `f4f9ca1`.

- Every 09, 10 and 11 demo run in a temporary directory with copies of the
  demo folder (`input` fed `65`); module 10 in the order 01, 02, 03, 02, 05
  to 12, then 04, 09, 12 again; outputs as quoted on the slides.
- Every Python fence of the three module files and the seven native files
  executed in a temporary directory with the supplied data and a fresh
  `watchlist.db`. All run as shown; the failures are continuation fragments
  (their demos ran) and the intended `AttributeError`.
- `uv run ruff check` on the three demo folders : clean.
- `check-fences.py` : no problems; `check-slide-references.py` : all resolve.
- Scratch build : preamble and 09 to 11 copied to `build/slidev/scratch`,
  enrichments temporarily replaced by the seven above, then config restored
  (`git checkout`) and the scratch folder removed :

```bash
PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-slidev \
  bun run build/slidev.ts --slides-dir build/slidev/scratch
bun run build/slidev.ts --check-only
```

  `3 modules, 56 source slides, 66 pages, 75 original code/output fences`;
  `66 pages, 56 topics, 0 failures, 1 upstream warning`. Four canonical slides
  overflowed on the first build and were shortened until it passed.
- Not done, by request : browser click-through, reverse and reduced-motion
  runs, PDF and click exports, checker scripts.

## Coordinator adjustments needed

- `build/slidev.config.ts` : add the seven enrichments above
  (`each-object-has-its-own-health.md` is new). `compactSlides` entries
  `10-python-database-access-4/5/6` and `11-python-classes-9` still name the
  same slides (Using with, Inserting Data, Prepared Statements, `__str__` and
  `__repr__`); module 09 has none.
- `ruff.toml` : keep `"demos/09-python-io/**" = ["SIM115", "UP015"]`
  (SIM115 in 05 and 06, UP015 for `"rt"` in 06) but update its comment : the
  chapter now teaches `with` first and opens files by hand afterwards so older
  code can be recognised (Closing Files, File Object Attributes, Result of
  Calling open).
- `src/exercises/11-python-classes.md` line 236 : *When a Plain Attribute Is
  Not Enough* now turns `health`, not `length`, into a property.
- Unchanged and still true : Exercise 09 references (*File Open Modes*, *Using
  with*, *The csv Module*, *Paths with pathlib*), Exercise 10 (*Last inserted
  row id* uses `:memory:`; *Filtering and Grouping Data* keeps `COUNT`, `SUM`,
  `COALESCE`), Exercise 11 titles.
- Release workflow : no change (folder allowlist). `build/notes/slide-gaps.md`
  and `build/tasks.md` mention old demo files historically only.
- Review targets : `moving-the-file-position` draws an 11-cell row with a
  `...` cell; `each-object-has-its-own-health` notes reach about 640 px
  right of the visual's origin in the side layout.
