> Historical record (2026-10-14). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# WP3c implementation report

Branch: `t3/wp3c-slides-demos` (renamed by the host during this session). Package complete within its owned files; coordinator integration remains below.

## Changes and decisions

- 07: comprehensions first, then generator expressions and function-taking built-ins, then map/filter/reduce as recognition material. Fourteen sequential demoNN files. Neutral examples, annotations on new signatures, deterministic sorted set output. Dictionary from Keys was already one slide at this base; shortened it to immutable defaults versus independent mutable values rather than retain redundant constructions. This removes the need for its C420 ignore and the dictionary demo's C416 ignore.
- 08: real Python 3.14 traceback from demo01, read bottom-up (only file paths abbreviated). Ten common exceptions in one table; assertions get their own short demo slide. OSError/FileNotFoundError replace IOError, including extra/firstexception.py. Typed handlers ordered specific first. Corrected slide/demo drift, the nonterminating input loop, and the misleading finally example. Demos 01, 06, 09 and 10 intentionally exit 1 with their demonstrated exceptions.
- 09: recovered the bytes material from `git show prg400-wordle:src/slides/03-data-structures/03-data-structures.md` and `git show prg400-wordle:demos/03-datastructures/09_bytesandbytesarrays.py`; adapted its ABCDE encoding/mutation example beside binary files. Short binary read/struct round-trip examples, one file-position slide, CSV writer/reader and DictReader slides with neutral planet data. Separate self-contained CSV demos avoid a repeated pill (the linter rejects repeated numbers). Fourteen sequential NN files, following the package convention rather than the inherited demoNN names. Preserved the open-result SVG. Fixed text-read counts, current-position wording and deterministic encoding.
- Preserved the explicit open/close-to-with progression; no generators proper, decorators or collections depth added.

## Verification

- `uv sync`: PASS, CPython 3.14.3.
- `uv run python build/check-fences.py`: PASS, 310 fences, 304 parseable, six pre-existing-style snippets.
- `uv run ruff check .`: one expected C417 finding, solely the renamed teaching demo. PASS with the pending ignore supplied on the command line (no coordinator files edited).
- `uv run python -m compileall -q demos solutions`: FAIL on existing files outside this package in demos/12-pythonlibraries-networking, demos/12-pythonlibraries-xml and demos/13-appendix-generators/more (Python 2 syntax and a module-level return).
- Scoped compileall for the three owned demo folders plus solutions: PASS.
- Shared absolute-path build from this worktree's build directory: PASS, PDF and HTML generated, 238 slides total. Separate post-build lint: PASS, all slides within budget, no warnings. Existing shared dependencies/browser worked; no install needed.
- Ran all 38 numbered slide demos in temporary copies of their data directories, with stdin `42`; also exercised exception input with `six`. All return 0 except the four intentional module 08 exception demonstrations. Ran both module 08 supplementary exception demos too.
- Audited every Python line on demo-backed slides against its demo, including comments: PASS.
- Verified displayed outputs by execution: sum of squares 2854; any/all True/False; empty any/all False/True; reduction 24; dictionary/set/list outputs; traceback line 5 calling line 2 and exact Python 3.14 caret markers; conversion ValueError text; assertion output 32.0; finally output ordering; bytes b'ABCDE', 65, ABCDE, bytearray(b'FBCDE'), FBCDE; JPEG prefix ffd8ff; struct (1, 2, 3); text round-trip; file position b'AB', 2, b'AB'; CSV ['name', 'moons'], ['Earth', '1'], ['Mars', '2'], Earth: 1 moons, Mars: 2 moons.
- Unreferenced legacy IO scripts (including the GUI-launching startprocess.py and createexecutable tooling) are unchanged and were not treated as course slide demos.

## Exact coordinator-only changes

In `ruff.toml`:

1. Replace the old syntactic-sugar per-file-ignore entry with:

```toml
# This recognition example deliberately contrasts map/lambda with a comprehension.
"demos/07_comprehensions/demo13_syntactic_sugar.py" = ["C417"]
```

2. Delete these obsolete entries (and their now-obsolete explanatory comment):

```toml
"demos/07_comprehensions/demo11_dictionary_comprehension.py" = ["C416"]
"demos/07_comprehensions/demo12_dictionary_from_keys.py" = ["C420"]
```

3. Replace the exception folder entry and its classic-IOError comment with:

```toml
# The exception chapter demonstrates bare except and explicit file closing
# before context managers; modes are spelled out for teaching.
"demos/08-exceptionhandling/**" = ["B904", "E722", "SIM115", "UP015"]
```

In `build/check-fences.py`, delete the two-line UP024 explanatory comment and use:

```python
RUFF_IGNORE = "UP015,UP018,UP030,UP031,UP032"
```

No workflow/bundle change is required: existing demo directories remain unchanged. The module 09 ignore is a directory glob and survives all renames. The only ignore path needing relocation is C417 above.

## Open integration issues

- Apply the coordinator-only configuration changes to restore the unmodified Ruff gate.
- Decide whether the broad compileall gate should exclude non-shipped historical demo folders or those files should be modernised separately; they are outside WP3c ownership.
- No push or merge performed. Commits are local, one per module, each co-authored by GPT-6 Astra.
