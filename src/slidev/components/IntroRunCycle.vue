<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $clicks } = useSlideContext()
const states = [
  { active: 0, editor: 'Imagine', disk: 'Imagine', output: 'Imagine', status: 'Saved', caption: 'The editor and the saved file contain the same statement.' },
  { active: 0, editor: 'Yesterday', disk: 'Imagine', output: 'Imagine', status: 'Unsaved change', caption: 'Edit the message. The saved file still contains Imagine.' },
  { active: 2, editor: 'Yesterday', disk: 'Imagine', output: 'Imagine', status: 'Unsaved change', caption: 'Run before saving. Python reads the saved file and prints Playing Imagine.' },
  { active: 1, editor: 'Yesterday', disk: 'Yesterday', output: 'Imagine', status: 'Saved', caption: 'Save the file. The terminal still shows the output of the previous run.' },
  { active: 2, editor: 'Yesterday', disk: 'Yesterday', output: 'Yesterday', status: 'Saved', caption: 'Run again. Python reads the updated file and prints Playing Yesterday.' },
]
const step = computed(() => Math.max(0, Math.min($clicks.value, states.length - 1)))
const state = computed(() => states[step.value])
</script>

<template>
  <div class="intro-cycle" :data-intro-step="step">
    <ol class="steps" aria-label="Edit, save and run cycle">
      <li v-for="(label, index) in ['Edit', 'Save', 'Run']" :key="label" :class="{ active: state.active === index }">{{ label }}</li>
    </ol>
    <div class="panels">
      <section :class="{ active: state.active === 0 }">
        <header>Editor · hello.py</header>
        <span class="status">{{ state.status }}</span>
        <pre>print("Playing {{ state.editor }}")</pre>
        <p>Working text in the editor</p>
      </section>
      <section :class="{ active: state.active === 1 }">
        <header>Saved file · hello.py</header>
        <span class="status">On disk</span>
        <pre>print("Playing {{ state.disk }}")</pre>
        <p>Source code Python reads</p>
      </section>
      <section :class="{ active: state.active === 2 }">
        <header>Terminal</header>
        <code>uv run python hello.py</code>
        <pre>Playing {{ state.output }}</pre>
        <p>Output from the most recent run</p>
      </section>
    </div>
    <p class="caption" aria-live="polite">{{ state.caption }}</p>
  </div>
</template>

<style scoped>
.intro-cycle { margin-top: 20px; color: var(--course-ink, #0f1729); }
.steps { display: flex; gap: 18px; padding: 0; margin: 0 0 16px; list-style: none; counter-reset: phase; }
.steps li { flex: 1; padding: 10px 16px; border-bottom: 4px solid #c3d3e3; font-size: 23px; counter-increment: phase; }
.steps li::before { content: counter(phase) '  '; font-family: monospace; }
.steps li.active { border-color: var(--course-accent, #24669a); font-weight: 600; }
.panels { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
section { padding: 16px; border: 2px solid #c3d3e3; border-radius: 8px; background: #f7f9fc; transition: border-color 250ms ease, background-color 250ms ease; }
section.active { border-color: var(--course-accent, #24669a); background: #e9f2fa; }
section:last-child { grid-column: 1 / -1; }
header { font-size: 18px; font-weight: 600; margin-bottom: 6px; }
.status, section p { font-size: 16px; color: #52657a; }
pre { font: 20px/1.5 'IBM Plex Mono', monospace; white-space: pre; margin: 8px 0; }
code { font: 16px/1.5 'IBM Plex Mono', monospace; }
section p { margin: 0; }
.caption { margin: 18px 0 0; font-size: 21px; min-height: 2.6em; }
@media (prefers-reduced-motion: reduce) { section { transition: none; } }
</style>
