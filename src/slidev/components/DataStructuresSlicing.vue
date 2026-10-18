<script setup>
// Indexing and slicing one list. Each item has one copy that rests under its
// cell and moves into the result row when the current expression selects it,
// so a result is assembled from the items it copies, in result order.
import { computed } from 'vue'

const props = defineProps({ run: { type: Object, required: true }, step: { type: Number, required: true } })
const cell = 122
const left = 96
const state = computed(() => props.run.states[props.step])
const values = computed(() => props.run.list.values)
const picked = computed(() => state.value.picked || [])
const selected = (index) => picked.value.includes(index)
const isList = computed(() => state.value.result === 'list')
const key = computed(() => state.value.key || null)
const bracket = computed(() => {
  if (!key.value || !isList.value || !picked.value.length) return null
  const low = Math.min(...picked.value)
  const high = Math.max(...picked.value) + 1
  return { x: left + low * cell, width: (high - low) * cell, reverse: (key.value.step || 1) < 0 }
})
const copyStyle = (index) => {
  const slot = picked.value.indexOf(index)
  const x = left + (slot < 0 ? index : slot) * cell
  const y = slot < 0 ? 28 : 196
  return { transform: `translate(${x}px, ${y}px)`, opacity: slot < 0 ? 0 : 1 }
}
const closeX = computed(() => left + picked.value.length * cell + 6)
</script>

<template>
  <div class="ds-slicing" :aria-label="`${run.list.name} and the result of the current expression`">
    <span class="name" style="top: 28px">{{ run.list.name }}</span>
    <span v-for="(_, i) in values" :key="`p${i}`" class="index" :class="{ on: selected(i) }" :style="{ left: `${left + i * cell}px`, top: '0px' }">{{ i }}</span>
    <span v-for="(_, i) in values" :key="`n${i}`" class="index negative" :class="{ on: selected(i) }" :style="{ left: `${left + i * cell}px`, top: '90px' }">{{ i - values.length }}</span>
    <div v-for="(value, i) in values" :key="`c${i}`" class="cell" :class="{ on: selected(i) }" :style="{ left: `${left + i * cell}px`, top: '28px' }" data-ds-value>{{ value }}</div>

    <div class="bracket" :class="{ shown: bracket, reverse: bracket?.reverse }" :style="bracket ? { left: `${bracket.x}px`, width: `${bracket.width}px` } : {}">
      <i class="arrow" />
    </div>
    <template v-if="key && isList && !bracket?.reverse">
      <span class="mark" :style="{ left: `${left + (key.start ?? 0) * cell}px` }">start {{ key.start ?? 0 }}</span>
      <span class="mark" :style="{ left: `${left + (key.stop ?? values.length) * cell}px` }">stop {{ key.stop ?? values.length }}</span>
    </template>
    <span v-if="bracket?.reverse" class="mark" :style="{ left: `${bracket.x + bracket.width / 2}px` }">step {{ key.step }}</span>

    <span class="name result-name" :class="{ shown: picked.length }" style="top: 196px">result</span>
    <span class="square" :class="{ shown: isList }" :style="{ transform: `translate(${left - 22}px, 196px)` }">[</span>
    <span class="square" :class="{ shown: isList }" :style="{ transform: `translate(${closeX}px, 196px)` }">]</span>
    <div v-for="(value, i) in values" :key="`copy${i}`" class="cell copy" :style="copyStyle(i)" :data-ds-result="picked.includes(i) ? picked.indexOf(i) : null">{{ value }}</div>
  </div>
</template>

<style scoped>
.ds-slicing { position: relative; height: 262px; font-family: 'IBM Plex Mono', monospace; }
.name { position: absolute; left: 0; height: 58px; display: flex; align-items: center; font: 600 18px 'IBM Plex Mono', monospace; color: var(--ds-accent); }
.result-name { color: var(--ds-select); opacity: 0; transition: opacity var(--ds-time) var(--ds-ease); }
.result-name.shown { opacity: 1; }
.index { position: absolute; width: 124px; text-align: center; font-size: 17px; line-height: 22px; color: var(--ds-muted); transition: color 300ms ease; }
.index.negative { opacity: .8; }
.index.on { color: var(--ds-select); font-weight: 600; }
.cell { position: absolute; box-sizing: border-box; width: 124px; height: 58px; display: flex; align-items: center; justify-content: center; border: 2px solid var(--ds-line); background: white; font-size: 21px; color: var(--ds-ink); transition: background-color 300ms ease, border-color 300ms ease; }
.cell.on { z-index: 1; background: var(--ds-select-soft); border-color: var(--ds-select); }
.cell.copy { left: 0; top: 0; border: 2px solid var(--ds-select); z-index: 2; background: white; transition: transform var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease); will-change: transform; }
.bracket { position: absolute; top: 118px; height: 12px; box-sizing: border-box; border: 2px solid var(--ds-select); border-top: 0; opacity: 0; transition: left var(--ds-time) var(--ds-ease), width var(--ds-time) var(--ds-ease), opacity 300ms ease; }
.bracket.shown { opacity: 1; }
.arrow { position: absolute; left: -9px; bottom: -7px; border: 6px solid transparent; border-right: 9px solid var(--ds-select); opacity: 0; transition: opacity 300ms ease; }
.bracket.reverse .arrow { opacity: 1; }
.mark { position: absolute; top: 134px; transform: translateX(-50%); font-size: 15px; color: var(--ds-select); white-space: nowrap; }
.square { position: absolute; left: 0; top: 0; height: 58px; display: flex; align-items: center; font-size: 32px; color: var(--ds-select); opacity: 0; transition: transform var(--ds-time) var(--ds-ease), opacity 300ms ease; }
.square.shown { opacity: 1; }
@media (prefers-reduced-motion: reduce) {
  .cell, .cell.copy, .bracket, .arrow, .square, .index, .result-name { transition: none; }
}
</style>
