import * as fs from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';
import { spawnSync } from 'node:child_process';

const workspace = path.resolve(import.meta.dirname, '..');
const root = path.join(workspace, 'libraries');
const production = path.resolve(workspace, '../Presentation-Template');
const shared = process.env.PRESENTATION_TEMPLATE_DIR
  || (fs.existsSync(path.join(production, 'build/slidev/build.ts'))
    ? production : path.resolve(workspace, '../_worktrees/presentation-template-slidev'));
const args = process.argv.slice(2).filter(arg => arg !== '--');
const value = (option: string) => {
  const index = args.indexOf(option);
  if (index < 0) return undefined;
  if (!args[index + 1] || args[index + 1].startsWith('--')) throw new Error(`${option} requires a value`);
  return args[index + 1];
};
function run(script: string, forwarded: string[], template = shared) {
  const result = spawnSync(process.execPath, ['run', path.join(template, 'build', script), ...forwarded], { cwd: root, stdio: 'inherit' });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exit(result.status ?? 1);
}

const exercises = args.includes('--exercises');
const marp = args.includes('--marp');
const serving = args.includes('--serve') || args.includes('--dev');
const slidesDir = path.resolve(root, value('--slides-dir') || 'src/slides');
const preamble = exercises ? '' : fs.readFileSync(path.join(slidesDir, '00-preamble/00-preamble.md'), 'utf8');
const defaultName = /^pdfName:\s*["']?([^\r\n"']+)/m.exec(preamble)?.[1].trim() || 'course.pdf';
const fallbackName = defaultName.replace(/\.pdf$/i, '-Marp.pdf');
const target = path.resolve(root, value('--out') || (marp && !exercises ? fallbackName : defaultName));

if (args.includes('--lint')) {
  run('lint-slides.ts', args.filter(arg => arg !== '--lint'));
} else if (exercises || marp) {
  const forwarded = args.filter(arg => arg !== '--marp' && arg !== '--dev');
  if (marp && !exercises && !value('--out')) forwarded.push('--out', target);
  if (args.includes('--dev') && !forwarded.includes('--serve')) forwarded.push('--serve');
  run('build.ts', forwarded, process.env.PRESENTATION_TEMPLATE_DIR || production);
  if (marp && !exercises && !serving && !args.includes('--no-html')) {
    const html = /\.pdf$/i.test(target) ? target.replace(/\.pdf$/i, '.html') : `${target}.html`;
    fs.copyFileSync(path.join(root, 'build/dist/combined.html'), html);
    // Retain the original standalone HTML link for existing student bundles.
    if (!value('--out')) fs.copyFileSync(html, path.join(root, defaultName.replace(/\.pdf$/i, '.html')));
  }
} else if (serving) {
  run('slidev/build.ts', [...args.filter(arg => arg !== '--serve' && arg !== '--dev'), '--dev']);
} else {
  if (args.includes('--notes')) throw new Error('Use the slidev --notes command for a separate trainer build. Ordinary builds package the student presentation.');
  const ignored = new Set(['--force', '--skip-lint', '--no-html']);
  const forwarded = args.filter((arg, index) => !ignored.has(arg) && arg !== '--out' && args[index - 1] !== '--out');
  const selected = args.includes('--range') || args.includes('--with-clicks');
  const prepareOnly = args.includes('--prepare') || args.includes('--check-only') || args.includes('--serve-only');
  if (!selected && !prepareOnly) {
    if (!forwarded.includes('--pdf')) forwarded.push('--pdf');
    if (!forwarded.includes('--check')) forwarded.push('--check');
  }
  if (args.includes('--range') && !forwarded.includes('--with-clicks') && !forwarded.includes('--pdf')) forwarded.push('--pdf');
  run('slidev/build.ts', forwarded);
  if (!selected && !prepareOnly) {
    if (!args.includes('--skip-lint')) run('lint-slides.ts', ['--slides-dir', slidesDir]);
    const output = path.join(root, 'build/slidev/dist');
    fs.mkdirSync(path.dirname(target), { recursive: true });
    const exportedPdf = path.join(output, 'course-slidev.pdf');
    if (path.resolve(exportedPdf) !== target) fs.copyFileSync(exportedPdf, target);
    if (!args.includes('--no-html')) {
      const { packageStudentPresentation } = await import(pathToFileURL(path.join(shared, 'build/slidev/delivery.ts')).href);
      packageStudentPresentation(root, output, target, path.join(workspace, 'build/dist/PRG400-Python-Libraries-and-Tools-slides.zip'));
    }
  }
}
