<script setup>
// An optional result, for the native Type Hinting slide : a dictionary lookup
// that may find nothing, the kinds of result a `-> int | None` annotation
// allows, and the caller's name that receives one of them. Every part has a
// fixed place given by the run; values are chips that keep their identity and
// move between places, so a step moves a value and nothing else shifts.
// Moving back replays the step in reverse.
//
// run.dict : { name, type, x, y, rows: [{ id, key, value }] }; one dashed slot
//   below the rows shows a key the lookup did not find
// run.returns : { x, y, label, lanes: [{ id, type }] }, one lane per kind
// run.names : [{ id, x, y }], a name label and the box its chip sits in
// run.chips : [{ id, text, enter? }]; `enter` is the place a chip comes from
//   when it appears, so a result can emerge from where it was made
// run.places : { placeId: { x, y } }, the top left corner of a chip
// state.dict : true once the dictionary exists
// state.missing : { key, note }, the key the lookup did not find, or absent
// state.chips : { chipId: placeId }; a chip shows while it has a place
// state.names : [nameId, ...], the names that exist
// state.active : ['dict' | 'returns' | nameId, ...], what the current line uses
// state.lane : the lane id the current result goes through, or absent
// state.check : { name, text }, a test on a name and its result, or absent
// state.mark : [chipId, ...], the chips the current line made or tested
import { computed } from 'vue'

const props = defineProps({ run: { type: Object, required: true }, step: { type: Number, required: true } })
const rowHeight = 44
const rowPitch = 42
const keyWidth = 130
const valueWidth = 96
const labelHeight = 30
const laneHeight = 54
const lanePitch = 64
const laneWidth = 236
const nameLabel = 108
const nameBox = 150
const state = computed(() => props.run.states[props.step])
const active = computed(() => new Set(state.value.active || []))
const dict = computed(() => props.run.dict)
const rowTop = i => dict.value.y + labelHeight + i * rowPitch
const missingTop = computed(() => rowTop(dict.value.rows.length) + 12)
const returns = computed(() => props.run.returns)
const laneTop = i => returns.value.y + labelHeight + i * lanePitch
const height = computed(() => Math.max(
  missingTop.value + rowHeight,
  laneTop(returns.value.lanes.length - 1) + laneHeight,
  ...props.run.names.map(name => name.y + rowHeight),
  ...props.run.states.filter(item => item.check).map(item =>
    props.run.names.find(name => name.id === item.check.name).y + rowHeight + 42),
  ...Object.values(props.run.places).map(place => place.y + 40),
) + 4)

// The nearest earlier state with a value, or the first later one.
function lastKnown(pick) {
  const now = pick(state.value)
  if (now !== undefined) return now
  const states = props.run.states
  for (let i = props.step - 1; i >= 0; i--) { const value = pick(states[i]); if (value !== undefined) return value }
  for (const item of states) { const value = pick(item); if (value !== undefined) return value }
  return undefined
}
const missing = computed(() => lastKnown(item => item.missing) || { key: '', note: '' })
const check = computed(() => lastKnown(item => item.check) || { name: '', text: '' })
const names = computed(() => props.run.names.map(name => ({
  ...name,
  shown: (state.value.names || []).includes(name.id),
  on: active.value.has(name.id),
  check: state.value.check?.name === name.id,
})))
const checkName = computed(() => props.run.names.find(name => name.id === check.value.name))
const firstStep = id => props.run.states.findIndex(item => item.chips?.[id])
const chips = computed(() => props.run.chips.map(chip => {
  const now = state.value.chips?.[chip.id]
  const before = props.step < firstStep(chip.id)
  const place = now || (before && chip.enter) || lastKnown(item => item.chips?.[chip.id])
  return {
    ...chip, ...props.run.places[place],
    status: now ? 'shown' : before ? 'before' : 'after',
    mark: (state.value.mark || []).includes(chip.id),
  }
}))
</script>

<template>
  <div class="appendix-optional" :style="{ height: `${height}px` }" :data-optional-step="step">
    <div class="dict" :class="{ shown: state.dict, on: active.has('dict') }" :style="{ left: `${dict.x}px`, top: `${dict.y}px` }" data-optional-dict>
      <div class="label"><span class="name">{{ dict.name }}</span><span class="type">{{ dict.type }}</span></div>
      <div v-for="(row, i) in dict.rows" :key="row.id" class="row" :style="{ top: `${rowTop(i) - dict.y}px` }">
        <span class="key" :style="{ width: `${keyWidth}px` }">{{ row.key }}</span>
        <span class="value" :style="{ width: `${valueWidth}px` }">{{ row.value }}</span>
      </div>
    </div>
    <div
      class="row missing" :class="{ shown: Boolean(state.missing) }"
      :style="{ left: `${dict.x}px`, top: `${missingTop}px` }" data-optional-missing
    >
      <span class="key" :style="{ width: `${keyWidth}px` }">{{ missing.key }}</span>
      <span class="value" :style="{ width: `${valueWidth}px` }" />
      <span class="note">{{ missing.note }}</span>
    </div>

    <div class="returns" :class="{ on: active.has('returns') }" :style="{ left: `${returns.x}px`, top: `${returns.y}px` }" data-optional-returns>
      <div class="label"><span class="type">{{ returns.label }}</span></div>
      <div
        v-for="(lane, i) in returns.lanes" :key="lane.id" class="lane" :class="{ lit: state.lane === lane.id }"
        :style="{ top: `${laneTop(i) - returns.y}px`, width: `${laneWidth}px` }" :data-optional-lane="lane.id"
      >
        <span class="lane-type">{{ lane.type }}</span><span class="lane-slot" />
      </div>
    </div>

    <div
      v-for="name in names" :key="name.id" class="caller" :class="{ shown: name.shown, on: name.on }"
      :style="{ left: `${name.x}px`, top: `${name.y}px` }" :data-optional-name="name.id"
    >
      <span class="caller-label" :style="{ width: `${nameLabel}px` }">{{ name.id }}</span>
      <span class="caller-box" :style="{ width: `${nameBox}px` }" />
    </div>
    <div
      v-if="checkName" class="check" :class="{ shown: Boolean(state.check) }"
      :style="{ left: `${checkName.x + nameLabel}px`, top: `${checkName.y + rowHeight + 14}px` }" data-optional-check
    >{{ check.text }}</div>

    <div
      v-for="chip in chips" :key="chip.id" class="chip" :class="[chip.status, { mark: chip.mark }]"
      :style="{ left: `${chip.x}px`, top: `${chip.y}px` }" :data-optional-chip="chip.id" :data-optional-status="chip.status"
    >{{ chip.text }}</div>
  </div>
</template>

<style scoped>
.appendix-optional { position: relative; font-family: 'IBM Plex Mono', monospace; color: var(--ds-ink); }
.label { height: 30px; display: flex; align-items: baseline; gap: 12px; white-space: nowrap; }
.label .name { font: 600 18px 'IBM Plex Mono', monospace; color: var(--ds-accent); }
.label .type { font-size: 15px; letter-spacing: .02em; color: var(--ds-muted); }
.dict { position: absolute; opacity: 0; transform: translateY(10px); transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease); }
.dict.shown { opacity: 1; transform: none; }
.row { position: absolute; left: 0; display: flex; height: 44px; font-size: 18px; white-space: nowrap; }
.key, .value {
  box-sizing: border-box; height: 44px; display: flex; align-items: center; padding-left: 12px;
  border: 2px solid var(--ds-line); background: white; transition: background-color 300ms ease, border-color 300ms ease;
}
.value { margin-left: -2px; }
.dict.on .key { border-color: var(--ds-select); background: var(--ds-select-soft); }
.missing { opacity: 0; transform: translateY(-12px); transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease); }
.missing.shown { opacity: 1; transform: none; }
.missing .key, .missing .value { border-style: dashed; border-color: var(--ds-change); background: var(--ds-change-soft); color: var(--ds-change); }
.missing .value { background: transparent; }
.missing .note { align-self: center; margin-left: 12px; font-size: 14px; letter-spacing: .04em; color: var(--ds-change); }

.returns { position: absolute; }
.lane {
  position: absolute; left: 0; height: 54px; box-sizing: border-box; display: flex; align-items: center; gap: 10px; padding: 0 8px 0 14px;
  border: 2px solid #c3d3e3; border-radius: 8px; background: #f7f9fc; transition: border-color 300ms ease, background-color 300ms ease;
}
.lane-type { width: 62px; font: 600 18px 'IBM Plex Mono', monospace; color: var(--ds-muted); transition: color 300ms ease; }
.lane-slot { flex: 1; height: 40px; box-sizing: border-box; border: 2px dashed #c3d3e3; border-radius: 5px; }
.returns.on .lane { border-color: var(--ds-line); }
.lane.lit { border-color: var(--ds-select); background: var(--ds-select-soft); }
.lane.lit .lane-type { color: var(--ds-select); }

.caller {
  position: absolute; height: 44px; display: flex; align-items: center; opacity: 0; transform: translateX(-10px);
  transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease);
}
.caller.shown { opacity: 1; transform: none; }
.caller-label { font-size: 20px; white-space: nowrap; }
.caller-box { box-sizing: border-box; height: 44px; border: 2px solid var(--ds-line); border-radius: 5px; background: white; transition: background-color 300ms ease, border-color 300ms ease; }
.caller.on .caller-box { border-color: var(--ds-select); background: var(--ds-select-soft); }
.check {
  position: absolute; height: 28px; display: flex; align-items: center; padding: 0 12px; border-radius: 14px;
  background: var(--ds-select); color: white; font-size: 15px; white-space: nowrap;
  opacity: 0; transform: translateY(-8px); transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease);
}
.check.shown { opacity: 1; transform: none; }

.chip {
  position: absolute; z-index: 2; height: 40px; box-sizing: border-box; display: flex; align-items: center; padding: 0 12px;
  border: 2px solid var(--ds-line); border-radius: 5px; background: white; font-size: 18px; white-space: nowrap;
  transition: left var(--ds-time) var(--ds-ease), top var(--ds-time) var(--ds-ease), opacity var(--ds-time) var(--ds-ease),
    background-color 300ms ease, border-color 300ms ease;
}
.chip.before, .chip.after { opacity: 0; }
.chip.mark { border-color: var(--ds-select); background: var(--ds-select-soft); }
@media (prefers-reduced-motion: reduce) {
  .dict, .key, .value, .missing, .lane, .lane-type, .caller, .caller-box, .check, .chip { transition: none; }
}
</style>
