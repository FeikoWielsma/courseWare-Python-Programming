import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';
import { spawnSync } from 'node:child_process';

// Finds the Presentation-Template this course builds with. PRESENTATION_TEMPLATE_DIR is the development
// override; otherwise the commit pinned in build/toolchain.json is fetched once into the per-machine cache
// <cache>/toolchain/<commit prefix> (from PRESENTATION_TEMPLATE_REPOSITORY when set, e.g. CI's HTTPS URL)
// and its dependencies installed. Every checkout and worktree of every course on the machine shares it.
// The cache is COURSEWARE_CACHE_DIR, else %LOCALAPPDATA%/courseware, ~/Library/Caches/courseware or
// $XDG_CACHE_HOME/courseware (~/.cache/courseware).
//   bun run build/toolchain.ts --path                       prints the template folder
//   bun run build/toolchain.ts toolchain [--prune [--keep N]] reports the pin and the cache (and prunes it)
//   bun run build/toolchain.ts <command> ...                runs the template's courseware.ts (pin, verify, build ...)
const courseRoot = path.resolve(import.meta.dirname, '..');
const git = (cwd: string, ...args: string[]) => spawnSync('git', args, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
// A commit prefix keeps node_modules paths under the Windows 260-character limit; HEAD is checked in full.
const folderName = (commit: string) => commit.slice(0, 12);
const installedMarker = (dir: string) => path.join(dir, '.git/courseware-installed');

export function cacheRoot(env: NodeJS.ProcessEnv = process.env): string {
  if (env.COURSEWARE_CACHE_DIR) return path.resolve(env.COURSEWARE_CACHE_DIR);
  if (process.platform === 'win32') return path.join(env.LOCALAPPDATA || path.join(os.homedir(), 'AppData/Local'), 'courseware');
  if (process.platform === 'darwin') return path.join(os.homedir(), 'Library/Caches/courseware');
  return path.join(env.XDG_CACHE_HOME || path.join(os.homedir(), '.cache'), 'courseware');
}

export const toolchainCache = (env: NodeJS.ProcessEnv = process.env) => path.join(cacheRoot(env), 'toolchain');

export function templateDir(root = courseRoot, env: NodeJS.ProcessEnv = process.env): string {
  if (env.PRESENTATION_TEMPLATE_DIR) {
    const dir = path.resolve(env.PRESENTATION_TEMPLATE_DIR);
    console.error(`DEVELOPMENT OVERRIDE: Presentation-Template from PRESENTATION_TEMPLATE_DIR=${dir}, not the pinned commit`);
    return dir;
  }
  const { repository, commit } = JSON.parse(fs.readFileSync(path.join(root, 'build/toolchain.json'), 'utf8'));
  if (!/^[0-9a-f]{40}$/.test(commit)) throw new Error(`build/toolchain.json: commit must be a full SHA, got ${JSON.stringify(commit)}`);
  const dir = path.join(toolchainCache(env), folderName(commit));
  if (!fs.existsSync(installedMarker(dir))) {
    // Checkouts building at the same time take turns: one fetches and installs, the others then reuse it.
    withLock(`${dir}.lock`, () => {
      if (!fs.existsSync(dir)) fetchPin(env.PRESENTATION_TEMPLATE_REPOSITORY || repository, commit, dir);
      checkCheckout(dir, commit);
      if (!fs.existsSync(installedMarker(dir))) install(dir, commit);
    });
  }
  checkCheckout(dir, commit);
  // Last use, for toolchain --prune.
  const now = new Date();
  fs.utimesSync(installedMarker(dir), now, now);
  return dir;
}

function checkCheckout(dir: string, commit: string) {
  const head = fs.existsSync(path.join(dir, '.git')) ? git(dir, 'rev-parse', 'HEAD').stdout.trim() : '';
  if (head !== commit) throw new Error(`The cached toolchain ${dir} is at ${head || 'no commit'}, not the pin ${commit}. Delete that folder to fetch it again.`);
  const status = git(dir, 'status', '--porcelain');
  if (status.status || status.stdout) throw new Error(`The cached toolchain ${dir} has local changes:\n${status.stdout}${status.stderr}Delete that folder to fetch it again.`);
}

function install(dir: string, commit: string) {
  for (const folder of ['build', 'build/slidev'].map(folder => path.join(dir, folder)).filter(folder => fs.existsSync(path.join(folder, 'package.json')))) {
    if (spawnSync(process.execPath, ['install', '--frozen-lockfile'], { cwd: folder, stdio: ['ignore', 2, 2] }).status !== 0) {
      throw new Error(`bun install --frozen-lockfile failed in ${folder}`);
    }
  }
  fs.writeFileSync(installedMarker(dir), `${commit}\n`);
}

const sleep = (ms: number) => Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
const alive = (pid: number) => {
  try { process.kill(pid, 0); return true; } catch (error) { return (error as NodeJS.ErrnoException).code === 'EPERM'; }
};

/** Runs action holding the lock folder; a lock whose process has gone is taken over. */
export function withLock<T>(lock: string, action: () => T, timeoutMs = 15 * 60_000): T {
  fs.mkdirSync(path.dirname(lock), { recursive: true });
  const deadline = Date.now() + timeoutMs;
  for (let announced = false; ; ) {
    try {
      fs.mkdirSync(lock);
      fs.writeFileSync(path.join(lock, 'pid'), `${process.pid}\n`);
      break;
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code !== 'EEXIST') throw error;
    }
    let owner = NaN;
    try { owner = Number(fs.readFileSync(path.join(lock, 'pid'), 'utf8')); } catch { /* still being written */ }
    if (Number.isInteger(owner) && owner > 0 && !alive(owner)) { fs.rmSync(lock, { recursive: true, force: true }); continue; }
    if (Date.now() > deadline) throw new Error(`Timed out waiting for ${lock} (process ${owner}). Delete it if no build is running.`);
    if (!announced) { console.error(`Waiting for another build to finish preparing ${path.basename(lock, '.lock')} ...`); announced = true; }
    sleep(250);
  }
  try { return action(); } finally { fs.rmSync(lock, { recursive: true, force: true }); }
}

// A partial fetch never takes the cache name: it is fetched beside it and renamed when complete.
function fetchPin(repository: string, commit: string, dir: string) {
  console.error(`Fetching Presentation-Template ${commit} from ${repository} into ${dir}`);
  const partial = `${dir}.partial-${process.pid}`;
  fs.mkdirSync(partial, { recursive: true });
  let reason = '';
  const ok = (...args: string[]) => {
    const result = git(partial, ...args);
    reason = result.stderr.trim().split('\n').pop() || reason;
    return result.status === 0;
  };
  const fetched = ok('init', '--quiet') && ok('remote', 'add', 'origin', repository)
    && (ok('fetch', '--quiet', '--depth=1', 'origin', commit) || ok('fetch', '--quiet', 'origin'))
    && ok('-c', 'advice.detachedHead=false', 'checkout', '--quiet', commit);
  if (!fetched) {
    fs.rmSync(partial, { recursive: true, force: true });
    throw new Error(`Cannot fetch Presentation-Template ${commit} from ${repository} (${reason}). build/toolchain.json must pin a pushed commit; set PRESENTATION_TEMPLATE_DIR to a checkout for development.`);
  }
  fs.renameSync(partial, dir);
}

/** Bytes of every file under dir, and of those not hard-linked elsewhere (Bun links packages from its global cache). */
function usage(dir: string) {
  let size = 0, own = 0;
  const walk = (folder: string) => {
    for (const entry of fs.readdirSync(folder, { withFileTypes: true })) {
      const file = path.join(folder, entry.name);
      if (entry.isDirectory()) walk(file);
      else {
        const stat = fs.lstatSync(file);
        size += stat.size;
        if (stat.nlink < 2) own += stat.size;
      }
    }
  };
  if (fs.existsSync(dir)) walk(dir);
  return { size, own };
}

const megabytes = (bytes: number) => `${(bytes / 1e6).toFixed(0)} MB`;

type CacheEntry = { name: string; dir: string; commit: string; used: number };

export function cacheEntries(env: NodeJS.ProcessEnv = process.env): CacheEntry[] {
  const cache = toolchainCache(env);
  if (!fs.existsSync(cache)) return [];
  return fs.readdirSync(cache, { withFileTypes: true })
    .filter(entry => entry.isDirectory() && /^[0-9a-f]{12}$/.test(entry.name))
    .map(entry => {
      const dir = path.join(cache, entry.name);
      const marker = installedMarker(dir);
      const installed = fs.existsSync(marker);
      return { name: entry.name, dir, commit: installed ? fs.readFileSync(marker, 'utf8').trim() : `${entry.name} (not installed)`, used: installed ? fs.statSync(marker).mtimeMs : fs.statSync(dir).mtimeMs };
    })
    .sort((a, b) => b.used - a.used);
}

/** Removes cached toolchains except the course's pin and the keep most recently used others, and the old per-checkout cache. */
export function prune(root = courseRoot, env: NodeJS.ProcessEnv = process.env, keep = 2) {
  const pinned = folderName(JSON.parse(fs.readFileSync(path.join(root, 'build/toolchain.json'), 'utf8')).commit);
  const others = cacheEntries(env).filter(entry => entry.name !== pinned);
  const removed: string[] = [];
  for (const entry of others.slice(keep)) {
    // A toolchain being fetched or installed right now is left alone.
    if (fs.existsSync(`${entry.dir}.lock`)) continue;
    fs.rmSync(entry.dir, { recursive: true, force: true });
    removed.push(entry.dir);
  }
  const cache = toolchainCache(env);
  if (fs.existsSync(cache)) for (const name of fs.readdirSync(cache)) {
    const partial = /\.partial-(\d+)$/.exec(name);
    if (partial && !alive(Number(partial[1]))) { fs.rmSync(path.join(cache, name), { recursive: true, force: true }); removed.push(path.join(cache, name)); }
  }
  const legacy = path.join(root, '.courseware/toolchain');
  if (fs.existsSync(legacy)) { fs.rmSync(legacy, { recursive: true, force: true }); removed.push(legacy); }
  return removed;
}

/** toolchain [--prune [--keep N]]: the cache report, then the template's own pin report. */
function toolchain(args: string[]) {
  if (args.includes('--prune')) {
    const keep = args.includes('--keep') ? Number(args[args.indexOf('--keep') + 1]) : 2;
    if (!Number.isInteger(keep) || keep < 0) throw new Error('--keep needs a whole number');
    const removed = prune(courseRoot, process.env, keep);
    console.log(removed.length ? `Removed:\n${removed.map(dir => `  ${dir}`).join('\n')}` : 'Nothing to prune.');
  }
  console.log(`Toolchain cache: ${toolchainCache()}`);
  let total = 0, totalOwn = 0;
  for (const entry of cacheEntries()) {
    const { size, own } = usage(entry.dir);
    total += size; totalOwn += own;
    console.log(`  ${entry.name}  ${megabytes(size).padStart(7)} (${megabytes(own)} not shared)  last used ${new Date(entry.used).toISOString().slice(0, 16).replace('T', ' ')}  ${entry.commit}`);
  }
  console.log(`  total ${megabytes(total)}, of which ${megabytes(totalOwn)} is not hard-linked to Bun's package cache`);
  const legacy = path.join(courseRoot, '.courseware/toolchain');
  if (fs.existsSync(legacy)) console.log(`Unused per-checkout cache ${legacy} (${megabytes(usage(legacy).size)}): toolchain --prune removes it.`);
}

function reportErrors(action: () => void) {
  try { action(); } catch (error) { console.error(`ERROR ${(error as Error).message}`); process.exitCode = 1; }
}

/** Runs the template's courseware.ts in the course root with the given arguments and this process's own. */
export function courseware(...args: string[]) {
  reportErrors(() => {
    const entry = path.join(templateDir(), 'build/courseware.ts');
    if (!fs.existsSync(entry)) throw new Error(`${entry} not found: that template predates build/courseware.ts.`);
    const own = process.argv.slice(2);
    const forwarded = [...args, ...own].filter((arg, index, all) => arg !== '--prune' && arg !== '--keep' && all[index - 1] !== '--keep');
    process.exitCode = spawnSync(process.execPath, ['run', entry, ...forwarded], { cwd: courseRoot, stdio: 'inherit' }).status ?? 1;
    if ([...args, ...own].filter(arg => arg !== '--')[0] === 'toolchain' && !process.exitCode) toolchain(own);
  });
}

if (import.meta.main) {
  if (process.argv[2] === '--path') reportErrors(() => console.log(templateDir()));
  else courseware();
}
