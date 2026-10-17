import * as path from 'path';
import * as fs from 'fs';
import { spawnSync } from 'child_process';

const root = path.resolve(import.meta.dirname, '..');
const course = path.join(root, 'libraries');
const template = process.env.PRESENTATION_TEMPLATE_DIR
  ?? path.resolve(root, '../Presentation-Template');
const args = process.argv.slice(2).filter(arg => arg !== '--');
const lint = args.includes('--lint');
const script = lint ? 'lint-slides.ts' : 'build.ts';
const result = spawnSync(process.execPath, [
  'run', path.join(template, 'build', script),
  ...args.filter(arg => arg !== '--lint'),
], { cwd: course, stdio: 'inherit' });
if (result.error) throw result.error;
process.exitCode = result.status ?? 1;
if (process.exitCode === 0 && !lint && !args.includes('--exercises') && !args.includes('--serve')) {
  const html = path.join(course, 'build/dist/combined.html');
  if (fs.existsSync(html)) {
    fs.copyFileSync(html, path.join(course, 'PRG400-Python-Libraries-and-Tools.html'));
  }
}
