# Exercise 2 : A Listening Log Tool

Turn a fixed listening report into `logtool.py`, with `count` and `errors`
subcommands. `data/listening.log` is fictional personal history. Each line has
an ISO date, time, level, action and track title. Titles can contain spaces.
`count` reports successful `INFO` plays and skips per title. `errors` selects
lines at one level.

Start from `exercises/starters/02-command-line-programs/`. Run from `libraries/`.
The complete solution is in `solutions/solution02-command-line-programs/`.
Use invented data, not files from work.

### Step 1 : Accept a file

Run `solutions/solution02-command-line-programs/logreport_start.py` to see the
fixed report. Give your own script an `ArgumentParser` with a positional
`logfile` argument converted to `Path`. Read that path instead of a constant.
Use `line.split(maxsplit=4)` to retain a title containing spaces.

:::hint
The slides *ArgumentParser* and *Path Arguments* show positional arguments and
`type=Path`. The fundamentals string demos show `split`; `maxsplit` limits how
many splits are made. The starter supplies the line-reading code.
:::

### Step 2 : Add subcommands

Register `count` and `errors` with `add_subparsers`. Attach each handler with
`set_defaults`. Both receive a logfile path. Give `errors` a `--level` option
with default `ERROR`.

Implement `count` with a dictionary or `Counter` keyed by action and title.
Print `PLAY` and `SKIP` counts for each title, ignoring other actions and
non-INFO lines. Implement `errors` by printing matching lines.

:::hint
The slide *Subcommands* and demo `subcommands` show handler registration.
The starter supplies the counting function, so the required work is the CLI.
:::

### Step 3 : Filter dates

Add `--since` to both commands. Accept an ISO date such as `2026-10-13` or a
fixed-width timestamp such as `2026-10-12 09:00:00`. Keep lines whose first
19 characters are at least that value. ISO dates in this format sort in date
order as strings. Keep the unfiltered lines when the option is absent.

:::hint
The slide *Options and Flags* shows optional values. The fundamentals string
and comparison slides show slices and `>=`.
:::

### Step 4 : Report statuses

Return 0 for a successful count or no matching errors, 1 when `errors` finds
lines, and 2 when the file cannot be read. Print file errors on stderr.
Use `raise SystemExit(main())` at the entry point. With no verb, show help.

Run these commands and inspect their exit statuses:

```bash
uv run python work/logtool.py count data/listening.log
uv run python work/logtool.py errors data/listening.log --level WARN
uv run python work/logtool.py errors data/listening.log --level FATAL
uv run python work/logtool.py count missing.log
```

The statuses are 0, 1, 0 and 2 respectively.

:::hint
The slides *main and the Exit Status* and *Standard Output and Standard Error*
show the entry point and diagnostic stream.
:::

### If time permits

Accept `-` as the input path and read stdin. Add `--quiet` to suppress results
while retaining the exit status. Add PEP 723 metadata to make dependencies
explicit if adding a rich table.

:::hint
The demo `unix_citizen` shows stdin, quiet mode and grep-style statuses.
The slide *Inline Script Metadata* shows a PEP 723 block.
:::
