> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# Slidev delivery verification

Independent verification of the integrated baseline on 2026-10-18, before the
default cutover. This checks the accepted plan's 13 course modules and both
appendices. The separate `libraries/` companion course is outside scope.

## Result

**Verified:** the c7ec5ce shared build exports and validates the current course;
all nine Pele diagrams clear the effective 10px text floor; PDF links target
real pages and their sampled rectangles cover printed labels; physical wheel
navigation and student/trainer notes workflows work; source-watch authoring
refreshes from a temporary slide copy.

**Cutover blocker:** ordinary builds, release artefacts and the student bundle
still use Marp. Slidev is available as an opt-in command. Do not switch the
default until the coordinator updates and locally verifies the release workflow,
bundle allowlist, launcher and named Marp fallback.

## Verified checks

| Area | Status | Evidence |
| --- | --- | --- |
| Course coverage | **Verified** | Build reports 13 modules, 226 source topics, 241 Slidev pages and all 299 original code/output fences. Marp comparison build reports 239 pages. The two additional Slidev pages are the existing native examples. |
| Mermaid to Pele | **Verified** | `check_diagrams.ts` audited nine fences with Pele 1.6.0. All labels, nodes and edges passed; no placeholder or SVG bounds failure. Effective label text ranges from 10.2px to 26.6px; `08-exception-handling-1` is now 14.1px. Its exported page 143 was rendered and visually checked for text legibility, overlap and clipping. |
| Normal reveal navigation | **Verified** | Puppeteer ArrowRight then ArrowLeft restored the hidden state. Physical CDP wheel events advanced and reversed reveals, grouped a three-event momentum burst into one reveal, ignored Ctrl-wheel, preserved scrolling in a scrollable panel and ignored an editable control. Wheel navigation also crossed the source-slide boundary forward and backward. |
| Source and appendix navigation | **Verified** | In T3 Preview, the Type Hinting source header opened its module overview. Clicking “Appendix Python Libraries” on that overview opened `13-appendix-libraries-overview`. Both appendix overview routes resolve. |
| Presenter controls | **Verified, basic path** | The student app's Presenter Mode control opened `/presenter/00-preamble-1`; Play Mode returned to slides. Presenter view exposed navigation, layout and notes controls. Drawing, remote control, screen mirroring and multi-display operation were not comprehensively checked. |
| Student notes privacy | **Verified** | The public build was produced without `--notes`. The notes-only phrase “Welcome students to the Python Programming course.” is absent from the student JS assets and presenter view reports “No notes.” |
| Trainer notes | **Verified** | The wrapper's actual `--notes` build was stored separately at `C:/Users/feiko/AppData/Local/Temp/prg400-slidev-variants-7812dcbd004646318b9c597c0b397b4a/trainer-dist`; the prior student folder was restored to `build/slidev/dist`. The trainer phrase is present in its assets and visible in the trainer presenter view. The student and trainer variants did not share an output folder. |
| Source watch | **Verified** | `slidev.ts --dev --slides-dir <temporary copy> --port 53001` started the authoring server. Changing the temporary copy's Variables title refreshed `build/slidev/converted.md` to “Variables Watch Probe”; the server returned HTTP 200 at `http://localhost:53001`. Canonical sources were not edited. |
| Full PDF and links | **Verified** | `course-slidev.pdf`: 241 pages, 28 bookmarks, 874 link annotations. All 874 are internal destinations resolving to real PDF pages; no annotation rectangle exceeds its page. On rendered schedule page 3, module/appendix labels and topic titles line up with their annotation rectangles and targets. Examples: “Variables and Data Types” targets page 24, “Type Hinting” page 216, “Python Libraries” page 225, and “What is Python?” page 4. On rendered page 25, the “Variables and Data Types” header rectangle covers the printed header and targets its page 24 overview. |
| Click PDF | **Verified, representative** | `--with-clicks --range 143` exported eight states; page text includes the exception labels. This selected slide has no links, so selected-export link mapping was not exercised by this PDF. |
| Offline assets | **Verified, browser-delivery path** | Full `--check` loads all 241 frames with external HTTP blocked, no missing images, layout overflow, diagram placeholders or sub-10px diagram text. Viewing still requires a local static server; `file://` is unsupported. |
| Release default and fallback | **Missing, cutover blocker** | `build/package.json` maps ordinary `build` to the Marp template. `.forgejo/workflows/release.yml` emits Marp PDF/HTML and its bundle allowlist does not include `build/slidev/dist` or its launcher. The intended named Marp fallback has not been implemented because Slidev is not yet the default. |

## Exact commands

Run from the course root in PowerShell. `PRESENTATION_TEMPLATE_DIR` was set
explicitly for every shared Slidev command.

```powershell
$env:PRESENTATION_TEMPLATE_DIR='C:/Git/courseWare/_worktrees/presentation-template-slidev'
bun C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts --pdf --check
bun C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts --compare --check
bun C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts --with-clicks --range 143
bun build/slidev_checks/check_diagrams.ts
bun build/slidev_checks/check_delivery.ts
bun run --cwd C:/Git/courseWare/_worktrees/presentation-template-slidev/build typecheck
bun test --cwd C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev convert.test.ts pdf.test.ts
bun C:/Git/courseWare/_worktrees/presentation-template-slidev/build/slidev/build.ts --notes
```

`--pdf --check` passed with 241 exported pages and zero validation failures.
`--compare --check` reported 239 Marp pages and zero Slidev validation failures.
Both reported the known upstream FloatingVue warning:
`Failed to patch FloatingVue ... reading 'Popper'`.
The diagram audit passed. TypeScript and all seven shared converter/PDF tests
passed. The physical wheel cases are in `build/slidev_checks/check_delivery.ts`.

The `--notes` command uses the normal wrapper output path; for this check, the
existing student `build/slidev/dist` was moved to a unique scratch directory,
the trainer build was moved to a separate scratch directory, and the student
output was restored. The trainer scratch path is recorded above.

PDF annotation audit and representative text/rectangle mapping:

```powershell
@'
from pypdf import PdfReader
p = 'build/slidev/dist/course-slidev.pdf'
r = PdfReader(p)
print('pages', len(r.pages), 'bookmarks', len(r.outline))
# Iterate /Annots on every page; check each /Link /Dest page reference against
# the document page references, and each /Rect against that page's MediaBox.
'@ | uv run --with pypdf python -
```

Rendered page 3, page 25 and page 143 with PyMuPDF and inspected them visually.
The schedule links to every overview/source route; this audit checked every
annotation's page reference and bounds, but visually compared only the examples
listed above.

## Remaining work for the coordinator

1. Keep the release default on Marp until the Slidev student folder, static
   launcher, ordinary build command and CI release packaging are implemented
   and verified together. Add an explicit Marp fallback command when making
   that cutover.
2. Verify the deployed/student bundle from the release workflow, including the
   static server entry point and links from delivery instructions. A local
   Slidev export does not prove that the release contains it.
3. Re-run full visual review after the independent animation pilot is integrated.
   This verification does not review unreleased animation content; current native
   content remains the two existing Data Structures examples.
4. Treat external-URI PDF link actions as unverified: this course PDF has no
   external URI annotations to sample. Selected/click PDF link destinations and
   presenter features beyond the basic navigation and notes path also need
   separate checks if those workflows are part of the cutover acceptance.

## Checkout

- Course branch at start: `t3/verify-slidev-delivery`, `53d3e2de7c5cbfa01a4f97aa0c11c90f2926dbdf`.
- Shared feature worktree: `C:/Git/courseWare/_worktrees/presentation-template-slidev`, `c7ec5cef3ec4b43809b8da79aeaedc30c37b2307`.
- Only this report and the new `build/slidev_checks/check_delivery.ts` are in scope for this verification commit.
