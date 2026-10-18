import * as fs from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';

const courseRoot = path.resolve(import.meta.dirname, '..');
const output = path.join(courseRoot, 'build/slidev/dist');
const student = path.join(output, 'student');
const checksDir = path.join(courseRoot, 'build/slidev_checks');
const template = process.env.PRESENTATION_TEMPLATE_DIR;

if (!template) {
  throw new Error('Set PRESENTATION_TEMPLATE_DIR to the Slidev-capable Presentation-Template worktree.');
}
if (!fs.existsSync(path.join(student, 'index.html'))) {
  throw new Error(`Packaged student app not found: ${student}`);
}
if (!fs.existsSync(path.join(output, 'manifest.json'))) {
  throw new Error(`Slidev manifest not found: ${path.join(output, 'manifest.json')}`);
}

const { serveDirectory } = await import(pathToFileURL(path.join(template, 'build/slidev/build.ts')).href);
const server = serveDirectory(student, 0);
const children: ReturnType<typeof Bun.spawn>[] = [];

function run(label: string, command: string[]) {
  console.log(`RUN ${label}: ${command.join(' ')}`);
  const child = Bun.spawn(command, { cwd: courseRoot, stdout: 'inherit', stderr: 'inherit' });
  children.push(child);
  return child.exited.then(code => {
    if (code !== 0) throw new Error(`${label} exited with status ${code}.`);
    console.log(`PASS ${label}`);
  });
}

try {
  await new Promise<void>((resolve, reject) => {
    server.once('listening', resolve);
    server.once('error', reject);
  });
  const address = server.address();
  if (!address || typeof address === 'string') throw new Error('Cannot start the packaged student server.');
  const origin = `http://127.0.0.1:${address.port}`;
  console.log(`Serving ${student} at ${origin}`);

  const animationChecks = fs.readdirSync(checksDir)
    .filter(name => /^check_.*\.py$/.test(name))
    .sort()
    .map(name => path.join(checksDir, name));
  if (animationChecks.length === 0) throw new Error(`No animation checks found in ${checksDir}.`);

  const checks = animationChecks.map(script => run(
    path.basename(script),
    ['uv', 'run', 'python', script, '--browser', origin],
  ));
  checks.push(run('physical wheel delivery probe', [
    'bun', 'run', path.join(checksDir, 'check_delivery.ts'),
    '--origin', origin, '--output', output,
  ]));
  const results = await Promise.allSettled(checks);
  const failures = results.flatMap((result, index) => result.status === 'rejected'
    ? [`${index < animationChecks.length ? path.basename(animationChecks[index]) : 'physical wheel delivery probe'}: ${String(result.reason)}`]
    : []);
  if (failures.length) throw new Error(`Slidev delivery checks failed:\n${failures.join('\n')}`);
  console.log(`Slidev delivery checks passed: ${animationChecks.length} animation checks and the physical wheel probe.`);
} finally {
  for (const child of children) {
    if (child.exitCode === null) child.kill();
  }
  await Promise.all(children.map(child => child.exited));
  await new Promise<void>((resolve, reject) => server.close(error => error ? reject(error) : resolve()));
}
