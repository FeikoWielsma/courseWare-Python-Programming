import * as fs from 'node:fs';
import * as path from 'node:path';
import { spawnSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import { templateDir } from './toolchain.ts';

/** Assemble the portable course site, including its freshly built static deck. */
export async function buildSite(course: string, template: string, args: string[] = []) {
  const outIndex = args.indexOf('--out');
  if (outIndex >= 0 && (!args[outIndex + 1] || args[outIndex + 1].startsWith('--'))) {
    throw new Error('--out requires a directory');
  }
  const out = outIndex < 0 ? path.join(course, 'build/site/dist') : path.resolve(course, args[outIndex + 1]);
  const run = (script: string, flags: string[]) => {
    const result = spawnSync(process.execPath, ['run', path.join(template, 'build', script), ...flags], { cwd: course, stdio: 'inherit' });
    if (result.error || result.status !== 0) throw new Error(`${script} failed: ${result.error?.message || `exit ${result.status}`}`);
  };

  // Building here makes `site` usable from a fresh checkout, independent of CI ordering.
  run('courseware.ts', ['build', 'fundamentals', '--marp']);
  const { readManifest, deliverable } = await import(pathToFileURL(path.join(template, 'build/artifacts.ts')).href);
  const manifest = readManifest(path.join(course, '.courseware/fundamentals/marp'));
  const html = fs.readFileSync(path.resolve(course, deliverable(manifest, 'html').path), 'utf8');
  const embedded = html.replace(/<div class="bespoke-marp-note"[^>]*>[\s\S]*?<\/div>/g, '');
  run('site/build-site.ts', args.filter(arg => arg !== '--'));
  fs.writeFileSync(path.join(out, 'slides-marp.html'), embedded);

  const shortcut = path.join(course, 'build/site/student-shortcut');
  fs.mkdirSync(shortcut, { recursive: true });
  fs.writeFileSync(path.join(shortcut, 'index.html'), '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=site/index.html"><title>Python Programming exercises</title></head><body><p><a href="site/index.html">Open the Python Programming exercise site</a></p></body></html>\n');
}

if (import.meta.main) {
  try {
    await buildSite(path.resolve(import.meta.dirname, '..'), templateDir(), process.argv.slice(2).filter(arg => arg !== '--'));
  } catch (error) {
    console.error(String(error));
    process.exitCode = 1;
  }
}
