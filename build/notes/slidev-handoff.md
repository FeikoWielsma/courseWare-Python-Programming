# Slidev migration handoff

Updated 2026-10-18. Start here when continuing the presentation migration,
Marp parity work, comparison, theme, navigation or exports.

Current status: the 13-module rollout and teaching-example rewrite are complete,
with Slidev as the local build/delivery default and explicit Marp fallback.
Read [the current rollout and verification record](slidev-rollout.md) first.
It records 275 pages, 33 native additions, successful packaged-navigation checks
and the shared-template merge prerequisite for remote releases.

Historical context below records the original foundation handoff. Read
[the accepted migration plan](slidev-migration-plan.md) and
[integration evidence](slidev-integration.md) for subsequent decisions and the
subsequent decisions. The old stopping points and counts below are superseded
by the rollout record; production-template main remains untouched.

## Objective and current stopping point

The user wants a fair, full-course comparison of Marp and Slidev, with at least
Marp feature parity and useful native Slidev features. The working foundation
and batch conversion are complete. **Full feature parity has not been audited
or established.** The earlier completion messages referred to the foundation,
not to this expanded objective.

The most recent implementation request was:

> just keep going until we atleast have feature parity with the marp build so
> we can properly compare, while taking advantage of slidev features.

The user then requested this handoff. A parity investigation had started with
read-only inspection; no additional parity implementation or complete native
showcase module was built during that investigation. Resume with the audit below.
There is no automatic continuation or background agent implementing it.

## Start in the correct repositories

| Repository | Path | Branch and saved state |
| --- | --- | --- |
| Python course | `C:/Git/courseWare/Python-Programming` | `feature/slidev-course`; foundation commit `1c73280`, followed by the documentation handoff commit |
| Shared Slidev foundation | `C:/Git/courseWare/_worktrees/presentation-template-slidev` | `feature/slidev-foundation`; `2953b4e` foundation, `2d6f137` logo fix, `fb036ff` wheel navigation and matching syntax highlighting |
| Shared production checkout | `C:/Git/courseWare/Presentation-Template` | `main`, observed at `8dce2bd`; left unchanged |

Read the course `AGENTS.md`, shared writing style and conventions, and the shared
worktree's `AGENTS.md`. Shared edits belong in the worktree. The production
checkout services other courses. Before merging shared changes, its instructions
require before/after PDF page-count and per-page-text comparisons for two
unrelated courses. That merge check has **not** been performed. Nothing here was
pushed, merged, released or submitted as a PR.

Run `git status --short` in both working repositories before editing. The wheel
component, Shiki setup and their shared documentation are saved in `fb036ff`;
they are not pending files that can be discarded.

## User decisions to preserve

- Keep Marp and Slidev available side by side. Marp remains the release default.
- The early research compared Marp+, Reveal.js and Slidev; Custom Lab was dropped.
  The current implementation scope is Slidev adoption alongside Marp.
- IBM Plex Sans for headings/body; IBM Plex Mono for code and labels. Fonts are
  bundled locally. This was already implemented before the user's font question.
- Logo top-right; linked module name top-left, opening that module's overview;
  page number and demo/exercise markers bottom-right.
- No automatic pagination or automatic font fitting. Original one-page slides
  remain one page; use explicit layout choices for dense slides.
- Reveal code blocks, output, pictures and other content progressively. Backward
  navigation reverses reveals. Code blocks currently reveal as whole blocks;
  line-by-line code choreography is used only in native additions.
- Mouse wheel/trackpad navigation is implemented: down is next reveal/slide, up
  is previous reveal/slide. It follows arrow-key semantics, rather than skipping
  the remaining reveals to change pages immediately.
- Syntax highlighting now matches Marp: Shiki `min-light`, with comment colour
  replacement `#c2c3c5` -> `#4a9c59`. Magic Move uses the same theme.
- Keep canonical course prose, code fences, demos and the Wordle exercise spine.
  Native additions quote the existing neutral demos; slides stay non-Wordle.

## Implemented and verified baseline

All 13 fundamentals modules, including both appendices, plus the preamble are
converted. There are 226 source slides and 13 generated module overviews:
239 original Marp pages. Slidev retains each original page and adds two native
Magic Move examples, giving 241 pages. All 299 original code/output fences are
retained unchanged. The separate `libraries/` companion course is not converted.

There are 15 explicit compact-slide choices in `build/slidev.config.ts`, and an
explicit two-column layout for Accessing Lists in `src/slidev/style.css`. The
module overviews and source slides have stable route aliases based on module
slug and source position. Inserting original source slides changes later IDs in
that module; inserting enrichments does not.

The comparison portal synchronizes native Slidev navigation to the associated
Marp topic. It offers a source-topic picker, side-by-side/single-engine views,
full-size links, PDFs, converted Markdown and the manifest. This is not a fully
bidirectional synchronization mechanism: Marp navigation does not drive Slidev.

The two native additions are `src/slidev/list-mutation.md` (five code/collection
states) and `src/slidev/tuple-unpacking.md` (three code states). Their code comes
from demos `02_updatinglists.py` and `08_destructurewithtuples.py` in
`demos/03-datastructures/`. A Python checker executes snapshots and compares the
displayed state/output. These are two examples, not a fully enriched module.

Wheel behaviour lives in shared `build/slidev/template/global-bottom.vue`:
24px accumulated threshold, 180ms gesture quiet period, 700ms cooldown. It
ignores horizontal scrolling, Ctrl/Command-wheel, editable controls, dialogs,
scrollable content and non-presentation routes. Browser checks exercised forward
and reverse reveals, crossing slide boundaries, sustained momentum, zoom
exclusion and scrollable content. These wheel scenarios were checked manually
through browser automation; they are not yet permanent checks in `check.ts`.

## Commands and local preview

PowerShell, from the Python course root:

```powershell
# Only needed on a fresh setup; dependencies stay in the shared worktree.
bun install --cwd ../_worktrees/presentation-template-slidev/build
bun install --cwd ../_worktrees/presentation-template-slidev/build/slidev

# Build both engines and serve the comparison on port 4188.
bun run --cwd build slidev:compare

# Build Slidev, export the complete final-state PDF, validate the built course.
bun run --cwd build slidev --pdf --check

# A separate five-state PDF for the current list-mutation example.
bun run --cwd build slidev --with-clicks --range 53

# Validate existing output, or serve it without rebuilding.
bun run --cwd build slidev:check
bun run --cwd build slidev --serve-only

# Offline viewing from the generated delivery folder, without Node/Bun.
python build/slidev/dist/serve.py

# Verify the native Python snapshots against demos and displayed state.
uv run python build/check-slidev-examples.py

# Shared foundation checks.
bun run --cwd ../_worktrees/presentation-template-slidev/build typecheck
bun test --cwd ../_worktrees/presentation-template-slidev/build/slidev convert.test.ts
```

Use one server on 4188. A Python launcher was started during this session;
process lifetime is not guaranteed. Check the listener before starting another.
Refresh an existing browser after a static rebuild; merely changing its hash can
keep the previous JavaScript bundle loaded.

| View | URL when served on 4188 |
| --- | --- |
| Comparison | `http://localhost:4188/#03-data-structures-3` |
| Native list Magic Move | `http://localhost:4188/slidev/#/03-data-structures-3-enhancement` |
| Module overview | `http://localhost:4188/slidev/#/03-data-structures-overview` |
| Native browser exporter | `http://localhost:4188/slidev/#/export` |

`build/slidev.ts` selects `PRESENTATION_TEMPLATE_DIR` first, then the production
template if it has `build/slidev/build.ts`, otherwise the experimental worktree.
Use an explicit environment override if another agent changes those checkouts.
The separate Marp commands still call the production template directly.

## Implementation map

Paths below are relative to the shared worktree unless marked course.

| File | Responsibility |
| --- | --- |
| `build/slidev/convert.ts` | Source parsing, code preservation, click groups, stable routes, module overviews; config interface |
| `build/slidev/convert.test.ts` | Five converter regression tests |
| `build/slidev/prepare.ts` | Course discovery, image embedding, enrichment insertion, native workspace generation, manifest |
| `build/slidev/build.ts` | CLI, static build/server, portable Marp comparison, fonts/licenses and delivery files |
| `build/slidev/portal.ts` | Comparison page and topic synchronization |
| `build/slidev/check.ts` | All-page browser geometry, source coverage, offline assets and basic reveal checks |
| `build/slidev/export-pdf.ts` | Browser printing through native Slidev PrintSlide; page/state count checks |
| `build/slidev/pdf.ts` | Complete-course PDF metadata and outline bookmarks |
| `build/slidev/template/` | Native Vue components, layouts, theme CSS, setup and wheel handler |
| `build/slidev/package.json`, `bun.lock` | Isolated pinned Slidev/font dependencies |
| Course `build/slidev.config.ts` | Explicit compact layouts and native enrichment insertion points |
| Course `src/slidev/` | Native additions and explicit course CSS; future course components/layouts |
| Course `build/check-slidev-examples.py` | Execute native Python snapshots and compare demo lines/state |

The generated Vite project is under shared `build/slidev/.work/<course-hash>/` so
normal dependency resolution works. Its review copy is course
`build/slidev/converted.md`; static output is course `build/slidev/dist/`.
Both are ignored outputs. Edit source files, not generated copies. The complete
developer reference is shared `docs/slidev.md`; the historical implementation
report is course `build/notes/slidev-foundation.md`.

## Evidence and limits

- Latest `validation.json`: 241 pages, 226 topics, no failures; external HTTP
  blocked, no missing images, geometry overflow or SVG font-size changes.
- Latest full PDF was rebuilt after the highlighting fix: 241 pages, with
  bookmarks. The current `pdf-export.json` records that count.
- The full baseline PDFs were rendered into contact sheets and visually reviewed
  before the highlighting change. The latest recoloured full PDF has not had a
  fresh complete contact-sheet review.
- `course-slidev-clicks-53.pdf` contains five distinct states, but **predates the
  highlighting fix**. Regenerate it before judging the current colours.
- Shared typecheck, converter tests and cold/warm Marp/exercise smoke builds
  passed during the foundation work. Shared typecheck and full browser checks
  also passed after wheel/highlighting changes. Root TypeScript checking does
  not constitute Vue template typechecking.
- The earlier course checks passed: 556 Python fences, slide references, Ruff,
  and native snapshot execution. Re-run checks appropriate to subsequent edits.
- Slidev 53/Twoslash logs one known nonblocking FloatingVue private-patch warning:
  `Failed to patch FloatingVue ... reading 'Popper'`. The checker records it and
  fails other console errors. This is not zero-warning output.
- PDF bookmarks work. Browser hash links are not remapped to internal PDF
  destinations; their utility in exported documents needs parity work.
- Interactive Slidev delivery requires a static server. `file://` is unsupported.
  The existing exercise site still opens from disk and still uses Marp previews.
- `--serve` serves built files; it is not a source-watching authoring server.
  Native dev/watch authoring has not been integrated or verified.
- Notes handling has a student-safe default and a `--notes` build option, but
  presenter notes, presenter controls, drawing, overview and other native flows
  have not received a comprehensive parity test.
- CI, release allowlists and student delivery still publish Marp outputs.
  They have not been migrated to Slidev.

PDF export uses Slidev's native PrintSlide renderer via `/course-export`, not a
parallel handwritten HTML renderer. Native CLI combined printing stalled; its
per-slide mode exported the course but only the initial Magic Move state. The
shared print route filters selected slides before mounting states, avoiding an
entire hidden course render for a small range. Keep that path unless new evidence
supports changing it. There is no standalone Playwright dependency.

UnoCSS interpreted SVG `font-size="17"` as a 68px utility. The converter applies
explicit inline pixel sizes to preserve SVG user units; the browser checker
verifies them. Preserve this regression fix.

## Next work, in order

1. **Audit real Marp parity.** Compare current production Marp output, shared
   assembly/theme/build behaviour and actual trainer/student workflows with
   Slidev. Record a matrix of feature, Marp behaviour, Slidev behaviour, evidence
   and remaining work. Include original page/content/code coverage, images and
   sizing directives, tables/layout classes, diagrams, typography/highlighting,
   module/appendix navigation, PDFs/links, notes/presenter use, authoring/watch,
   offline delivery, exercise previews and CI/release packaging. Completion:
   every observed feature is classified as verified, missing, unverified or an
   explicit delivery tradeoff. Do not declare parity from screenshot similarity.
2. **Close the comparison blockers found by that audit.** Prioritize broken or
   materially different classroom/document workflows. PDF internal navigation,
   live authoring and exercise-site/delivery integration are candidates, not
   already approved designs. Keep existing Marp commands and release behaviour
   working while adding an opt-in comparison path. Completion: each blocker has
   an implemented flow and evidence, or a concrete documented limitation.
3. **Enrich a complete module using Slidev.** Data Structures is a sensible
   starting point because two native examples already exist. Indexing/slicing,
   nested references, stacks, set operations and dictionary mutation are ideas,
   not implemented features. Use existing demos, reversible click choreography,
   meaningful motion and accurate displayed state. Keep the original pages
   available for comparison and preserve explicit pagination. Completion: a
   complete module can be taught through the native deck, original concepts are
   covered, every added state/output is checked against Python, and final/click
   exports are readable.
4. **Verify and hand back concrete comparison evidence.** Build both engines,
   exercise ordinary/reverse/wheel navigation and native features, verify offline
   assets, regenerate full and click PDFs, inspect rendered exports and record
   exact commands/results. Promote important manual regressions to persistent
   checks where justified. Re-read shared merge requirements before integration.
   Completion: update the matrix with evidence and state any remaining gaps
   plainly. Keep the same source content and page-boundary guarantees.

The user authorized continued implementation toward parity; routine reversible
work can proceed. A new permission round is not needed to investigate or fix the
existing comparison. Changes to release defaults should be explicit and reviewable.
