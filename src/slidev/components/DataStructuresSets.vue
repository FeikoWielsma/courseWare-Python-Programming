<script setup>
// Two sets as overlapping circles. Each name appears once, in the region of
// the sets that hold it. An operator lights the regions in its result.
import { computed } from 'vue'

const props = defineProps({ run: { type: Object, required: true }, step: { type: Number, required: true } })
const r = 118
const cy = 160
const cx = [128, 274]
const xi = (cx[0] + cx[1]) / 2
const h = Math.sqrt(r * r - ((cx[1] - cx[0]) / 2) ** 2)
const p1 = `${xi} ${cy - h}`
const p2 = `${xi} ${cy + h}`
const paths = {
  left: `M ${p1} A ${r} ${r} 0 1 0 ${p2} A ${r} ${r} 0 0 1 ${p1} Z`,
  both: `M ${p1} A ${r} ${r} 0 0 1 ${p2} A ${r} ${r} 0 0 1 ${p1} Z`,
  right: `M ${p1} A ${r} ${r} 0 1 1 ${p2} A ${r} ${r} 0 0 0 ${p1} Z`,
}
const left = computed(() => props.run.sets.left)
const right = computed(() => props.run.sets.right)
const regions = computed(() => ({
  left: left.value.members.filter(name => !right.value.members.includes(name)),
  both: left.value.members.filter(name => right.value.members.includes(name)),
  right: right.value.members.filter(name => !left.value.members.includes(name)),
}))
// Each lune is centred between the two circles' edges on its side.
const centres = { left: (cx[0] + cx[1]) / 2 - r, both: xi, right: (cx[0] + cx[1]) / 2 + r }
const chips = computed(() => Object.entries(regions.value).flatMap(([region, names]) =>
  [...names].sort().map((name, i) => ({ name, region, x: centres[region], y: cy + (i - (names.length - 1) / 2) * 50 }))))
const state = computed(() => props.run.states[props.step])
const result = computed(() => state.value.result)
const lit = (region) => Boolean(result.value && regions.value[region].length && regions.value[region].every(name => result.value.includes(name)))
const chipClass = (chip) => {
  if (state.value.test) return chip.name === state.value.test ? 'on' : 'dim'
  if (!result.value) return ''
  return result.value.includes(chip.name) ? 'on' : 'dim'
}
const ring = (side) => state.value.within === props.run.sets[side].name
</script>

<template>
  <div class="ds-sets" :aria-label="`${left.name} and ${right.name}`">
    <svg width="412" height="290" viewBox="0 0 412 290" aria-hidden="true">
      <path v-for="(d, region) in paths" :key="region" :d="d" class="region" :class="{ lit: lit(region) }" :data-ds-region="region" />
      <circle :cx="cx[0]" :cy="cy" :r="r" class="ring" :class="{ on: ring('left') }" />
      <circle :cx="cx[1]" :cy="cy" :r="r" class="ring" :class="{ on: ring('right') }" />
    </svg>
    <span class="label" :style="{ left: `${cx[0] - r}px` }">{{ left.name }}</span>
    <span class="label end" :style="{ right: `${412 - cx[1] - r}px` }">{{ right.name }}</span>
    <span
      v-for="chip in chips" :key="chip.name" class="chip" :class="chipClass(chip)"
      :style="{ left: `${chip.x}px`, top: `${chip.y}px` }" :data-ds-member="chip.name" :data-ds-region="chip.region"
    >'{{ chip.name }}'</span>
  </div>
</template>

<style scoped>
.ds-sets { position: relative; width: 412px; height: 290px; font-family: 'IBM Plex Mono', monospace; }
svg { position: absolute; left: 0; top: 0; overflow: visible; }
.region { fill: var(--ds-select); fill-opacity: 0; transition: fill-opacity var(--ds-time) var(--ds-ease); }
.region.lit { fill-opacity: .2; }
.ring { fill: none; stroke: var(--ds-line); stroke-width: 2; transition: stroke 300ms ease, stroke-width 300ms ease; }
.ring.on { stroke: var(--ds-select); stroke-width: 4; }
.label { position: absolute; top: 2px; font: 600 18px 'IBM Plex Mono', monospace; color: var(--ds-accent); }
.chip {
  position: absolute; transform: translate(-50%, -50%); padding: 3px 7px; border-radius: 5px; white-space: nowrap;
  border: 1.5px solid var(--ds-line); background: white; font-size: 15px; color: var(--ds-ink);
  transition: opacity var(--ds-time) var(--ds-ease), border-color 300ms ease, background-color 300ms ease, color 300ms ease;
}
.chip.on { border-color: var(--ds-select); background: var(--ds-select-soft); color: #0d4f60; font-weight: 600; }
.chip.dim { opacity: .4; }
@media (prefers-reduced-motion: reduce) {
  .region, .ring, .chip { transition: none; }
}
</style>
