> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# Slidev appendices package

Recorded 2026-10-18. The last native animation package : one addition in each
appendix, on the canonical music examples refreshed by the coordinator in
`46dfeb5` (see [engaging-examples.md](engaging-examples.md) and
`build/slidev-agent-brief.md`). Canonical appendix slides and demos are not
changed. Native slides follow the approved Data Structures pilot : stationary
code with an active line, moving values, reversible click steps, reduced
motion through `DataStructuresRun`'s `--ds-time`, fixed geometry and no font
scaling or pagination.

## Insertion table

| Module | Insert after (existing title) | Native file (`src/slidev/appendices/`) | States | Clicks | Demo | Layout | Visual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12-appendix-type-hinting` | `Optional Values` | `a-lookup-that-may-find-nothing.md` | 7 | 6 | `12-appendix-type-hinting/03_optional.py` (lines 1-2 and 9-14, verbatim) | stack, output 230px | `AppendixOptional` |
| `13-appendix-libraries` | `The json Module` | `a-playlist-round-trip.md` | 5 | 4 | `13-appendix-libraries/04_json_strings.py` (whole) | stack, output 280px | `AppendixJson` |

12 states, 10 clicks. Scratch-build routes : `12-appendix-type-hinting-4-enhancement`,
`13-appendix-libraries-5-enhancement`. Pills : `demo03 · optional`,
`demo04 · json_strings`.

Enrichments for `build/slidev.config.ts` :

```ts
{ module: '12-appendix-type-hinting', after: 'Optional Values', file: 'src/slidev/appendices/a-lookup-that-may-find-nothing.md' },
{ module: '13-appendix-libraries', after: 'The json Module', file: 'src/slidev/appendices/a-playlist-round-trip.md' },
```

No `compactSlides` change is needed; `13-appendix-libraries-1` keeps its entry.

## Components

New, uniquely named, scoped styles; each header comment documents its state
schema. Each slide keeps its data as one JSON object (`const run = {...}`),
inside the existing `DataStructuresRun` shell. No existing component is edited.

| Component | Role |
| --- | --- |
| `AppendixOptional.vue` | A dictionary as key/value rows with its annotation (`dict[str, int]`); a dashed slot for a key the lookup did not find; one lane per kind of result of `-> int \| None`; caller names; chips (`'Comet'`, `None`) that move between explicit places and can enter from where they were made; a test badge (`is None → True`) |
| `AppendixJson.vue` | Two dictionaries as key/value rows (a list value as item cells) and the JSON `str` between them. Each text line flies in from the row or list item it was written from; each restored row flies in from its text line; a `hi` part (`null`) and rows can be marked; for `==` the text dims and same-key rows are joined by lines marked `==` |

## How the states map to execution

- `a-lookup-that-may-find-nothing` `{1-2|5|6|2|6|7|8}` : definition, the
  annotation's two lanes (`int`, `None`); `durations` (`'Orbit'` 222,
  `'Echo'` 185); the call binds `title` to `'Comet'` (caption : the same
  dictionary as `durations`); `.get(title)` : a copy of `'Comet'` moves from
  `title` into the dashed key slot, marked `not a key`, and `None` emerges from
  the empty value slot into the `None` lane; the call ends and `None` moves into
  `seconds` (the lane stays lit); `seconds is None` is `True`; the `None` branch
  prints. The final caption names the `else` branch, which would receive an `int`.
- `a-playlist-round-trip` `{1-3|4|5|6|7}` : `playlist` (name, tracks as
  `'Orbit'` `'Echo'`, cover `None`); `dumps` : eight lines fly from their rows,
  `cover` up to first place (`sort_keys`), `"Orbit"` and `"Echo"` from their
  item cells in order, `None` and `null` both marked; `loads` : `restored`
  rows fly from their text lines in the text's order (`cover`, `name`,
  `tracks`, as `list(restored)` gives), `null` and `None` marked; `print(text)` ;
  `restored == playlist` pairs the rows by key, the joining lines cross.

## Expected output

From `uv run python` in each demo folder (Python 3.14.3) :

| Slide | Output (state) |
| --- | --- |
| `a-lookup-that-may-find-nothing` | `Track not found` (6) |
| `a-playlist-round-trip` | the eight JSON lines (3), `True` (4) |

`03_optional.py` also prints `222` from `parse_seconds`, which the native slide
does not show (that function is not on it). Checked separately :
`list(restored)` is `['cover', 'name', 'tracks']`, `restored is playlist` and
`restored["tracks"] is playlist["tracks"]` are both `False`.

## Author checks (2026-10-18)

Branch `t3/8cd1a711` from `606d34f`; shared toolchain
`C:/Git/courseWare/_worktrees/presentation-template-slidev` at `82f5134`.

- Both demos run with `uv run python` : output as above.
- A throwaway inline Python snippet parsed each `run` as JSON, confirmed that
  states, fence ranges, output groups and captions have equal counts (7 and 5),
  executed each displayed fence with `python -I -c` (output equals the
  flattened `run.output`) and confirmed every displayed line is a demo line.
- Scratch build : preamble, 12 and 13 copied to `build/slidev/scratch`,
  enrichments temporarily replaced by the two above, then config restored
  (`git checkout`) and the scratch folder removed :

```bash
PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-slidev \
  bun run build/slidev.ts --slides-dir build/slidev/scratch --check
```

  `2 modules, 26 source slides, 30 pages, 32 original code/output fences`;
  `30 pages, 26 topics, 0 failures, 1 upstream warning`.
- A temporary screenshot of every click state of the two routes (and one frame
  260 ms into each forward step) was looked at once for overlap; it led to
  moving the `==` badges to the restored row ends and keeping the `None` lane
  lit. Screenshots and script were outside the repository and not kept.
- Not done, by request : reverse and reduced-motion runs, PDF and click
  exports, full-course build, checker scripts.

## Coordinator adjustments needed

- `build/slidev.config.ts` : add the two enrichments above.
- Release workflow, README and checks : no change needed for this package.
- Review targets : the restored `None` row's change tone and the crossing
  `==` lines in the final state; the `seconds` box ends about 70 px left of the
  output panel in `a-lookup-that-may-find-nothing`.
