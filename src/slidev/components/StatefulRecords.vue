<script setup>
// Names and the rows of one table or query result, for the native slides of
// module 10. Each name is a labelled box with a short description of its
// value (a connection, a cursor, a number); a name can also hold one row,
// which then moves out of its slot in the table into the name's box. Rows
// keep their identity : a fetched row is the same object in the table slot and
// in the name. Geometry is explicit in the run, so nothing shifts between
// steps. Moving back replays the step in reverse.
//
// run.names : [{ id, x, y, width }], the boxes of the names
// run.table : { x, y, label, columns: [{ text, width }] }
// run.rows : [{ id, cells: [...] }], every row the table or result ever holds
// state.names : { nameId: text | { row: rowId } }; a name shows once it has
//   an entry
// state.badges : { nameId: text }, a note inside the box, such as an open
//   transaction
// state.table : true once the table or result exists
// state.rows : { rowId: 'result' | 'pending' | 'committed' | 'gone' }; a row a
//   name holds is drawn in that name's box; 'gone' leaves an empty slot
// state.next : the slot boundary a cursor reads next, or null
// state.active : [nameId, ...], the names the current line uses
// state.mark : [rowId, ...], the rows the current line made or changed
import { computed } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
  labelWidth: { type: Number, default: 56 },
})
const boxHeight = 46
const rowHeight = 40
const tableLabel = 22
const tableHead = 30
const state = computed(() => props.run.states[props.step])
const table = computed(() => props.run.table)
const rowWidth = computed(() => table.value.columns.reduce((sum, column) => sum + column.width, 0))
const slotTop = i => table.value.y + tableLabel + tableHead + i * rowHeight
const height = computed(() => Math.max(
  slotTop(props.run.rows.length),
  ...props.run.names.map(name => name.y + boxHeight),
) + 4)

function lastKnown(pick) {
  const states = props.run.states
  const now = pick(state.value)
  if (now !== undefined) return now
  for (let i = props.step - 1; i >= 0; i--) { const value = pick(states[i]); if (value !== undefined) return value }
  for (const item of states) { const value = pick(item); if (value !== undefined) return value }
  return undefined
}
const names = computed(() => props.run.names.map(name => {
  const value = lastKnown(item => item.names?.[name.id])
  return {
    ...name,
    shown: state.value.names?.[name.id] !== undefined,
    text: typeof value === 'string' ? value : '',
    badge: state.value.badges?.[name.id] || '',
    on: (state.value.active || []).includes(name.id),
  }
}))
function holderIn(item, rowId) {
  const entry = Object.entries(item.names || {}).find(([, value]) => value && typeof value === 'object' && value.row === rowId)
  return entry && props.run.names.find(name => name.id === entry[0])
}
// Where a row is drawn in a state : in the box of the name that holds it, in
// its table slot, or nowhere (not there yet, or gone).
function placeIn(item, row, i) {
  const name = holderIn(item, row.id)
  if (name) return { left: name.x + props.labelWidth + 3, top: name.y + (boxHeight - rowHeight) / 2, held: true }
  const status = item.rows?.[row.id]
  if (status && status !== 'gone') return { left: table.value.x, top: slotTop(i), held: false }
  return null
}
// A row that is not there fades out (or in) where it last was, or will be.
function nearest(row, i) {
  const states = props.run.states
  for (let s = props.step - 1; s >= 0; s--) { const at = placeIn(states[s], row, i); if (at) return at }
  for (const item of states) { const at = placeIn(item, row, i); if (at) return at }
  return { left: table.value.x, top: slotTop(i) }
}
const rows = computed(() => props.run.rows.map((row, i) => {
  const status = state.value.rows?.[row.id]
  const at = placeIn(state.value, row, i)
  return {
    ...row, ...(at || nearest(row, i)),
    status: at?.held ? 'held' : at ? status : status === 'gone' ? 'gone' : 'hidden',
    empty: Boolean(at?.held) || status === 'gone',
    slotTop: slotTop(i),
    mark: (state.value.mark || []).includes(row.id),
  }
}))
const nextTop = computed(() => (state.value.next === null || state.value.next === undefined
  ? null : slotTop(state.value.next)))
const lastNext = computed(() => lastKnown(item => (item.next === null ? undefined : item.next)))
</script>

<template>
  <div class="stateful-records" :style="{ height: `${height}px` }" :data-records-step="step">
    <div
      v-for="name in names" :key="name.id" class="name" :class="{ shown: name.shown, on: name.on }"
      :style="{ left: `${name.x}px`, top: `${name.y}px` }" :data-records-name="name.id"
    >
      <span class="label" :style="{ width: `${labelWidth}px` }">{{ name.id }}</span>
      <span class="box" :style="{ width: `${name.width}px` }"><span class="text">{{ name.text }}</span><span v-if="name.badge" class="badge">{{ name.badge }}</span></span>
    </div>
    <div class="table" :class="{ shown: state.table }" :style="{ left: `${table.x}px`, top: `${table.y}px`, width: `${rowWidth}px` }">
      <div class="table-label">{{ table.label }}</div>
      <div class="head"><span v-for="column in table.columns" :key="column.text" :style="{ width: `${column.width}px` }">{{ column.text }}</span></div>
    </div>
    <div
      v-for="row in rows" :key="`slot-${row.id}`" class="slot" :class="{ shown: state.table && row.empty }"
      :style="{ left: `${table.x}px`, top: `${row.slotTop}px`, width: `${rowWidth + 2}px` }"
    />
    <div
      class="next" :class="{ shown: state.table && nextTop !== null }"
      :style="{ left: `${table.x - 64}px`, top: `${(nextTop ?? slotTop(lastNext ?? 0)) - 11}px` }" data-records-next
    >next</div>
    <div
      v-for="row in rows" :key="row.id" class="row" :class="[row.status, { mark: row.mark }]"
      :style="{ left: `${row.left}px`, top: `${row.top}px` }" :data-records-row="row.id" :data-records-status="row.status"
    >
      <span v-for="(cell, i) in row.cells" :key="i" class="cell" :style="{ width: `${table.columns[i].width + 2}px` }">{{ cell }}</span>
      <span v-if="row.status === 'pending'" class="tag">not committed</span>
    </div>
  </div>
</template>

<style scoped>
.stateful-records { position: relative; font-family: 'IBM Plex Mono', monospace; }
.name {
  position: absolute; height: 46px; display: flex; align-items: center; opacity: 0; transform: translateX(-10px);
  transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease);
}
.name.shown { opacity: 1; transform: none; }
.name .label { font-size: 20px; color: var(--ds-ink); }
.name .box {
  box-sizing: border-box; height: 46px; display: flex; align-items: center; gap: 10px; padding: 0 12px;
  border: 2px solid var(--ds-line); border-radius: 5px; background: white; font-size: 17px; color: var(--ds-ink); white-space: nowrap;
  transition: background-color 300ms ease, border-color 300ms ease;
}
.name .text { flex: 1; overflow: hidden; text-overflow: ellipsis; }
.name.on .box { border-color: var(--ds-select); background: var(--ds-select-soft); }
.badge { font-size: 12px; letter-spacing: .05em; padding: 2px 8px; border-radius: 10px; background: var(--ds-change); color: white; }
.table { position: absolute; opacity: 0; transition: opacity var(--ds-time) var(--ds-ease); }
.table.shown { opacity: 1; }
.table-label { height: 22px; font-size: 13px; letter-spacing: .06em; color: var(--ds-muted); white-space: nowrap; }
.head { display: flex; height: 30px; }
.head span { box-sizing: border-box; padding: 0 10px; display: flex; align-items: center; font: 600 15px 'IBM Plex Mono', monospace; color: var(--ds-muted); border-bottom: 2px solid #c3d3e3; }
.slot { position: absolute; height: 40px; box-sizing: border-box; border: 2px dashed #c3d3e3; border-radius: 4px; opacity: 0; transition: opacity var(--ds-time) var(--ds-ease); }
.slot.shown { opacity: 1; }
.next {
  position: absolute; width: 58px; height: 22px; display: flex; align-items: center; justify-content: flex-end; padding-right: 14px; box-sizing: border-box;
  font-size: 14px; color: var(--ds-select); opacity: 0; transition: top var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease);
}
.next::after { content: ''; position: absolute; right: 0; top: 4px; border: 7px solid transparent; border-left: 11px solid var(--ds-select); border-right: 0; }
.next.shown { opacity: 1; }
.row {
  position: absolute; display: flex; height: 40px; z-index: 1;
  transition: left var(--ds-time) var(--ds-ease), top var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease);
}
.cell {
  box-sizing: border-box; height: 40px; margin-right: -2px; padding: 0 10px; display: flex; align-items: center;
  border: 2px solid var(--ds-line); background: white; font-size: 17px; color: var(--ds-ink); white-space: nowrap;
  transition: background-color 300ms ease, border-color 300ms ease;
}
.row.hidden, .row.gone { opacity: 0; }
.row.pending .cell { border-style: dashed; border-color: var(--ds-change); background: var(--ds-change-soft); }
.row.held .cell, .row.mark .cell { border-color: var(--ds-select); background: var(--ds-select-soft); }
.row .tag { position: absolute; left: calc(100% + 10px); top: 11px; font-size: 12px; letter-spacing: .05em; color: var(--ds-change); white-space: nowrap; }
@media (prefers-reduced-motion: reduce) {
  .name, .name .box, .table, .slot, .next, .row, .cell { transition: none; }
}
</style>
