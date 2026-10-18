#!/usr/bin/env bun
import * as fs from 'node:fs';
import * as path from 'node:path';
import { createHash } from 'node:crypto';
import { pathToFileURL } from 'node:url';

type DiagramApi = {
  DIAGRAM_RENDERER: string;
  diagramCacheFile: (code: string, rootDir?: string) => string;
  diagramHash: (code: string) => string;
  embedDiagram: (code: string, rootDir?: string) => string;
};

function markdownFiles(folder: string): string[] {
  if (!fs.existsSync(folder)) return [];
  return fs.readdirSync(folder, { withFileTypes: true }).flatMap(entry => {
    const fullPath = path.join(folder, entry.name);
    return entry.isDirectory() ? markdownFiles(fullPath) : entry.name.endsWith('.md') ? [fullPath] : [];
  });
}

function fail(message: string): never {
  throw new Error(message);
}

function normalized(value: string): string {
  return value.replace(/<[^>]+>/g, '')
    .replace(/&(?:amp|lt|gt|quot|apos);/g, entity => ({ '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&apos;': "'" })[entity]!)
    .replace(/\s+/g, ' ').trim();
}

async function main() {
  const root = path.resolve(process.cwd());
  const shared = process.env.PRESENTATION_TEMPLATE_DIR;
  if (!shared) fail('Set PRESENTATION_TEMPLATE_DIR to the Slidev-capable Presentation-Template worktree.');
  const diagramsUrl = pathToFileURL(path.join(shared, 'build/src/diagrams.ts')).href;
  const { DIAGRAM_RENDERER, diagramCacheFile, diagramHash, embedDiagram } = await import(diagramsUrl) as DiagramApi;
  const { parseModule } = await import(pathToFileURL(path.join(shared, 'build/src/parser.ts')).href);
  const { withBrowser, browserTimeoutMs } = await import(pathToFileURL(path.join(shared, 'build/browser.ts')).href);
  const { readManifest, deliverable } = await import(pathToFileURL(path.join(shared, 'build/artifacts.ts')).href);
  const sources = [
    ...markdownFiles(path.join(root, 'src/slides')),
    ...markdownFiles(path.join(root, 'src/slidev')),
  ];
  const found: { file: string; code: string }[] = [];

  for (const file of sources) {
    const markdown = fs.readFileSync(file, 'utf8');
    for (const match of markdown.matchAll(/^```mermaid[^\r\n]*\r?\n([\s\S]*?)\r?\n```/gm)) {
      found.push({ file: path.relative(root, file).replace(/\\/g, '/'), code: match[1].trim() });
    }
  }

  if (!found.length) fail('No Mermaid fences found in canonical slides or native Slidev additions.');
  const failures: string[] = [];
  const summary: string[] = [];
  if (!/^pele@\d+\.\d+\.\d+$/.test(DIAGRAM_RENDERER)) failures.push(`Unexpected renderer pin: ${DIAGRAM_RENDERER}`);

  for (const [index, diagram] of found.entries()) {
    const { file, code } = diagram;
    const label = `${file} [diagram ${index + 1}]`;
    const hash = diagramHash(code);
    const rendererInput = `${DIAGRAM_RENDERER}\nIBM Plex Sans, Helvetica Neue, Arial, sans-serif\nIBM Plex Mono, ui-monospace, monospace\n${code.trim()}`;
    const expectedHash = createHash('sha1').update(rendererInput).digest('hex');
    const simulatedBumpHash = createHash('sha1').update(rendererInput.replace(DIAGRAM_RENDERER, DIAGRAM_RENDERER.replace(/\d+\.\d+\.\d+$/, '0.0.0'))).digest('hex');
    if (hash !== expectedHash || hash === simulatedBumpHash) failures.push(`${label}: cache key does not encode the pinned renderer/font inputs.`);
    const cacheFile = diagramCacheFile(code, root);
    const cacheDir = path.dirname(cacheFile);
    if (!fs.existsSync(cacheFile)) failures.push(`${label}: cache missing for ${DIAGRAM_RENDERER} (${hash}).`);
    if (fs.existsSync(path.join(cacheDir, `placeholder-mermaid-${hash}.svg`))) failures.push(`${label}: renderer placeholder exists.`);
    const svg = fs.existsSync(cacheFile) ? fs.readFileSync(cacheFile, 'utf8') : '';
    const rendered = embedDiagram(code, root);
    if (rendered.includes('placeholder-mermaid') || rendered.includes('Diagram render error')) failures.push(`${label}: rendering returned a placeholder.`);
    if (!/^<svg\b/.test(svg) || !svg.includes('</svg>')) failures.push(`${label}: cache entry is not a complete SVG.`);
    if (/placeholder-mermaid|Diagram render error/.test(svg)) failures.push(`${label}: cached SVG is a placeholder.`);
    if (!/class="[^"]*\bpele\b/.test(svg)) failures.push(`${label}: Pele SVG class is missing.`);
    const viewBox = /\bviewBox="([\d.-]+)\s+([\d.-]+)\s+([\d.]+)\s+([\d.]+)"/.exec(svg);
    if (!viewBox || Number(viewBox[1]) !== 0 || Number(viewBox[2]) !== 0 || Number(viewBox[3]) <= 0 || Number(viewBox[4]) <= 0) {
      failures.push(`${label}: SVG viewBox is missing, nonpositive or not tight at origin.`);
    }
    if (!/font:16px\s/.test(svg)) failures.push(`${label}: expected Pele's 16px user-unit font declaration.`);

    const sourceNodes = new Set([...code.matchAll(/(?<![\w-])([A-Za-z][\w-]*)\s*[\[{]/g)].map(match => match[1]));
    const sourceEdges = [...code.matchAll(/(?:-->|==>|-\.->|--x|--o)/g)].length;
    const svgNodes = [...svg.matchAll(/<g\s+class="pele-node(?:\s|")/g)].length;
    const svgEdges = [...svg.matchAll(/<g\s+class="pele-edge(?:\s|")/g)].length;
    if (svgNodes !== sourceNodes.size) failures.push(`${label}: ${sourceNodes.size} source nodes but ${svgNodes} rendered nodes.`);
    if (svgEdges !== sourceEdges) failures.push(`${label}: ${sourceEdges} source edges but ${svgEdges} rendered edges.`);

    const visibleText = [...svg.matchAll(/<text\b[^>]*>([\s\S]*?)<\/text>/g)].map(match => normalized(match[1]));
    const labels = [...code.matchAll(/[\w-]+\s*[\[{]([^}\]]+)[\]}]/g)].map(match => normalized(match[1]));
    for (const sourceLabel of labels) {
      const textRuns = sourceLabel.split(/\s+/).filter(Boolean);
      const foundLabel = visibleText.some(text => text.includes(sourceLabel))
        || (textRuns.length > 1 && textRuns.every(run => visibleText.some(text => text.includes(run))));
      if (!foundLabel) failures.push(`${label}: source label is absent from SVG text: ${sourceLabel}`);
    }

    const ids = [...svg.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
    const duplicateIds = ids.filter((id, position) => ids.indexOf(id) !== position);
    if (duplicateIds.length) failures.push(`${label}: duplicate SVG ids: ${[...new Set(duplicateIds)].join(', ')}`);
    if (/%%\s*\{\s*init|\b(?:style|classDef)\s+[\w-]+\s+fill\s*:/i.test(code)) failures.push(`${label}: theme or hardcoded-color directive found in canonical source.`);
    summary.push(`${label}: ${code.split(/\r?\n/, 1)[0]}, nodes=${svgNodes}, edges=${svgEdges}, viewBox=${viewBox?.[3]}x${viewBox?.[4]}, ids=${ids.length}, cache=${fs.existsSync(cacheFile) ? 'hit' : 'miss'}`);
  }

  const output = path.join(root, '.courseware/fundamentals/student');
  const manifestPath = path.join(output, 'manifest.json');
  if (!fs.existsSync(manifestPath)) fail('Build Slidev first; .courseware/fundamentals/student/manifest.json is missing.');
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const browserCases: { id: string; title: string; source: string }[] = [];
  for (const sourceFile of [...new Set(found.map(item => item.file))]) {
    if (!sourceFile.startsWith('src/slides/')) continue;
    const absoluteFile = path.join(root, sourceFile);
    const parsed = await parseModule(absoluteFile);
    const diagramSlides = parsed.content.filter((slide: { raw: string }) => slide.raw.includes('class="pele'));
    const sourceDiagrams = found.filter(item => item.file === sourceFile);
    if (diagramSlides.length !== sourceDiagrams.length) failures.push(`${sourceFile}: parser found ${diagramSlides.length} rendered diagram slides for ${sourceDiagrams.length} fences.`);
    for (const slide of diagramSlides) {
      const topic = manifest.topics.find((item: { module: string; title: string; id: string }) => item.module === path.basename(path.dirname(absoluteFile)) && item.title === slide.title);
      if (!topic) failures.push(`${sourceFile}: no Slidev source route for diagram slide "${slide.title}".`);
      else browserCases.push({ id: topic.id, title: slide.title, source: sourceFile });
    }
  }

  if (browserCases.length) {
    const presentation = path.join(root, deliverable(readManifest(output), 'presentation').path);
    await withBrowser({ dir: presentation, port: 0 }, async ({ page, origin }) => {
      for (const testCase of browserCases) {
        await page.goto(`${origin}/slidev/#/${testCase.id}`, { waitUntil: 'networkidle0', timeout: browserTimeoutMs });
        await page.waitForSelector(`.course-frame[data-source-id="${testCase.id}"] svg.pele`, { timeout: browserTimeoutMs });
        const state = await page.evaluate(async (id: string) => {
          await document.fonts.ready;
          const frame = document.querySelector<HTMLElement>(`.course-frame[data-source-id="${id}"]`);
          const svg = frame?.querySelector<SVGSVGElement>('svg.pele');
          if (!frame || !svg) return { missing: true };
          const box = svg.getBoundingClientRect();
          const body = frame.querySelector<HTMLElement>('.course-body')!.getBoundingClientRect();
          const viewBox = svg.viewBox.baseVal;
          const drawn = svg.getBBox();
          const scale = Math.abs(svg.getScreenCTM()!.d);
          const text = [...svg.querySelectorAll<SVGTextElement>('text')];
          const escaped = text.filter(node => {
            const rect = node.getBoundingClientRect();
            return rect.left < box.left - 1 || rect.top < box.top - 1 || rect.right > box.right + 1 || rect.bottom > box.bottom + 1
              || rect.left < body.left - 1 || rect.top < body.top - 1 || rect.right > body.right + 1 || rect.bottom > body.bottom + 1;
          }).map(node => node.textContent || '');
          return {
            missing: false, scale: Number(scale.toFixed(3)), renderedFontPx: Number((Math.min(...text.map(node => parseFloat(getComputedStyle(node).fontSize))) * scale).toFixed(1)),
            labels: text.length, nodes: svg.querySelectorAll('.pele-node').length, edges: svg.querySelectorAll('.pele-edge').length,
            viewBox: [viewBox.width, viewBox.height], drawn: [drawn.x, drawn.y, drawn.x + drawn.width, drawn.y + drawn.height],
            viewBoxOverflow: drawn.x < 0 || drawn.y < 0 || drawn.x + drawn.width > viewBox.width + 1 || drawn.y + drawn.height > viewBox.height + 1,
            duplicateIds: [...svg.querySelectorAll('[id]')].map(node => node.id).filter((value, index, all) => all.indexOf(value) !== index),
            escaped,
          };
        }, testCase.id);
        summary.push(`${testCase.id} browser: text=${state.renderedFontPx ?? 'missing'}px, labels=${state.labels ?? 0}, nodes=${state.nodes ?? 0}, edges=${state.edges ?? 0}, scale=${state.scale ?? 'n/a'}`);
        if (state.missing) failures.push(`${testCase.id}: the built browser slide has no Pele diagram.`);
        else {
          if (state.renderedFontPx < 10) failures.push(`${testCase.id}: diagram text renders at ${state.renderedFontPx}px; minimum is 10px.`);
          if (state.viewBoxOverflow) failures.push(`${testCase.id}: rendered SVG content escapes its viewBox.`);
          if (state.duplicateIds.length) failures.push(`${testCase.id}: duplicate browser SVG ids: ${state.duplicateIds.join(', ')}`);
          if (state.escaped.length) failures.push(`${testCase.id}: diagram text escapes its SVG/frame bounds: ${state.escaped.join(', ')}`);
        }
      }
    });
  }

  console.log(`Renderer: ${DIAGRAM_RENDERER}; audited ${found.length} Mermaid fence(s).`);
  for (const line of summary) console.log(line);
  if (failures.length) fail(failures.join('\n'));
  console.log('Static diagram checks passed. Use the full browser check to inspect rendered font scale and slide-frame fit.');
}

main().catch(error => { console.error(error); process.exitCode = 1; });
