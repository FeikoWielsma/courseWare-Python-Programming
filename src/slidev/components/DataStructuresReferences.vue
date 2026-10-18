<script setup>
// Lists that hold lists. Each name refers to an outer list; each outer slot
// holds a reference, drawn as an arrow, to an inner list object. Inner lists
// are drawn once per object, so two slots referring to one list share it.
import { computed, useId } from 'vue'

const props = defineProps({ run: { type: Object, required: true }, step: { type: Number, required: true } })
const markerPrefix = `ds-${useId()}`
const width = 380
const gap = 44
const cell = 56
const slotTop = [40, 96]
const state = computed(() => props.run.states[props.step])

// Where each inner object sits : one shared object between the slots,
// separate objects level with their own slot.
function layout(name) {
  const refs = props.run.states.map(item => item.refs[name]).find(Boolean)
  const unique = [...new Set(refs)]
  return Object.fromEntries(unique.map((id, i) => [id, unique.length === 1 ? 68 : [24, 112][i]]))
}
const panels = computed(() => props.run.names.map((name, p) => {
  const places = layout(name)
  const refs = state.value.refs[name]
  return {
    name, x: p * (width + gap), shown: Boolean(refs),
    slots: (props.run.states.map(item => item.refs[name]).find(Boolean)).map((_, i) => {
      const target = refs ? refs[i] : Object.keys(places)[i] || Object.keys(places)[0]
      const y0 = slotTop[i] + 29
      const y1 = places[target] + 29
      const active = (state.value.via?.name === name && state.value.via.slot === i) || state.value.reading === name
      return { i, top: slotTop[i], active, path: `M 98 ${y0} C 140 ${y0}, 150 ${y1}, 192 ${y1}` }
    }),
    objects: Object.entries(places).map(([id, top]) => {
      const values = state.value.objects[id] || props.run.states.map(item => item.objects[id]).find(Boolean)
      const changed = state.value.changed?.object === id ? state.value.changed.index : -1
      const active = props.run.states[props.step].refs[name]?.some((ref, i) => ref === id && ((state.value.via?.name === name && state.value.via.slot === i) || state.value.reading === name))
      return { id, top, values, changed, active, present: Boolean(state.value.objects[id]) }
    }),
  }
}))
</script>

<template>
  <div class="ds-references" :style="{ width: `${2 * width + gap}px` }">
    <div v-for="panel in panels" :key="panel.name" class="panel" :class="{ shown: panel.shown }" :style="{ left: `${panel.x}px`, width: `${width}px` }" :data-ds-name="panel.name">
      <span class="name">{{ panel.name }}</span>
      <svg class="arrows" :width="width" height="200" aria-hidden="true">
        <defs>
          <marker :id="`${markerPrefix}-head-${panel.name}`" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="13" markerHeight="13" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" class="head" /></marker>
          <marker :id="`${markerPrefix}-head-on-${panel.name}`" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="13" markerHeight="13" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" class="head on" /></marker>
        </defs>
        <path v-for="slot in panel.slots" :key="slot.i" :d="slot.path" class="ref" :class="{ on: slot.active }" :marker-end="`url(#${markerPrefix}-head-${slot.active ? 'on-' : ''}${panel.name})`" />
      </svg>
      <template v-for="slot in panel.slots" :key="`s${slot.i}`">
        <span class="index" :style="{ top: `${slot.top}px` }">{{ slot.i }}</span>
        <div class="slot" :class="{ on: slot.active }" :style="{ top: `${slot.top}px` }"><i /></div>
      </template>
      <div
        v-for="object in panel.objects" :key="object.id" class="inner" :class="{ present: object.present, on: object.active }"
        :style="{ top: `${object.top}px` }" :data-ds-object="object.id"
      >
        <span v-for="(value, i) in object.values" :key="i" class="cell" :class="{ change: i === object.changed }" data-ds-value>
          <Transition name="ds-swap" mode="out-in"><span :key="value">{{ value }}</span></Transition>
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.ds-references { position: relative; height: 200px; font-family: 'IBM Plex Mono', monospace; }
.panel { position: absolute; top: 0; height: 200px; opacity: 0; transform: translateY(14px); transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease); }
.panel.shown { opacity: 1; transform: none; }
.name { position: absolute; left: 40px; top: 4px; font: 600 18px 'IBM Plex Mono', monospace; color: var(--ds-accent); }
.arrows { position: absolute; left: 0; top: 0; overflow: visible; }
.ref { fill: none; stroke: #8fb0cf; stroke-width: 2.5; transition: stroke 300ms ease, d var(--ds-time) var(--ds-ease); }
.ref.on { stroke: var(--ds-select); stroke-width: 3; }
.head { fill: #8fb0cf; }
.head.on { fill: var(--ds-select); }
.index { position: absolute; left: 14px; width: 30px; height: 58px; display: flex; align-items: center; justify-content: flex-end; font-size: 17px; color: var(--ds-muted); }
.slot { position: absolute; left: 52px; width: 58px; height: 58px; box-sizing: border-box; border: 2px solid var(--ds-line); background: white; display: flex; align-items: center; justify-content: center; transition: background-color 300ms ease, border-color 300ms ease; }
.slot i { width: 12px; height: 12px; border-radius: 50%; background: #8fb0cf; transform: translateX(16px); transition: background-color 300ms ease; }
.slot.on { z-index: 1; border-color: var(--ds-select); background: var(--ds-select-soft); }
.slot.on i { background: var(--ds-select); }
.inner { position: absolute; left: 200px; display: flex; opacity: 0; transition: opacity var(--ds-time) var(--ds-ease); }
.inner.present { opacity: 1; }
.cell { box-sizing: border-box; width: 58px; height: 58px; margin-right: -2px; display: flex; align-items: center; justify-content: center; border: 2px solid var(--ds-line); background: white; font-size: 21px; color: var(--ds-ink); transition: background-color 300ms ease, border-color 300ms ease; }
.inner.on .cell { border-color: var(--ds-select); }
.cell.change { position: relative; z-index: 1; border-color: var(--ds-change) !important; background: var(--ds-change-soft); }
.ds-swap-enter-active, .ds-swap-leave-active { transition: opacity 200ms ease, transform 200ms ease; }
.ds-swap-enter-from { opacity: 0; transform: translateY(-10px); }
.ds-swap-leave-to { opacity: 0; transform: translateY(10px); }
@media (prefers-reduced-motion: reduce) {
  .panel, .ref, .slot, .slot i, .inner, .cell, .ds-swap-enter-active, .ds-swap-leave-active { transition: none; }
}
</style>
