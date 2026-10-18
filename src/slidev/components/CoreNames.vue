<script setup>
// Names and the objects they refer to, for the native slides of modules 02 and
// 05. Each frame (a namespace, or one function call) lists its names, and each
// name has an arrow to one object. Every frame, name and object the run ever
// shows has a fixed place, so a step moves arrows, shows or hides rows and
// changes objects; nothing else shifts. Moving back replays the step in reverse.
//
// run.frames : [{ id, label }], top to bottom
// run.order : optional object ids, top to bottom (default : first appearance)
// direction 'row' puts the objects in one row below the frames, each arrow
//   ending on top of its object, for a name that walks along a series of values
// state.names : { frameId: { name: objectId | null } }; a frame shows while it
//   has an entry; a null reference is a note row, such as `global y`
// state.objects : { objectId: { type, value } | { type, items: [...] } }; an
//   object no shown name refers to is drawn dashed, for the step it lost its name
// state.active : ['frameId.name', ...], the names the current line uses
// state.mark : { object, index?, tone? }, or a list of them : the object (or
//   list item) just made or changed; tone 'select' (default) or 'change'
import { computed, useId } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
  frameWidth: { type: Number, default: 230 },
  gap: { type: Number, default: 120 },
  cellWidth: { type: Number, default: 58 },
  direction: { type: String, default: 'column' },
  pitch: { type: Number, default: 92 },
})
const markerPrefix = `core-${useId()}`
const top = 4
const rowHeight = 44
const frameHead = 32
const framePad = 10
const frameGap = 18
const objectHeight = 46
const objectPitch = 76
const tagHeight = 22
const state = computed(() => props.run.states[props.step])

function firstSeen(pick) {
  const seen = []
  for (const item of props.run.states) for (const key of pick(item)) if (!seen.includes(key)) seen.push(key)
  return seen
}
// Fixed geometry, from every state of the run.
const frameRows = computed(() => Object.fromEntries(props.run.frames.map(frame =>
  [frame.id, firstSeen(item => Object.keys(item.names[frame.id] || {}))])))
const frameTops = computed(() => {
  let y = top
  return Object.fromEntries(props.run.frames.map(frame => {
    const at = y
    y += frameHead + frameRows.value[frame.id].length * rowHeight + framePad + frameGap
    return [frame.id, at]
  }))
})
const objectIds = computed(() => props.run.order || firstSeen(item => Object.keys(item.objects)))
const framesBottom = computed(() => Math.max(...props.run.frames.map(frame =>
  frameTops.value[frame.id] + frameHead + frameRows.value[frame.id].length * rowHeight + framePad)))
const inRow = computed(() => props.direction === 'row')
const objectX = computed(() => props.frameWidth + props.gap)
function place(id) {
  const i = objectIds.value.indexOf(id)
  return inRow.value
    ? { x: objectX.value + i * props.pitch, y: framesBottom.value + 40 + tagHeight }
    : { x: objectX.value, y: top + tagHeight + i * objectPitch }
}
const height = computed(() => (inRow.value
  ? framesBottom.value + 40 + tagHeight + objectHeight + tagHeight
  : Math.max(framesBottom.value, top + tagHeight + objectIds.value.length * objectPitch - (objectPitch - objectHeight))) + 4)

// The value an object shows : now, or the nearest state that has it, so a
// hidden object fades out (or in) with the content it had.
function objectValue(id) {
  if (state.value.objects[id]) return state.value.objects[id]
  const states = props.run.states
  for (let i = props.step - 1; i >= 0; i--) if (states[i].objects[id]) return states[i].objects[id]
  return states.find(item => item.objects[id]).objects[id]
}
function reference(frame, name) {
  const now = state.value.names[frame]
  if (now && name in now) return now[name]
  const states = props.run.states
  for (let i = props.step - 1; i >= 0; i--) if (states[i].names[frame] && name in states[i].names[frame]) return states[i].names[frame][name]
  return states.find(item => item.names[frame] && name in item.names[frame]).names[frame][name]
}

const frames = computed(() => props.run.frames.map(frame => {
  const now = state.value.names[frame.id]
  return {
    ...frame,
    shown: Boolean(now),
    top: frameTops.value[frame.id],
    height: frameHead + frameRows.value[frame.id].length * rowHeight + framePad,
    rows: frameRows.value[frame.id].map((name, i) => ({
      name, i, note: reference(frame.id, name) === null, ret: name === 'return',
      shown: Boolean(now && name in now),
      active: (state.value.active || []).includes(`${frame.id}.${name}`),
    })),
  }
}))
const referenced = computed(() => new Set(Object.values(state.value.names).flatMap(names => Object.values(names))))
const arrows = computed(() => frames.value.flatMap(frame => frame.rows.filter(row => !row.note).map(row => {
  const target = reference(frame.id, row.name)
  const y0 = frame.top + frameHead + row.i * rowHeight + rowHeight / 2
  const at = place(target)
  const x0 = props.frameWidth - 18
  const bend = Math.min(70, props.gap / 2)
  if (inRow.value) {
    const x1 = at.x + props.cellWidth / 2
    const y1 = at.y - 3
    return {
      key: `${frame.id}.${row.name}`, active: row.active, shown: frame.shown && row.shown,
      path: `M ${x0} ${y0} C ${x0 + bend} ${y0}, ${x1} ${y1 - 70}, ${x1} ${y1}`,
    }
  }
  const x1 = at.x - 3
  const y1 = at.y + objectHeight / 2
  return {
    key: `${frame.id}.${row.name}`, active: row.active, shown: frame.shown && row.shown,
    path: `M ${x0} ${y0} C ${x0 + bend} ${y0}, ${x1 - bend} ${y1}, ${x1} ${y1}`,
  }
})))
const objects = computed(() => objectIds.value.map(id => {
  const value = objectValue(id)
  const present = Boolean(state.value.objects[id])
  const mark = [].concat(state.value.mark || []).find(item => item.object === id) || null
  return {
    id, ...value, ...place(id),
    status: !present ? 'hidden' : referenced.value.has(id) ? 'present' : 'orphan',
    tone: mark && mark.index === undefined ? (mark.tone || 'select') : '',
    markIndex: mark && mark.index !== undefined ? mark.index : -1,
    markTone: mark?.tone || 'select',
  }
}))
</script>

<template>
  <div class="core-names" :style="{ height: `${height}px` }" :data-core-step="step">
    <div
      v-for="frame in frames" :key="frame.id" class="frame" :class="{ shown: frame.shown }"
      :style="{ top: `${frame.top}px`, width: `${frameWidth}px`, height: `${frame.height}px` }" :data-core-frame="frame.id"
    >
      <header>{{ frame.label }}</header>
      <div
        v-for="row in frame.rows" :key="row.name" class="row" :class="{ shown: row.shown, on: row.active, note: row.note, ret: row.ret }"
        :style="{ top: `${frameHead + row.i * rowHeight}px` }" :data-core-name="row.name"
      >
        <span class="label">{{ row.ret ? 'return value' : row.name }}</span><i v-if="!row.note" />
      </div>
    </div>
    <svg class="arrows" :height="height" aria-hidden="true">
      <defs>
        <marker :id="`${markerPrefix}-head`" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" class="head" /></marker>
        <marker :id="`${markerPrefix}-head-on`" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" class="head on" /></marker>
      </defs>
      <path
        v-for="arrow in arrows" :key="arrow.key" :d="arrow.path" class="ref" :class="{ on: arrow.active, shown: arrow.shown }"
        :marker-end="`url(#${markerPrefix}-head${arrow.active ? '-on' : ''})`" :data-core-ref="arrow.key"
      />
    </svg>
    <div
      v-for="object in objects" :key="object.id" class="object" :class="[object.status, object.tone]"
      :style="{ top: `${object.y}px`, left: `${object.x}px` }" :data-core-object="object.id" :data-core-status="object.status"
    >
      <span class="tag" :class="{ below: inRow }">{{ object.type }}</span>
      <TransitionGroup v-if="object.items" tag="div" name="core-cell" class="cells">
        <span
          v-for="(item, i) in object.items" :key="i" class="cell" :class="{ [object.markTone]: i === object.markIndex }"
          :style="{ width: `${cellWidth}px` }" data-core-value
        >{{ item }}</span>
      </TransitionGroup>
      <span v-else class="box" :style="inRow ? { width: `${cellWidth}px` } : null" data-core-value>{{ object.value }}</span>
    </div>
  </div>
</template>

<style scoped>
.core-names { position: relative; font-family: 'IBM Plex Mono', monospace; }
.frame {
  position: absolute; left: 0; box-sizing: border-box; border: 2px solid #c3d3e3; border-radius: 8px; background: #f7f9fc;
  opacity: 0; transform: translateY(12px); transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease);
}
.frame.shown { opacity: 1; transform: none; }
.frame header { height: 30px; padding: 0 12px; display: flex; align-items: center; font: 600 13px 'IBM Plex Mono', monospace; letter-spacing: .1em; color: var(--ds-muted); }
.row {
  position: absolute; left: 8px; right: 8px; height: 38px; box-sizing: border-box; border: 2px solid var(--ds-line); border-radius: 5px; background: white;
  display: flex; align-items: center; padding: 0 12px; font-size: 20px; color: var(--ds-ink);
  opacity: 0; transform: translateX(-10px);
  transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease), background-color 300ms ease, border-color 300ms ease;
}
.row.shown { opacity: 1; transform: none; }
.row .label { flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.row i { width: 12px; height: 12px; border-radius: 50%; background: #8fb0cf; transition: background-color 300ms ease; }
.row.on { border-color: var(--ds-select); background: var(--ds-select-soft); }
.row.on i { background: var(--ds-select); }
.row.note { border-style: dashed; background: transparent; font-size: 17px; color: var(--ds-muted); }
.row.ret { font-size: 16px; font-style: italic; }
.arrows { position: absolute; left: 0; top: 0; width: 100%; overflow: visible; pointer-events: none; }
.ref { fill: none; stroke: #8fb0cf; stroke-width: 2.5; opacity: 0; transition: stroke 300ms ease, opacity var(--ds-time) var(--ds-ease), d var(--ds-time) var(--ds-ease); }
.ref.shown { opacity: 1; }
.ref.on { stroke: var(--ds-select); stroke-width: 3; }
.head { fill: #8fb0cf; }
.head.on { fill: var(--ds-select); }
.object { position: absolute; height: 46px; display: flex; transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease); }
.object .tag { position: absolute; left: 2px; top: -21px; font-size: 13px; letter-spacing: .06em; color: var(--ds-muted); }
.object .tag.below { top: 50px; left: 0; right: 0; text-align: center; }
.object .cells { display: flex; }
.box, .cell {
  box-sizing: border-box; height: 46px; display: flex; align-items: center; justify-content: center;
  border: 2px solid var(--ds-line); background: white; font-size: 20px; color: var(--ds-ink); white-space: nowrap;
  transition: background-color 300ms ease, border-color 300ms ease, color 300ms ease;
}
.box { min-width: 64px; padding: 0 14px; border-radius: 5px; }
.cell { margin-right: -2px; }
.object.select .box, .cell.select { position: relative; z-index: 1; border-color: var(--ds-select); background: var(--ds-select-soft); }
.object.change .box, .cell.change { position: relative; z-index: 1; border-color: var(--ds-change); background: var(--ds-change-soft); }
.object.hidden { opacity: 0; transform: translateX(14px); }
.object.orphan { opacity: .55; }
.object.orphan .box, .object.orphan .cell { border-style: dashed; color: var(--ds-muted); }
.core-cell-enter-active, .core-cell-leave-active { transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease); }
.core-cell-enter-from, .core-cell-leave-to { opacity: 0; transform: translateY(-16px); }
@media (prefers-reduced-motion: reduce) {
  .frame, .row, .row i, .ref, .object, .box, .cell, .core-cell-enter-active, .core-cell-leave-active { transition: none; }
}
</style>
