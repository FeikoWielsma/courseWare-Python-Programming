> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# Libraries migration safety net

Implemented 2026-10-18, before the mechanical Slidev migration in
[libraries-slidev-plan.md](libraries-slidev-plan.md). The fundamentals working
changes were left in place. No engine default or release asset names changed.

## Initial findings

The first checks ran against the original libraries content and deliberately
reported failures rather than substituting network responses in the runner:

- 119 demos compiled, including six interactive GUI demos. Of 113 executed
  demos, nine failed: the first argparse demo and eight scraping demos.
- `03_first_parser.py` required a second positional argument that its bare-run
  sample did not supply. Its calculation also disagreed with the slide.
- Scraping demos 01–05, 07, 08 and 10 made live requests despite the README's
  offline promise. Both scraping solutions also required the network.
- The output audit found two mismatches: the NumPy memory-output labels differed
  from the demo, and pandas `last_patched` was shown as `str` although the demo
  parses it as `datetime64[us]`.
- The inventory's page count was outdated. The actual Marp PDF has 168 pages,
  verified with the shared toolchain's `pdf-lib`, rather than 162.

Original per-command JSON records are retained locally under the ignored
`libraries/build/initial-baseline/`. The original Marp source and PDF are under
`libraries/build/marp-baseline/combined.md` and `course.pdf`. SHA-256:

```text
combined.md  4971d6fd24a33c796fc7c3c4723326b5b07bbfbf4b1c672a2d413af13147c9e3
course.pdf   9bf812113646889e64653d7b9845b6cc03e77cfe84f0f8b246d931a502e3fb35
```

These generated files are local evidence, not checked-in teaching artifacts.
Before Phase 1, regenerate a Marp baseline from the repaired sources so that
the mechanical migration compares identical content in both engines.

## Repairs and checks

The argparse demo now accepts one integer and prints its square, matching its
existing slide. The duration-formatting rewrite remains in Phase 2.

Scraping demos use the existing first-page HTML fixture by default. `--live`
retains real requests; demo 01 builds an explicit fixture-backed response object.
The scraping solution defaults to the fixture's first page and uses both live
pages only with `--live`. The query solution can also rebuild its database
offline. The handout and README explain this distinction. No second page is
fabricated or silently duplicated.

The NumPy and pandas output fences now match their demos. README module 08
explicitly says that it has interactive demos and no handout or solution.

New scripts under `libraries/build/`:

- `check-demos.py`: compiles all demos and runs every non-interactive demo from
  its own folder, with a 45-second per-command timeout.
- `check-solutions.py`: runs all 24 solution scripts and eight additional
  documented logtool commands, including stdin, help, missing files and the
  intentional statuses 1 and 2. Checks count output and error stream placement.
- `check-outputs.py`: audits all 13 text fences. Five literal stdout excerpts
  are checked against executed demos; eight annotated references or recorded
  benchmark outputs have explicit classifications. New Python/text pairs run
  the Python fence. Unknown or stale classifications fail.
- `check_support.py`: copies the course into temporary storage, so databases,
  reports and plots cannot overwrite working files. A Python audit hook blocks
  socket resolution, connection and send attempts; Python children inherit the
  hook. A caught network exception still fails the check. This is an execution
  guard for these Python examples, not an operating-system network sandbox.

Raw results go to ignored `libraries/build/demo-baseline/`. Stdout comparisons
allow whitespace differences and omitted surrounding output, retaining token
order and values. The exercise handouts currently contain no `text` output
fences; prose claims and annotated diagrams are not a complete executable
exercise-output contract yet.

CI runs all three scripts and invokes the existing shared fence checker from
`libraries/`, which audits both its slides and its handouts. The ignore rule now
allows versioned Python/build configuration files under `libraries/build/`
while keeping generated outputs ignored. The student allowlist still removes
that entire build directory.

## Verification

Executed from the course root unless indicated:

```bash
uv run --project libraries python libraries/build/check-demos.py
uv run --project libraries python libraries/build/check-solutions.py
uv run --project libraries python libraries/build/check-outputs.py
uv run --project libraries ruff check libraries
uv lock --check --project libraries
bun run --cwd build lint:libraries
bun run --cwd build libraries -- --skip-lint --force
bun run --cwd build libraries -- --exercises --force
# From libraries/:
uv run python ../../Presentation-Template/build/tools/check-fences.py
```

Results: 119 compiled / 113 executed demos; 32 solution commands; five stdout
quotes / eight classified references; 176 Python fences (173 complete modules,
three snippets). Zero findings in these checks, Ruff, lockfile and slide lint.
Both Marp documents build successfully. GUI windows were not launched and live
HTTP was not contacted.

Seven isolated behavior probes also passed: caught networking, networking in a
Python child, timeout, wrong stdout and wrong stream placement are rejected;
ordinary success and an expected nonzero exit are accepted. Probe JSON records
are ignored alongside the demo records.

## Next phase

Phase 1 is now complete; see [the migration record](libraries-slidev-phase1.md)
for routing, comparison, validation and delivery evidence. Phases 2 and 3 remain
open, including the music/photo rewrite and native additions. This Phase 0 pass
establishes the safety net and repairs the concrete failures it found.
