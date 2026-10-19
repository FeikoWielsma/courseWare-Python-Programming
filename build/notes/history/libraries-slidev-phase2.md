> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# Libraries Slidev Phase 2

Completed 2026-10-18. Scope: the optional course under `libraries/`.
The fundamentals and Wordle exercise contracts are outside this change.

## Content and data

The CLI, toolbelt, pandas and tkinter examples now share a music library.
NumPy uses a generated tone, a photo array and a days-by-hours listening grid.
Inheritance uses Character, Mage, Warrior and Priest, with Mount and Inventory
for composition. The scraper toolkit capstone and the scraping/SQLAlchemy book
dataset remain. The subprocess appendix received a wording and log-data pass.

Slides, demos, eight exercise handouts, solutions and new standalone starters
were updated together. Exercise hints name the relevant slide or demo. There is
no GUI exercise. The tkinter sequence adds a readonly genre Combobox and a
Choosing a Genre slide. SQLAlchemy now demonstrates flush explicitly before
commit. Demo fences were aligned with their source scripts.

`libraries/build/make-data.py` regenerates 40 tracks, ten artist lookup rows,
listening events, a 7 by 24 plays grid, the 64 by 48 photo, spreadsheets,
database and reports. Twelve committed artifacts reproduce; PNG files compare exact decoded pixels.
Song metadata identifies its release edition; some durations therefore differ
from the fundamentals examples. Counts and listening dates are fictional.
See [the source record](../../../libraries/data/SOURCES.md) for metadata and NASA
photo attribution. Older inventory files remain for the optional reference GUI
examples; live course demos use the new data.

## Native additions

Ten additions cover method lookup, constructor state, HTML tree navigation,
session persistence, views/copies, broadcasting, axes, selections, grouping and
join types. They reuse DataStructuresRun, StatefulObjects and CoreNames, with
one new ArrayGrid renderer for arrays and frames.

`libraries/build/native_states.py` executes demo excerpts to produce the code,
stdout and displayed state. Its `--check` mode compares all 55 states and the
generated Markdown. Constructor states use execution tracing; session states
use SQLAlchemy inspection. Data and native-state checks also run in CI.

Browser checks covered forward and reverse state changes, output, grid values
and containment. Focused review found and fixed method-lookup positioning and
join-caption overflow. The final broadcasting sequence was rechecked after
removing an unrelated second example. All ten additions were visually inspected.

## Verification

| Check | Result |
|---|---|
| Data regeneration | 12 artifacts match: exact bytes or exact PNG pixels |
| Native state regeneration | 10 additions, 55 executed states match |
| Demo runner | 119 compiled, 113 executed, zero failures |
| Solution runner | 37 command cases, zero failures |
| GUI Windows smoke | Six windows constructed; add, sorting and SQL filtering checked |
| Fence audit | 144 Python fences: 139 complete, five snippets; zero findings |
| Slide references | All exercise slide references resolve |
| Output audit | No literal stdout quotes; five reference blocks classified |
| Ruff | Zero findings |
| Libraries lockfile | Pass; no new dependencies |
| Slidev build and validation | 179 pages, 160 topics, zero failures |
| Slide budgets | All within budget |
| Marp fallback | 169 PDF pages; HTML also built |
| Exercise PDF | Built successfully |
| Student presentation ZIP | 302 public entries; PDF identical to canonical PDF |

The 179 Slidev pages comprise 160 canonical topics, nine module overviews and
ten native additions. Validation blocks external HTTP. It retains one known
upstream FloatingVue warning. The ZIP contains no source, build or notes
directories and no Markdown, Vue or TypeScript authoring files.

Reproduce the implementation checks from the repository root:

```bash
uv run --project libraries python libraries/build/make-data.py --check
uv run --project libraries python libraries/build/native_states.py --check
uv run --project libraries python libraries/build/check-demos.py
uv run --project libraries python libraries/build/check-solutions.py
uv run --project libraries python libraries/build/check-outputs.py
uv run ruff check .
uv lock --check --project libraries
bun run --cwd build libraries
bun run --cwd build libraries:marp -- --skip-lint --force
bun run --cwd build libraries -- --exercises --force
```

Run the shared fence and slide-reference checkers from `libraries/`.
Raw run logs, browser QA payloads and build artifacts remain ignored.

## Phase 3 closeout

The delivery review, browser and Linux GUI checks, PDF visual review, bundle
review, and teaching-examples update are recorded in
[the Phase 3 delivery record](libraries-slidev-phase3.md). No release was
published by this work.
