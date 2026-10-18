# Exercise 3 : Checking a Music Library

Build `library_check.py`, a report of missing durations and duplicate titles.
The supplied `data/tracks-import.csv` contains 41 records: one duplicated title
and one missing duration. Its play counts are made up, not from work.

Start from `exercises/starters/03-modern-toolbelt/`. Run from `libraries/`.
The solution is in `solutions/solution03-modern-toolbelt/`.

### Step 1 : Read the import

Use `csv.DictReader` to load `data/tracks-import.csv`. Print the number of records.
Keep the file path as an argument to `load(source: Path) -> list[dict[str, str]]`.

:::hint
The demo `tqdm_basics` loads the track CSV before starting its loop.
:::

### Step 2 : Find import problems

Write `find_issues(rows)` returning a list of `(title, problem)` tuples.
Report `missing duration` when `duration_s` is empty. Report `duplicate title`
when a title has already appeared. Maintain a set of seen titles during the loop.
Do not discard either record of a duplicate; report what was found.

:::hint
The demo `tqdm_write` tests an empty field while visiting rows. Sets and loops
were introduced in the fundamentals course.
:::

### Step 3 : Show progress

Wrap the checking loop with `tqdm`. Give it `desc="Checking"` and `unit="track"`.
Add `time.sleep(0.01)` inside the loop to simulate slower file inspection.
Use `tqdm.write` if printing a message while the bar is active.

:::hint
The slides *tqdm Progress Bars* and *tqdm.write* show these calls.
:::

### Step 4 : Print the report

Build a rich table with `Title` and `Problem` columns. Sort the issues by title
and add one row per issue. Colour the problem cell with rich markup.
Print the record and issue counts after the table. The fixture has two issues.

:::hint
The slide *rich Tables* shows `Table`, `add_column`, `add_row` and cell markup.
:::

### If time permits

Create `library_check_cli.py` with a typer command. Accept a source path and
`--strict`. Print the same table, returning status 1 when strict mode finds
issues and status 2 when the file cannot be read. Otherwise return status 0.

:::hint
The slides *typer* and *typer Trade-offs* show annotated parameters and
`typer.Exit`. *main and the Exit Status* in Command-line Programs shows the
meaning of exit statuses.
:::
