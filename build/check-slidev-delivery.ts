import * as fs from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';
import { templateDir } from './toolchain.ts';

const courseRoot = path.resolve(import.meta.dirname, '..');
// The student build's artifact manifest names the packaged presentation.
const output = path.join(courseRoot, '.courseware/fundamentals/student');
const checksDir = path.join(courseRoot, 'build/slidev_checks');
const template = templateDir();
const { readManifest, deliverable } = await import(pathToFileURL(path.join(template, 'build/artifacts.ts')).href);
const student = path.join(courseRoot, deliverable(readManifest(output), 'presentation').path);
if (!fs.existsSync(path.join(student, 'index.html'))) {
  throw new Error(`Packaged student app not found: ${student}`);
}

const { serve } = await import(pathToFileURL(path.join(template, 'build/browser.ts')).href);
const server = await serve(student, { port: 0 });
const origin = server.url;
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
  console.log(`Serving ${student} at ${origin}`);

  const animationChecks = fs.readdirSync(checksDir)
    .filter(name => /^check_.*\.py$/.test(name))
    .sort()
    .map(name => path.join(checksDir, name));
  if (animationChecks.length === 0) throw new Error(`No animation checks found in ${checksDir}.`);

  // The animation checks run side by side, one Chrome each. The wheel probe
  // times gestures in tens of milliseconds, so it runs alone afterwards.
  const failures: string[] = [];
  await Promise.all(animationChecks.map(script =>
    run(path.basename(script), ['uv', 'run', 'python', script, '--browser', origin])
      .catch(error => { failures.push(`${path.basename(script)}: ${String(error)}`); })));
  try {
    await run('physical wheel delivery probe', [
      process.execPath, 'run', path.join(checksDir, 'check_delivery.ts'),
      '--origin', origin, '--output', output,
    ]);
  } catch (error) { failures.push(`physical wheel delivery probe: ${String(error)}`); }
  if (failures.length) throw new Error(`Slidev delivery checks failed:\n${failures.join('\n')}`);
  console.log(`Slidev delivery checks passed: ${animationChecks.length} animation checks and the physical wheel probe.`);
} finally {
  for (const child of children) {
    if (child.exitCode === null) child.kill();
  }
  await Promise.all(children.map(child => child.exited));
  await server.close();
}
