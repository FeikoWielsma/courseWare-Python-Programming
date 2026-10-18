# Libraries Slidev migration

Implemented 2026-10-18. Phase 1 of
[the libraries plan](libraries-slidev-plan.md), after the
[Phase 0 repairs](libraries-review.md). The example rewrite and native additions
remain in Phase 2.

## Build and delivery

`build/libraries.ts` now mirrors the fundamentals routing, using `libraries/`
as the course root. The shared template already provides the required toolchain;
no shared-template files changed.

```bash
bun run --cwd build libraries
bun run --cwd build libraries:marp -- --skip-lint --force
bun run --cwd build libraries:serve
bun run --cwd build libraries -- --skip-lint --compare
bun run --cwd build libraries -- --exercises --force
bun run --cwd build lint:libraries
```

Ordinary builds export and validate Slidev, run layout lint, and create
`PRG400-Python-Libraries-and-Tools.pdf` plus
`build/dist/PRG400-Python-Libraries-and-Tools-slides.zip`. The ZIP contains the
PDF and a `slides/` folder with the Python launcher. Native authoring uses port
3030 by default; `--port` can override it. `--exercises` retains the shared
exercise builder. `--prepare`, `--check-only`, `--serve-only`, selected-page
exports and `--out` retain the fundamentals wrapper's behavior.

Marp creates named `-Marp.pdf` and `-Marp.html` fallback files. Its HTML is also
copied to the original `PRG400-Python-Libraries-and-Tools.html` alias. Only the
Marp path copies standalone HTML. The canonical PDF name now contains Slidev.

CI builds both engines and retains `lint:libraries`. Its existing PDF/HTML upload
glob includes both engines, and the existing `build/dist/*.zip` loop includes
the new presentation ZIP. The student bundle copies the public presentation to
`libraries/slides/` before removing `libraries/build/` and `libraries/src/`.
The two course launchers both use 4188, so run one at a time.

## Content and layouts

The manifest records nine modules, 159 canonical source topics, nine generated
module overviews, 168 pages and 145 original code/output fences. Both Marp and
Slidev already include the overviews, so both PDFs have 168 pages.

The repaired Marp source and PDF were saved before migration as
`libraries/build/marp-baseline/phase1-combined.md` and `phase1-course.pdf`.
The rebuilt combined Markdown is byte-identical to that baseline. Source-file
hashes agree with the Slidev manifest. No canonical slides, demos, handouts or
solutions changed during Phase 1.

`libraries/build/slidev.config.ts` sets the title and blue course accent.
`compactSlides` and `enrichments` remain empty. No pagination changes, font
fitting, reduced type sizes or output narrowing were needed.

## Executed verification

- The comparison build and ordinary default build pass all-page validation:
  168 frames, 159 topics, zero failures. External HTTP is blocked. There are no
  geometry issues, horizontal `PRE` overflows, missing images, diagram
  placeholders, undersized diagram labels or SVG font mismatches. The existing
  upstream FloatingVue warning remains.
- Both exported PDFs have 168 pages, independently counted with the shared
  toolchain's `pdf-lib`. The exercises PDF/HTML also builds successfully.
- The comparison portal was inspected through the collaborative browser for
  all nine modules: Base Classes and Subclasses, Inline Script Metadata, rich
  Tables, Web Scraping, Relationships, axis Argument, info and describe,
  ttk.Treeview, and Standard Input and Pipelines. All three Mermaid diagrams
  were also inspected: Inherited Members, Web Scraping and groupby. Content is
  readable and contained in both engines. The PEP 723 `# /// script` lines stay
  inside their code fence and do not become slide titles.
- The student ZIP has 284 entries. Its PDF is byte-identical to the canonical
  Slidev PDF; it contains the launcher and no authoring Markdown, Vue,
  TypeScript, `src/`, `build/`, notes or comparison material. An extracted ZIP's
  actual Python launcher serves the app on 4188. Forward/reverse keyboard
  navigation restores the initial reveal state: step opacities
  `[0, 0, 0, 0]` → `[1, 0, 0, 0]` → `[0, 0, 0, 0]`.
- `libraries:serve -- --port 3031` starts the native authoring server and
  responds with HTTP 200. The temporary authoring process was stopped after
  verification.
- Layout lint reports all slides within budget; repository Ruff and
  `git diff --check` pass. Phase 0 Python sources are unchanged in this phase.

Generated validation, PDFs, baseline files and extracted-package evidence remain
ignored under `libraries/build/`. This pass checks browser layouts and the
final-state export path; the module contact-sheet export review and native
animation checks remain part of the later delivery phase. No remote release or
shared-template merge was performed.
