<script setup>
// A JSON round trip, for the native Python Libraries slide : a dictionary,
// the JSON text `dumps` writes from it and the dictionary `loads` builds from
// that text. Text lines and rows keep their identity; each one arrives from
// the row or line it was made from, so the step shows where it came from and
// where it went (a key moving up because the keys are sorted, `None` becoming
// `null` and back). Moving back replays the step in reverse.
//
// run.dicts : [{ id, label, type, x }], each dictionary's column
// run.rows : { dictId: [{ id, key, value } | { id, key, items: [...], from? }] },
//   in insertion order; `from` is the text line a row is read from
// run.text : { x, label, type, width, lines: [{ id, text, hi?, from? }] };
//   `hi` is the part of the line a mark lights; `from` is 'dictId.rowId' or
//   'dictId.rowId.itemIndex', the row or list item the line is written from
// state.show : ['dictId' | 'text', ...], what exists
// state.active : ['dictId' | 'text', ...], what the current line uses
// state.mark : { 'dictId.rowId' | 'text.lineId' | 'text': tone }, tone
//   'select' or 'change'
// state.pairs : [rowId, ...], rows of the first and the last dictionary
//   compared with each other, joined by a line marked `==` at its end
import { computed } from 'vue'

const props = defineProps({ run: { type: Object, required: true }, step: { type: Number, required: true } })
const keyWidth = 96
const valueWidth = 172
const rowWidth = keyWidth + valueWidth - 2
const rowHeight = 44
const rowPitch = 42
const top = 28
const lineHeight = 25
const textPad = 8
const itemPitch = 78
const charWidth = 9
const state = computed(() => props.run.states[props.step])
const shown = computed(() => new Set(state.value.show || []))
const active = computed(() => new Set(state.value.active || []))
const mark = computed(() => state.value.mark || {})
const text = computed(() => props.run.text)
const dictX = id => props.run.dicts.find(item => item.id === id).x
const rowTop = i => top + i * rowPitch
const lineTop = i => top + textPad + i * lineHeight
const lineLeft = computed(() => text.value.x + 12)
const textHeight = computed(() => 2 * textPad + text.value.lines.length * lineHeight + 4)
const height = computed(() => Math.max(top + textHeight.value, ...Object.values(props.run.rows).map(rows => rowTop(rows.length - 1) + rowHeight)) + 4)

// Where a text line is written from : over its row's key, or over the item.
function lineSource(line) {
  const [dict, rowId, item] = line.from.split('.')
  const i = props.run.rows[dict].findIndex(row => row.id === rowId)
  const indent = line.text.length - line.text.trimStart().length
  const x = item === undefined
    ? dictX(dict) + 12 - indent * charWidth
    : dictX(dict) + keyWidth + 6 + Number(item) * itemPitch + 4 - indent * charWidth
  return { x, y: rowTop(i) + (rowHeight - lineHeight) / 2 }
}
const lines = computed(() => text.value.lines.map((line, i) => {
  const at = { x: lineLeft.value, y: lineTop(i) }
  const from = line.from ? lineSource(line) : { x: at.x, y: at.y - 10 }
  const here = shown.value.has('text')
  const parts = line.hi ? line.text.split(line.hi) : [line.text]
  return {
    ...line, ...at, here,
    dx: here ? 0 : from.x - at.x, dy: here ? 0 : from.y - at.y,
    before: parts[0], hi: line.hi ? line.hi : '', after: line.hi ? parts.slice(1).join(line.hi) : '',
    hiTone: line.hi ? mark.value[`text.${line.id}`] || '' : '',
  }
}))
const lineIndex = id => text.value.lines.findIndex(line => line.id === id)
const dicts = computed(() => props.run.dicts.map(dict => ({
  ...dict,
  here: shown.value.has(dict.id),
  on: active.value.has(dict.id),
  rows: props.run.rows[dict.id].map((row, i) => {
    const at = { x: dict.x, y: rowTop(i) }
    const source = row.from ? { x: lineLeft.value - 12, y: lineTop(lineIndex(row.from)) - (rowHeight - lineHeight) / 2 } : { x: at.x, y: at.y + 14 }
    const here = shown.value.has(dict.id)
    return {
      ...row, ...at, here,
      dx: here ? 0 : source.x - at.x, dy: here ? 0 : source.y - at.y,
      tone: mark.value[`${dict.id}.${row.id}`] || '',
    }
  }),
})))
const first = computed(() => props.run.dicts[0])
const last = computed(() => props.run.dicts[props.run.dicts.length - 1])
const everyPair = computed(() => [...new Set(props.run.states.flatMap(item => item.pairs || []))])
const pairs = computed(() => everyPair.value.map(id => {
  const a = props.run.rows[first.value.id].findIndex(row => row.id === id)
  const b = props.run.rows[last.value.id].findIndex(row => row.id === id)
  const x0 = first.value.x + rowWidth + 2
  const x1 = last.value.x - 2
  const y0 = rowTop(a) + rowHeight / 2
  const y1 = rowTop(b) + rowHeight / 2
  const bend = (x1 - x0) / 2.4
  return {
    id, x0, y0, x1, y1,
    path: `M ${x0} ${y0} C ${x0 + bend} ${y0}, ${x1 - bend} ${y1}, ${x1} ${y1}`,
    shown: (state.value.pairs || []).includes(id),
  }
}))
const comparing = computed(() => (state.value.pairs || []).length > 0)
</script>

<template>
  <div class="appendix-json" :style="{ height: `${height}px` }" :data-json-step="step">
    <template v-for="dict in dicts" :key="dict.id">
      <div class="label" :class="{ shown: dict.here }" :style="{ left: `${dict.x}px` }">
        <span class="name">{{ dict.label }}</span><span class="type">{{ dict.type }}</span>
      </div>
      <div
        v-for="row in dict.rows" :key="`${dict.id}.${row.id}`" class="row" :class="[row.tone, { here: row.here, on: dict.on }]"
        :style="{ left: `${row.x}px`, top: `${row.y}px`, transform: `translate(${row.dx}px, ${row.dy}px)` }"
        :data-json-row="`${dict.id}.${row.id}`"
      >
        <span class="key" :style="{ width: `${keyWidth}px` }">{{ row.key }}</span>
        <span class="value" :style="{ width: `${valueWidth}px` }">
          <template v-if="row.items"><span v-for="(item, i) in row.items" :key="i" class="item">{{ item }}</span></template>
          <template v-else>{{ row.value }}</template>
        </span>
      </div>
    </template>

    <div class="label" :class="{ shown: shown.has('text') }" :style="{ left: `${text.x}px` }">
      <span class="name">{{ text.label }}</span><span class="type">{{ text.type }}</span>
    </div>
    <div
      class="text" :class="[mark.text, { shown: shown.has('text'), on: active.has('text'), dim: comparing }]"
      :style="{ left: `${text.x}px`, top: `${top}px`, width: `${text.width}px`, height: `${textHeight}px` }" data-json-text
    />
    <div
      v-for="line in lines" :key="line.id" class="line" :class="{ here: line.here, dim: comparing }"
      :style="{ left: `${line.x}px`, top: `${line.y}px`, transform: `translate(${line.dx}px, ${line.dy}px)` }" :data-json-line="line.id"
    ><span>{{ line.before }}</span><span v-if="line.hi" class="hi" :class="line.hiTone">{{ line.hi }}</span><span>{{ line.after }}</span></div>

    <svg class="pairs" :height="height" aria-hidden="true">
      <path v-for="pair in pairs" :key="pair.id" :d="pair.path" class="pair" :class="{ shown: pair.shown }" :data-json-pair="pair.id" />
    </svg>
    <span
      v-for="pair in pairs" :key="`eq-${pair.id}`" class="equal" :class="{ shown: pair.shown }"
      :style="{ left: `${pair.x1 - 44}px`, top: `${pair.y1 - 12}px` }"
    >==</span>
  </div>
</template>

<style scoped>
.appendix-json { position: relative; font-family: 'IBM Plex Mono', monospace; color: var(--ds-ink); }
.label {
  position: absolute; top: 0; height: 26px; display: flex; align-items: baseline; gap: 10px; white-space: nowrap;
  opacity: 0; transition: opacity var(--ds-time) var(--ds-ease);
}
.label.shown { opacity: 1; }
.label .name { font: 600 18px 'IBM Plex Mono', monospace; color: var(--ds-accent); }
.label .type { font-size: 14px; color: var(--ds-muted); }

.row {
  position: absolute; z-index: 1; display: flex; height: 44px; font-size: 15px; white-space: nowrap; opacity: 0;
  transition: transform var(--ds-time) var(--ds-ease), opacity calc(var(--ds-time) * .4) ease;
}
.row.here { opacity: 1; }
.key, .value {
  box-sizing: border-box; height: 44px; display: flex; align-items: center; gap: 6px; padding-left: 10px;
  border: 2px solid var(--ds-line); background: white; transition: background-color 300ms ease, border-color 300ms ease;
}
.value { margin-left: -2px; padding-left: 6px; }
.value:not(:has(.item)) { padding-left: 10px; }
.item { box-sizing: border-box; width: 72px; height: 32px; display: flex; align-items: center; justify-content: center; border: 2px solid #c3d3e3; border-radius: 4px; transition: border-color 300ms ease, background-color 300ms ease; }
.row.on .key { border-color: var(--ds-select); }
.row.select .key, .row.select .value { position: relative; z-index: 1; border-color: var(--ds-select); background: var(--ds-select-soft); }
.row.select .item { border-color: var(--ds-select); background: white; }
.row.change .value { position: relative; z-index: 1; border-color: var(--ds-change); background: var(--ds-change-soft); }

.text {
  position: absolute; box-sizing: border-box; border: 2px solid #c3d3e3; border-radius: 6px; background: #f7f9fc; opacity: 0;
  transition: opacity var(--ds-time) var(--ds-ease), border-color 300ms ease, background-color 300ms ease;
}
.text.shown { opacity: 1; }
.text.on { border-color: var(--ds-line); }
.text.select { border-color: var(--ds-select); background: var(--ds-select-soft); }
.text.shown.dim { opacity: .45; }
.line {
  position: absolute; z-index: 1; height: 25px; display: flex; align-items: center; font-size: 15px; white-space: pre; opacity: 0;
  transition: transform var(--ds-time) var(--ds-ease), opacity calc(var(--ds-time) * .4) ease;
}
.line.here { opacity: 1; }
.line.here.dim { opacity: .3; }
.hi { border-radius: 3px; transition: background-color 300ms ease, color 300ms ease; }
.hi.change { background: var(--ds-change-soft); color: var(--ds-change); box-shadow: 0 0 0 2px var(--ds-change-soft); }

.pairs { position: absolute; left: 0; top: 0; width: 100%; overflow: visible; pointer-events: none; z-index: 2; }
.pair { fill: none; stroke: var(--ds-select); stroke-width: 2.5; opacity: 0; transition: opacity var(--ds-time) var(--ds-ease); }
.pair.shown { opacity: 1; }
.equal {
  position: absolute; z-index: 3; width: 34px; height: 24px; display: flex; align-items: center; justify-content: center;
  border-radius: 12px; background: var(--ds-select); color: white; font-size: 13px; opacity: 0; transition: opacity var(--ds-time) var(--ds-ease);
}
.equal.shown { opacity: 1; }
@media (prefers-reduced-motion: reduce) {
  .label, .row, .key, .value, .item, .text, .line, .hi, .pair, .equal { transition: none; }
}
</style>
