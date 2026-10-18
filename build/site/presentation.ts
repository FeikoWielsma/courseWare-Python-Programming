// Course-owned entry point; the exercise site's inline source previews remain
// portable under file://. The presentation itself uses its included server.
export const presentationPage = {
  file: 'presentation.html',
  title: 'Course slides',
  linkText: 'Open the course slides',
  body: `<div class="index-body"><main>
<p class="eyebrow">PRG400 · Python Programming</p>
<h1>Course slides</h1>
<p>The animated presentation shows code execution, changing values and references one step at a time.</p>
<p>From the course folder, run:</p>
<pre><code>python slides/serve.py</code></pre>
<p>Then <a href="http://localhost:4188/slidev/" target="_blank" rel="noopener">open the presentation</a>.
Use the arrow keys or scroll to advance. Going back reverses each step.</p>
<p>In Codespaces, open port 4188 from the Ports panel.</p>
<p><a href="../PRG400-Python-Programming.pdf">Read the slides PDF</a> directly.
The <a href="../PRG400-Python-Programming-Marp.html">Marp fallback</a> also opens directly from disk.</p>
<p>Slide previews inside exercise hints remain available without starting a server.</p>
</main></div>`,
};
