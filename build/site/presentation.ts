// Course-owned entry point; the exercise site's inline source previews remain
// portable under file://. Embed the standalone Marp deck for the same reason.
export const presentationPage = {
  file: 'presentation.html',
  title: 'Course slides',
  linkText: 'Open the course slides',
  body: `<div class="index-body"><main>
<p class="eyebrow">PRG400 · Python Programming</p>
<h1>Course slides</h1>
<p>The slides are embedded below. Use the arrow keys or scroll to move between slides.
<a href="slides-marp.html" target="_blank" rel="noopener">Open the slides in a new tab</a>.</p>
<div class="presentation-frame">
  <iframe title="Python Programming slides" src="slides-marp.html" allow="fullscreen" loading="lazy"></iframe>
</div>
<p><a href="../PRG400-Python-Programming.pdf">Read the slides PDF</a> directly.
The <a href="slides-marp.html">static fallback</a> also opens directly from disk.</p>
<p>Slide previews inside exercise hints remain available without starting a server.</p>
<style>
.presentation-frame { width: 100%; height: min(72vh, 760px); min-height: 420px; margin: 1.5rem 0; overflow: hidden; border: 1px solid var(--line, #d0d7de); border-radius: 10px; background: #fff; }
.presentation-frame iframe { display: block; width: 100%; height: 100%; border: 0; }
@media (max-width: 640px) { .presentation-frame { height: 64vh; min-height: 320px; } }
</style>
</main></div>`,
};
