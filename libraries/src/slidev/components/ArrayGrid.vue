<script setup>
import { computed } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
})
const grids = computed(() => props.run.states[props.step].grids)
const maximumRows = name => Math.max(...props.run.states.map(state =>
  state.grids.find(grid => grid.name === name)?.values.length || 0))
</script>

<template>
  <div class="array-grids" :data-array-step="step">
    <section v-for="grid in grids" :key="grid.name" :aria-label="grid.name">
      <header>{{ grid.name }}</header>
      <div class="array-grid" :style="{
        gridTemplateColumns: `minmax(${grid.labelWidth || 70}px, 1fr) repeat(${grid.columns.length}, minmax(0, 1fr))`,
        minHeight: `${(maximumRows(grid.name) + 1) * 34}px`,
      }">
        <span class="corner">{{ grid.index || '' }}</span>
        <span v-for="column in grid.columns" :key="column" class="column">{{ column }}</span>
        <template v-for="(row, i) in grid.values" :key="i">
          <span class="row-label" :title="String(grid.labels?.[i] ?? i)">{{ grid.labels?.[i] ?? i }}</span>
          <span v-for="(value, j) in row" :key="j" class="cell"
            :class="{ selected: grid.selected?.some(([r, c]) => r === i && c === j) }"
            :title="String(value)" :data-array-cell="`${grid.name}:${i}:${j}`">{{ value }}</span>
        </template>
      </div>
    </section>
  </div>
</template>

<style scoped>
.array-grids { display: grid; gap: 14px; color: var(--course-ink, #0f1729); }
section { min-width: 0; border: 1px solid #9bb9d6; border-radius: 6px; overflow: hidden; }
header { padding: 6px 10px; background: #eef3f9; font: 600 16px 'IBM Plex Mono', monospace; }
.array-grid { display: grid; align-content: start; font: 16px 'IBM Plex Mono', monospace; }
.array-grid > span { min-width: 0; box-sizing: border-box; height: 34px; padding: 7px 8px;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap; border-top: 1px solid #d8e4ef; }
.row-label, .column, .corner { color: #45617c; background: #f7f9fc; }
.cell { border-left: 1px solid #d8e4ef; transition: background-color 300ms ease, color 300ms ease; }
.selected { background: #ddf0f4; color: #126e87; font-weight: 600; }
@media (prefers-reduced-motion: reduce) { .cell { transition: none; } }
</style>
