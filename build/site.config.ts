import * as path from 'path';
import { spawnSync } from 'child_process';

// Shared exercise site. The coordinator supplies course content and quiz questions separately.
export default {
  title: 'Python Programming',
  eyebrow: 'PRG400 · Python Programming',
  storagePrefix: 'prg400-site:',
  solutions: 'next-page',
  eggs: true,
  starterRows: [
    { label: 'Starter folder', value: 'exercises/starters/{slug}/' },
    { label: 'Handouts', value: 'exercises/handouts/{slug}/', exists: 'exercises/handouts/{slug}/' },
    { label: 'Run the game', value: 'uv run python -m wordle' },
    { label: 'Run the tests', value: 'uv run pytest' },
  ],
};

// A script entry point keeps the wiring to two files and works with Windows Bun shims.
if (import.meta.main) {
  const template = process.env.PRESENTATION_TEMPLATE_DIR ?? path.resolve(import.meta.dirname, '../../Presentation-Template');
  const result = spawnSync(process.execPath, ['run', path.join(template, 'build/site/build-site.ts'), ...process.argv.slice(2)], { stdio: 'inherit' });
  process.exitCode = result.status ?? 1;
}
