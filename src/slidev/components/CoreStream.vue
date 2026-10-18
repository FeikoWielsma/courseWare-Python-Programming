<script setup>
// What the print() calls have written so far, for the module 01 native slide.
// Each call adds one piece of text, followed by a newline mark when it ended
// the line. The output panel shows finished lines; this shows the open one too,
// with the cursor where the next print() will continue.
//
// state.writes : [{ text, newline }], in the order they were written
import { computed } from 'vue'

const props = defineProps({ run: { type: Object, required: true }, step: { type: Number, required: true } })
const writes = computed(() => props.run.states[props.step].writes)
// Group the writes into the lines they appear on.
const lines = computed(() => {
  const result = [[]]
  const before = props.step > 0 ? props.run.states[props.step - 1].writes.length : 0
  writes.value.forEach((write, i) => {
    result[result.length - 1].push({ ...write, key: i, fresh: props.step > 0 && i >= before })
    if (write.newline) result.push([])
  })
  return result
})
</script>

<template>
  <section class="core-stream" aria-label="Text written by print" :data-core-step="step">
    <header>Written by print()</header>
    <div v-for="(line, n) in lines" :key="n" class="line">
      <span v-for="write in line" :key="write.key" class="write" :class="{ fresh: write.fresh }" data-core-write>
        <span class="text">{{ write.text }}</span><span v-if="write.newline" class="newline" title="newline">newline</span>
      </span>
      <span v-if="n === lines.length - 1" class="caret" aria-hidden="true" />
    </div>
  </section>
</template>

<style scoped>
.core-stream { border: 2px solid #c3d3e3; border-radius: 8px; background: #f7f9fc; padding: 4px 16px 6px; font-family: 'IBM Plex Mono', monospace; }
header { font: 600 11px/1.6 'IBM Plex Mono', monospace; letter-spacing: .16em; text-transform: uppercase; color: var(--ds-muted); }
.line { min-height: 30px; display: flex; align-items: center; flex-wrap: nowrap; white-space: pre; font-size: 18px; color: var(--ds-ink); }
.write { display: inline-flex; align-items: center; border-bottom: 3px solid transparent; transition: border-color 300ms ease; }
.write.fresh { border-bottom-color: var(--ds-select); }
.write .text { background: white; }
.newline {
  margin-left: 6px; padding: 1px 6px; border-radius: 4px; font-size: 12px; letter-spacing: .04em;
  background: var(--ds-select-soft); color: var(--ds-select); border: 1px solid var(--ds-select);
}
.caret { display: inline-block; width: 11px; height: 22px; margin-left: 2px; background: var(--ds-accent); opacity: .7; }
.write { animation: core-arrive var(--ds-time) var(--ds-ease); }
@keyframes core-arrive { from { opacity: 0; transform: translateY(-8px); } }
@media (prefers-reduced-motion: reduce) {
  .write { animation: none; transition: none; }
}
</style>
