> Historical record (2026-10-15). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# WP3a notes : slides and demos 01 to 03

Branch : t3/wp3a-slides-demos-01-03 (worktree), fast-forwarded to prg400-wordle 57429f8 first.

## Done

- 01 : identifiers trimmed to PEP 8 naming, reserved words are the 3.14 kwlist plus soft
  keywords, History wording merged, running Python described through `uv run` everywhere,
  `--dev` / pytest explained once; stale path in 03_ruff_findings.py docstring fixed
- 02 : operators moved in from 04 (demos 08, 09), formatting is f-Strings + Format
  Specifications (SVG redrawn), escape table corrected, string methods table cut to the
  course's methods + docs link, summary rewritten; demos renumbered 10-15
- 03 : bytes slide and demo deleted, demos 09-11 renumbered, Multidimensional Lists is a
  grid, Sets split into Sets + Set Operations, cross-language comparisons and the
  "dicts are unordered" claim removed
- Gates : check-fences, ruff, compileall, build, lint all clean

## Decisions

- ruff per-file ignores for renamed demos are file-level `# ruff: noqa:` comments in the
  demo itself, so the gate passes without touching ruff.toml
- 10_dictionaries.py no longer ends in a NameError: the line is commented like the KeyError
- Set examples print `sorted(...)` because string-set order changes between runs
- Shared build crashes on Windows with EBUSY removing the puppeteer temp profile; worked
  around locally with a bun --preload that ignores that one error (not committed)
