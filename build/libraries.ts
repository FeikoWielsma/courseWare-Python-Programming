import { courseware } from './toolchain.ts';

// --out is relative to libraries/; both decks share the course archive.
const archivedMarp = process.argv.includes('--marp')
  && !process.argv.includes('--exercises') && !process.argv.includes('--out');
courseware('build', 'libraries', ...(archivedMarp
  ? ['--out', '../archive/PRG400-Python-Libraries-and-Tools-Marp.pdf'] : []));
