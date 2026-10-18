> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# Plan : Libraries and Tools to Slidev, with an example rewrite

Drafted 2026-10-18. Scope: the optional companion course in `libraries/`
(`PRG400-Python-Libraries-and-Tools`). Read with the course `AGENTS.md`,
[slidev-handoff.md](slidev-handoff.md), [slidev-rollout.md](slidev-rollout.md)
and [engaging-examples.md](engaging-examples.md). Nothing here touches the
fundamentals deck or the Wordle exercise spine.

Implementation status, 2026-10-18: Phase 0 is implemented and verified, including
repairs for the failures found on the original content. The measured Marp baseline
is 168 pages. See [the findings and verification record](libraries-review.md).
Phase 1 is also implemented and verified; see
[the migration record](libraries-slidev-phase1.md). Phase 2 is implemented and
verified: shared data, example and exercise rewrites, and ten native additions.
See [the Phase 2 record](libraries-slidev-phase2.md). Phase 3 is implemented and
verified; see [the Phase 3 delivery record](libraries-slidev-phase3.md).

## 1. Where it stands

| | Fundamentals (`src/`) | Libraries (`libraries/`) |
|---|---|---|
| Engine | Slidev default, Marp fallback | Marp only, through `build/libraries.ts` |
| Source slides | 230 | 162 in 9 modules plus preamble |
| Code fences | 299 | 124 `python` fences, 3 Mermaid diagrams |
| Demos | per module | 119 files; 6 `INTERACTIVE` tkinter demos |
| Exercises | Wordle spine, 13 stages | 8 independent exercises with solutions, no exercise 08 |
| Automated checks | fences, refs, ruff, starters, solutions, animations, delivery | ruff and lockfile only |
| Examples | music, photos, films, WoW | server inventory, books.toscrape, temperatures, employees |

The shared template already has the Slidev build on `main`
(`2c1d0f8 Merge branch 'feature/slidev-foundation'`), so this migration needs
no shared-template feature work. It only needs course-side wiring, unless a
blocker turns up in Phase 1.

Things found while inventorying, to fix along the way:

- `demos/02-command-line-programs/03_first_parser.py` describes "the square of
  a number" but prints `number**2 + number2`.
- In module 02, `/// script` metadata lines inside a fence start with `# `.
  Check that the Slidev converter does not treat them as slide headings. A
  `grep "^# "` counts them as titles.
- Exercise 08 (GUI) has no handout or solution. That is deliberate (interactive
  only), but the README table should say so.
- `libraries/build/` holds only `dist/` and the logo. There is no slide config
  and no demo or solution runner.

## 2. Decisions for the trainer

Each decision has a recommendation; the plan below assumes it.

| # | Question | Recommendation |
|---|---|---|
| D1 | Default engine for libraries | Slidev default, Marp kept as `libraries:marp`, mirroring the fundamentals |
| D2 | Native animated additions | A small set, ~10 additions, only where state is the lesson (§5). Not the 33-addition depth of the fundamentals |
| D3 | Theme for the data modules (NumPy, pandas, GUI, toolbelt, CLI) | Music listening history: real songs and real lengths, the learner's own invented play counts. This continues module 09's CSV listening history |
| D4 | Inheritance module | WoW, continuing Classes: `Character` → `Mage`/`Warrior`/`Priest`; keep the scraper toolkit as the applied capstone |
| D5 | Web scraping and SQLAlchemy | Keep books.toscrape.com: it is a real, legal practice site, and the offline fixture already exists |
| D6 | NumPy | Photos as arrays (shape, slicing, axis) and a generated audio tone (vectorised arithmetic, `np.where`, random) |
| D7 | Subprocess appendix | Light touch: it is about running real programs (`git`, `python`); only the wording is aligned |

## 3. Phase 0 : safety net before changing anything

There are no automated libraries checks today, so add them first. Both the
migration and the rewrite then have something to measure against.

1. **`libraries/build/check-demos.py`**:
   - Runs every non-interactive demo with `cwd` at its folder and network
     disabled, with a timeout.
   - Records exit status and stdout to a baseline in
     `libraries/build/demo-baseline/`, ignored by git.
   - Skips `# INTERACTIVE` demos but compiles them.
   - Fails if a demo needs the network: `httpx`/`requests` demos must use their
     offline transport or fixture.
2. **`libraries/build/check-solutions.py`**: runs every solution script and its
   documented command line. Where an exercise quotes output, compare against
   the handout.
3. **Fence audit**: reuse the shared `check-fences.py` against
   `libraries/src/slides`. Add the slide-output audit used for the
   fundamentals: execute `python` fences followed by `text` fences and compare.
4. **Wire into CI**, in `.forgejo/workflows/release.yml` beside the existing
   `libraries` steps: `uv run --project libraries python libraries/build/check-demos.py`
   and `check-solutions.py`.
5. **Record the Marp baseline**: page count, `combined.md` and the PDF.
   Phase 1 compares Slidev against it.

Exit: both scripts pass on the unchanged content. Known failures are listed in
`build/notes/libraries-review.md` rather than fixed silently.

## 4. Phase 1 : mechanical Slidev migration, with no content changes

Goal: the same content on Slidev, one source slide per page, every fence kept.

1. **Wiring**:
   - Give `build/libraries.ts` the same routing as `build/course.ts`: default
     builds Slidev, `--marp` builds the fallback, `--exercises` is unchanged.
   - Add `libraries:marp` and `libraries:serve` scripts to `build/package.json`.
2. **Config**: create `libraries/build/slidev.config.ts` with title
   `Python Libraries and Tools`, the course accent, and empty `compactSlides`
   and `enrichments`.
3. **Build** with `bun run --cwd build libraries -- --skip-lint --compare` and
   fix what the validator reports:
   - geometry overflows, by adding explicit `compactSlides` entries (no
     automatic font fitting, per the handoff decisions)
   - Mermaid containment for the three diagrams
   - the `# /// script` fence in module 02
4. **Check wide content**: pandas `print(df)` output and NumPy 2-D arrays are
   wide. Check horizontal overflow in `PRE` (the check flags `PRE horizontal`).
   Prefer narrowing the demo output (`pd.set_option("display.width", …)`, fewer
   columns) over shrinking type, and keep slide and demo identical.
5. **Delivery**:
   - Produce `PRG400-Python-Libraries-and-Tools-slides.zip` with the student
     launcher, as the fundamentals do.
   - Keep the HTML copy step in `libraries.ts` for the Marp fallback only.
6. **CI and release**:
   - Replace `bun run libraries -- --skip-lint --force` with the Slidev build
     plus `--marp`, and keep `lint:libraries`.
   - Release assets: add the Slidev PDF and ZIP, and keep the Marp PDF/HTML
     names so existing links still work.
   - The bundle allowlist already ships `libraries/`. Confirm that
     `libraries/build` is still stripped and the slides ZIP travels as an asset.
7. **Docs**: update `MAINTAINING.md` §Optional libraries and tools and the
   `libraries/README.md` "What is in this bundle" list.

Exit:
- Slidev validation reports 0 failures with external HTTP blocked.
- Lint is in budget.
- Page count matches the Marp baseline plus generated overviews.
- All fences are preserved (the converter throws on loss).
- Comparison portal spot-check of every module.

Commit this phase separately so the rewrite diff is reviewable on its own.

## 5. Phase 2 : the example rewrite, module by module

Rules carried over from the fundamentals:
- Real names and real facts (song lengths, release years, book titles from
  books.toscrape).
- Invented numbers only where they are plainly the learner's own data (play
  counts).
- Every fence identical to its demo, and every quoted output produced by
  running it.
- Slide titles stay stable where an exercise cites them.
- No timings.

### Shared data (new, under `libraries/data/`)

| File | Contents | Replaces |
|---|---|---|
| `tracks.csv` | ~40 well-known songs: `title, artist, year, genre, duration_s, plays, last_played`. Lengths are real; plays are a fictional personal history; a few deliberate gaps for Missing Values | `servers.csv`, `servers.xlsx` |
| `artists.csv` | `artist, country, formed, members` for merge/join types; a few artists deliberately absent, so join types differ | `sites.csv` |
| `listening.log` | Timestamped `PLAY / SKIP / PAUSE` lines, plus some `WARN` lines (missing file, slow stream) | `cli-sample.log` |
| `plays-hourly.csv` | Plays per hour per day for NumPy aggregation and axis work | `server-load*.csv` |
| `photo.png` | A small own or public-domain photo, about 64×48, for photos-as-arrays | none (new) |
| report outputs | Regenerated from the new data | `servers-report.*`, `servers-plot.png` |

One generator script, `libraries/build/make-data.py`, writes the CSV, XLSX and
DB files deterministically, so the data can be rebuilt and reviewed. The
song list reuses the fundamentals cast (Imagine 183 s, Yesterday 125 s,
Respect 149 s, Toxic 199 s, Thriller 357 s, Hey Jude, Bohemian Rhapsody …) and
extends it to cover enough genres and decades for `groupby`.

### Module map

**01 Inheritance** (D4)
- Duplicated Code, Base Classes, Overriding and super: `Character` →
  `Mage(Character)`, `Warrior`, `Priest`. Health, mana and rage show what a
  subclass adds.
- Polymorphism: each class's `attack()` or `ability()` called in one loop over
  a raid group.
- Abstract Base Classes / Enforcing the Contract: an abstract `Ability` with
  `cast()`.
- Composition: a character *has* a `Mount` and an `Inventory`, contrasted with
  *is a* `Mage`.
- Scraper Toolkit: kept as the real-world capstone (it reuses module 04).
- Exercise 01: replace `employee.py`/`company.py` with a WoW party or guild
  roster, with the same learning goals: a base class, two subclasses,
  overriding, `super()`, an abstract method, composition.

**02 Command-line Programs**
- `sys.argv` → `argparse` with a `playlist.py` tool reading `tracks.csv`:
  - positional file and `--genre`/`--limit` options
  - mutually exclusive `--longest`/`--shortest`
  - subcommands `list`, `stats`, `top`
  - `Path`/`FileType` arguments
  - exit status on a missing file
- Fix `03_first_parser.py`: one positional, the duration in seconds, printed
  as `m:ss`. This reuses `format_duration` from the fundamentals.
- Exercise 02: `logtool.py` becomes a `listening.log` report: count plays and
  skips per title, `--since`, `--level WARN`, stdout versus stderr.

**03 Modern Toolbelt**
- `tqdm`: a progress bar while "converting" tracks (sleep-simulated);
  nested bars for albums and tracks.
- `rich`:
  - a table of the top tracks
  - progress
  - a traceback from a bad duration
  - `inspect` on a `Track` object
  - logging with a `listening.log` handler
- `httpx`/`requests`: keep the offline mock transport; the payload becomes a
  small JSON "now playing" response.
- `typer`: the same `playlist` CLI as module 02, which makes the trade-off
  slide concrete.
- Exercise 03: `health.py`/`health_cli.py` becomes a `library_check` tool that
  reports missing durations and duplicate titles, with a rich table and a typer
  CLI.

**04 Web Scraping**: unchanged dataset (D5). Wording pass only; check every
quoted output against the fixture.

**05 SQLAlchemy**: unchanged books dataset (D5). One optional enhancement: the
*sqlite3 and SQLAlchemy* slide could show the fundamentals film watchlist query
both ways. Decide at review; not required.

**06 NumPy** (D6)
- First array, memory use, speed: one minute of a 440 Hz tone
  (`np.sin` over sample times) against the same loop in plain Python.
- Shape, reshape, indexing, slicing, views and copies: `photo.png` read with
  `matplotlib.image.imread` as a `(height, width, 3)` array. Crop with slices,
  flip with `[::-1]`, and show that a view of the photo changes the original.
- Vectorised arithmetic, masking, `np.where`: change the volume of the tone,
  clip it with `np.where`, find silence with a boolean mask.
- Broadcasting: per-channel colour correction (`photo * [1.1, 1.0, 0.9]`).
- Aggregations, `axis`: `plays-hourly.csv` as a days × hours array. Busiest hour
  is `axis=0`, busiest day is `axis=1`. Photo brightness per row is the second
  example.
- Random numbers: shuffle play with `rng.permutation`, using a seeded
  generator.
- Exercise 06: server-load alerts become a listening-habits analysis. Keep the
  same six steps (load, per item, per hour, alerts → "binge hours", baseline,
  bands).

**07 Pandas**
- All `servers` frames become `tracks` (index `title`); `sites.csv` becomes
  `artists.csv` for `merge`/join types. `groupby` becomes genre and decade.
- Missing Values: tracks with no `last_played`.
- `read_sql`/`to_sql` keep their slides on the books database from module 05,
  which shows the handover between modules.
- Plotting: plays per decade.
- Exercise 07 already uses books; keep it, with a wording pass.

**08 GUI Toolkits**
- The inventory form becomes a playlist editor: entry for the title, a combobox
  for the genre, a Treeview of `tracks.csv`, then the Treeview backed by SQLite.
- These demos stay `INTERACTIVE`. Check them by hand on Windows and on Linux in
  the devcontainer.

**09 Appendix: Running Other Programs** (D7): keep `git --version` and
`python -c`. Align only the prose and the data paths.

### Native Slidev additions (D2)

Candidates, in priority order. Each one quotes its demo verbatim and gets a
Python-executed state check, like `build/slidev_checks/`.

| Module | After slide | Animation |
|---|---|---|
| 01 | Overriding Methods | Method lookup walks `Mage` → `Character` → `object` |
| 01 | Extending with super | `super().__init__` fills the `Character` part of a `Mage` object |
| 04 | Navigating the Tree | Cursor moves through parent, children and siblings of a book card |
| 05 | Session | Objects move from pending to flushed to committed |
| 06 | Views and Copies | Two names on one photo buffer; a write through the view shows in both |
| 06 | Broadcasting | Shapes `(h, w, 3)` and `(3,)` align and stretch, step by step |
| 06 | axis Argument | Collapsing a days × hours grid along `axis=0`, then `axis=1` |
| 07 | loc and iloc | Label versus position selection highlighted on the same frame |
| 07 | groupby | Split, apply, combine on the genre column |
| 07 | merge / Join Types | Inner, left, right and outer joins on `tracks` and `artists` |

Reuse the existing components (`DataStructuresRun`, `StatefulObjects`,
`CoreNames`, collection grids). A new component is only justified for the
array and frame grids: one `ArrayGrid` that serves NumPy and pandas. Add it to
the course's `src/slidev/components`. If the fundamentals could use it too,
move it to the shared template in a separate, regression-checked change.

## 6. Phase 3 : verification and delivery

- `check-demos.py`, `check-solutions.py`, the fence and output audit, and
  `ruff` all pass with zero findings.
- `uv lock --check --project libraries` passes. Add no new dependencies:
  `matplotlib.image` already covers PNG and the stdlib `wave` covers audio.
- Slidev build with `--compare`: 0 failures, lint in budget.
- Browser check of every native addition: forward and back, reduced motion,
  the restored state matches.
- Render each module's PDF pages into contact sheets and review them visually;
  spot-check the Marp fallback.
- Exercise PDF builds; each handout's quoted output matches its solution run.
- Student ZIP contains no `src/`, `build/`, notes or trainer material.
- Update `MAINTAINING.md`, `libraries/README.md`, the AGENTS teaching-examples
  rule (one line for libraries), and log the result in `slidev-rollout.md`.

## 7. Order of work and commits

1. Phase 0 checks, with the baseline recorded (commit).
2. Phase 1 Slidev migration, content unchanged (commit). The release can
   already switch here.
3. `make-data.py` and the new data files (commit).
4. Modules 07 → 06 → 08 → 03 → 02 first, since they share `tracks.csv`, then
   01, then the wording passes on 04, 05 and 09. One commit per module covering
   slides, demos, exercise and solution together.
5. Native additions, one commit per module, each with its state check.
6. Phase 3 delivery pass and docs (commit).

Modules are independent after step 3, so steps 4 and 5 can be split across
agents, one module per agent. The coordinator owns `make-data.py`, the configs,
CI and the docs.

## 8. Risks

- **pandas and NumPy output width** is the most likely source of overflow.
  Fix it in the demo (`display.width`, column selection), not with smaller
  fonts.
- **Real facts drift**: song lengths differ per release. Use the commonly
  cited album length and note the source in `make-data.py`.
- **Image licensing**: use a photo the trainer owns or one in the public domain.
  Record its source next to the file.
- **Interactive GUI demos** cannot be checked in CI. Keep them compile-only in
  CI and review them by hand.
- **Exercise contract changes**: handouts, solutions and quoted output must
  change together per module. `check-solutions.py` exists to catch drift.
- **Marp fallback**: keep building it until the trainer drops it. Native
  additions are Slidev-only and must not be required to follow the Marp deck.
