# A gentler Python introduction

Trainer feedback, implemented 2026-10-19. Module 01 assumes less experience with
computers and programming. Its first learning goal is to edit, save and run a
Python source file and relate the statements to the output.

## Content

- Module 01 defines programs, source code, output, files, folders, the editor,
  terminal and prompts. Its examples use `print()`, strings and comments, followed
  by repairing a missing quote. Interactive mode follows script execution.
- Essential uv installation and run commands remain in Module 01. A bare project
  avoids presenting generated functions and entry-point guards before they are
  taught. Full tooling, Ruff, project files, PATH, history and detailed syntax
  reference move to appendix 14.
- Five small music demos replace the introduction's original demos. Five existing
  demos move to the appendix, together with the block-execution animation and its
  provenance check. The student bundle includes the new demo folder.
- Exercise 1 creates `wordle.py` with plain statements. Its solution and generated
  Exercise 2 starter have no Ruff dependency or word list. Exercise 3 now supplies
  the word list, with the later IO exercise's reference updated accordingly.
- The opening quiz questions assess running saved files and statement order.
  README, AGENTS, plan and tasks describe the revised progression.

## Verification

- Ran the bare-project setup and guided messages in an isolated temporary folder
  using Python 3.14; verified the missing-quote error and all ten demos.
- Fences: 523 checked, no problems. Slide references resolve. Ruff passes.
- Twelve generated starters are current. All thirteen solution stages pass,
  including the stage tests, transcripts and mypy checks. The quiz checker passes
  all 39 questions, including 26 executable examples.
- The core animation check passes ten slides and 68 states after relocating its
  reference demo and route.
- Slide lint reports all slides within budget. The Slidev build validates all
  292 pages with no failures and one upstream FloatingVue warning. Exercises PDF,
  Marp fallback PDF/HTML and the offline exercise site build. All fundamentals
  artifact manifests verify.
- Inspected selected rendered slides and Exercise 1 PDF pages. The exercise
  layout is readable. Opened the offline guide and confirmed that its Preparing
  Python preview opens the correct Module 01 slide.

## Rendering limitation

Some exported Slidev PDF pages crop their header (observed on Creating a Project,
Running a Python File and Reading a Syntax Error). The teaching content remains
visible. The browser deck has the header in its expected position; the automatic
layout check does not report this PDF-only problem. The Marp fallback is rebuilt.
Shared renderer changes are outside this content revision.

Tool command references checked against the official
[uv installation guide](https://docs.astral.sh/uv/getting-started/installation/),
[uv project guide](https://docs.astral.sh/uv/guides/projects/) and
[VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial).
