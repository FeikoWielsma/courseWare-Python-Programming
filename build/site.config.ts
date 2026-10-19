import * as path from 'path';
import * as fs from 'fs';
import { spawnSync } from 'child_process';
import questions from './site/quiz.json';
import { wordlePlugin } from './site/plugin.ts';
import { presentationPage } from './site/presentation.ts';
import { templateDir } from './toolchain.ts';

// Shared exercise site. The coordinator supplies course content and quiz questions separately.
export default {
  title: 'Python Programming',
  eyebrow: 'PRG400 · Python Programming',
  storagePrefix: 'prg400-site:',
  solutions: 'next-page',
  eggs: true,
  extraPages: [presentationPage],
  moduleDeckHref(module: string) {
    return `presentation.html?module=${encodeURIComponent(module)}`;
  },
  starterRows(entry: { label: string; modName: string }) {
    const exercise = Number(entry.label);
    if (exercise === 1) return [];
    const rows = [
      { label: 'Starter folder', value: 'exercises/starters/{slug}/' },
      { label: 'Handouts', value: 'exercises/handouts/{slug}/', exists: 'exercises/handouts/{slug}/' },
      { label: 'Run the game', value: exercise < 6 ? 'uv run python wordle.py' : 'uv run python -m wordle' },
    ];
    if (exercise === 13) rows.push({ label: 'Run the tests', value: 'uv run pytest' });
    if (exercise >= 12) rows.push({ label: 'Type-check (after Step 1 installs mypy)', value: 'uv run mypy wordle' });
    return rows;
  },
  quiz: {
    questions,
    title: 'The PRG400 Python quiz', eyebrow: 'PRG400 · Python Programming',
    linkText: 'Take the Python quiz', startLabel: 'Start the quiz', restartLabel: 'Try again', finishLabel: 'See your result',
    ranks: [
      [1, 'Python Pro', 'A precise reading of the whole course.'],
      [0.8, 'Confident Coder', 'You can explain most of the choices your code makes.'],
      [0.6, 'Working Programmer', 'Good foundations. Review the questions that surprised you.'],
      [0.4, 'Careful Learner', 'Take another pass through the examples and try again.'],
      [0, 'Code Explorer', 'Every question is a useful place to start.'],
    ],
  },
  plugins: [wordlePlugin],
};

// A script entry point keeps the wiring to two files and works with Windows Bun shims.
if (import.meta.main) {
  const result = spawnSync(process.execPath, ['run', path.join(templateDir(), 'build/site/build-site.ts'), ...process.argv.slice(2)], { stdio: 'inherit' });
  process.exitCode = result.status ?? 1;
  if (process.exitCode === 0) {
    const siteDir = path.join(import.meta.dirname, 'site/dist');
    const courseDir = path.resolve(import.meta.dirname, '..');
    const marpHtml = fs.readFileSync(path.join(courseDir, 'PRG400-Python-Programming-Marp.html'), 'utf8');
    const embeddedDeck = marpHtml.replace(/<div class="bespoke-marp-note"[^>]*>[\s\S]*?<\/div>/g, '');
    fs.writeFileSync(path.join(siteDir, 'slides-marp.html'), embeddedDeck);
    const shortcutDir = path.join(import.meta.dirname, 'site/student-shortcut');
    fs.mkdirSync(shortcutDir, { recursive: true });
    fs.writeFileSync(path.join(shortcutDir, 'index.html'), '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=site/index.html"><title>Python Programming exercises</title></head><body><p><a href="site/index.html">Open the Python Programming exercise site</a></p></body></html>\n');
  }
}
