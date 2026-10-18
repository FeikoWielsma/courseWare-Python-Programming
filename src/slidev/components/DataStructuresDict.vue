<script setup>
// A dictionary as rows of key and value, in insertion order. A row keeps its
// identity, and its place, while its value changes; the replaced value and a
// deleted row stay visible, struck through, for the step that removed them.
import { computed } from 'vue'

const props = defineProps({ run: { type: Object, required: true }, step: { type: Number, required: true } })
const rowHeight = 50
const keyWidth = 190
const valueWidth = 170
const top = 64
const capacity = computed(() => Math.max(...props.run.states.map(state => state.rows.length)))
const ghostTop = computed(() => top + capacity.value * (rowHeight - 2) + 32)
const state = computed(() => props.run.states[props.step])
const seen = (id) => props.run.states.map(item => item.rows.some(row => row.id === id))

const rows = computed(() => {
  const ids = [...new Set(props.run.states.flatMap(item => item.rows.map(row => row.id)))]
  return ids.map(id => {
    const at = state.value.rows.findIndex(row => row.id === id)
    const appears = seen(id)
    const first = appears.indexOf(true)
    const last = appears.lastIndexOf(true)
    const home = (index) => top + index * (rowHeight - 2)
    let status = 'present'
    let y = at >= 0 ? home(at) : 0
    let row = state.value.rows[at]
    if (at < 0 && props.step < first) {
      status = 'pending'
      row = props.run.states[first].rows.find(item => item.id === id)
      y = home(props.run.states[first].rows.indexOf(row)) + 24
    }
    else if (at < 0) {
      status = props.step === last + 1 ? 'ghost' : 'gone'
      row = props.run.states[last].rows.find(item => item.id === id)
      y = ghostTop.value
    }
    // Every value the row has held, so a replaced value can leave visibly.
    const values = [...new Set(props.run.states.flatMap(item => item.rows.filter(r => r.id === id).map(r => r.value)))]
    const previous = props.run.states[props.step - 1]?.rows.find(r => r.id === id)?.value
    return {
      id, key: row.key, status, y,
      tone: state.value.active === id ? (state.value.tone || 'select') : '',
      values: values.map(value => {
        const now = status === 'present' ? row.value === value : value === row.value
        const replaced = status === 'present' && !now && previous === value
        const before = values.indexOf(value) > values.indexOf(row.value)
        return { value, place: now ? 'now' : replaced ? 'replaced' : before ? 'later' : 'old' }
      }),
    }
  })
})
const hasGhost = computed(() => rows.value.some(row => row.status === 'ghost'))
</script>

<template>
  <div class="ds-dict" :style="{ height: `${ghostTop + rowHeight + 4}px` }">
    <span class="name">{{ run.name }}</span>
    <span class="head" :style="{ left: '0px', width: `${keyWidth}px` }">key</span>
    <span class="head" :style="{ left: `${keyWidth - 2}px`, width: `${valueWidth}px` }">value</span>
    <span class="removed" :class="{ shown: hasGhost }" :style="{ top: `${ghostTop - 26}px` }">removed</span>
    <div
      v-for="row in rows" :key="row.id" class="row" :class="[row.status, row.tone]"
      :style="{ transform: `translateY(${row.y}px)` }" :data-ds-row="row.id" :data-ds-status="row.status"
    >
      <span class="key" :style="{ width: `${keyWidth}px` }" data-ds-key>{{ row.key }}</span>
      <span class="value" :style="{ width: `${valueWidth}px` }">
        <span v-for="item in row.values" :key="item.value" class="item" :class="item.place" :data-ds-value="item.place === 'now' ? '' : null">{{ item.value }}</span>
      </span>
    </div>
  </div>
</template>

<style scoped>
.ds-dict { position: relative; width: 460px; font-family: 'IBM Plex Mono', monospace; }
.name { position: absolute; left: 0; top: 0; font: 600 18px 'IBM Plex Mono', monospace; color: var(--ds-accent); }
.head { position: absolute; top: 36px; padding-left: 14px; box-sizing: border-box; font: 600 12px 'IBM Plex Mono', monospace; letter-spacing: .14em; text-transform: uppercase; color: var(--ds-muted); }
.removed { position: absolute; left: 0; font-size: 15px; color: var(--ds-remove); opacity: 0; transition: opacity 300ms ease; }
.removed.shown { opacity: 1; }
.row {
  position: absolute; left: 0; top: 0; display: flex; height: 50px; font-size: 20px; color: var(--ds-ink);
  transition: transform var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease);
}
.key, .value { box-sizing: border-box; height: 50px; display: flex; align-items: center; padding-left: 14px; border: 2px solid var(--ds-line); background: white; transition: background-color 300ms ease, border-color 300ms ease; }
.value { position: relative; margin-left: -2px; }
.row.select .key, .row.select .value { position: relative; z-index: 1; border-color: var(--ds-select); background: var(--ds-select-soft); }
.row.change .value { position: relative; z-index: 1; border-color: var(--ds-change); background: var(--ds-change-soft); }
.row.pending { opacity: 0; }
.row.gone { opacity: 0; }
.row.ghost { opacity: .75; }
.row.ghost .key, .row.ghost .value { border-style: dashed; border-color: var(--ds-remove); background: var(--ds-remove-soft); color: var(--ds-remove); text-decoration: line-through; }
.item { position: absolute; left: 14px; transition: transform var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease); white-space: nowrap; }
.item.now { opacity: 1; }
.item.later { opacity: 0; transform: translateY(-22px); }
.item.old { opacity: 0; transform: translateX(176px); }
.item.replaced { opacity: .8; transform: translateX(176px); color: var(--ds-remove); text-decoration: line-through; }
@media (prefers-reduced-motion: reduce) {
  .row, .key, .value, .item, .removed { transition: none; }
}
</style>
