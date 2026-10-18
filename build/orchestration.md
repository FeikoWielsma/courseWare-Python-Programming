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

## DONE (2026-10-18)

Every package is merged into `prg400-wordle` (last : WP8a, b30458a). All gates pass
(fences, ruff, 13 solution stages, starters, quiz), the slides build and lint clean,
the exercises PDF and the site build, and every italic slide reference resolves.
What remains is the trainer's : see `build/tasks.md` Round 9.

## Resumed (2026-10-17) : the finishing wave

| WP | Model | Task id |
|---|---|---|
| WP2a exercises 1-4, from `t3/wordle-exercises-1-to-4` | Claude Opus 5.5 | `prg400-wp2a-r2` |
| WP2b exercises 5-8, from `t3/wp2b-exercise-texts` | Codex GPT-6-Astra | `prg400-wp2b-r2` |
| WP2c exercises 9-13, fresh | Claude Sonnet 5.5 | `prg400-wp2c-r2` |
| WP3b slides 04-06, from `t3/wp3b-slides-demos-1` | Antigravity Gemini 3.8 Flash | `prg400-wp3b-r3` |
| WP6 site extras : quiz, Wordle egg, per-exercise run rows | Codex GPT-6-Luna | `prg400-wp6-r1` |

**Result of the wave (2026-10-17) :** WP2a, WP2b, WP2c, WP3b and WP6 merged; the full
build passes (slides, lint, exercises PDF, site with quiz). WP7 (Claude Sonnet 5.5,
`prg400-wp7-r1`) is fixing the solution / text mismatches WP2c found in Exercises
9 to 13. After it : WP5, the student review, on Codex GPT-6.1-Sol (wrote no texts).

**WP5 review (Codex GPT-6.1-Sol), merged 0fafe8b :** no blockers, 12 major and 14
minor findings in `build/notes/wp5.md`; Day 4 estimated at 280 against 195 minutes.
Fix round running : WP8a solutions and texts (Claude Sonnet, `prg400-wp8a-r1`),
WP8b factual slide errors (Codex Astra, `prg400-wp8b-r1`), WP8c site egg, starter
rows and PDF pagination on template branch `exercise-pdf-pagination` (Codex Luna,
`prg400-wp8c-r1`). F25 (README) fixed by the coordinator.

**Fix round :** WP8b (slide facts) and WP8c (site egg, starter rows) merged; the
template's `exercise-pdf-pagination` is merged into its `main` (3d146e1). WP8a
(solutions and texts) hit the Claude limit; its queued run resumes on its own.
All gates and the full build pass on the merged state.

Done by the coordinator meanwhile : `extraoo/` archived, the List Operations slide
shows its stack demo, README / MAINTAINING / AGENTS document the spine (7956916).

Still to do after this wave : merge each branch (drop any `build/site/dist/`),
check every italic slide reference in the exercises resolves, build the site and
both PDFs, CI wiring for `check-quiz.py` and for building the site into the
release and the bundle, then WP5 (a student review on a provider that wrote none
of the texts) and a fix round. Pushing Presentation-Template `main` (CI clones it)
and merging into PRG400 `master` wait for the trainer.

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

---

# Toolchain simplification run (started 2026-10-18)

Design: `build/notes/courseware-toolchain-simplification.md`. Brief: `build/agent-brief.md`.
Integration: course `toolchain/integration` (`_worktrees/prg-toolchain-int`), template
`feature/courseware-cli` (`_worktrees/presentation-template-cli`).
Providers: Claude (Sonnet coordinator, Opus 5.5 for hard work, Haiku 5.5 menial),
Antigravity Gemini 3.8 Flash and Cursor Grok 4.7 (menial), Codex Luna/Sol after its
quota resets. Expect quota cut-offs: every package commits often and keeps its notes
file; resume from branch + notes.

| Package | Agent | Branch | Status |
|---|---|---|---|
| T0 baselines (Python decks, two unrelated courses) | Haiku 5.5 | `tc/baseline` | merged; baselines in _baselines (Python, Go, PowerShell; Git-Fundamentals and Bash have no build tooling) |
| T1 inventory of commands, consumers, deliverables | Gemini 3.8 Flash | `tc/inventory` | merged |
| T2 browser/serving duplication survey | Grok 4.7 | `tc/browser-survey` | merged; feeds stage 6 |
| T3 shared orchestration entry + migrate both decks (stage 1-2) | Opus 5.5 | template `feature/courseware-cli` (aa78ed9 + docs), course `tc/stage1` | merged into integration; template branch NOT yet merged to Presentation-Template main (additive; merge after all stages + 2-course regression) |
| T4 outputs separation + artifact manifest (stage 3) | Opus 5.5 | template `feature/courseware-cli`, course `tc/stage3` | launching |
| T5 shared browser/serve module in the template (stage 6a) | Grok 4.7 | template `feature/courseware-browser` (139b7d5, 4a9b1ce) | done; to merge into feature/courseware-cli after T4; course checks (stage 6b) wait for T4 to avoid path conflicts |
| T6 notes index + history banners (stage 7 prep) | Gemini 3.8 Flash | `tc/docs` | merged. Follow-up (coordinator): AGENTS.md still tells agents to read `slidev-handoff.md`, now bannered historical; point it at `build/notes/README.md`; write the MAINTAINING.md operating guide from `toolchain-docs.md` outline after stages 3-5 |
