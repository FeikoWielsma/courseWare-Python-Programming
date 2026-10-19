> Historical record (2026-10-17). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# WP5 : student review of PRG400

Date: 2026-10-17. Reviewer: GPT-6.1-sol. Package: `wp5`.
Baseline: `e8cfef222363674bf775af2f1548fd2aff05f417`.
Branch: `t3/review-prg400-course` (initial name: `t3/9ab9a97c`).
Worktree: `C:/Users/feiko/.t3/worktrees/Python-Programming/t3-9ab9a97c`.
Scratch evidence: `C:/Users/feiko/AppData/Local/Temp/prg400-wp5-9ab9a97c`.

## Verdict and method

The prescribed exercise path is completable; no blocker was reproduced. The core game is coherent. Do not sign off the complete package yet: fix save/resume, the hidden site's Wordle rendering, missing reference tests and factual slide errors. Rebudget Day 4 or make an explicit cut. A trainer can pilot the main sequence with known limitations; students should not have to discover them unaided.

Read AGENTS.md in full, plan sections1–6, README and tasks before changes. Copied each Exercise2–13 starter to its own scratch directory outside the repo. Exercise1 began with `uv init wordle` in an empty scratch folder. Implemented from instructions/skeletons/hints and then compared with reference solutions. No solutions, starters, handouts, slides, demos or configuration were edited.

**Method limitation:** initial reads of Exercises2–5 inadvertently included solution blocks before reconstruction. Those are functional instruction checks, **not blind beginner trials**. Exercises6–13 were read through a solution-stripping helper first. Final stages and important intermediate states were run; this is not a timed human study or an exhaustive replay of every editing keystroke. A fresh human beginner pass of2–5 remains desirable.

Checked existing uv/Python/editor prerequisites; did not reinstall VS Code/extensions. Tested missing-file and EOF recovery; did not send an actual interactive Ctrl+C. EOF exercises the same handler. Python3.14.3, uv0.11.2, scratch pytest9.1.1/mypy2.4.0. Reference copies used their own locked environments.

Scratch harness escaping/replacement mistakes were corrected and are not course findings. Port8765 initially served another process's site; switched to48763 and verified the worktree build before recording browser results.

## Small fixes committed

Each includes `Co-Authored-By: GPT-6.1-sol <noreply@openai.com>`.

| Ex | Commit | Original problem / change |
|---|---|---|
| 2 | `bd86270` | Step3: inner string “takes single quotes”. Python3.14 permits reused double quotes; reframed as readability choice. Ran both forms. |
| 3 | `9eb7366` | Step2 linked Sets for operators; Step4 linked Accessing Values in Dictionary for get. Corrected to Set Operations / Dictionary Functions and Methods. |
| 8 | `1ac7d44` | Step4: “Use the messages in the solution below.” Supplied required strings before revealing the implementation. |
| 9 | `0f989ef` | Said students typed the word file; actually copied it. Step3 repeated a list-returning call but displayed935. Explicit fresh REPL, len(load_words()), exit(), correct provenance. |
| 11 | `4b7c12b` | Steps3/5 omitted REPL-echoed guess mark lists. Added captured output; removed false claim that Exercise10 repeats the secret on a win. |
| 13 | `4dfc07d` | Intro grouped pytest into stdlib. Identified it as the third-party runner installed in5. Analogous slide remains wrong (F11). |

## Open findings, severity ordered

No blockers. Major = wrong/misleading; minor = polish or a documented edge. These remain open; fixes above are already applied.

| ID | Severity | Location and quote | What happens / reproduction | Concrete proposed fix |
|---|---|---|---|---|
| F01 | major | `build/site/assets/wordle.js:76`: `var word = guesses[r] ...` | Submitted guesses are objects, indexed as strings. After `error`, coloured tiles have no letters and accessible names say `undefined absent`. Even a winning green row is blank. | Read `guesses[r].word`; keep `.states` for colours. Browser-test submitted text, duplicate-letter score and accessible labels. |
| F02 | major | Ex13 Step4: “Save the secret and the guesses”; `Game.is_over` uses `guesses_left == 0`. | Start --easy, make7 nonwinning guesses, interrupt; restart without flags: `Guess 8/6`, then `Got it in 8!`. A resumed --hard game also accepts trick after slate if restarted without flags. Confirmed in student and untouched reference copies. | Persist/restore max_guesses and hard in Ex13/storage/main/game/tests. Make exhaustion <=0 in Ex11 and solutions11–13; test lowering the limit below history length. Regenerate dependent starters. |
| F03 | major | Ex10 Steps3–5: “Start a test file, tests/test_stats.py”. | Four quoted tests pass in student project; none exists in solution10 or later solutions/starters. Reference remains12 tests at10 instead of16. Catching up loses the safety net. | Add the4 tests to solutions10–13; regenerate starters11–13. |
| F04 | major | Ex13 Steps3/6: `assert not follows_hints("clink", history)` / `test_check_guess_rejects_capital_letters`. | Both missing from solution13/tests/test_ex13.py. Text creates6 cases; reference has5. Student total21, reference20. | Copy missing assertion, capital-letter test and imports into the reference file. Keep the6-case transcript. |
| F05 | major | Ex10 Steps3–5 points at Retrieving Data; Step4 needs GROUP BY. | Module10 teaches DB-API/SELECT-all, not aggregates, NULL/COALESCE, WHERE/GROUP BY/ORDER BY. Hints permit completion, but preceding slides do not prepare a Python beginner to derive the ★★★ query. | Add a neutral SQL aggregation/grouping slide/demo, or supply SQL as a ★ step and have students process rows. Increase timing. |
| F06 | major | Ex10 Step6: `with connect() as connection:`; solutions10–13 main/game. | Context manages transaction, not closing (slide correctly says so). Reference print_stats(); gc.collect() under -W always::ResourceWarning reports unclosed database. record_game commits internally, so an outer context cannot undo a committed insert after a later exception. | Explicitly close with finally/closing and choose one transaction owner. Update Ex10 and solutions10–13; regenerate starters. |
| F07 | major | Module02 Variables: “Variables represent memory locations”; Python Numbers: “Delete single object ... with del”. | Contradicts name/object diagram and Functions. `a=[]; b=a; del a; print(b)` prints[]. Rebinding can choose an existing object, not necessarily allocate one. | Rewrite affected module02 bullets as name binding/removal, retain diagram. |
| F08 | major | Module03 List Functions and Methods: `list.pop(obj=list[-1])`, `list.sort([key, reverse])`. | pop takes index: [10,20,30].pop(1) returns20; pop(20) raises IndexError. sort(None,True) raises TypeError (keyword-only options). | Use pop(index=-1) and sort(key=..., reverse=...) with correct descriptions; check demo wording. |
| F09 | major | Module03 Usage of Tuples: “Tuples can be dictionary keys”; Properties of Dictionary Keys: “Keys must be immutable”. | Immutable tuple containing a list is unhashable, exactly like Ex3's `(guess, ruled_out_letters)`. `{("crane", []): 1}` raises TypeError. | Teach hashability; tuple requires all hashable items. Add this neutral counterexample to module03. |
| F10 | major | Module06 Locating Modules diagram: “current directory”. | For python subdir/script.py, first sys.path entry is script directory, not shell cwd. Relevant to package and cwd experiments. | Distinguish script-directory from REPL/-m cwd lookup in diagram/summary. Replace Windows CMD set PYTHONPATH with PowerShell syntax or label shell. |
| F11 | major | Module13 Standard Library Overview lists pytest. | pytest is not in sys.stdlib_module_names and fresh Python does not include it. Exercise intro fixed; slide still contradicts setup. | Separate third-party pytest, already installed in5, from standard library list. |
| F12 | major | Module13 summary: “isoformat does both without a pattern”. | isoformat formats; fromisoformat parses. Earlier slide is right, summary wrong. | Name formatting/parsing APIs separately. |
| F13 | minor | Final117-page PDF: pp67/80 have only “Solution on next page”. | Forced pagination orphans cues. Other fragments: Ex5 Step5 tail p37; Ex6 Step4 output p45; Ex10 Step3 output p78; Ex11 Step4 output p92; Ex13 Step6 hint p115. Ex6 Step2 table follows prompt on next page (41/42). Ex4 full solution splits final else to p30. | Shared Presentation-Template PDF style/preprocessing: keep cue with prior block; keep short prompt/table and hint/output groups. Consider shorter script solution excerpts. Rebuild and visually inspect. No shared build changes made here. |
| F14 | minor | Ex2 Steps2–3: “does it have five letters?” | Input a raises IndexError in indexed table before length check. No if yet, so temporary precondition is defensible but unstated. | Add sentence requiring5-letter input until Ex4; explain that a later printed check does not protect earlier indexes. |
| F15 | minor | Solutions/starters09–13 __main__: “Restore words.txt and try again.” | After Ex9 deletes root words.txt, advice is wrong; missing allowed list gives same message. | Ex9 should update handler to name wordle/data/words.txt and allowed.txt; mirror in solutions09–13; regenerate starters. |
| F16 | minor | Solutions09–13 data/answers.txt; text says words.txt is answer list. | Byte-identical unused/unmentioned file in all5 stages. SHA256 `66e7cd04e609bdc7ca1e93eda2161821042b137e3b1b6557a19e6cd3cc10ccf8`. Apparent third list confuses the two-list lesson. | Remove answers.txt from solutions09–13 and regenerate starters10–13. |
| F17 | minor | Module05 Scope: “Modifying a global variable ... requires global”. | Mutation through global list.append works without global; rebinding name requires it. | Say “Rebinding a global name inside a function requires global”. |
| F18 | minor | Module09 Opening Files: “buffering ... 0, no buffering”. | Text open(...,buffering=0) raises ValueError on3.14. | Qualify zero-buffering as binary-only; line-buffering as text-mode. |
| F19 | minor | Module02 String Operations: [2:5] “3rd to 6th”; number table sqrt requires x>0. | Slice is third through fifth characters; sqrt(0) is valid. | Correct comment/domain in slides and matching demo if needed. |
| F20 | minor | build/site.config.ts starter rows: tests from5, mypy from12. | Paths/game commands are right, but fresh5/6/7/11 cannot immediately collect new imported names;12 has not installed mypy. Bodies explain most staging, summary does not. | Qualify checks with prerequisite step, or omit premature rows. |
| F21 | minor | Wordle JS key handler intercepts Enter. | Open dialog: Close focused. Enter leaves it open, says Enter five letters. Escape/mouse close work. | Preserve normal Enter/Space activation on focused buttons; scope guess keys appropriately. |
| F22 | minor | Ex9 Steps1/5 marked ★★: only signatures and `...`. | ★★ is defined as skeleton/body-to-fill, but these give no structural body. Hints eventually supply strategy; expectations/time suffer. | Add short loop/filter/with skeleton or relabel ★★★. |
| F23 | minor | Ex12 Step3 quoted best_guess vs solution12. | Quote puts empty guard before counts; folder computes counts first. Equivalent behaviour, violates verbatim-code contract. Intentional earlier-step intermediate versions are excluded. | Prefer moving guard before letter_counts in reference12 and dependent stages. |
| F24 | minor | Ex13 Step4 “continues at guess2”. | History restored but previous board never redrawn in new terminal. board command is only optional in11. | Print restored Game before first resumed prompt and update expected output. |
| F25 | minor | README, Checking your own code: “The course sets both up in module1”. | Refers to Ruff and mypy, but mypy is installed only in appendix12. A student trying the advertised command earlier has no project-local checker. | Say Ruff is set up in1 and mypy in12, consistent with the dependency examples immediately above. |
| F26 | minor | Module12 recap: “A comment ... goes stale, an annotation does not”. | Annotations can contradict code until tooling checks them; the appendix's own not-enforced example demonstrates that. | Qualify the claim: a checker can detect drift in annotations; Python alone cannot. |

## Execution evidence

Scratch scripts: review.py (copies starters, hides solutions, captures runs), student_early.py (1–5), student_middle.py (6–8), student_late.py (9–10), student_classes.py (11–12), student_appendix.py (13), reference_review.py (copies and runs solutions), factual_review.py (Python3.14 counterexamples). Per-command stdout/stderr/exit logs are beside each scratch project. Preserve this directory to resume.

| Ex | Executed result |
|---|---|
| 1 | Empty uv init; greeting; Ruff clean/error/fix;5610-character list. Exact hello.py spacing rechecked with isolated Ruff defaults: one F401 as quoted. |
| 2 | react table, slices/counts, tabs/raw string match. Short input reproduces F14; both f-string quote forms work. |
| 3 | TRUST,935 words, set/history/stats outputs match; tuple reassignment gives quoted TypeError. |
| 4 | Win, quit,6-guess loss, invalid guesses without turn cost, letters command all match. |
| 5 |5 selected scoring tests and all9 pass; error/crane yields one coloured R. |
| 6 | Package plays via -m; removed old script/test; pytest path configured;4 pass. |
| 7 | Display test before solver;4 solver/all8 pass; slate ->15 candidates/GRACE/still guess2. |
| 8 |8 tests after wrapper;3 written exception tests ->11 pass.3 invalid-input reasons keep turn1; missing file/EOF recover. |
| 9 |981 lines ->935 words; write5610; old cwd loader fails, new returns935;12 pass; crone accepted; CSV two-game stats2/1 match. |
| 10 |4 new stats tests /16 total pass.4 games ->4played/3won/75%,1/2/3 each1#,streak1. Reference only12 tests (F03). |
| 11 | Step2 exactly1/3 tests passes; zero/negative experiment matches; final3/15 pass. Captured both REPL sessions for output correction. Lowered-limit edge reproduced. |
| 12 | Expected used_letters error; alias-only3 errors; propagated Mark passes; intentional yelow caught. Empty hint crashes before Optional fix, then no-candidate message.15 tests pass. |
| 13 | Fixed date289/drill/935; daily twice same answer; easy10; hard rejection; JSON interruption/resume/clear; capital rejection.6 Ex13/21 total pass; mypy9 files clean. Deliberate wrong assertion produces readable failure then restored. |

All13 reference copies match saved build/transcripts. Reference pytest counts for5–13:9,4,8,11,12,12,15,15,20. Both reference mypy runs pass. Green current checks miss the persistence/site defects and omitted coverage.

## PDF/site

Built requested commands from build/ with PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/Presentation-Template. Initial PDF116 pages; final117. Rendered every page with PyMuPDF, inspected10 contact sheets and affected final pages. No unreadable fonts/indentation; grouping defects F13. Scratch pdf/ holds PNGs/extraction.

Headless Chrome uses Puppeteer from shared template node_modules. All13 decks return200 with rendered SVG slides. All62 inline preview buttons open the corresponding SVG dialog; every authored italic slide reference resolves. Ex3's resolved-but-wrong topics corrected. Starter paths exist; commands use script through5, package from6; tests/mypy staging is F20. Progress survives reload; hints open; solution confirmation appears.

Quiz checker:39 questions/25 executable examples pass. Browser:39 completed with1 deliberately wrong ->38/39, Confident Coder, streak38; restart goes to Question1. Printed certificate view generated. Typing wordle in name field does not trigger game. Hidden Wordle opens outside fields, short-input message/escape/win work; letters disappear and focused Close cannot activate with Enter (F01/F21). No JS page errors on tested paths. Evidence: site-report.json, site-interactions.json, site-finish.json, wordle-after-guess.png, quiz-complete.png, quiz-certificate.pdf in scratch.

Generated site/dist/PDF/HTML never committed. No push, merge or master commit.

## Timing : median ★★ participant

Estimates include required steps (including required ★★★ with hints), reading, typing and ordinary debugging; exclude optional closers. Not stopwatch measurements.

| Ex | Plan/stated min | Estimate | Range | Pressure |
|---|---:|---:|---|---|
| 1 |30|35|25–50|Install/terminal restart/interpreter selection.|
| 2 |45|40|30–50|Indexed rows/bool formatting.|
| 3 |60|50|40–65|Four collection models/bool-to-int update.|
| 4 |75|80|65–100|Nested loop/commands/else and three games.|
| 5 |90|105|85–130|First function refactor/pytest/duplicate-letter algorithm.|
| 6 |45|50|40–65|Imports/file cleanup.|
| 7 |75|90|70–110|Nested comprehension/all/sum and solver wiring.|
| 8 |60|70|55–85|Handlers and first written tests.|
| 9 |45|75|60–90|Six steps: cleaning/REPL/relocation/two lists/CSV/stats.|
|10|60|95|75–115|SQL gap/four tests/return-contract refactor.|
|11|90|110|90–135|Methods/properties/setter and loop refactor.|
|12|40 stated|50|40–65|Mark propagation/invariance/Optional narrowing.|
|13|75 stated|110|90–140|Seven steps/hard/storage/six test cases.|

Core total800min vs675 planned (+125). Day1:125/135; Day2:185/165; Day3:210/180; Day4:280/195. Day4 is4h40 of exercises before lectures/breaks/questions. Apply plan's explicit skip options for slower groups; do not count on both appendices fitting.

## Slide coverage by exercise

| Ex | Coverage / gaps |
|---|---|
|1|Toolchain/running/editor covered; Path/function/guard explicitly supplied incantations. Manual PATH examples are not PowerShell; Unix example appends executable-looking path instead of containing directory. Label/fix if retained.|
|2|Operators/methods/index/slice/format covered; !s is supplied in hint. Correct name/object and slice/domain errors.|
|3|Sets/tuple/list/dict/annotations sufficient; imports supplied. Correct methods/hashability.|
|4|while/continue/enumerate/match/else covered. match slide returns inside function-shaped example before Functions; simpler literal-command example would transfer better. No blocker.|
|5|Signatures/defaults/returns/mutation covered; early guard/pytest supplied. Scoring is first real algorithm; allow time. Fix global wording.|
|6|Package/import/entry point covered; pytest path setup supplied. Fix module lookup/shell specificity.|
|7|Comprehensions/zip/all/sum/key/generator covered; strict and tie rule supplied. Flat two-for set comprehension is denser than nested-list slide; add neutral flat example.|
|8|Exception types/handling/raising/tracebacks covered. pytest.raises with-context before IO module but explained in text/hint. Small exception-test slide here would reduce appendix dependence.|
|9|Path/read/write/with/CSV covered; __file__/parents/isascii supplied. Six steps exceed45min; qualify buffering.|
|10|DB-API/parameters/transactions/fetching covered; aggregate/NULL/WHERE/GROUP BY/ORDER BY gap is substantial. Slide correctly requires close; exercise omits it.|
|11|Public attributes/methods/properties/setter/str in same order; no core gap. Later persistence exposes exhausted-state defect.|
|12|Literal/alias/collections/Optional/mypy covered; invariance explained via notes/instructions. Recap says annotations cannot go stale, but they can without tooling; qualify.|
|13|Dates/JSON/regex/argv/assert/raises/parametrize covered. Required fullmatch absent from matching slide (only match/search/findall): add. Fix pytest/isoformat. Feature slide uses ValueError from demo's validating divide; identify wrapper so students do not reuse ordinary division from8.|

For time, IO internals/binary struct and DB metadata are candidates to shorten to make room for actual exercise prerequisites. Most unused slide content is reasonable background.

## Known leftovers

- answers.txt duplication: **confirmed** in09–13, F16.
- connect() cwd-relative: **confirmed/documented**. Ex10 Step1 explicitly requires project folder; optional closer asks for fixed location. Intentional limitation, not blocker.
- Ex7 pytest until Step4: **dismissed as missing explanation**. Step1 runs only display test; Step2 warns of future imports; Step3 explicitly delays solver tests until Step4. Game remains playable.

## Gates and next action

- check-fences:378 checked, no problems.
- ruff check .:all passed.
- make-starters --check:12 up to date; only proves consistency with incomplete current solution tests.
- check-quiz:39 questions/25 examples pass.
- Requested PDF/site builds succeed. No slides edited, so slide-edit lint gate does not apply.

Before teaching: F01–F06, factual slides F07–F12, feasible Day4 schedule. Fix F13 before printing a class set. Remaining items are small follow-ups. Retain scratch evidence; final coordinator report should state the2–5 blind-review limitation.
