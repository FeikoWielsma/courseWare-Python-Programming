<script setup>
// The items a for loop walks, for the native slides of module 04. Each row is
// one loop's sequence, with an end slot that lights when no items are left.
// The loop variable is one tag above the item it refers to; it slides from
// item to item, and to the next row when a later loop rebinds the same name.
// Each item records what its pass did, so the final state reads on its own.
//
// run.rows : [{ id, label, variable, items: [...], width? }], top to bottom
// state.cursor : { row, at } | null, the item the loop variable refers to
// state.status : { rowId: ['ran' | 'skip' | 'stop' | 'never' | '', ...] };
//   '' is an item not reached yet, 'never' one the loop will not reach
// state.ended : [rowId, ...], loops that ran out of items
import { computed } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
  labelWidth: { type: Number, default: 170 },
  tileWidth: { type: Number, default: 58 },
})
const tileGap = 8
const tileHeight = 50
const rowPitch = 112
const tileTop = 32
const endWidth = 132
const state = computed(() => props.run.states[props.step])
const words = { skip: 'continue', stop: 'break' }

const tileX = (row, i) => props.labelWidth + i * ((row.width || props.tileWidth) + tileGap)
const rows = computed(() => props.run.rows.map((row, r) => {
  const width = row.width || props.tileWidth
  const status = state.value.status?.[row.id] || []
  const cursorHere = state.value.cursor?.row === row.id
  return {
    ...row, y: r * rowPitch, width,
    ended: (state.value.ended || []).includes(row.id),
    endX: tileX(row, row.items.length) + 10,
    tiles: row.items.map((text, i) => ({
      i, text, x: tileX(row, i), status: status[i] || '',
      current: cursorHere && state.value.cursor.at === i,
      word: words[status[i]] || '',
    })),
  }
}))
// The tag stays where it was last bound, or waits above the first item.
const cursor = computed(() => {
  const states = props.run.states
  let at = state.value.cursor
  const shown = Boolean(at)
  if (!at) at = states.slice(0, props.step).reverse().find(item => item.cursor)?.cursor || states.find(item => item.cursor).cursor
  const r = props.run.rows.findIndex(row => row.id === at.row)
  const row = props.run.rows[r]
  return { shown, name: row.variable, x: tileX(row, at.at), y: r * rowPitch, width: row.width || props.tileWidth }
})
const width = computed(() => Math.max(...rows.value.map(row => row.endX + endWidth)))
</script>

<template>
  <div class="core-loop" :style="{ height: `${run.rows.length * rowPitch - 12}px`, width: `${width}px` }" :data-core-step="step">
    <template v-for="row in rows" :key="row.id">
      <span class="label" :style="{ top: `${row.y + tileTop}px`, width: `${labelWidth - 18}px` }">{{ row.label }}</span>
      <span
        v-for="tile in row.tiles" :key="`${row.id}-${tile.i}`" class="tile" :class="[tile.status, { current: tile.current }]"
        :style="{ transform: `translate(${tile.x}px, ${row.y + tileTop}px)`, width: `${row.width}px` }"
        :data-core-row="row.id" :data-core-status="tile.status" data-core-value
      >{{ tile.text }}<small>{{ tile.word }}</small></span>
      <span
        class="end" :class="{ ended: row.ended }" :style="{ transform: `translate(${row.endX}px, ${row.y + tileTop}px)` }"
        :data-core-end="row.id"
      >{{ row.ended ? 'no items left' : 'end' }}</span>
    </template>
    <span
      class="cursor" :class="{ shown: cursor.shown }"
      :style="{ transform: `translate(${cursor.x}px, ${cursor.y}px)`, width: `${cursor.width}px` }" data-core-cursor
    >{{ cursor.name }}</span>
  </div>
</template>

<style scoped>
.core-loop { position: relative; font-family: 'IBM Plex Mono', monospace; }
.label { position: absolute; left: 0; height: 50px; display: flex; align-items: center; justify-content: flex-end; font: 600 19px 'IBM Plex Mono', monospace; color: var(--ds-accent); white-space: nowrap; }
.tile, .end, .cursor { position: absolute; left: 0; top: 0; box-sizing: border-box; }
.tile {
  height: 50px; display: flex; align-items: center; justify-content: center; border: 2px solid var(--ds-line); border-radius: 5px;
  background: white; color: var(--ds-ink); font-size: 21px; white-space: nowrap;
  transition: background-color 300ms ease, border-color 300ms ease, color 300ms ease, opacity 300ms ease;
}
.tile small { position: absolute; left: -12px; right: -12px; top: 52px; text-align: center; font-size: 13px; letter-spacing: .04em; }
.tile.ran { background: var(--ds-panel); border-color: var(--ds-accent); }
.tile.skip { background: var(--ds-change-soft); border-color: var(--ds-change); border-style: dashed; color: var(--ds-change); }
.tile.skip small { color: var(--ds-change); }
.tile.stop { background: var(--ds-remove-soft); border-color: var(--ds-remove); color: var(--ds-remove); }
.tile.stop small { color: var(--ds-remove); }
.tile.never { opacity: .45; border-style: dashed; color: var(--ds-muted); }
.tile.current { z-index: 1; border-width: 3px; border-color: var(--ds-select); box-shadow: 0 0 0 4px var(--ds-select-soft); }
.end {
  width: 132px; height: 50px; display: flex; align-items: center; justify-content: center; border: 2px dashed #c3d3e3; border-radius: 5px;
  font-size: 15px; color: var(--ds-muted); transition: background-color 300ms ease, border-color 300ms ease, color 300ms ease;
}
.end.ended { border-style: solid; border-color: var(--ds-select); background: var(--ds-select-soft); color: var(--ds-ink); }
.cursor {
  height: 28px; display: flex; align-items: flex-start; justify-content: center; font: 600 17px/22px 'IBM Plex Mono', monospace; color: var(--ds-select);
  opacity: 0; transition: transform var(--ds-time) var(--ds-ease), width var(--ds-time) var(--ds-ease), opacity 300ms ease;
}
.cursor::after { content: ''; position: absolute; left: 50%; bottom: 0; margin-left: -6px; border: 6px solid transparent; border-top: 7px solid var(--ds-select); border-bottom: 0; }
.cursor.shown { opacity: 1; }
@media (prefers-reduced-motion: reduce) {
  .tile, .end, .cursor { transition: none; }
}
</style>
