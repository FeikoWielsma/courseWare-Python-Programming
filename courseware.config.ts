// Decks built by the shared Presentation-Template build/courseware.ts.
// PDF names come from each deck's src/slides/00-preamble/00-preamble.md (pdfName).
export default {
  decks: {
    fundamentals: { renderer: 'slidev', archive: 'build/dist/Python-Programming-slides.zip' },
    libraries: {
      dir: 'libraries',
      renderer: 'slidev',
      archive: 'build/dist/PRG400-Python-Libraries-and-Tools-slides.zip',
    },
  },
  // The student bundle is an allowlist: tracked files below these paths, plus each deck's
  // PDFs, HTML and presentation (slides/, libraries/slides/) from its build manifests.
  // A new demo folder needs one edit, here.
  bundle: {
    archive: 'build/dist/Python-Programming-student.zip',
    include: [
      'README.md',
      // Only the archive index and manifest-declared Marp outputs travel.
      'archive/README.md',
      // Travels so the Ruff extension sees the course rules; the student writes pyproject.toml.
      'ruff.toml',
      // GitHub Codespaces setup, used by the GitHub mirror of the student repository.
      '.devcontainer',
      'demos/01-pythonintro',
      'demos/02-variablesanddatatypes',
      'demos/03-datastructures',
      'demos/04-controlflow',
      'demos/05-functions',
      'demos/06-modules',
      'demos/07_comprehensions',
      'demos/08-exceptionhandling',
      'demos/09-python-io',
      'demos/10-python-database-access',
      'demos/11-python-classes',
      'demos/12-appendix-type-hinting',
      'demos/13-appendix-libraries',
      'demos/14-appendix-python-tooling',
      'solutions',
      'exercises',
      'appendices',
      // Curated background reading; every part of it is meant for the student.
      'reference',
      'libraries',
    ],
    exclude: ['libraries/build', 'libraries/src'],
    // The offline exercise site (bun run site); students open site/index.html from disk.
    // Add a root-level shortcut in the student checkout and ZIP.
    generated: { site: 'build/site/dist', '.': 'build/site/student-shortcut' },
    // Known failure: the Marp HTML embeds the preamble's trainer notes (Marp presenter view).
    // Waived until the Marp renderer stops emitting them; remove this line to make it fail again.
    waiveMarpHtmlNotes: true,
  },
  // Each build is released as build-<short commit>; latest follows the newest build.
  release: { pointer: 'latest' },
  // Synchronised by courseware.ts sync-student after a release, with its own retry.
  student: {
    repository: 'ssh://git@git.feikowielsma.nl:222/SpiralTrain/Python-Programming-Student.git',
    sshKeyEnv: 'STUDENT_REPO_SSH_KEY',
    // Codespaces only runs on GitHub. The mirror shares the history, so `git pull` keeps working.
    mirrors: [{ repository: 'git@github.com:FeikoWielsma/Python-Programming-Student.git', sshKeyEnv: 'STUDENT_MIRROR_DEPLOY_KEY' }],
    author: { name: 'Forgejo CI/CD', email: 'ci@feikowielsma.nl' },
    // Keeps a student's own scratch work out of `git status` when they pull.
    gitignore: [
      '# System and Python temp files',
      'Thumbs.db',
      'Desktop.ini',
      '.DS_Store',
      '**/__pycache__/',
      '**/*.py[cod]',
      '**/*$py.class',
      '**/.venv/',
      '**/venv/',
      '**/env/',
      '**/.mypy_cache/',
      '**/.ruff_cache/',
      '**/.pytest_cache/',
      '',
      '# Custom course work folders created by the student',
      '/course-work/',
      '/my-project/',
    ],
  },
};
