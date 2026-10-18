<script setup>
// One file on disk and the file objects opened on it, for the native slides of
// module 09. The file's content is a row of cells; each file object is a box
// with its mode and its open or closed state. An open file object has a
// position, drawn as a marker between two cells. Characters a file object has
// written but not yet flushed sit in its buffer, in its own lane; flushing
// moves those same cells up into the file. Every cell has a fixed column, so a
// step only moves cells, markers and states. Moving back replays the step.
//
// run.file : { name }, the file on disk
// run.cells : ['o', 'n', ...], every character or byte the file ever holds;
//   a newline shows as \n
// run.handles : [{ id, mode }], one lane each, top to bottom
// state.disk : how many of run.cells are on disk (null : no file yet)
// state.buffer : { handle, count } | null, the cells after state.disk that
//   wait in that file object's buffer
// state.handles : { handleId: { status: 'open' | 'closed', position, label } };
//   a file object shows once it has an entry; position is a cell boundary,
//   label the text beside the marker (default : the name)
// state.read : { from, to } | null, the cells the current line read
// state.active : [handleId, ...], the file objects the current line uses
import { computed } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
  boxWidth: { type: Number, default: 200 },
  cellWidth: { type: Number, default: 50 },
})
const fileTop = 24
const cellHeight = 46
const laneTop = 100
const lanePitch = 74
const boxHeight = 56
const state = computed(() => props.run.states[props.step])
const x0 = computed(() => props.boxWidth + 40)
const laneOf = id => props.run.handles.findIndex(handle => handle.id === id)
const laneY = id => laneTop + laneOf(id) * lanePitch
const height = computed(() => laneTop + props.run.handles.length * lanePitch - (lanePitch - boxHeight) + 4)
const width = computed(() => x0.value + props.run.cells.length * props.cellWidth + 70)

// The nearest state that knows a file object : now, before or after, so a
// box fades out (or in) with the content it had.
function handleState(id) {
  const states = props.run.states
  if (state.value.handles[id]) return state.value.handles[id]
  for (let i = props.step - 1; i >= 0; i--) if (states[i].handles[id]) return states[i].handles[id]
  return states.find(item => item.handles[id]).handles[id]
}
const handles = computed(() => props.run.handles.map(handle => {
  const now = handleState(handle.id)
  return {
    ...handle, ...now, top: laneY(handle.id),
    shown: Boolean(state.value.handles[handle.id]),
    on: (state.value.active || []).includes(handle.id),
  }
}))
const markers = computed(() => handles.value.filter(handle => handle.position !== undefined).map(handle => ({
  id: handle.id,
  shown: handle.shown && handle.status === 'open',
  on: handle.on,
  left: x0.value + handle.position * props.cellWidth,
  height: handle.top + boxHeight / 2 - (fileTop + cellHeight),
  label: handle.label ?? handle.id,
})))
const exists = computed(() => state.value.disk !== null && state.value.disk !== undefined)
function placeIn(item, i) {
  const disk = item.disk || 0
  const buffer = item.buffer
  if (i < disk) return { where: 'disk', top: fileTop }
  if (buffer && i < disk + buffer.count) return { where: 'buffer', top: laneY(buffer.handle) + (boxHeight - cellHeight) / 2 }
  return null
}
// A cell that is not there now waits, invisible, where it last was (or will
// first be), so it fades in and out in place.
function nearest(i) {
  const states = props.run.states
  for (let s = props.step - 1; s >= 0; s--) { const at = placeIn(states[s], i); if (at) return at }
  for (const item of states) { const at = placeIn(item, i); if (at) return at }
  return { top: fileTop }
}
const cells = computed(() => props.run.cells.map((text, i) => {
  const at = placeIn(state.value, i)
  const read = Boolean(state.value.read) && i >= state.value.read.from && i < state.value.read.to
  // A newline is shown as Python writes it, whether the run holds the
  // character itself or its two-character escape.
  const shown = text === '\n' || text === '\\n' ? '\\n' : text
  return { key: i, text: shown, where: at ? at.where : 'none', read, left: x0.value + i * props.cellWidth, top: (at || nearest(i)).top }
}))
</script>

<template>
  <div class="stateful-file" :style="{ height: `${height}px`, width: `${width}px` }" :data-file-step="step">
    <div class="file-label" :class="{ shown: exists }" :style="{ left: `${x0}px` }">on disk · {{ run.file.name }}</div>
    <div class="file-name" :class="{ shown: exists }" :style="{ top: `${fileTop}px`, width: `${boxWidth}px` }">{{ run.file.name }}</div>
    <div
      class="file-track" :class="{ shown: exists, empty: exists && !state.disk }"
      :style="{ left: `${x0}px`, top: `${fileTop}px`, width: `${run.cells.length * cellWidth}px`, height: `${cellHeight}px` }"
      data-file-track
    ><span v-if="exists && !state.disk">empty file</span></div>
    <div
      v-for="handle in handles" :key="handle.id" class="handle" :class="{ shown: handle.shown, on: handle.on, closed: handle.status === 'closed' }"
      :style="{ top: `${handle.top}px`, width: `${boxWidth}px`, height: `${boxHeight}px` }" :data-file-handle="handle.id" :data-file-status="handle.status"
    >
      <span class="name">{{ handle.id }}</span>
      <span class="mode">mode '{{ handle.mode }}'</span>
      <span class="status">{{ handle.status }}</span>
    </div>
    <div
      v-for="handle in handles" :key="`buffer-${handle.id}`" class="buffer-tag"
      :class="{ shown: state.buffer && state.buffer.handle === handle.id && state.buffer.count > 0 }"
      :style="{ top: `${handle.top + boxHeight - 2}px`, left: `${x0}px` }"
    >{{ handle.id }} buffer, not on disk yet</div>
    <div
      v-for="marker in markers" :key="`marker-${marker.id}`" class="marker" :class="{ shown: marker.shown, on: marker.on }"
      :style="{ left: `${marker.left}px`, top: `${fileTop + cellHeight}px`, height: `${marker.height}px` }" :data-file-position="marker.id"
    ><span>{{ marker.label }}</span></div>
    <span
      v-for="cell in cells" :key="cell.key" class="cell" :class="[cell.where, { read: cell.read }]"
      :style="{ left: `${cell.left}px`, top: `${cell.top}px`, width: `${cellWidth + 2}px`, height: `${cellHeight}px` }" data-file-cell
    >{{ cell.text }}</span>
  </div>
</template>

<style scoped>
.stateful-file { position: relative; font-family: 'IBM Plex Mono', monospace; }
.file-label { position: absolute; top: 0; font-size: 13px; letter-spacing: .06em; color: var(--ds-muted); opacity: 0; transition: opacity var(--ds-time) var(--ds-ease); }
.file-name {
  position: absolute; left: 0; height: 46px; box-sizing: border-box; display: flex; align-items: center; justify-content: flex-end; padding-right: 4px;
  font-size: 18px; color: var(--ds-ink); opacity: 0; transition: opacity var(--ds-time) var(--ds-ease);
}
.file-label.shown, .file-name.shown { opacity: 1; }
.file-track {
  position: absolute; box-sizing: border-box; border: 2px solid transparent; border-radius: 5px; opacity: 0;
  display: flex; align-items: center; padding-left: 14px; font-size: 15px; color: var(--ds-muted);
  transition: opacity var(--ds-time) var(--ds-ease), border-color 300ms ease;
}
.file-track.shown { opacity: 1; }
.file-track.empty { border: 2px dashed var(--ds-line); }
.handle {
  position: absolute; left: 0; box-sizing: border-box; border: 2px solid var(--ds-line); border-radius: 6px; background: #f7f9fc;
  display: grid; grid-template: 'name status' 30px 'mode status' 18px / 1fr auto; padding: 2px 10px 4px 12px; column-gap: 8px;
  opacity: 0; transform: translateX(-10px);
  transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease), background-color 300ms ease, border-color 300ms ease;
}
.handle.shown { opacity: 1; transform: none; }
.handle.on { border-color: var(--ds-select); background: var(--ds-select-soft); }
.handle .name { grid-area: name; font-size: 20px; line-height: 30px; color: var(--ds-ink); }
.handle .mode { grid-area: mode; font-size: 13px; line-height: 18px; color: var(--ds-muted); }
.handle .status {
  grid-area: status; align-self: center; font-size: 13px; letter-spacing: .06em; padding: 2px 8px; border-radius: 10px;
  background: var(--ds-select); color: white; transition: background-color 300ms ease, color 300ms ease;
}
.handle.closed { border-style: dashed; background: transparent; }
.handle.closed .status { background: #dfe5ec; color: var(--ds-muted); }
.buffer-tag { position: absolute; font-size: 12px; letter-spacing: .06em; color: var(--ds-change); opacity: 0; transition: opacity var(--ds-time) var(--ds-ease); }
.buffer-tag.shown { opacity: 1; }
.marker {
  position: absolute; width: 0; border-left: 3px solid #8fb0cf; margin-left: -1.5px; opacity: 0;
  transition: left var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease), border-color 300ms ease;
}
.marker::before { content: ''; position: absolute; left: -8px; top: -2px; border: 6.5px solid transparent; border-bottom: 9px solid #8fb0cf; border-top: 0; transition: border-color 300ms ease; }
.marker span { position: absolute; left: 8px; bottom: -4px; font-size: 15px; white-space: nowrap; color: var(--ds-muted); transition: color 300ms ease; }
.marker.shown { opacity: 1; }
.marker.on { border-left-color: var(--ds-select); }
.marker.on::before { border-bottom-color: var(--ds-select); }
.marker.on span { color: var(--ds-select); }
.cell {
  position: absolute; box-sizing: border-box; display: flex; align-items: center; justify-content: center;
  border: 2px solid var(--ds-line); background: white; font-size: 20px; color: var(--ds-ink); white-space: pre;
  transition: top var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease), background-color 300ms ease, border-color 300ms ease;
}
.cell.buffer { border-style: dashed; border-color: var(--ds-change); background: var(--ds-change-soft); z-index: 1; }
.cell.none { opacity: 0; }
.cell.read { z-index: 1; border-color: var(--ds-select); background: var(--ds-select-soft); }
@media (prefers-reduced-motion: reduce) {
  .file-label, .file-name, .file-track, .handle, .handle .status, .buffer-tag, .marker, .marker::before, .marker span, .cell { transition: none; }
}
</style>
