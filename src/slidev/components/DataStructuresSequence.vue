<script setup>
// One list whose items keep their identity across the steps of a run. Every
// object the run ever holds is rendered once and placed by the current step :
// waiting to arrive, in its slot, just removed (a struck-through ghost under
// its old slot), returned by pop(), or gone. Moving back replays it in reverse.
import { computed } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
  // row : index labels above, as on the Accessing Lists slide
  // stack : index 0 at the bottom, the last item on top
  orientation: { type: String, default: 'row' },
  cellWidth: { type: Number, default: 124 },
  cellHeight: { type: Number, default: 58 },
})
const cellHeight = props.cellHeight
const left = 96
const capacity = computed(() => Math.max(...props.run.states.map(state => state.items.length)))
const state = computed(() => props.run.states[props.step])
const ids = computed(() => Object.keys(props.run.objects))

const slot = (index) => props.orientation === 'row'
  ? { x: left + index * (props.cellWidth - 2), y: 28 }
  : { x: left, y: 24 + (capacity.value - 1 - index) * (cellHeight - 2) }
const returnedSlot = computed(() => ({ x: left + props.cellWidth + (props.orientation === 'stack' ? 24 : 150), y: 24 }))

function placement(id) {
  const states = props.run.states
  const now = state.value
  const at = now.items.indexOf(id)
  if (at >= 0) return { status: 'present', ...slot(at) }
  if (now.returned === id) return { status: 'returned', ...returnedSlot.value }
  const seen = states.map(item => item.items.includes(id) || item.returned === id)
  const first = seen.indexOf(true)
  const last = seen.lastIndexOf(true)
  if (props.step < first) {
    const home = slot(states[first].items.indexOf(id))
    return { status: 'pending', x: home.x, y: home.y - (props.orientation === 'row' ? 34 : 70) }
  }
  const before = states[last]
  const home = before.returned === id ? returnedSlot.value : slot(before.items.indexOf(id))
  const ghost = props.orientation === 'row' && props.step === last + 1
  return { status: ghost ? 'ghost' : 'gone', x: home.x, y: home.y + (props.orientation === 'row' ? 92 : -30) }
}
const cells = computed(() => ids.value.map(id => {
  const place = placement(id)
  return {
    id, value: props.run.objects[id], ...place,
    tone: state.value.active === id ? (state.value.tone || 'select') : '',
    style: { transform: `translate(${place.x}px, ${place.y}px)`, width: `${props.cellWidth}px`, height: `${cellHeight}px` },
  }
}))
const hasGhost = computed(() => cells.value.some(cell => cell.status === 'ghost'))
const top = computed(() => state.value.items.length ? slot(state.value.items.length - 1) : null)
const wellHeight = computed(() => capacity.value * (cellHeight - 2) + 2)
</script>

<template>
  <div class="ds-sequence" :class="orientation" :style="{ height: orientation === 'row' ? '186px' : `${wellHeight + 64}px` }">
    <template v-if="orientation === 'row'">
      <span class="name" :style="{ top: '28px' }">{{ run.name }}</span>
      <span class="name removed" :class="{ shown: hasGhost }" style="top: 120px">removed</span>
      <span v-for="i in capacity" :key="`i${i}`" class="index" :class="{ shown: i <= state.items.length }" :style="{ left: `${slot(i - 1).x}px`, width: `${cellWidth}px` }">{{ i - 1 }}</span>
    </template>
    <template v-else>
      <span class="name" :style="{ top: '0px', left: `${left}px`, height: '24px' }">{{ run.name }}</span>
      <div class="well" :style="{ left: `${left - 8}px`, width: `${cellWidth + 16}px`, height: `${wellHeight + 8}px` }" />
      <span v-for="i in capacity" :key="`i${i}`" class="index side" :class="{ shown: i <= state.items.length }" :style="{ top: `${slot(i - 1).y}px`, left: `${left - 48}px`, height: `${cellHeight}px` }">{{ i - 1 }}</span>
      <span class="top-mark" :class="{ shown: top }" :style="{ transform: `translateY(${top ? top.y : 24}px)`, left: `${left + cellWidth + 14}px`, height: `${cellHeight}px` }">&#8592; top</span>
      <span class="returned-label" :class="{ shown: state.returned }" :style="{ left: `${returnedSlot.x}px`, top: '0px' }">returned</span>
    </template>
    <div
      v-for="cell in cells" :key="cell.id" class="cell" :class="[cell.status, cell.tone]" :style="cell.style"
      :data-ds-item="cell.id" :data-ds-status="cell.status" data-ds-value
    >{{ cell.value }}</div>
  </div>
</template>

<style scoped>
.ds-sequence { position: relative; font-family: 'IBM Plex Mono', monospace; }
.name { position: absolute; left: 0; height: 58px; display: flex; align-items: center; font: 600 18px 'IBM Plex Mono', monospace; color: var(--ds-accent); }
.name.removed { color: var(--ds-remove); font-weight: 400; font-size: 15px; opacity: 0; transition: opacity 300ms ease; }
.name.removed.shown { opacity: 1; }
.index { position: absolute; top: 0; text-align: center; font-size: 17px; line-height: 22px; color: var(--ds-muted); opacity: 0; transition: opacity 300ms ease; }
.index.side { width: 36px; height: 58px; display: flex; align-items: center; justify-content: flex-end; }
.index.shown { opacity: 1; }
.cell {
  position: absolute; left: 0; top: 0; box-sizing: border-box; height: 58px;
  display: flex; align-items: center; justify-content: center;
  border: 2px solid var(--ds-line); background: white; color: var(--ds-ink); font-size: 20px; white-space: nowrap;
  transition: transform var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease), background-color 300ms ease, border-color 300ms ease, color 300ms ease;
  will-change: transform;
}
.stack .cell { font-size: 24px; }
.cell.present.select, .cell.returned { z-index: 1; border-color: var(--ds-select); background: var(--ds-select-soft); }
.cell.present.change { z-index: 1; border-color: var(--ds-change); background: var(--ds-change-soft); }
.cell.pending { opacity: 0; }
.cell.ghost { opacity: .75; border-style: dashed; border-color: var(--ds-remove); background: var(--ds-remove-soft); color: var(--ds-remove); text-decoration: line-through; }
.cell.gone { opacity: 0; border-color: var(--ds-remove); background: var(--ds-remove-soft); }
.well { position: absolute; top: 20px; box-sizing: border-box; border: 2px solid #c3d3e3; border-top: 0; border-radius: 0 0 8px 8px; }
.top-mark { position: absolute; top: 0; height: 58px; display: flex; align-items: center; font-size: 17px; color: var(--ds-select); opacity: 0; transition: transform var(--ds-time) var(--ds-ease), opacity 300ms ease; }
.top-mark.shown { opacity: 1; }
.returned-label { position: absolute; font-size: 15px; color: var(--ds-select); opacity: 0; transition: opacity 300ms ease; }
.returned-label.shown { opacity: 1; }
@media (prefers-reduced-motion: reduce) {
  .cell, .index, .name.removed, .top-mark, .returned-label { transition: none; }
}
</style>
