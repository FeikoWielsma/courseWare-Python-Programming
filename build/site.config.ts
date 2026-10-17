import * as path from 'path';
import { spawnSync } from 'child_process';
import questions from './site/quiz.json';
import { wordlePlugin } from './site/plugin.ts';

// Shared exercise site. The coordinator supplies course content and quiz questions separately.
export default {
  title: 'Python Programming',
  eyebrow: 'PRG400 · Python Programming',
  storagePrefix: 'prg400-site:',
  solutions: 'next-page',
  eggs: true,
  starterRows(entry: { label: string; modName: string }) {
    const exercise = Number(entry.label);
    if (exercise === 1) return [];
    const rows = [
      { label: 'Starter folder', value: 'exercises/starters/{slug}/' },
      { label: 'Handouts', value: 'exercises/handouts/{slug}/', exists: 'exercises/handouts/{slug}/' },
      { label: 'Run the game', value: exercise < 6 ? 'uv run python wordle.py' : 'uv run python -m wordle' },
    ];
    if (exercise >= 5) rows.push({ label: 'Run the tests', value: 'uv run pytest' });
    if (exercise >= 12) rows.push({ label: 'Type-check', value: 'uv run mypy wordle' });
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
  const template = process.env.PRESENTATION_TEMPLATE_DIR ?? path.resolve(import.meta.dirname, '../../Presentation-Template');
  const result = spawnSync(process.execPath, ['run', path.join(template, 'build/site/build-site.ts'), ...process.argv.slice(2)], { stdio: 'inherit' });
  process.exitCode = result.status ?? 1;
}
