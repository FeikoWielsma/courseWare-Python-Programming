import { test, expect } from 'bun:test';
import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';
import { buildSite } from './site.ts';

test('site builds its missing deck before rendering, embeds without notes, and honors --out', async () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'prg400-site-'));
  try {
    const template = path.join(root, 'template');
    const course = path.join(root, 'course');
    fs.mkdirSync(path.join(template, 'build/site'), { recursive: true });
    fs.mkdirSync(course);
    fs.writeFileSync(path.join(template, 'build/courseware.ts'), `
      import * as fs from 'node:fs';
      fs.mkdirSync('.courseware/fundamentals/marp', { recursive: true });
      fs.writeFileSync('fallback.html', '<p>Slides</p><div class="bespoke-marp-note">Trainer only</div>');
      fs.writeFileSync('.courseware/fundamentals/marp/artifacts.json', JSON.stringify({ deliverables: [{ role: 'html', path: 'fallback.html' }] }));
    `);
    fs.writeFileSync(path.join(template, 'build/artifacts.ts'), `
      import * as fs from 'node:fs';
      import * as path from 'node:path';
      export const readManifest = dir => JSON.parse(fs.readFileSync(path.join(dir, 'artifacts.json'), 'utf8'));
      export const deliverable = (manifest, role) => manifest.deliverables.find(item => item.role === role);
    `);
    fs.writeFileSync(path.join(template, 'build/site/build-site.ts'), `
      import * as fs from 'node:fs';
      if (!fs.existsSync('fallback.html')) throw new Error('Deck not built first');
      const out = process.argv[process.argv.indexOf('--out') + 1];
      fs.mkdirSync(out, { recursive: true });
      fs.writeFileSync(out + '/index.html', 'Site');
    `);
    await buildSite(course, template, ['--out', 'custom-site']);
    expect(fs.readFileSync(path.join(course, 'custom-site/slides-marp.html'), 'utf8')).toBe('<p>Slides</p>');
    expect(fs.existsSync(path.join(course, 'custom-site/index.html'))).toBe(true);
    expect(fs.readFileSync(path.join(course, 'build/site/student-shortcut/index.html'), 'utf8')).toContain('site/index.html');
    await expect(buildSite(course, template, ['--out'])).rejects.toThrow('--out requires');
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});
