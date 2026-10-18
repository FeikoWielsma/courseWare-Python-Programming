<script setup>
// A class and its instances, for the native slides of module 11. Each object
// (the class, or one instance) is a box listing its own attributes; an arrow
// from each instance leads to its class. Reading an attribute lights the place
// Python finds it : on the object, or through the arrow on the class. Every
// box and attribute has a fixed place, so a step only shows rows, changes
// values and lights lookups. Moving back replays the step in reverse.
//
// run.boxes : [{ id, label, tag, x, y, width }], explicit geometry
// run.links : [{ from, to }], instance to class; drawn sideways when the boxes
//   are side by side, downwards when one is below the other
// state.attrs : { boxId: { name: value } }; a box shows once it has an entry
// state.read : [{ box, attr, via? }], the attributes the current line reads;
//   via is the instance the lookup started from, when it is found on the class
// state.mark : [{ box, attr, tone }], attributes made or changed; tone
//   'select' (made), 'change' (changed) or 'remove' (refused)
// state.note : { box, attr, text, tone? }, a note beside an attribute, such as
//   the value a property's getter computed
// state.active : [boxId, ...], the objects the current line uses
import { computed, useId } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
})
const markerPrefix = `stateful-${useId()}`
const head = 32
const rowHeight = 38
const pad = 8
const state = computed(() => props.run.states[props.step])

function firstSeen(boxId) {
  const seen = []
  for (const item of props.run.states) for (const name of Object.keys(item.attrs[boxId] || {})) if (!seen.includes(name)) seen.push(name)
  return seen
}
const slots = computed(() => Object.fromEntries(props.run.boxes.map(box => [box.id, firstSeen(box.id)])))
const boxHeight = id => head + slots.value[id].length * rowHeight + pad
const rowTop = (box, attr) => box.y + head + slots.value[box.id].indexOf(attr) * rowHeight
const height = computed(() => Math.max(...props.run.boxes.map(box => box.y + boxHeight(box.id))) + 4)
// The value an attribute shows : now, or the nearest state that has it, so a
// row fades out (or in) with the value it had.
function value(boxId, attr) {
  const has = item => item.attrs[boxId] && attr in item.attrs[boxId]
  if (has(state.value)) return state.value.attrs[boxId][attr]
  const states = props.run.states
  for (let i = props.step - 1; i >= 0; i--) if (has(states[i])) return states[i].attrs[boxId][attr]
  return states.find(has).attrs[boxId][attr]
}
const reads = computed(() => state.value.read || [])
const boxes = computed(() => props.run.boxes.map(box => {
  const now = state.value.attrs[box.id]
  return {
    ...box,
    shown: Boolean(now),
    height: boxHeight(box.id),
    on: (state.value.active || []).includes(box.id),
    rows: slots.value[box.id].map((attr, i) => {
      const mark = (state.value.mark || []).find(item => item.box === box.id && item.attr === attr)
      const read = reads.value.some(item => item.box === box.id && item.attr === attr)
      return {
        attr, i, value: value(box.id, attr),
        shown: Boolean(now && attr in now),
        tone: mark ? mark.tone || 'select' : read ? 'select' : '',
      }
    }),
  }
}))
const links = computed(() => (props.run.links || []).map(link => {
  const from = props.run.boxes.find(box => box.id === link.from)
  const to = props.run.boxes.find(box => box.id === link.to)
  const on = reads.value.some(item => item.via === link.from && item.box === link.to)
  let path, label
  if (to.y >= from.y + boxHeight(from.id)) {
    const x = Math.min(Math.max(from.x + from.width / 2, to.x + 20), to.x + to.width - 20)
    const y0 = from.y + boxHeight(from.id) + 2
    path = `M ${x} ${y0} L ${x} ${to.y - 4}`
    label = { x: x + 10, y: (y0 + to.y) / 2 - 8, anchor: 'start' }
  } else {
    const y = Math.min(from.y, to.y) + head / 2 + 2
    const right = to.x > from.x
    const x0 = right ? from.x + from.width + 2 : from.x - 2
    const x1 = right ? to.x - 4 : to.x + to.width + 4
    path = `M ${x0} ${y} L ${x1} ${y}`
    label = { x: (x0 + x1) / 2, y: y - 18, anchor: 'middle' }
  }
  return {
    key: `${link.from}-${link.to}`, path, label, on,
    shown: Boolean(state.value.attrs[link.from] && state.value.attrs[link.to]),
  }
}))
const note = computed(() => {
  const now = state.value.note
  const last = now || [...props.run.states.slice(0, props.step)].reverse().find(item => item.note)?.note
    || props.run.states.find(item => item.note)?.note
  if (!last) return null
  const box = props.run.boxes.find(item => item.id === last.box)
  return { ...last, shown: Boolean(now), left: box.x + box.width + 16, top: rowTop(box, last.attr) + 4 }
})
</script>

<template>
  <div class="stateful-objects" :style="{ height: `${height}px` }" :data-objects-step="step">
    <svg class="links" :height="height" aria-hidden="true">
      <defs>
        <marker :id="`${markerPrefix}-head`" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" class="head" /></marker>
        <marker :id="`${markerPrefix}-head-on`" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" class="head on" /></marker>
      </defs>
      <g v-for="link in links" :key="link.key" class="link" :class="{ shown: link.shown, on: link.on }" :data-objects-link="link.key">
        <path :d="link.path" :marker-end="`url(#${markerPrefix}-head${link.on ? '-on' : ''})`" />
        <text :x="link.label.x" :y="link.label.y" :text-anchor="link.label.anchor" dominant-baseline="hanging">class</text>
      </g>
    </svg>
    <div
      v-for="box in boxes" :key="box.id" class="box" :class="{ shown: box.shown, on: box.on, cls: box.tag === 'class' }"
      :style="{ left: `${box.x}px`, top: `${box.y}px`, width: `${box.width}px`, height: `${box.height}px` }" :data-objects-box="box.id"
    >
      <header><span class="label">{{ box.label }}</span><span class="tag">{{ box.tag }}</span></header>
      <div
        v-for="row in box.rows" :key="row.attr" class="row" :class="[row.tone, { shown: row.shown }]"
        :style="{ top: `${head + row.i * rowHeight}px` }" :data-objects-attr="`${box.id}.${row.attr}`"
      ><span class="attr">{{ row.attr }}</span><span class="value">{{ row.value }}</span></div>
    </div>
    <div
      v-if="note" class="note" :class="[note.tone || 'select', { shown: note.shown }]"
      :style="{ left: `${note.left}px`, top: `${note.top}px` }" data-objects-note
    >{{ note.text }}</div>
  </div>
</template>

<style scoped>
.stateful-objects { position: relative; font-family: 'IBM Plex Mono', monospace; }
.links { position: absolute; left: 0; top: 0; width: 100%; overflow: visible; pointer-events: none; }
.link { opacity: 0; transition: opacity var(--ds-time) var(--ds-ease); }
.link.shown { opacity: 1; }
.link path { fill: none; stroke: #8fb0cf; stroke-width: 2.5; transition: stroke 300ms ease; }
.link text { font: 13px 'IBM Plex Mono', monospace; letter-spacing: .06em; fill: var(--ds-muted); transition: fill 300ms ease; }
.link.on path { stroke: var(--ds-select); stroke-width: 3; }
.link.on text { fill: var(--ds-select); }
.head { fill: #8fb0cf; }
.head.on { fill: var(--ds-select); }
.box {
  position: absolute; box-sizing: border-box; border: 2px solid #c3d3e3; border-radius: 8px; background: #f7f9fc;
  opacity: 0; transform: translateY(12px);
  transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease), border-color 300ms ease;
}
.box.shown { opacity: 1; transform: none; }
.box.on { border-color: var(--ds-select); }
.box.cls { background: #eef3f9; }
.box header { height: 30px; padding: 0 12px; display: flex; align-items: center; justify-content: space-between; gap: 10px; }
.box .label { font-size: 20px; color: var(--ds-ink); }
.box .tag { font-size: 13px; letter-spacing: .06em; color: var(--ds-muted); white-space: nowrap; }
.row {
  position: absolute; left: 8px; right: 8px; height: 34px; box-sizing: border-box; border: 2px solid var(--ds-line); border-radius: 5px; background: white;
  display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 0 10px; font-size: 16px; color: var(--ds-ink); white-space: nowrap;
  opacity: 0; transform: translateX(-10px);
  transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease), background-color 300ms ease, border-color 300ms ease;
}
.row.shown { opacity: 1; transform: none; }
.row .value { color: var(--ds-ink); }
.row.select { border-color: var(--ds-select); background: var(--ds-select-soft); }
.row.change { border-color: var(--ds-change); background: var(--ds-change-soft); }
.row.remove { border-color: var(--ds-remove); background: var(--ds-remove-soft); }
.note {
  position: absolute; height: 30px; display: flex; align-items: center; padding: 0 12px; border-radius: 15px; font-size: 16px; white-space: nowrap;
  opacity: 0; transform: translateX(-8px); transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease);
}
.note.shown { opacity: 1; transform: none; }
.note.select { background: var(--ds-select-soft); color: var(--ds-select); border: 2px solid var(--ds-select); }
.note.remove { background: var(--ds-remove-soft); color: var(--ds-remove); border: 2px solid var(--ds-remove); }
@media (prefers-reduced-motion: reduce) {
  .link, .link path, .link text, .box, .row, .note { transition: none; }
}
</style>
