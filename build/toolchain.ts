import * as fs from 'node:fs';
import * as path from 'node:path';
import { spawnSync } from 'node:child_process';

// Finds the Presentation-Template this course builds with. PRESENTATION_TEMPLATE_DIR is the development
// override; otherwise the commit pinned in build/toolchain.json is fetched once into .courseware/toolchain/<commit>
// (from PRESENTATION_TEMPLATE_REPOSITORY when set, e.g. CI's HTTPS URL) and its dependencies installed.
//   bun run build/toolchain.ts --path         prints the template folder
//   bun run build/toolchain.ts <command> ...  runs the template's courseware.ts (toolchain, pin, verify, build ...)
const courseRoot = path.resolve(import.meta.dirname, '..');
const git = (cwd: string, ...args: string[]) => spawnSync('git', args, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });

export function templateDir(root = courseRoot, env = process.env): string {
  if (env.PRESENTATION_TEMPLATE_DIR) {
    const dir = path.resolve(env.PRESENTATION_TEMPLATE_DIR);
    console.error(`DEVELOPMENT OVERRIDE: Presentation-Template from PRESENTATION_TEMPLATE_DIR=${dir}, not the pinned commit`);
    return dir;
  }
  const { repository, commit } = JSON.parse(fs.readFileSync(path.join(root, 'build/toolchain.json'), 'utf8'));
  if (!/^[0-9a-f]{40}$/.test(commit)) throw new Error(`build/toolchain.json: commit must be a full SHA, got ${JSON.stringify(commit)}`);
  const dir = path.join(root, '.courseware/toolchain', commit);
  if (!fs.existsSync(dir)) fetchPin(env.PRESENTATION_TEMPLATE_REPOSITORY || repository, commit, dir);
  const head = fs.existsSync(path.join(dir, '.git')) ? git(dir, 'rev-parse', 'HEAD').stdout.trim() : '';
  if (head !== commit) throw new Error(`The cached toolchain ${dir} is at ${head || 'no commit'}, not the pin. Delete that folder to fetch it again.`);
  const status = git(dir, 'status', '--porcelain');
  if (status.status || status.stdout) throw new Error(`The cached toolchain ${dir} has local changes:\n${status.stdout}${status.stderr}Delete that folder to fetch it again.`);
  const installed = path.join(dir, '.git/courseware-installed');
  if (!fs.existsSync(installed)) {
    for (const folder of ['build', 'build/slidev'].map(folder => path.join(dir, folder)).filter(folder => fs.existsSync(path.join(folder, 'package.json')))) {
      if (spawnSync(process.execPath, ['install', '--frozen-lockfile'], { cwd: folder, stdio: ['ignore', 2, 2] }).status !== 0) {
        throw new Error(`bun install --frozen-lockfile failed in ${folder}`);
      }
    }
    fs.writeFileSync(installed, `${commit}\n`);
  }
  return dir;
}

// A partial fetch never takes the cache name: it is fetched beside it and renamed when complete.
function fetchPin(repository: string, commit: string, dir: string) {
  console.error(`Fetching Presentation-Template ${commit} from ${repository}`);
  const partial = `${dir}.partial-${process.pid}`;
  fs.mkdirSync(partial, { recursive: true });
  const ok = (...args: string[]) => git(partial, ...args).status === 0;
  const fetched = ok('init', '--quiet') && ok('remote', 'add', 'origin', repository)
    && (ok('fetch', '--quiet', '--depth=1', 'origin', commit) || ok('fetch', '--quiet', 'origin'))
    && ok('-c', 'advice.detachedHead=false', 'checkout', '--quiet', commit);
  if (!fetched) {
    fs.rmSync(partial, { recursive: true, force: true });
    throw new Error(`Cannot fetch Presentation-Template ${commit} from ${repository}. build/toolchain.json must pin a pushed commit; set PRESENTATION_TEMPLATE_DIR to a checkout for development.`);
  }
  fs.renameSync(partial, dir);
}

function reportErrors(action: () => void) {
  try { action(); } catch (error) { console.error(`ERROR ${(error as Error).message}`); process.exitCode = 1; }
}

/** Runs the template's courseware.ts in the course root with the given arguments and this process's own. */
export function courseware(...args: string[]) {
  reportErrors(() => {
    const entry = path.join(templateDir(), 'build/courseware.ts');
    if (!fs.existsSync(entry)) throw new Error(`${entry} not found: that template predates build/courseware.ts.`);
    process.exitCode = spawnSync(process.execPath, ['run', entry, ...args, ...process.argv.slice(2)], { cwd: courseRoot, stdio: 'inherit' }).status ?? 1;
  });
}

if (import.meta.main) {
  if (process.argv[2] === '--path') reportErrors(() => console.log(templateDir()));
  else courseware();
}
