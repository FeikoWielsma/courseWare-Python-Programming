# Slidev integration evidence

Continuation of [the adoption plan](slidev-migration-plan.md), 2026-10-18.

## Initial Luna audit

Merged `1e5967b` from `t3/audit-slidev-mermaid-parity`. The
[audit](slidev-parity-diagrams.md) describes its original 241-page baseline;
subsequent fixes are recorded here rather than rewriting those observations.

## Diagram and PDF fixes

- `Unexpected Errors` now has an explicit compact grid in course config/CSS.
  Original prose, Mermaid source and the single source-page boundary remain.
  Luna's diagram check measures the minimum label at 14.1px, previously 5.5px.
- Shared validation measures Pele text after its SVG screen transform,
  normalized to the 1280px canvas. Sub-10px labels and render placeholders fail.
- PDF export collects visible anchor rectangles from each native printed frame
  and maps semantic/numeric slide routes to PDF destinations. Range/click PDFs
  use their actual exported page order, link to the first included state, and
  omit destinations outside the selected range. Web links retain URI actions.
- Two regression tests cover semantic/numeric routes, coordinates, external
  URLs, serialization and selected/click-state destination handling.

Executed against shared feature worktree:

```powershell
bun run --cwd ../_worktrees/presentation-template-slidev/build typecheck
bun test --cwd ../_worktrees/presentation-template-slidev/build/slidev convert.test.ts pdf.test.ts
$env:PRESENTATION_TEMPLATE_DIR='C:/Git/courseWare/_worktrees/presentation-template-slidev'
bun run --cwd build slidev --pdf --check
bun build/slidev_checks/check_diagrams.ts
```

Results: TypeScript and seven tests pass; 241 pages, 226 source topics, 299
original code/output fences, zero browser validation failures, nine diagrams
passing. The known upstream FloatingVue warning remains recorded.

Independent `pypdf` inspection of the rebuilt full PDF found 874 link annotations,
all 874 destinations belonging to actual PDF pages, and preserved outlines.
The eight-state exception-slide PDF was regenerated; its final page contains all
exception labels. Poppler rendered page 143 at 1280px, and the resulting image
was visually inspected for legibility and overlap. Generated evidence remains
under ignored `build/slidev/`; the PDF is `dist/course-slidev.pdf`.

These checks establish the fixes above. The complete course animation rollout,
default build/release cutover, authoring integration and final acceptance remain
open. Shared production checkout remains unchanged.
