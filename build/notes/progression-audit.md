# Teaching progression audit

Reviewed 2026-10-19 after moving the detailed tooling out of the introduction and
bringing `input()` forward. Scope: Exercises 1 to 13 against their associated
fundamentals slides, demos and solution stages. The separate `libraries/` course
is outside this pass.

The review distinguishes a missing prerequisite from a difficult application of
already taught syntax. The first needs earlier teaching; the second needs more
scaffolding or a trainer decision about the required path.

## Trainer simplification follow-up

The later trainer feedback supersedes the initial fixes for formatting, early
file reading and environment variables below. Teaching more prerequisites did
not remove the overload in those exercises.

- Exercise 2 uses ordinary output with no alignment widths, fill or `!s`.
  Aligned display is an optional experiment, supported by appendix 14.
- Exercise 3 starts with four words written directly in Python. Exercise 4
  expands the list enough to support its example games. Exercises 5 to 8 return
  the practice list from `load_words()`; they need no data file.
- Exercise 9 first reads the larger file, demonstrates relative paths and then
  uses the package location. Missing-file recovery moves here from Exercise 8.
- A Python `secret = "crane"` variable makes checks repeatable throughout.
  Shell settings are removed from every exercise. Environment variables move
  to appendix 14, with a neutral music example and demo.
- Solutions, generated starters, transcripts and course guidance follow the
  same progression. Exercises 10 to 13 receive only the necessary secret-setting
  wording/code updates; their larger scaffolding work remains deferred below.

Verification of the simplification pass: 550 Python fences, all slide
references, Ruff, generated starters, all thirteen solution stages and the
quiz pass. Native animation examples and traced Python executions pass.
Exercises 2 and 3 quoted final output matches execution; the smaller-list hint
check gives two candidates and suggests CRANE. A temporary Exercise 9 project
reproduces the relative-path failure and the package-relative success.
The rebuilt 300-page Slidev deck validates with zero layout failures and the
existing upstream warning. Revised exercise PDF pages, the relocated file-list
slide, both appendix slides and the offline exercise pages were inspected.
The shifted Data Structures summary keeps its compact layout at its new ID.
The Marp fallback PDF/HTML are rebuilt too. Final fundamentals manifests pass
for exercises, Marp and the student presentation.

## Initial audit corrections (historical where superseded)

- **The opening of Module 02 assumed the object vocabulary it was introducing.**
  Variables now start with naming values and assignment. The following object
  slide defines type, identity, aliasing and namespace without bringing in scope
  and methods before their lessons.
- **Exercise 2 needed formatting details that the slides did not demonstrate.**
  The new *Formatting Text Columns* slide and demo show fill characters and `!s`
  before alignment. The exercise explicitly leaves the supplied formatting in
  place so students can concentrate on comparisons. Boolean-to-integer conversion
  is now demonstrated before Exercise 3 uses `int(guess == secret)`.
- **Exercise 3 introduced imports, file reading and random selection through
  supplied code, with no earlier slide demonstration.** Module 03 now has three
  small slides and demos: *Using Library Code*, *Reading a Text List* and
  *Choosing a Random Item*. The text-file demo has a neutral music fixture and
  explicitly names the working folder. Exercise 9 remains the fuller file-IO
  treatment; Exercise 6 remains the module/package treatment.
- **Module 03 showed loop syntax before Module 04 taught it.** Moved the
  *Unpacking in for Loops* slide and its examples into Module 04. Removed the
  premature `for` and `if` examples from the dictionary-method demo and moved the
  dictionary-iteration example alongside the loop demo. Updated affected Slidev
  layout and animation route IDs.
- **Exercise 4's fixed-secret override relied on an unexplained OS concept.**
  Module 04 now introduces environment variables, `os.environ.get`, and the
  PowerShell/session and Bash/single-command setting forms with a music example.
- **Exercise 5 used the import guard before Module 06 explained it.** A new
  *Running and Importing a File* slide and demo now teach the guard in Module 05.
  It also explains importing a function and cached imports before the exercise
  asks students to check their own function interactively.
- **Exercises 7, 8 and 11 could leave students testing stale definitions.** Added
  explicit restart/import instructions; Exercise 11 also asks for a new object
  after changing the class.
- **Exercise 7's solver demonstration varied the guess instead of the candidate.**
  The corrected example keeps `slate` and its observed marks fixed, then compares
  `crane` and `trace` as candidate secrets. Executed both calls to confirm the
  shown results.
- **Exercise 9 removed a required file before the replacement loader existed.**
  The old root-level word list stays until the package-relative loader has been
  implemented and checked. It is then removed before the game is run again.
- **Exercise 9's loop skeleton turned into a different comprehension solution.**
  The solution now follows the supplied loop: clean once, validate, add to a set,
  then sort. Propagated that equivalent implementation through solution stages
  09 to 13 and regenerated their dependent starters.
- **Exercise 10 used datetime formatting before the libraries appendix.** A short
  *Recording a Timestamp* slide and demo introduce precisely the timestamp API
  used by the database insert, with the full datetime topic still in the appendix.
  The explanation of SQLite Boolean storage now describes integer storage rather
  than claiming that the SQL type name does not exist.
- **Exercises 10 and 11 bundled different integration jobs into one step.**
  Exercise 10 Step 6 now has separate substeps for the result tuple, recording the
  result and displaying statistics. Exercise 11 Step 5 separates `__str__` from
  refactoring `play`. These are sections of the same required steps; contracts
  and stage outputs stay intact.
- **The appendices retained stale tooling assumptions.** Exercise 12 no longer
  refers to installing Ruff in Exercise 1 or claims that the exercise code was
  annotated from Exercise 2. Its slide summary now recaps typing and checking.
  Exercise 13 explains its test-tool installation directly and no longer promises
  that all of its steps are small and independent.
- **Several guided code-writing steps lacked a hint pointing to their teaching
  source.** Added references to actual slide titles, including setup, imports,
  exceptions, class creation, file operations, timestamps and testing. Corrected
  malformed dictionary-method descriptions while checking these references.

## Exercise 2, 5 and 7 scaffolding follow-up

Implemented on 2026-10-19 after the trainer requested these three changes.

- Exercise 2 now checks plain input before cleaning it, then supplies the display
  formatting as a separate checkpoint. Students check the two first-letter
  comparisons with plain prints before copying a supplied formatted row. The
  canonical solution separates reading and cleaning into two assignments; its
  final output is unchanged. Temporary diagnostic prints are explicitly replaced.
- Exercise 5 now supplies a runnable first pass of `score_guess`. Students check
  its green matches before completing the second-pass condition and removal of
  a consumed letter. The CRANE/ERROR example explains the remaining-letter list,
  and three calls check the completed function before the game uses it.
- Exercise 7 now runs a loop-based renderer before asking for its generator form.
  A temporary `solver_check.py` checks one candidate against two observations,
  then turns the loop into `all` and the outer comprehension. Distinct letters,
  word counts, one proposed word's score and selection with `max` each have their
  own substep and small check. The temporary file is removed after integration.

Every code-writing substep has a hint pointing back to a teaching source.
Functions, names, final scoring and solver behaviour retain their contracts.
Intermediate practice snippets are deliberately temporary; completed functions
are checked against the canonical solutions.

The follow-up rehearsal executed the intermediate snippets from the exercise
text in order. It checked Exercise 2's input, cleaning, display, comparisons and
table, then compared the assembled final output with the canonical solution.
For Exercise 5 it checked the first-pass marks and remaining letters, filled the
second-pass skeleton and compared its function AST with the completed solution.
For Exercise 7 it executed the temporary helper checks and both renderer forms,
then verified that the assembled solver functions match the canonical ASTs.

Final follow-up checks pass: 549 code fences, all slide references, Ruff, twelve
generated starters, all thirteen solution stages and 39 quiz questions. The
exercise PDF and offline site are rebuilt. Selected revised PDF pages and the
substep/progress grouping for all three exercises were inspected. All fundamentals
artifact manifests verify. The slide sources were unchanged by this follow-up.

## Deferred Exercises 10 to 13

The trainer explicitly postponed further scaffolding of Exercises 10 to 13 on
2026-10-19. The scaffolding follow-up left their text and solutions intact.
The subsequent simplification pass changes only their secret-setting
instructions/code to Python variables. Their required feature set, earlier
audit corrections and existing substep boundaries remain in place.

- **Exercise 10:** add runnable checks between returning the game result,
  recording it and displaying statistics. The existing 6a/6b/6c headings divide
  the actions but do not yet provide independent checkpoints for each change.
- **Exercise 11:** guide the mechanical `play` refactor separately from writing
  the board renderer and methods. Verify state changes on a small object before
  connecting the full command loop.
- **Exercise 12:** review the cross-module `Mark` alias migration and the order
  of mypy checks alongside the neighbouring integrations. This is a follow-up
  review item, not a newly established defect.
- **Exercise 13:** split save/resume into saving, loading and connecting the
  restored game. Check persisted settings and interruption behaviour at their
  own checkpoints.

When this work resumes, retain the stage contracts, playable game behaviour,
output checks and generated-starter workflow. Reducing the required feature set
would need a separate spine decision. No timing or four-day schedule change is
part of this deferral.

## Verification of the initial audit

Executed all eight added/moved demo programs, checked the guard's direct-run and
import behaviour, and executed the corrected solver comparison and environment
override. All thirteen solution stages pass their applicable tests, transcripts
and type checks after the word-cleaning change.

The initial audit checks passed: 533 code fences, all slide references, Ruff, twelve
generated starters, 39 quiz questions, native animation checks and slide lint.
The rebuilt Slidev deck validates all 300 pages with no failures and the existing
FloatingVue warning. Exercises, Marp fallback and offline site build; fundamentals
artifact manifests verify.

Rendered and inspected the eight added/moved teaching slides and selected
exercise PDF pages. Checked the database integration's three substeps in the
browser, including their progress-counter grouping. The existing Slidev PDF
header-cropping limitation described in [the introduction note](gentler-introduction.md)
is still visible on some exported pages; the teaching content is readable.
