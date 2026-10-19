# Chapter 1 background and visuals

Updated 2026-10-19 after trainer feedback about missing Python context and sparse slides.

- Keep the opening practical sequence and existing demo contracts.
- Add Python Background, Python Features and Python Applications after interactive mode.
- Add a local SVG history timeline, project-folder diagram and toolchain comparison table.
- Insert a native Slidev walkthrough after Changing a Program. Five states distinguish
  editor text, the saved file and the most recent output, including running before saving.
- Leave the pre-existing changes in `src/slidev/style.css` untouched.

## Sources

Facts checked against the [Python FAQ](https://docs.python.org/3.14/faq/general.html),
[Python 2.0 release](https://www.python.org/download/releases/2.0/),
[Python 3.0 release](https://www.python.org/download/releases/3.0/),
[Python 2 sunset](https://www.python.org/doc/sunset-python-2/) and
[Python applications](https://www.python.org/about/apps/).

## Verification

- Fence check: 550 fences, no problems. Exercise slide references and Ruff pass.
- `bun run --cwd build lint`: all slides within budget.
- Static Slidev build succeeds; full-deck validation checks 304 frames. No chapter 1
  failures. Two failures remain elsewhere: database slide `10-python-database-access-15`
  overflows by 29px; exception hierarchy labels on `08-exception-handling-1` measure 9.8px.
- Visually inspected Files and Folders, Editor Setup, all three background slides and
  the native walkthrough in the existing port 3030 development server.
- Checked native states 0 through 4 and back to 0 using keyboard navigation. The
  longest caption fits inside the content area. Reduced motion disables transitions.
- `bun run --cwd build slidev -- --pdf --range 3-25` succeeds and captures 23 pages.
  PDF: `.courseware/fundamentals/range-3-25/course-slidev-3-25.pdf`.

The ordinary student build encountered a locked output folder, so the static review
build used `.courseware/fundamentals/chapter1-review`. The PDF uses the standard range
variant. Supplying `--output` with a PDF range exports the PDF but then fails in manifest
assembly because the wrapper assumes the standard range path; no shared tooling changed.
