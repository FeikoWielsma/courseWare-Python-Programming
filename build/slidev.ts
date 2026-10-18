import * as path from 'node:path';
import * as fs from 'node:fs';
import { spawnSync } from 'node:child_process';

const shared = path.resolve(import.meta.dirname, '../../Presentation-Template');
const template = process.env.PRESENTATION_TEMPLATE_DIR
  || (fs.existsSync(path.join(shared, 'build/slidev/build.ts'))
    ? shared
    : path.resolve(import.meta.dirname, '../../_worktrees/presentation-template-slidev'));
const result = spawnSync(process.execPath, ['run', path.join(template, 'build/slidev/build.ts'), ...process.argv.slice(2)], { stdio: 'inherit' });
process.exitCode = result.status ?? 1;
