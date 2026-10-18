<script setup>
// A list comprehension at work, for the native slides of module 07. The source
// list is drawn once : one row of items, or a list of inner lists. The loop
// variable is a tag above the item it refers to (and, with two for clauses, a
// second tag above the inner list). An item the comprehension adds moves from
// its source cell into the next slot of the new list : the same object, now
// referred to from two lists. Moving back replays the step in reverse.
//
// run.source : { name, rows: [{ id, items: [{ id, text }] }], nested }
//   nested draws each row as an inner list inside the outer one
// run.variables : { item, row? }, the names the for clauses bind
// run.result : { name }, the name the finished list is bound to
// state.list : the new list exists (the comprehension has started)
// state.cursor : { row?, item } | null, what the loop variables refer to
// state.tested : { itemId: true | false }, the if condition for each item tested
// state.result : [itemId, ...], the new list's items in order
// state.bound : the finished list is bound to run.result.name
import { computed } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
  cellWidth: { type: Number, default: 150 },
  labelWidth: { type: Number, default: 140 },
})
const cellHeight = 50
const innerGap = 28
const innerPad = 8
const state = computed(() => props.run.states[props.step])
const nested = computed(() => Boolean(props.run.source.nested))
const sourceY = computed(() => (nested.value ? 64 : 34))
const testY = computed(() => sourceY.value + cellHeight + 6)
const resultY = computed(() => sourceY.value + cellHeight + 66)
const pitch = computed(() => props.cellWidth - 2)

// Fixed geometry : every source cell and result slot has one place.
const rows = computed(() => {
  let x = props.labelWidth + (nested.value ? innerPad + 6 : 0)
  return props.run.source.rows.map(row => {
    const at = x
    const width = row.items.length * pitch.value + 2
    x += width + (nested.value ? innerGap : 0)
    return { ...row, x: at, width }
  })
})
const sourceCells = computed(() => rows.value.flatMap(row => row.items.map((item, i) => ({
  ...item, row: row.id, x: row.x + i * pitch.value,
}))))
const where = id => sourceCells.value.find(cell => cell.id === id)
const outerWidth = computed(() => {
  const last = rows.value[rows.value.length - 1]
  return last.x + last.width - props.labelWidth + innerPad + 6
})
const capacity = computed(() => Math.max(1, ...props.run.states.map(item => (item.result || []).length)))
const slotX = i => props.labelWidth + i * pitch.value

const cells = computed(() => sourceCells.value.map(cell => {
  const tested = state.value.tested?.[cell.id]
  return {
    ...cell,
    current: state.value.cursor?.item === cell.id,
    test: tested === undefined ? '' : tested ? 'True' : 'False',
    kept: tested === true, left: tested === false,
  }
}))
// A result item rests on its source cell, invisible, until it is added.
const added = computed(() => sourceCells.value.filter(cell => props.run.states.some(item => (item.result || []).includes(cell.id))).map(cell => {
  const at = (state.value.result || []).indexOf(cell.id)
  const last = state.value.result?.[state.value.result.length - 1]
  return {
    ...cell, shown: at >= 0, fresh: at >= 0 && cell.id === last && !state.value.bound,
    x: at >= 0 ? slotX(at) : cell.x, y: at >= 0 ? resultY.value : sourceY.value,
  }
}))
const itemTag = computed(() => {
  const states = props.run.states
  const cursor = state.value.cursor || states.slice(0, props.step).reverse().find(item => item.cursor)?.cursor
    || states.find(item => item.cursor)?.cursor
  return { shown: Boolean(state.value.cursor), x: cursor ? where(cursor.item).x : props.labelWidth }
})
const rowTag = computed(() => {
  if (!nested.value) return null
  const states = props.run.states
  const cursor = state.value.cursor || states.slice(0, props.step).reverse().find(item => item.cursor)?.cursor
    || states.find(item => item.cursor)?.cursor
  const row = rows.value.find(item => item.id === cursor?.row) || rows.value[0]
  return { shown: Boolean(state.value.cursor), x: row.x, width: row.width }
})
const width = computed(() => Math.max(props.labelWidth + outerWidth.value, slotX(capacity.value)) + 4)
const height = computed(() => resultY.value + cellHeight + 4)
</script>

<template>
  <div class="mid-comp" :style="{ width: `${width}px`, height: `${height}px` }" :data-mid-step="step">
    <span class="label" :style="{ top: `${sourceY}px`, width: `${labelWidth - 18}px` }">{{ run.source.name }}</span>
    <span
      class="label result" :class="{ bound: state.bound, shown: state.list }"
      :style="{ top: `${resultY}px`, width: `${labelWidth - 18}px` }" data-mid-result-name
    >{{ state.bound ? run.result.name : 'new list' }}</span>

    <div
      v-if="nested" class="outer" :style="{ left: `${labelWidth}px`, top: `${sourceY - innerPad}px`, width: `${outerWidth}px`, height: `${cellHeight + 2 * innerPad}px` }"
    />
    <span
      v-for="row in (nested ? rows : [])" :key="row.id" class="inner"
      :class="{ current: state.cursor?.row === row.id }"
      :style="{ left: `${row.x - 4}px`, top: `${sourceY - 4}px`, width: `${row.width + 8}px`, height: `${cellHeight + 8}px` }" :data-mid-row="row.id"
    />
    <span
      v-for="cell in cells" :key="cell.id" class="cell" :class="{ current: cell.current, kept: cell.kept, left: cell.left }"
      :style="{ transform: `translate(${cell.x}px, ${sourceY}px)`, width: `${cellWidth}px` }" :data-mid-item="cell.id" data-mid-value
    >{{ cell.text }}</span>
    <span
      v-for="cell in cells" :key="`t-${cell.id}`" class="test" :class="{ shown: cell.test, kept: cell.kept, left: cell.left }"
      :style="{ left: `${cell.x}px`, top: `${testY}px`, width: `${cellWidth}px` }" :data-mid-test="cell.id"
    >{{ cell.test }}</span>

    <div class="list" :class="{ shown: state.list, bound: state.bound }" :style="{ left: `${labelWidth - 6}px`, top: `${resultY - 6}px`, width: `${capacity * pitch + 14}px`, height: `${cellHeight + 12}px` }" />
    <span
      v-for="cell in added" :key="`r-${cell.id}`" class="cell copy" :class="{ shown: cell.shown, fresh: cell.fresh }"
      :style="{ transform: `translate(${cell.x}px, ${cell.y}px)`, width: `${cellWidth}px` }" :data-mid-added="cell.id" :data-mid-shown="cell.shown"
    >{{ cell.text }}</span>

    <span
      v-if="rowTag" class="tag row-tag" :class="{ shown: rowTag.shown }"
      :style="{ transform: `translateX(${rowTag.x}px)`, width: `${rowTag.width}px` }" data-mid-row-tag
    >{{ run.variables.row }}</span>
    <span
      class="tag" :class="{ shown: itemTag.shown }"
      :style="{ transform: `translate(${itemTag.x}px, ${sourceY - 30}px)`, width: `${cellWidth}px` }" data-mid-item-tag
    >{{ run.variables.item }}</span>
  </div>
</template>

<style scoped>
.mid-comp { position: relative; font-family: 'IBM Plex Mono', monospace; }
.label { position: absolute; left: 0; height: 50px; display: flex; align-items: center; justify-content: flex-end; font: 600 19px 'IBM Plex Mono', monospace; color: var(--ds-accent); white-space: nowrap; }
.label.result { font-weight: 400; font-size: 16px; color: var(--ds-muted); opacity: 0; transition: opacity 300ms ease, color 300ms ease; }
.label.result.shown { opacity: 1; }
.label.result.bound { font-weight: 600; font-size: 19px; color: var(--ds-accent); }
.outer { position: absolute; box-sizing: border-box; border: 2px solid #c3d3e3; border-radius: 8px; }
.inner {
  position: absolute; box-sizing: border-box; border: 2px solid transparent; border-radius: 6px;
  transition: border-color 300ms ease, background-color 300ms ease;
}
.inner.current { border-color: var(--ds-select); background: var(--ds-select-soft); }
.cell {
  position: absolute; left: 0; top: 0; box-sizing: border-box; height: 50px;
  display: flex; align-items: center; justify-content: center;
  border: 2px solid var(--ds-line); background: white; color: var(--ds-ink); font-size: 19px; white-space: nowrap;
  transition: transform var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease), background-color 300ms ease, border-color 300ms ease, color 300ms ease;
}
.cell.kept { background: var(--ds-panel); border-color: var(--ds-accent); }
.cell.left { border-style: dashed; color: var(--ds-muted); background: transparent; }
.cell.current { z-index: 1; border-width: 3px; border-color: var(--ds-select); box-shadow: 0 0 0 4px var(--ds-select-soft); }
.cell.copy { opacity: 0; z-index: 2; }
.cell.copy.shown { opacity: 1; }
.cell.copy.fresh { border-color: var(--ds-select); background: var(--ds-select-soft); }
.test { position: absolute; text-align: center; font-size: 14px; letter-spacing: .04em; opacity: 0; transition: opacity 300ms ease; }
.test.shown { opacity: 1; }
.test.kept { color: var(--ds-accent); }
.test.left { color: var(--ds-muted); }
.list {
  position: absolute; box-sizing: border-box; border: 2px dashed #c3d3e3; border-radius: 8px;
  opacity: 0; transition: opacity 300ms ease, border-color 300ms ease;
}
.list.shown { opacity: 1; }
.list.bound { border-style: solid; }
.tag {
  position: absolute; left: 0; top: 0; height: 26px; display: flex; align-items: flex-start; justify-content: center;
  font: 600 17px/20px 'IBM Plex Mono', monospace; color: var(--ds-select);
  opacity: 0; transition: transform var(--ds-time) var(--ds-ease), width var(--ds-time) var(--ds-ease), opacity 300ms ease;
}
.tag::after { content: ''; position: absolute; left: 50%; bottom: 0; margin-left: -6px; border: 6px solid transparent; border-top: 7px solid var(--ds-select); border-bottom: 0; }
.tag.shown { opacity: 1; }
.row-tag { height: 24px; border-bottom: 2px solid var(--ds-select); }
.row-tag::after { display: none; }
@media (prefers-reduced-motion: reduce) {
  .label, .inner, .cell, .test, .list, .tag { transition: none; }
}
</style>
