> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# PRG400 Slidev parity and diagram audit

Audit date: 2026-10-18

Audit branch: `t3/audit-slidev-mermaid-parity`, based on `77a147894ecdc41ef4c74f29819c06496c96d93c`
Scope: the 13 fundamentals modules and both appendices. The separate `libraries/` course remains outside scope.

## Findings that affect cutover

The Slidev build keeps the full Marp source coverage and exports a 241-page deck. The Marp comparison PDF contains 239 pages. All 299 original code/output fences are retained. The nine canonical Mermaid diagrams render with Pele 1.6.0; there are no placeholders, no missing source nodes or edges, no duplicate SVG `id` attributes, and no diagram text escaping its SVG or slide bounds.

There is one verified diagram defect. On the `Unexpected Errors` slide, the exception inheritance diagram's eight labels are scaled from the SVG's declared 16px font to **5.5px on the slide**. The frame geometry check does not catch this because the SVG element itself fits inside the slide. The new course check reports this as a failure. Fix this before accepting diagram parity.

Other cutover blockers remain outside this audit's edit boundary:

1. Slidev's full PDF has 241 pages and bookmarks, but **zero PDF link annotations**. Marp's comparison PDF has 604 link annotations. Source-topic/module links therefore do not carry through as working PDF destinations. The PDF final/click state exports work; PDF link parity does not.
2. The course's ordinary build, release workflow and student bundle still use Marp. `build/package.json` exposes Slidev only through opt-in scripts; `.forgejo/workflows/release.yml` does not build or package the Slidev delivery folder. The selected “Slidev default after verification, Marp fallback” cutover is not implemented.
3. Source-watching authoring and comprehensive presenter/notes behavior are not verified. The current `--serve-only` command serves an already-built static directory.

## Diagram inventory

All fences are plain, unthemed horizontal flow diagrams. There is one legacy `graph LR` and eight `flowchart LR` fences. The inventory below comes from the canonical Markdown, manifest routes, generated SVGs and browser inspection. The “rendered text” column is the smallest actual browser font in CSS pixels after SVG scaling, not the font declaration stored inside the SVG.

| Source fence | Slide route and title | Type | Nodes / edges | SVG viewBox | Smallest rendered text |
| --- | --- | --- | ---: | ---: | ---: |
| [`01-python-intro.md:18`](../../src/slides/01-python-intro/01-python-intro.md) | `01-python-intro-1` — What is Python? | `graph LR` | 5 / 4 | 11.5px |
| [`04-control-flow-and-operators.md:37`](../../src/slides/04-control-flow-and-operators/04-control-flow-and-operators.md) | `04-control-flow-and-operators-2` — if Statement | `flowchart LR` | 4 / 4 | 20.4px |
| [`04-control-flow-and-operators.md:182`](../../src/slides/04-control-flow-and-operators/04-control-flow-and-operators.md) | `04-control-flow-and-operators-7` — while Loop | `flowchart LR` | 4 / 4 | 13.9px |
| [`04-control-flow-and-operators.md:236`](../../src/slides/04-control-flow-and-operators/04-control-flow-and-operators.md) | `04-control-flow-and-operators-9` — for Loop | `flowchart LR` | 5 / 5 | 23.7px |
| [`05-functions.md:444`](../../src/slides/05-functions/05-functions.md) | `05-functions-15` — Scope of Variables | `flowchart LR` | 4 / 3 | 23.1px |
| [`08-exception-handling.md:19`](../../src/slides/08-exception-handling/08-exception-handling.md) | `08-exception-handling-1` — Unexpected Errors | `flowchart LR` | 8 / 7 | **5.5px — blocker** |
| [`08-exception-handling.md:231`](../../src/slides/08-exception-handling/08-exception-handling.md) | `08-exception-handling-9` — try-finally Clause | `flowchart LR` | 6 / 6 | 10.2px |
| [`10-python-database-access.md:32`](../../src/slides/10-python-database-access/10-python-database-access.md) | `10-python-database-access-2` — DB API Concepts | `flowchart LR` | 6 / 5 | 24.1px |
| [`11-python-classes.md:338`](../../src/slides/11-python-classes/11-python-classes.md) | `11-python-classes-13` — The Rule of Thumb | `flowchart LR` | 3 / 2 | 26.6px |

The emitted browser SVGs contain the expected labels, node groups and edge groups for all nine source diagrams. Their drawing bounds are within positive `0 0 width height` viewBoxes; browser text boxes are within the SVG and slide body. All nine currently have zero actual SVG `id` attributes, so there is no cross-diagram ID collision in this corpus. Pele's source does create error placeholders on failures; none of the current source fences used that fallback, and no `placeholder-mermaid-*.svg` was found.

## Rendering path and native Slidev Mermaid behavior

The canonical path is build-time Pele, before Slidev compiles the Markdown:

1. Shared `build/src/parser.ts` calls `processDiagrams()` before splitting slides (`C:/Git/courseWare/_worktrees/presentation-template-slidev/build/src/parser.ts:5-10`).
2. `build/src/diagrams.ts` pins `DIAGRAM_RENDERER = 'pele@1.6.0'`. `diagramHash()` hashes that pin, the Sans and Mono font-family strings, and trimmed Mermaid source. The SVG cache lives at `build/.mermaid-cache/mermaid-<sha1>.svg`. A cold miss calls Pele; a failure writes a visible error placeholder (`.../build/src/diagrams.ts:8-26, 49-103`).
3. `build/slidev/prepare.ts` calls `parseModule()` for canonical files. It embeds local images, converts each original page, preserves source IDs, inserts configured native pages, and writes `slides.md` and the manifest. Native enrichment Markdown is separately passed through `processDiagrams()` at `prepare.ts:47-64`; it would use the same Pele path today.
4. The converted source contains inline SVG. The course layout retains it in the diagram step; `template/style.css:17-19, 50-52` fits it into the remaining body area. Pele's SVG uses palette variables and the stylesheet maps those variables to the course palette (`style.css:79`). The theme is therefore supplied by CSS around the inline SVG, rather than a Mermaid `init` directive.
5. Slidev compiles the generated Markdown, builds the static SPA, and its `PrintSlide` route exports the final or requested click states. `export-pdf.ts` verifies the number of exported pages. `pdf.ts` checks the full PDF page count and adds bookmarks.

**Native Slidev Mermaid is a different path.** The official [Mermaid feature page](https://sli.dev/features/mermaid) documents `mermaid` fences and per-fence options such as `theme` and `scale`. The official [Mermaid configuration page](https://sli.dev/custom/config-mermaid) documents client-side `setup/mermaid.ts` configuration and theme variables. The [custom renderer page](https://sli.dev/custom/config-mermaid-renderer) documents client-side `setup/mermaid-renderer.ts` and a renderer that receives the source and options.

The pinned Slidev 53.0.0 client source confirms those contracts: `@slidev/client/modules/mermaid.ts:1-41` imports Mermaid, caches by encoded source plus options, calls configured custom renderers first, then falls back to `mermaid.render()`. `@slidev/client/setup/mermaid.ts:1-15` merges `defineMermaidSetup()` results into Mermaid configuration. The installed types declare `MermaidSetup`, `MermaidRenderFn` and `MermaidRendererSetup` in `@slidev/types` (`node_modules/@slidev/types/dist/index.d.ts`).

Those native options and hooks do **not** affect today's canonical PRG400 fences: the shared parser has already replaced them with Pele SVG before Slidev sees them. Native additions also take Pele today because preparation explicitly preprocesses their Mermaid fences. Choosing Slidev's native renderer would require a deliberate preprocessing/configuration change and a renderer parity review. Mermaid support does not automatically animate a diagram: Slidev's [animation guide](https://sli.dev/guide/animations) describes explicit click steps (`v-click`, `v-after`, and related directives). Current Mermaid figures are static SVGs; transitions elsewhere in the deck come from click-group conversion or explicit Vue components.

## Cache, SVG and browser checks

Commands ran from this course worktree. The explicit shared build root kept all generated course output under this worktree:

```powershell
$env:PRESENTATION_TEMPLATE_DIR='C:/Git/courseWare/_worktrees/presentation-template-slidev'
bun 'C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts' --pdf --check
bun 'C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts' --compare --check
bun 'C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts' --with-clicks --range 143
bun build/slidev_checks/check_diagrams.ts
```

The first build began with no course diagram cache and logged nine `Rendering diagram (...)` messages. The warm `--prepare` run logged no render messages. It reported 13 modules, 226 source topics, 241 Slidev pages and 299 original code/output fences. The cache then held nine SVG files. The new check recomputes the expected hash from the pinned renderer/fonts/source and verifies that changing the version string changes that hash.

The browser-based whole-course check passed twice: 241 frames, 226 topics, no missing images, no frame geometry overflow, no SVG declared-font-size mutations, no source coverage failures and no external HTTP dependency failures. It recorded one upstream FloatingVue patch warning. The independent `check_diagrams.ts` static and browser checks verified all nine source labels/nodes/edges, no placeholders, no duplicate `id` attributes, theme class, viewBox/drawn-content containment and text/frame containment. It exits **1** solely for `08-exception-handling-1: diagram text renders at 5.5px; minimum is 10px.` That finding demonstrates a gap in the existing check: it compares SVG font attributes with CSS-computed font attributes but does not multiply by the SVG's effective screen transform.

The T3 Preview browser rendered the actual 1280×800 slides. The `Unexpected Errors` page screenshot at click 4 showed all eight labels and seven edges, but the diagram text was visibly tiny; browser measurements confirmed the 5.5px effective font. `getBBox()` for the drawing stayed inside its `733×328` viewBox. For all nine diagrams, the new Puppeteer check found no clipped text or viewBox overflow. A Preview `scroll` action did not advance a reveal, so wheel navigation is not claimed as re-verified by that action; see the parity matrix.

## Native additions, separate from canonical source

`src/slidev/list-mutation.md` and `src/slidev/tuple-unpacking.md` are the only current Slidev additions. They do not contain Mermaid. They provide two Data Structures examples with 5 and 3 Magic Move/code states, respectively; they do not yet constitute a complete enriched module. `uv run python build/check-slidev-examples.py` passed, matching all eight displayed states to the cited demos. Their behavior does not alter the nine canonical Mermaid cases above.

## Full parity matrix

“Verified” means executed against the generated course or source artifact in this worktree. “Unverified” means the route was not exercised end to end during this audit. The status “Missing” identifies a known parity gap. “Explicit tradeoff” describes an intentionally different supported workflow.

| Area | Status | Evidence and current behavior |
| --- | --- | --- |
| Canonical pages and source mapping | **Verified** | `--compare --check`: Marp output 239 pages; Slidev 241 pages. Manifest covers 226 source topics and generated overview/enrichment pages. The browser checker found every topic. Source boundaries remain one slide each. |
| Code/output fence coverage | **Verified** | Build reports all 299 original code/output fences retained; converter checks preserve the original fence bodies. `uv run python build/check-slidev-examples.py` passed 5 list states and 3 tuple states. |
| Images and local asset references | **Verified** | The shared `embedLocalImages()` path runs during preparation. Full browser check found zero missing images and no external HTTP dependency while HTTP was blocked. Exact image-by-image Marp pixel comparison was not performed. |
| Marp directives and original layouts | **Unverified** | Marp `size`, `paginate`, and theme behavior are replaced by the explicit Slidev 1280×800 course frame; configured compact slides are explicit. The converter tests cover tables, code overflow and slide boundaries. The course-wide checker found no element outside the content frame, but it does not prove that every table cell or directive has identical appearance. |
| Tables and dense slides | **Unverified** | Structural page boundaries, rows and representative large-table conversion are covered by `convert.test.ts`; course browser geometry reports zero overflow. All 15 `compactSlides` choices are explicit in course config. Text-scale/content fidelity for every table cell was not checked. |
| Mermaid syntax, node/edge labels and IDs | **Verified, with one typography blocker** | All 9 fences are the flowchart subset listed above. Pele 1.6.0 rendered all source labels/edges; no placeholders, duplicate SVG IDs or SVG-bound escapes. Unsupported Mermaid features outside the existing flowchart corpus remain unverified. The exception hierarchy text renders at 5.5px. |
| Diagram theme and fonts | **Verified, with one typography blocker** | Browser SVGs use `pele` CSS variables mapped to the course blue/teal palette. Declared user-unit fonts survive conversion and browser CSS. Effective rendered font scaling was measured: 5.5px on the exception tree and 10.2px on try/finally; other seven are 11.5–26.6px. |
| Module and appendix navigation | **Unverified** | Manifest contains route aliases for every source topic and generated module overview; the Preview showed the module header linking to its overview. The audit did not click every schedule/appendix link. |
| Final-state PDF | **Verified** | Browser export captured 241 pages; PDF post-processing accepted the page count and added bookmarks. `pypdf` read 241 pages and extracted the exception labels from the final slide. |
| Click PDF | **Verified for one representative diagram slide** | `--with-clicks --range 143` exported 8 states for the exception diagram slide; `pypdf` confirmed 8 pages and extractable diagram labels. This is not a click-PDF review of every animated addition. |
| PDF links and internal destinations | **Missing** | The Slidev PDF has bookmarks but zero link annotations. The Marp PDF has 604 link annotations. The shared PDF post-processor adds outlines, not link destinations. Hash-based source/module navigation therefore does not survive in the PDF. |
| Presenter mode and speaker notes | **Unverified** | The native Presenter Mode control is present in the browser. Slidev build defaults to `--without-notes`; `--notes` is an explicit build option. Note display, presenter controls and student/trainer variant handling were not comprehensively tested. |
| Live authoring and watch mode | **Missing** | Course wrapper commands build, serve built files or run checks; there is no integrated source-watching authoring command. `--serve-only` serves the existing `dist` folder. |
| Reverse navigation | **Verified** | Whole-course check drives ArrowRight then ArrowLeft and verifies the reveal returns to its hidden state. This reverses a regular reveal, not every native transition. |
| Wheel navigation | **Unverified in this audit** | The handoff records prior manual wheel coverage and the implementation is in `template/global-bottom.vue`. This turn's Preview scroll action did not update the click URL, so it supplies no new test evidence; wheel cases are not part of the persistent shared check. |
| Static/offline Slidev delivery | **Verified, with an explicit server requirement** | Static output includes the Slidev bundle, 28 local WOFF2 assets, logo and `serve.py`. Full browser validation blocked external HTTP and passed with no missing assets. Students need a local static server; `file://` opening is unsupported. |
| Exercise-site previews | **Explicit tradeoff** | Existing exercise site remains its current offline Marp-preview workflow. Slidev build does not replace preview thumbnails or exercise-site links. This preserves the existing exercise path but does not give it Slidev previews. |
| CI, release and student bundle | **Missing — cutover blocker** | `build/package.json` still maps ordinary `build` to the shared Marp build. `.forgejo/workflows/release.yml` builds the Marp PDF/HTML, and its student bundle allowlist includes neither `build/slidev/dist` nor a static Slidev launcher. The accepted default/fallback selection has not been applied to release packaging. |

## Coordinator follow-ups, in priority order

1. **Resolve and gate the exception diagram's effective font scale.** Add an explicit layout choice for `08-exception-handling-1` or adjust how that slide allocates diagram height. Re-run `bun build/slidev_checks/check_diagrams.ts`; it should pass the 10px floor for all nine diagrams. Promote the effective-font calculation, not only the SVG's unscaled `font-size`, into the coordinator-owned shared `build/slidev/check.ts` after the layout fix. The existing course check was green while this diagram remained tiny.
2. **Restore PDF destinations.** Add PDF link destination mapping for Slidev source/module route links and verify representative schedule, module-overview and in-slide links. Keep bookmarks as a separate feature; they do not substitute for link annotations.
3. **Implement the selected default and fallback in release.** Update the ordinary build scripts, release workflow, student bundle allowlist and delivery instructions to ship the verified Slidev static folder and its local server path. Preserve named Marp commands and artifacts as fallback. Keep exercise-site preview behavior explicit. The current code/build/release path must remain Marp until this change is reviewed and verified.
4. **Close remaining delivery verification.** Exercise presenter notes and control behavior; add or document source watch/live authoring; verify appendix navigation and browser wheel forward/reverse in a persistent check. Preserve trainer notes out of the student variant.
5. **Keep renderer work scoped.** Existing diagrams use a supported Pele flowchart subset and are stable across cold/warm cache. Do not switch to native Mermaid as an incidental fix for scaling: native hooks/options are client-side and follow a different render/cache/theme path. If native Mermaid is later adopted, test the full nine-diagram corpus and export behavior explicitly.

## Check results and evidence files

- `bun 'C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts' --pdf --check` — passed: 241 page export and 0 browser validation failures; 1 known upstream FloatingVue warning.
- `bun 'C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts' --compare --check` — passed: Marp comparison generated, 239 Marp pages, 241 Slidev pages; 0 browser validation failures; same upstream warning.
- `bun 'C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts' --with-clicks --range 143` — passed: 8 click-state PDF pages.
- `bun build/slidev_checks/check_diagrams.ts` — **expected failure surfaced**: one sub-10px diagram (`08-exception-handling-1`, 5.5px); remaining static/browser diagram assertions passed.
- `uv run python build/check-slidev-examples.py` — passed: five list states and three tuple states.
- `bun run --cwd 'C:/Git/courseWare/_worktrees/presentation-template-slidev/build' typecheck` — passed.
- `bun test --cwd 'C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev' convert.test.ts` — passed: 5 tests.
- `uv run --with pypdf python -c "..."` — inspected course PDFs: Marp 239 pages/604 link annotations; Slidev 241 pages/0 link annotations; click export 8 pages. Both full PDFs have outlines.

Generated build output is ignored. No canonical slides, demos, shared template files, existing checks, configs, release workflow or CI files were modified by this audit.
