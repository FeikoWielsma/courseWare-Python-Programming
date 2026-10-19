import { expect, test } from 'bun:test';
import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';
import { spawn, spawnSync } from 'node:child_process';
import { cacheEntries, cacheRoot, prune, templateDir, withLock } from './toolchain.ts';

const temp = (prefix: string) => fs.mkdtempSync(path.join(os.tmpdir(), prefix));
const git = (dir: string, ...args: string[]) => spawnSync('git', ['-C', dir, ...args], { encoding: 'utf8' }).stdout.trim();

/** A template repository with one commit, and a course pinning it (or another commit) at that repository, with its own machine cache. */
function fixture(commit?: string) {
  const remote = temp('template-');
  git(remote, 'init', '--quiet');
  fs.writeFileSync(path.join(remote, 'README.md'), 'template\n');
  git(remote, 'add', '.');
  git(remote, '-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '--quiet', '-m', 'one');
  const head = git(remote, 'rev-parse', 'HEAD');
  const course = temp('course-');
  fs.mkdirSync(path.join(course, 'build'));
  const pin = (sha: string, repository = remote, root = course) => fs.writeFileSync(path.join(root, 'build/toolchain.json'), JSON.stringify({ repository, commit: sha }));
  pin(commit ?? head);
  const env = { COURSEWARE_CACHE_DIR: temp('machine-cache-') };
  return { remote, head, course, pin, env, cache: path.join(env.COURSEWARE_CACHE_DIR, 'toolchain', (commit ?? head).slice(0, 12)) };
}

test('the override wins and needs no pin', () => {
  const course = temp('course-');
  expect(templateDir(course, { PRESENTATION_TEMPLATE_DIR: 'some/checkout' })).toBe(path.resolve('some/checkout'));
});

test('the machine cache is COURSEWARE_CACHE_DIR, else the platform cache folder, never the checkout', () => {
  expect(cacheRoot({ COURSEWARE_CACHE_DIR: 'here' })).toBe(path.resolve('here'));
  const expected = process.platform === 'win32' ? path.join('C:/Users/u/AppData/Local', 'courseware')
    : process.platform === 'darwin' ? path.join(os.homedir(), 'Library/Caches/courseware')
    : path.join('/xdg', 'courseware');
  expect(cacheRoot({ LOCALAPPDATA: 'C:/Users/u/AppData/Local', XDG_CACHE_HOME: '/xdg' })).toBe(expected);
});

test('a missing cache is fetched at the pin, then reused without the remote', () => {
  const { head, course, pin, cache, env } = fixture();
  expect(templateDir(course, env)).toBe(cache);
  expect(git(cache, 'rev-parse', 'HEAD')).toBe(head);
  expect(fs.readFileSync(path.join(cache, '.git/courseware-installed'), 'utf8')).toBe(`${head}\n`);
  expect(fs.readdirSync(path.dirname(cache))).toEqual([head.slice(0, 12)]);
  expect(fs.existsSync(path.join(course, '.courseware'))).toBe(false);
  pin(head, path.join(course, 'no-such-remote'));
  expect(templateDir(course, env)).toBe(cache);
});

test('every checkout pinning the same commit shares one cached toolchain', () => {
  const { head, course, pin, cache, env } = fixture();
  expect(templateDir(course, env)).toBe(cache);
  const other = temp('worktree-');
  fs.mkdirSync(path.join(other, 'build'));
  pin(head, path.join(other, 'no-such-remote'), other);
  expect(templateDir(other, env)).toBe(cache);
  expect(fs.readdirSync(path.dirname(cache))).toEqual([head.slice(0, 12)]);
});

test('PRESENTATION_TEMPLATE_REPOSITORY replaces the recorded URL for the fetch', () => {
  const { remote, course, pin, cache, env } = fixture();
  pin(JSON.parse(fs.readFileSync(path.join(course, 'build/toolchain.json'), 'utf8')).commit, 'ssh://unreachable.invalid/x.git');
  expect(templateDir(course, { ...env, PRESENTATION_TEMPLATE_REPOSITORY: `file://${remote.replace(/\\/g, '/')}` })).toBe(cache);
});

test('a pinned commit the remote does not have is a clear error and leaves no cache or lock', () => {
  const { course, env, cache } = fixture('0'.repeat(40));
  expect(() => templateDir(course, env)).toThrow(/Cannot fetch Presentation-Template 0{40}/);
  expect(fs.readdirSync(path.dirname(cache))).toEqual([]);
});

test('a cache with local changes or another commit is refused', () => {
  const { course, cache, env } = fixture();
  templateDir(course, env);
  fs.writeFileSync(path.join(cache, 'README.md'), 'edited\n');
  expect(() => templateDir(course, env)).toThrow(/has local changes:\n M README.md/);
  git(cache, 'checkout', '--quiet', '--', 'README.md');
  fs.writeFileSync(path.join(cache, 'stray.ts'), '');
  expect(() => templateDir(course, env)).toThrow(/\?\? stray.ts/);
  fs.rmSync(path.join(cache, 'stray.ts'));
  git(cache, '-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '--quiet', '--allow-empty', '-m', 'two');
  expect(() => templateDir(course, env)).toThrow(/is at [0-9a-f]{40}, not the pin/);
  fs.rmSync(path.join(cache, '.git'), { recursive: true, force: true });
  expect(() => templateDir(course, env)).toThrow(/is at no commit, not the pin/);
});

test('a malformed pin is rejected before anything is fetched', () => {
  const { course, pin, env } = fixture();
  pin('main');
  expect(() => templateDir(course, env)).toThrow(/commit must be a full SHA, got "main"/);
});

test('a lock left by a process that has gone is taken over; a live one is waited for', async () => {
  const lock = path.join(temp('locks-'), 'x.lock');
  fs.mkdirSync(lock);
  fs.writeFileSync(path.join(lock, 'pid'), '999999\n');
  expect(withLock(lock, () => 'ran')).toBe('ran');
  expect(fs.existsSync(lock)).toBe(false);
  const holder = spawn(process.execPath, ['-e', 'setTimeout(() => {}, 60000)']);
  try {
    fs.mkdirSync(lock);
    fs.writeFileSync(path.join(lock, 'pid'), `${holder.pid}\n`);
    expect(() => withLock(lock, () => 'ran', 600)).toThrow(/Timed out waiting for/);
  } finally { holder.kill(); }
  await new Promise(resolve => holder.once('exit', resolve));
  expect(withLock(lock, () => 'ran')).toBe('ran');
});

test('prune keeps the pin and the most recently used others, and removes the old per-checkout cache', () => {
  const { head, course, env, cache } = fixture();
  templateDir(course, env);
  const root = path.dirname(cache);
  const old = (name: string, daysAgo: number) => {
    const dir = path.join(root, name);
    fs.mkdirSync(path.join(dir, '.git'), { recursive: true });
    fs.writeFileSync(path.join(dir, '.git/courseware-installed'), `${name}${'0'.repeat(28)}\n`);
    const when = new Date(Date.now() - daysAgo * 86_400_000);
    fs.utimesSync(path.join(dir, '.git/courseware-installed'), when, when);
  };
  old('aaaaaaaaaaaa', 30); old('bbbbbbbbbbbb', 1); old('cccccccccccc', 5);
  fs.mkdirSync(path.join(course, '.courseware/toolchain/x'), { recursive: true });
  // The pin is the most recent; the pinned one is never counted against keep.
  expect(cacheEntries(env).map(entry => entry.name)).toEqual([head.slice(0, 12), 'bbbbbbbbbbbb', 'cccccccccccc', 'aaaaaaaaaaaa']);
  const removed = prune(course, env, 1);
  expect(removed).toEqual([path.join(root, 'cccccccccccc'), path.join(root, 'aaaaaaaaaaaa'), path.join(course, '.courseware/toolchain')]);
  expect(fs.readdirSync(root).sort()).toEqual([head.slice(0, 12), 'bbbbbbbbbbbb'].sort());
  expect(prune(course, env, 0)).toEqual([path.join(root, 'bbbbbbbbbbbb')]);
  expect(templateDir(course, env)).toBe(cache);
});
