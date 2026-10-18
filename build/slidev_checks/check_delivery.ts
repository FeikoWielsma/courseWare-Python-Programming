import * as fs from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';

const courseRoot = path.resolve(import.meta.dirname, '../..');
const args = process.argv.slice(2);
const option = (name: string) => {
  const index = args.indexOf(name);
  if (index < 0) return undefined;
  const value = args[index + 1];
  if (!value || value.startsWith('--')) throw new Error(`${name} requires a value.`);
  return value;
};
const output = path.resolve(option('--output') || path.join(courseRoot, 'build/slidev/dist'));
const template = process.env.PRESENTATION_TEMPLATE_DIR;
if (!template) throw new Error('Set PRESENTATION_TEMPLATE_DIR to the Slidev-capable Presentation-Template worktree.');
const { launchBrowser } = await import(pathToFileURL(path.join(template, 'build/lint-slides.ts')).href);
const originOption = option('--origin');
const { serveDirectory } = originOption
  ? { serveDirectory: undefined }
  : await import(pathToFileURL(path.join(template, 'build/slidev/build.ts')).href);
const manifest = JSON.parse(fs.readFileSync(path.join(output, 'manifest.json'), 'utf8'));
const server = originOption ? undefined : serveDirectory!(output, 0);
let origin = originOption?.replace(/\/$/, '');
type Browser = Awaited<ReturnType<typeof launchBrowser>>;
let browser: Browser | undefined;

const pause = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));
let page: Awaited<ReturnType<Browser['newPage']>>;
const current = () => new URL(page.url()).hash;
const clickCount = () => Number(new URLSearchParams(current().split('?')[1] || '').get('clicks') || 0);
const state = (id: string) => page.evaluate((sourceId: string) =>
  [...document.querySelectorAll<HTMLElement>(`.course-frame[data-source-id="${sourceId}"] .course-step`)]
    .map(element => getComputedStyle(element).opacity), id);
const require = (condition: unknown, message: string) => { if (!condition) throw new Error(message); };
const wheel = async (deltaY: number, modifiers = 0) => {
  const session = await page.createCDPSession();
  await session.send('Input.dispatchMouseEvent', { type: 'mouseWheel', x: 640, y: 400, deltaX: 0, deltaY, modifiers });
  await session.detach();
};

try {
  if (server) {
    await new Promise<void>(resolve => server.once('listening', resolve));
    const address = server.address();
    if (!address || typeof address === 'string') throw new Error('Cannot start Slidev delivery server.');
    origin = `http://127.0.0.1:${address.port}`;
  }
  if (!origin) throw new Error('No delivery origin is available.');
  browser = await launchBrowser();
  page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  const topic = manifest.topics.find((item: { id: string }) => item.id === '03-data-structures-3')
    || manifest.topics.find((item: { id: string }) => item.id === '02-variables-and-data-types-2');
  require(topic, 'Could not find a representative source topic.');
  await page.goto(`${origin}/slidev/#/${topic.id}`, { waitUntil: 'networkidle0' });
  await page.waitForSelector(`.course-frame[data-source-id="${topic.id}"] .course-step`);
  await pause(500);

  const initial = await state(topic.id);
  require(initial.length >= 2 && initial[0] === '0', `Expected hidden progressive content, got ${JSON.stringify(initial)}.`);
  await page.keyboard.press('ArrowRight'); await pause(250);
  const forward = await state(topic.id);
  await page.keyboard.press('ArrowLeft'); await pause(250);
  const reverse = await state(topic.id);
  require(forward[0] === '1' && reverse[0] === '0', 'Ordinary forward/reverse reveal failed.');
  console.log(`PASS ordinary reveal forward/reverse: ${topic.id}`);

  // Distinct short gestures used to disappear inside a 700ms lockout. Check
  // actual navigation state before the visual transition has finished.
  await wheel(90); await pause(60);
  require(clickCount() === 1, `First wheel response was delayed: ${current()}.`);
  await pause(120);
  await wheel(90); await pause(60);
  require(clickCount() === 2, `Fresh wheel gesture within 700ms was dropped: ${current()}.`);
  await wheel(-90); await pause(60);
  require(clickCount() === 1, `Immediate wheel reversal was dropped: ${current()}.`);
  await pause(120);
  await wheel(-90); await pause(60);
  require(clickCount() === 0, `Second reverse gesture was dropped: ${current()}.`);
  await pause(180);
  console.log('PASS quick separate wheel gestures and immediate reversal');

  await wheel(90); await pause(900);
  const wheelForward = await state(topic.id);
  require(wheelForward[0] === '1', 'Physical CDP wheel-down did not advance a reveal.');
  await wheel(-90); await pause(900);
  const wheelReverse = await state(topic.id);
  require(wheelReverse[0] === '0', 'Physical CDP wheel-up did not reverse a reveal.');
  console.log('PASS physical wheel forward/reverse');

  await wheel(90); await pause(20); await wheel(90); await pause(20); await wheel(90); await pause(950);
  const momentum = await state(topic.id);
  require(momentum[0] === '1' && momentum.filter(value => value === '1').length === 1,
    `Momentum burst advanced more than one state: ${JSON.stringify(momentum)}.`);
  console.log('PASS physical wheel momentum grouped to one reveal');

  await wheel(-90, 2); await pause(350);
  require((await state(topic.id))[0] === '1', 'Ctrl+wheel zoom gesture changed the reveal.');
  await wheel(-90); await pause(900);
  require((await state(topic.id))[0] === '0', 'Wheel reverse after zoom exclusion failed.');
  console.log('PASS Ctrl+wheel exclusion');

  await page.evaluate(() => {
    const panel = document.createElement('div');
    panel.dataset.wheelProbe = 'scrollable';
    Object.assign(panel.style, { position: 'fixed', left: '500px', top: '300px', zIndex: '99999', width: '280px', height: '150px', overflowY: 'auto', background: 'white' });
    panel.innerHTML = '<div style="height:800px">Scrollable probe</div>';
    document.querySelector('.course-frame[data-source-id="03-data-structures-3"]')!.append(panel);
  });
  const probeGeometry = await page.evaluate(() => {
    const panel = document.querySelector<HTMLElement>('[data-wheel-probe="scrollable"]')!;
    const rect = panel.getBoundingClientRect();
    return { rect: { x: rect.x, y: rect.y, width: rect.width, height: rect.height }, top: document.elementFromPoint(600, 350)?.outerHTML.slice(0, 150) };
  });
  const beforeScroll = current();
  await page.mouse.move(600, 350); await page.mouse.wheel({ deltaY: 120 }); await pause(350);
  const panelScroll = await page.$eval('[data-wheel-probe="scrollable"]', (element: Element) => (element as HTMLElement).scrollTop);
  require(panelScroll > 0 && current() === beforeScroll, `Wheel over scrollable content failed: scrollTop=${panelScroll}, route=${current()}, before=${beforeScroll}, probe=${JSON.stringify(probeGeometry)}.`);
  console.log('PASS wheel over scrollable content');

  await page.evaluate(() => {
    const control = document.createElement('textarea');
    control.dataset.wheelProbe = 'control';
    Object.assign(control.style, { position: 'fixed', left: '500px', top: '500px', zIndex: '99999', width: '220px', height: '60px' });
    document.querySelector('.course-frame[data-source-id="03-data-structures-3"]')!.append(control);
    control.focus();
  });
  const beforeControl = current();
  await page.mouse.move(600, 520); await page.mouse.wheel({ deltaY: 120 }); await pause(350);
  require(current() === beforeControl, 'Wheel over an editable control navigated the deck.');
  await page.evaluate(() => document.querySelector('[data-wheel-probe]')?.remove());
  console.log('PASS wheel over editable control');

  // The preceding route has multiple reveals. Advance beyond its last reveal
  // and confirm that wheel navigation crosses the actual source-slide boundary.
  let steps = 0;
  while ((await state(topic.id)).some(value => value === '0') && steps++ < 16) { await wheel(90); await pause(850); }
  const boundaryFrom = current();
  require(boundaryFrom.includes(topic.id), `Reveal loop left ${topic.id} before reaching its last state: ${boundaryFrom}.`);
  await wheel(90); await pause(900);
  const boundaryTo = current();
  require(boundaryFrom.split('?')[0] !== boundaryTo.split('?')[0], `Wheel did not cross the source-slide boundary from ${boundaryFrom}: ${boundaryTo}.`);
  await wheel(-90); await pause(900);
  require(current() === boundaryFrom, 'Wheel-up did not cross the slide boundary in reverse.');
  console.log(`PASS wheel slide boundary forward/reverse: ${boundaryFrom} -> ${boundaryTo}`);
} finally {
  await browser?.close();
  if (server) await new Promise<void>((resolve, reject) => server.close(error => error ? reject(error) : resolve()));
}
