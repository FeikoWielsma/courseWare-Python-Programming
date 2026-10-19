// Pacing for the browser checks. A click is read once it has rendered and its transitions have ended,
// not after a fixed sleep; the components animate with CSS transitions only (600 ms, --ds-time).
// Independent slides are read on several pages of one browser at once.
import { availableParallelism } from 'node:os';

/** Pages read at once: COURSE_CHECK_PAGES, else up to 4 by the CPU count. */
export const pageCount = Number(process.env.COURSE_CHECK_PAGES) || Math.max(1, Math.min(4, availableParallelism() - 1));

/**
 * Runs `read` for every item, on `pageCount` pages of the session's browser that each take the next
 * item when free. The session's own page is one of them. Every page has the same viewport.
 */
export async function onPages<T>(
  session: { page: unknown; browser: unknown },
  withPage: (browser: unknown, run: (page: any) => Promise<void>) => Promise<void>,
  items: T[],
  read: (page: any, item: T) => Promise<void>,
) {
  const queue = [...items];
  // A page in a background tab gets no key events and no animation frames in new headless Chrome
  // (CI runs the real browser), so every page is told it is focused and visible.
  const worker = async (page: any) => {
    const client = await page.createCDPSession();
    await client.send('Emulation.setFocusEmulationEnabled', { enabled: true });
    await page.bringToFront().catch(() => {});
    for (let item = queue.shift(); item !== undefined; item = queue.shift()) await read(page, item);
  };
  const extra = Array.from({ length: Math.min(pageCount, items.length) - 1 }, () => withPage(session.browser, worker));
  await Promise.all([worker(session.page), ...extra]);
}

/** Real time a click may take to render and finish its transitions before it is reported as stuck. */
export const settleTimeoutMs = 10000;
/** Longest transition a click may start, in animation time. The fixed waits these replace read at 650 ms. */
export const longestTransitionMs = 650;

type Page = {
  createCDPSession(): Promise<{ send(method: string, params?: object): Promise<unknown> }>;
  waitForFunction(fn: (...args: never[]) => unknown, options: object, ...args: unknown[]): Promise<unknown>;
  evaluate(fn: (...args: never[]) => unknown, ...args: unknown[]): Promise<any>;
};

const sessions = new WeakMap<Page, Awaited<ReturnType<Page['createCDPSession']>>>();

/**
 * Plays every animation of the current document `rate` times faster (DevTools' animation speed),
 * so a transition passes through the same frames to the same end state in less time. A navigation
 * starts a new document at normal speed.
 */
export async function animationRate(page: Page, rate: number) {
  let session = sessions.get(page);
  if (!session) {
    session = await page.createCDPSession();
    await session.send('Animation.enable');
    sessions.set(page, session);
  }
  await session.send('Animation.setPlaybackRate', { playbackRate: rate });
}

/**
 * Waits until the frame of `route` renders click `step` with no finite animation still running or
 * pending in the document. Returns a problem, or '' when it settled within settleTimeoutMs and no
 * transition it saw lasts longer than longestTransitionMs. The caller reads the state either way,
 * so a wrong click also fails on its content.
 */
export async function settle(page: Page, route: string, step: number): Promise<string> {
  const settled = await page.waitForFunction((sourceId: string, expected: number) => {
    const state = window as unknown as { courseLongest?: number };
    let moving = false;
    for (const animation of document.getAnimations()) {
      const end = Number(animation.effect?.getComputedTiming().endTime);
      if (animation.playState !== 'running' || end === Infinity) continue;
      moving = true;
      state.courseLongest = Math.max(state.courseLongest ?? 0, end);
    }
    const run = document.querySelector<HTMLElement>(`[data-source-id="${sourceId}"] .ds-run`);
    return !moving && Boolean(run) && Number(run!.dataset.dsStep) === expected;
  }, { polling: 'raf', timeout: settleTimeoutMs }, route, step).then(() => true, () => false);
  const longest: number = await page.evaluate(() => {
    const state = window as unknown as { courseLongest?: number };
    const value = state.courseLongest ?? 0;
    state.courseLongest = 0;
    return value;
  });
  if (!settled) return `click ${step} not rendered and settled ${settleTimeoutMs} ms after the key press`;
  if (longest > longestTransitionMs) return `click ${step} runs a ${Math.round(longest)} ms transition, longer than ${longestTransitionMs} ms`;
  return '';
}
