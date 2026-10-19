import { courseware } from './toolchain.ts';

// Keep the static fallback out of the student's main course folder.
const archivedMarp = process.argv.includes('--marp')
  && !process.argv.includes('--exercises') && !process.argv.includes('--out');
courseware('build', 'fundamentals', ...(archivedMarp
  ? ['--out', 'archive/PRG400-Python-Programming-Marp.pdf'] : []));
