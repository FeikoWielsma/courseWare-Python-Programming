<script setup>
// One program run on a native Data Structures slide : the code (default slot,
// a fence whose cumulative line ranges are the click states), the output the
// lines printed so far, a visual (named slot) and a caption for the step.
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  run: { type: Object, required: true },
  // stack : code above, visual and output below
  // pair : code and output side by side, visual below
  // side : code and output on the left, visual on the right
  // rows : code, output and visual, each across the full width
  layout: { type: String, default: 'stack' },
  outputWidth: { type: String, default: '340px' },
})
const { $clicks } = useSlideContext()
const step = computed(() => Math.max(0, Math.min($clicks.value, props.run.output.length - 1)))
// Reserve room for every line the run prints, so nothing below it moves.
const reserved = computed(() => `${30 + 23 * props.run.output.flat().length}px`)
// Hidden future output participates in layout, including wrapped error messages.
// Otherwise an auto-sized code column can move the visual when output appears.
const lines = computed(() => props.run.output.flatMap((group, index) =>
  group.map((text, n) => ({ text, key: `${index}-${n}`, shown: index <= step.value, fresh: index === step.value && index > 0 }))))
// Captions mark inline code with backticks, as the slides do.
const caption = computed(() => (props.run.captions?.[step.value] || '').split('`').map((text, i) => ({ text, code: i % 2 === 1 })))
</script>

<template>
  <div class="ds-run" :class="`ds-${layout}`" :style="{ '--ds-output-width': outputWidth }" :data-ds-step="step">
    <div class="ds-code"><slot /></div>
    <section class="ds-output" aria-label="Program output" :style="{ minHeight: reserved }">
      <header>Output</header>
      <ol>
        <li v-for="line in lines" :key="line.key" :class="{ fresh: line.fresh }" :style="{ visibility: line.shown ? 'visible' : 'hidden' }" :aria-hidden="!line.shown" :data-ds-output="line.shown ? '' : undefined">{{ line.text }}</li>
      </ol>
    </section>
    <div class="ds-visual"><slot name="visual" :step="step" /></div>
    <p class="ds-caption" aria-live="polite" data-ds-caption><template v-for="(part, i) in caption" :key="i"><code v-if="part.code">{{ part.text }}</code><template v-else>{{ part.text }}</template></template></p>
  </div>
</template>

<style scoped>
.ds-run {
  --ds-ink: var(--course-ink, #0f1729);
  --ds-muted: #5a6f86;
  --ds-panel: #eef3f9;
  --ds-line: #9bb9d6;
  --ds-accent: var(--course-accent, #24669a);
  --ds-select: #2a8aa8;
  --ds-select-soft: #ddf0f4;
  --ds-change: #c98a1c;
  --ds-change-soft: #fdf0d8;
  --ds-remove: #c8432a;
  --ds-remove-soft: #fbe4df;
  --ds-ease: cubic-bezier(.22, .75, .25, 1);
  --ds-time: 600ms;
  flex: 1 1 0;
  min-height: 0;
  display: grid;
  align-content: start;
  gap: 16px 24px;
}
.ds-stack { grid-template: 'code code' auto 'visual output' auto 'caption caption' auto / minmax(0, 1fr) var(--ds-output-width); }
.ds-pair { grid-template: 'code output' auto 'visual visual' auto 'caption caption' auto / auto minmax(0, 1fr); }
.ds-side { grid-template: 'code visual' auto 'output visual' auto 'output caption' auto / auto minmax(0, 1fr); }
.ds-rows { grid-template: 'code' auto 'output' auto 'visual' auto 'caption' auto / minmax(0, 1fr); }
.ds-code { grid-area: code; min-width: 0; }
.ds-output { grid-area: output; min-width: 0; }
.ds-visual { grid-area: visual; min-width: 0; position: relative; }

.ds-code :deep(.slidev-code-wrapper) { margin: 0; width: auto; max-width: 100%; }
.ds-code :deep(.slidev-code .line) {
  display: inline-block; width: calc(100% + 36px); margin: 0 -18px; padding: 0 18px;
  transition: background-color 300ms ease, box-shadow 300ms ease, opacity 300ms ease;
}
/* Lines that have not run yet are dimmed by Slidev; keep them legible in print. */
.ds-code :deep(.slidev-code .line.slidev-code-dishonored) { opacity: .36; }
/* The last line that ran is the active one. */
.ds-code :deep(.slidev-code .line.slidev-code-highlighted:not(:has(~ .line.slidev-code-highlighted))) {
  background: var(--ds-select-soft); box-shadow: inset 4px 0 0 var(--ds-select);
}

.ds-output { align-self: start; border: 1px solid #d9dde5; border-radius: 6px; background: #f5f7fa; padding: 6px 14px 6px; box-sizing: border-box; }
.ds-output header { font: 600 11px/1.6 'IBM Plex Mono', monospace; letter-spacing: .16em; text-transform: uppercase; color: var(--ds-muted); }
.ds-output ol { list-style: none; margin: 2px 0 0; padding: 0; }
.ds-output li { margin: 0; padding: 0 0 0 10px; font: 400 16px/1.45 'IBM Plex Mono', monospace; color: var(--ds-ink); white-space: pre-wrap; overflow-wrap: anywhere; border-left: 3px solid transparent; transition: border-color 300ms ease; }
.ds-output li.fresh { border-left-color: var(--ds-select); }

.ds-caption { grid-area: caption; margin: 0; font-size: 19px; line-height: 1.35; color: #34465a; min-height: 26px; }
.ds-caption code { font-size: .85em; padding: 1px 6px; border-radius: 4px; background: #eef3f9; color: var(--ds-accent); }

@media (prefers-reduced-motion: reduce) {
  .ds-run { --ds-time: 0ms; }
  .ds-code :deep(.slidev-code .line), .ds-output li { transition: none; }
}
</style>
