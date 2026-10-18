import * as fs from 'node:fs';
import * as path from 'node:path';
import { spawnSync } from 'node:child_process';

// The template is PRESENTATION_TEMPLATE_DIR when set, otherwise the sibling checkout ../Presentation-Template.
export function courseware(command: string, deck: string) {
  const template = process.env.PRESENTATION_TEMPLATE_DIR || path.resolve(import.meta.dirname, '../../Presentation-Template');
  const entry = path.join(template, 'build/courseware.ts');
  if (!fs.existsSync(entry)) throw new Error(`${entry} not found. Set PRESENTATION_TEMPLATE_DIR to a Presentation-Template checkout.`);
  const result = spawnSync(process.execPath, ['run', entry, command, deck, ...process.argv.slice(2)], { cwd: path.resolve(import.meta.dirname, '..'), stdio: 'inherit' });
  process.exitCode = result.status ?? 1;
}

if (import.meta.main) courseware('build', 'fundamentals');
