# Archive

The generated `*-Marp.pdf` and `*-Marp.html` files are optional static versions
of the two slide decks. The main course folders contain the current Slidev
presentations and PDFs. The Marp HTML files open directly from disk.

Rebuild these fallbacks with `bun run --cwd build build:marp` and
`bun run --cwd build libraries:marp`. Both commands write to this folder.
The student bundle includes these generated files and this index.

The historical material listed below is kept for trainers. It is not built,
linted, or shipped in the student bundle.

- `calculator/` : the calculator exercise spine of Exercises 2 to 11, replaced by
  the Wordle spine in October 2026. It has its own README.
- `demos/` : demo folders that no slide referenced, from earlier versions of this
  course and from adjacent courses (library tours, decorators, generators, GUI
  toolkits, mocking, a case study). Several are Python 2.
- `demos/05-functions/`, `06-modules/`, `08-exceptionhandling/`, `09-python-io/` :
  files that sat beside the live demos but that no demo or slide used. The setup.py
  packaging example with its committed build output, the executable-building
  experiments, older CSV and binary-file scripts, and their data files.
- `old-exercises/` : exercise documents from other courses (Word files on
  datetime, regular expressions, XML, decorators, NumPy) and mod_python notes.
- `PRG400-Python-Programming_og.pdf` and `PRG400-Python-Programming-Exercises_og.pdf` :
  the original deck and exercise booklet. Never edited.
