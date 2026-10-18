import { expect, test } from 'bun:test';
import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';
import { spawnSync } from 'node:child_process';
import { templateDir } from './toolchain.ts';

const temp = (prefix: string) => fs.mkdtempSync(path.join(os.tmpdir(), prefix));
const git = (dir: string, ...args: string[]) => spawnSync('git', ['-C', dir, ...args], { encoding: 'utf8' }).stdout.trim();

/** A template repository with one commit, and a course pinning it (or another commit) at that repository. */
function fixture(commit?: string) {
  const remote = temp('template-');
  git(remote, 'init', '--quiet');
  fs.writeFileSync(path.join(remote, 'README.md'), 'template\n');
  git(remote, 'add', '.');
  git(remote, '-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '--quiet', '-m', 'one');
  const head = git(remote, 'rev-parse', 'HEAD');
  const course = temp('course-');
  fs.mkdirSync(path.join(course, 'build'));
  const pin = (sha: string, repository = remote) => fs.writeFileSync(path.join(course, 'build/toolchain.json'), JSON.stringify({ repository, commit: sha }));
  pin(commit ?? head);
  return { remote, head, course, pin, cache: path.join(course, '.courseware/toolchain', commit ?? head) };
}

test('the override wins and needs no pin', () => {
  const course = temp('course-');
  expect(templateDir(course, { PRESENTATION_TEMPLATE_DIR: 'some/checkout' })).toBe(path.resolve('some/checkout'));
});

test('a missing cache is fetched at the pin, then reused without the remote', () => {
  const { head, course, pin, cache } = fixture();
  expect(templateDir(course, {})).toBe(cache);
  expect(git(cache, 'rev-parse', 'HEAD')).toBe(head);
  expect(fs.readFileSync(path.join(cache, '.git/courseware-installed'), 'utf8')).toBe(`${head}\n`);
  expect(fs.readdirSync(path.dirname(cache))).toEqual([head]);
  pin(head, path.join(course, 'no-such-remote'));
  expect(templateDir(course, {})).toBe(cache);
});

test('PRESENTATION_TEMPLATE_REPOSITORY replaces the recorded URL for the fetch', () => {
  const { remote, course, pin, cache } = fixture();
  pin(JSON.parse(fs.readFileSync(path.join(course, 'build/toolchain.json'), 'utf8')).commit, 'ssh://unreachable.invalid/x.git');
  expect(templateDir(course, { PRESENTATION_TEMPLATE_REPOSITORY: `file://${remote.replace(/\\/g, '/')}` })).toBe(cache);
});

test('a pinned commit the remote does not have is a clear error and leaves no cache', () => {
  const { course } = fixture('0'.repeat(40));
  expect(() => templateDir(course, {})).toThrow(/Cannot fetch Presentation-Template 0{40}/);
  expect(fs.readdirSync(path.join(course, '.courseware/toolchain'))).toEqual([]);
});

test('a cache with local changes or another commit is refused', () => {
  const { course, cache } = fixture();
  templateDir(course, {});
  fs.writeFileSync(path.join(cache, 'README.md'), 'edited\n');
  expect(() => templateDir(course, {})).toThrow(/has local changes:\n M README.md/);
  git(cache, 'checkout', '--quiet', '--', 'README.md');
  fs.writeFileSync(path.join(cache, 'stray.ts'), '');
  expect(() => templateDir(course, {})).toThrow(/\?\? stray.ts/);
  fs.rmSync(path.join(cache, 'stray.ts'));
  git(cache, '-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '--quiet', '--allow-empty', '-m', 'two');
  expect(() => templateDir(course, {})).toThrow(/is at [0-9a-f]{40}, not the pin/);
  fs.rmSync(path.join(cache, '.git'), { recursive: true, force: true });
  expect(() => templateDir(course, {})).toThrow(/is at no commit, not the pin/);
});

test('a malformed pin is rejected before anything is fetched', () => {
  const { course, pin } = fixture();
  pin('main');
  expect(() => templateDir(course, {})).toThrow(/commit must be a full SHA, got "main"/);
});
