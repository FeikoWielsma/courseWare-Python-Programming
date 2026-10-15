# Orchestration log : the PRG400 rework

Coordinator : the T3 thread that wrote `build/plan.md` (Claude Opus 5.5).
Integration branch : `prg400-wordle`. `master` is untouched until the trainer says so.
Read this first after a context reset or a quota interruption.

## Provider policy (from the trainer)

- Spread evenly, in the order claude >= codex > cursor > antigravity.
- Use the small models (GPT-6-Luna, Claude Haiku 5.5) wherever the work allows.
- Prose (exercise texts, slide wording) : Claude Opus 5.5, also reachable through Cursor.
- Quotas are $20 plans on each provider; 5-hour and weekly limits will be hit.
  Auto-continue is on. Claude runs out first.

## PAUSED by the trainer (2026-10-15)

Four packages were stopped mid-run with `task_cancel`, and their uncommitted work
saved as a WIP commit on their own branch. To resume, delegate each again with
its original brief (the client ids below, suffix `-r2` / `-r3`) plus one line :
"Continue from branch X : `git merge X` first, then read `build/notes/<wp>.md`".

| WP | Branch (worktree) | State at pause |
|---|---|---|
| WP2a exercises 1-4 (Claude Opus) | `t3/wordle-exercises-1-to-4` (t3-1522ee25), WIP 7e16656 | 3 commits + WIP |
| WP2b exercises 5-8 (Codex Astra) | `t3/wp2b-exercise-texts` (t3-bf58baee), WIP 1034e20 | 8 commits + WIP; WIP includes `build/site/dist`, drop it on merge |
| WP2c exercises 9-13 (Cursor Grok) | `t3/wp2c-exercises-9-to-13` (t3-4d482653) | nothing committed; restart |
| WP3b slides 04-06 (Antigravity) | `t3/wp3b-slides-demos-1` (t3-947a50aa), WIP 452f2ab | 2 commits + WIP; WIP includes `build/site/dist`, drop it on merge |

Everything else in the table below is merged into `prg400-wordle`.

## Status (2026-10-15, early morning)

| WP | Model | State |
|---|---|---|
| WP0 site port | Codex GPT-6.1-Sol | **Done, merged** : Presentation-Template `main` 27549e1 (local, not pushed). PySpark branch `shared-exercise-site` (d71b35d, 2c55b86) left unmerged for the trainer : PySpark `main` has unrelated uncommitted files. PRG400 wiring merged (fc2ed95). |
| WP1 solutions chain | Codex GPT-6-Luna | **Done, merged.** 13 stages, `build/check-solutions.py` in CI. |
| WP3c slides 07-09 | Codex GPT-6-Astra | **Done, merged**, config follow-ups applied (b232795). |
| WP3e appendices | Antigravity Gemini 3.8 Flash | **Done, merged.** |
| WP3a slides 01-03 | Claude Opus 5.5 | **Done, merged** (15abf7e, follow-ups 4fab5be). Open : module 04's summary still names operators (WP3b's); the `List Operations` slide carries a `listsasstacks` pill it does not show; Exercise 1 runs `uv run ruff` without adding ruff (WP2a); the code font renders `!=` and `<=` as ligatures in tables. |
| WP3d slides 10-11 | Claude Opus 5.5 | **Done, merged** (581051c). Open : `demos/11-python-classes/extraoo/` (old inheritance and classmethod material) still ships; archive it. |
| WP3b slides 04-06 | first Cursor Opus (failed : Cursor has only Grok/Auto left), now **Antigravity Gemini 3.8 Flash**, task `prg400-wp3b-r2`, continuing from branch `t3/wp3b-slides-demos` (4f6356a) |
| WP2a exercises 1-4 | Claude Opus 5.5 | Running, `prg400-wp2a-r1` (queued behind the rate limit) |
| WP2b exercises 5-8 | Codex GPT-6-Astra | Running, `prg400-wp2b-r1` |
| WP2c exercises 9-13 | Cursor Grok 4.7 | Running, `prg400-wp2c-r1` |

Notes :
- Cursor : only Grok and Auto have quota left. Do not route Opus through Cursor.
- The Chrome EBUSY crash is fixed in Presentation-Template `main` (4917847) : the
  build gives Chrome a profile directory it owns. Lint and build pass again.
- `build/site.config.ts` : the "Run the game" row says `uv run python -m wordle`
  for every exercise, wrong for Exercises 1 to 5 (`wordle.py`). Fix per exercise.
- WP2 exercise texts reference slide titles in italics while WP3a/b/d are still
  renaming slides : after all merges, check every italic reference resolves.

## Next, in order

1. As each WP3 finishes : review its report, merge its branch into `prg400-wordle`
   (`git merge --no-ff`), apply the coordinator-only changes it asks for
   (`ruff.toml` paths after demo renames, `check-fences.py` ignores), run all gates
   plus build and lint, commit.
   Expected overlaps : WP3a and WP3b both edit `04-control-flow-and-operators.md`
   (WP3a removes the operator slides, WP3b the rest); WP3a removes bytes from 03 and
   WP3c adds it to 09.
2. When WP1 finishes : merge; wire `build/check-solutions.py` into CI; regenerate and
   check starters.
3. When WP0 finishes : review the Presentation-Template branch and the PySpark
   comparison, merge `exercise-site` into Presentation-Template `main` (CI clones
   template `main`), merge the PRG400 site-wiring branch.
4. WP2 exercise texts, after WP1 (and ideally WP0), in `:::` markup, Claude Opus 5.5
   (direct or via Cursor) : WP2a Ex 1-4, WP2b Ex 5 conversion and 6-8, WP2c Ex 9-13.
5. Extras after WP2 : the PRG400 quiz (Q12) and a hidden Wordle Easter egg on the
   site (Q14), small models.
6. WP4 remainder : docs (`AGENTS.md`, `MAINTAINING.md`, `README.md`) on the spine,
   starters and the site; devcontainer check.
7. WP5 student review on a different provider from the authors, then a fix round.
