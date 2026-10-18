# Parallel Slidev foundation

Implemented 2026-10-18. Shared code is in the Presentation-Template worktree
`../_worktrees/presentation-template-slidev`, branch `feature/slidev-foundation`.
The default Marp build and published exercise site remain independent.

For continuing work, read `slidev-handoff.md` in this folder. It records the
expanded parity objective, saved repository state and remaining work; this file
is the foundation implementation report.

## Course coverage

- All 13 fundamentals modules, including both appendices, and the preamble.
- 226 source content slides plus 13 generated module overviews: 239 original pages.
- The same boundaries in Slidev, with two additional native Magic Move slides:
  241 pages. No automatic pagination or font fitting.
- All 299 original code/output fences retained unchanged. Source Markdown and
  Python demos were not edited.
- Explicit compact layouts are listed in `build/slidev.config.ts`. The crowded
  Accessing Lists slide has an explicit two-column layout in `src/slidev/style.css`.
- Native additions quote statements from the existing list and tuple demos.
  `build/check-slidev-examples.py` executes every snapshot and checks the displayed
  collection states and the final tuple values against the demos.

## Layout and navigation

Local IBM Plex fonts, original top stripe, SpiralTrain logo top-right, linked
module name top-left, and page numbers and demo/exercise markers bottom-right.
The module name opens that module's overview. The comparison's topic picker
opens the corresponding source page in both frameworks. Native Slidev navigation
keeps the Marp comparison on the associated source topic.

Syntax highlighting uses Marp's `min-light` theme and its green comment colour
replacement (`#c2c3c5` to `#4a9c59`), also in native Magic Move examples.

Ordinary slides reveal parent bullet groups, code/output blocks, tables and SVGs
in reading order. Previous hides the preceding step. Magic Move keeps its initial
code state visible and advances the code and collection together.

Mouse-wheel and trackpad scrolling navigate these same steps: down advances,
up reverses. A gesture quiet period and animation cooldown suppress momentum
skips. Scrollable content and Ctrl/Command-wheel retain their normal behaviour.
Browser checks verified forward/reverse reveals, crossing slide boundaries,
sustained momentum, zoom exclusion and scrollable content. Shared typecheck and
the full 241-page browser validation passed after this addition.

## Executed checks

- Shared converter tests: five passing tests for content/fence preservation,
  notes, original slide boundaries, and SVG font attributes.
- Shared TypeScript typecheck and cold/warm Marp/exercises smoke tests passed.
- Course fence checker: 556 Python fences checked, no findings.
- Exercise slide references, Ruff and the native snapshot execution check passed.
- Browser validation loaded all 241 final frames and all 226 source topics with
  external HTTP blocked. No content or horizontal code overflow, missing images,
  SVG font-size changes, private notes in visible export content, HTTP errors or
  forward/backward reveal failures. Marp comparison also loaded locally.
- The linked module name was clicked in the native browser and reached the
  correct overview. Native Magic Move advanced a list from three to four values
  and stepped back.
- Complete PDF: 241 pages, 241 outline bookmarks, selectable text, about 2.1 MB.
  Marp PDF: 239 pages, about 2.8 MB. Every PDF page was rendered to review contact
  sheets; contact sheets and selected full-size pages were inspected.
- Magic Move click PDF: exactly five pages with 0, 1, 2, 3, 4 mutation statements.
- The built comparison was opened through the included Python `serve.py` launcher,
  without a Node/Bun presentation server.

Generated evidence is in `build/slidev/dist/`: `manifest.json`, `validation.json`,
`pdf-export.json`, `click-export.json`, PDFs, and `review/`. These are ignored build
outputs. Rebuild commands are documented in `MAINTAINING.md`.

## Export findings and limits

The native CLI's combined print stalled. Per-slide CLI export produced the full
course, but the click option only captured the first Magic Move state. The shared
export now uses Slidev's native PrintSlide renderer through a small route that
filters selected slides before mounting click states. This also avoids rendering
every hidden state in a whole course for a five-page animation export.

UnoCSS attributify interpreted SVG `font-size="17"` as a utility and produced
68-pixel text. The converter now gives numeric SVG font attributes explicit
inline pixel values; a browser regression check verifies the actual sizes.

Slidev 53/Twoslash still logs one nonblocking FloatingVue private-structure patch
warning. The checker records this specific upstream warning and fails on other
console errors. TypeScript hover features need a separate pilot before use.

Interactive delivery requires a local static server. The original exercise site
still supports `file://` and retains Marp previews and links. PDF bookmarks work;
interactive browser links are not rewritten into internal PDF destinations.
Release allowlists and CI still publish the existing Marp outputs. The optional
`libraries/` companion deck was not part of this fundamentals conversion.
