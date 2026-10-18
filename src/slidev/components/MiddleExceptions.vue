<script setup>
// An exception looking for a handler, for the native slides of module 08. Each
// frame (the module, or one function call) lists the clauses of its try
// statement. The exception object is one card beside the clause it has reached;
// it moves from clause to clause, and up to the caller when a call ends
// without handling it. Moving back replays the step in reverse.
//
// run.frames : [{ id, label, clauses: [{ id, text }] }], caller above callee
// run.exceptions : { id: { type, message } }
// state.frames : [frameId, ...], the frames that exist in this state
// state.clauses : { 'frameId.clauseId': status }, where status is
//   'run' (its block is running), 'raised' (its block stopped at the exception),
//   'match' (the handler that matches), 'unchecked' (a later handler, never
//   compared), 'skip' (a block that does not run) or 'ran' (finished)
// state.exception : { id, at: 'frameId.clauseId', handled } | null
import { computed } from 'vue'

const props = defineProps({
  run: { type: Object, required: true },
  step: { type: Number, required: true },
  frameWidth: { type: Number, default: 320 },
  gap: { type: Number, default: 40 },
  cardWidth: { type: Number, default: 260 },
})
const rowHeight = 46
const frameHead = 32
const framePad = 10
const frameGap = 20
const words = { raised: 'raised', match: 'matches', unchecked: 'not checked', skip: 'skipped' }
const state = computed(() => props.run.states[props.step])

const layout = computed(() => {
  let y = 0
  return props.run.frames.map(frame => {
    const top = y
    const height = frameHead + frame.clauses.length * rowHeight + framePad
    y += height + frameGap
    return { ...frame, top, height }
  })
})
const height = computed(() => {
  const last = layout.value[layout.value.length - 1]
  return last.top + last.height + 4
})
const frames = computed(() => layout.value.map(frame => ({
  ...frame,
  shown: (state.value.frames || []).includes(frame.id),
  rows: frame.clauses.map((clause, i) => {
    const status = state.value.clauses?.[`${frame.id}.${clause.id}`] || ''
    return { ...clause, i, status, word: words[status] || '' }
  }),
})))
function rowTop(at) {
  const [frameId, clauseId] = at.split('.')
  const frame = layout.value.find(item => item.id === frameId)
  return frame.top + frameHead + frame.clauses.findIndex(clause => clause.id === clauseId) * rowHeight
}
// Each exception keeps its card : where it is now, or where it last was (or
// will first be), invisible, so it fades in and out in place.
const cards = computed(() => Object.entries(props.run.exceptions).map(([id, exception]) => {
  const states = props.run.states
  const now = state.value.exception?.id === id ? state.value.exception : null
  const near = now || states.slice(0, props.step).reverse().find(item => item.exception?.id === id)?.exception
    || states.find(item => item.exception?.id === id).exception
  return { id, ...exception, shown: Boolean(now), handled: Boolean(now?.handled), y: rowTop(near.at) - 2 }
}))
</script>

<template>
  <div class="mid-exc" :style="{ height: `${height}px`, width: `${frameWidth + gap + cardWidth}px` }" :data-mid-step="step">
    <div
      v-for="frame in frames" :key="frame.id" class="frame" :class="{ shown: frame.shown }"
      :style="{ top: `${frame.top}px`, width: `${frameWidth}px`, height: `${frame.height}px` }" :data-mid-frame="frame.id"
    >
      <header>{{ frame.label }}</header>
      <div
        v-for="row in frame.rows" :key="row.id" class="clause" :class="row.status"
        :style="{ top: `${frameHead + row.i * rowHeight}px` }" :data-mid-clause="`${frame.id}.${row.id}`" :data-mid-status="row.status"
      >
        <code>{{ row.text }}</code><small>{{ row.word }}</small>
      </div>
    </div>
    <div
      v-for="card in cards" :key="card.id" class="card" :class="{ shown: card.shown, handled: card.handled }"
      :style="{ transform: `translate(${frameWidth + gap}px, ${card.y}px)`, width: `${cardWidth}px`, '--mid-gap': `${gap}px` }"
      :data-mid-exception="card.id" :data-mid-handled="card.handled"
    >
      <strong>{{ card.type }}</strong>
      <span>{{ card.message }}</span>
      <em>{{ card.handled ? 'handled' : 'looking for a handler' }}</em>
    </div>
  </div>
</template>

<style scoped>
.mid-exc { position: relative; font-family: 'IBM Plex Mono', monospace; }
.frame {
  position: absolute; left: 0; box-sizing: border-box; border: 2px solid #c3d3e3; border-radius: 8px; background: #f7f9fc;
  opacity: 0; transform: translateY(12px); transition: opacity var(--ds-time) var(--ds-ease), transform var(--ds-time) var(--ds-ease);
}
.frame.shown { opacity: 1; transform: none; }
.frame header { height: 30px; padding: 0 12px; display: flex; align-items: center; font: 600 13px 'IBM Plex Mono', monospace; letter-spacing: .1em; color: var(--ds-muted); }
.clause {
  position: absolute; left: 8px; right: 8px; height: 40px; box-sizing: border-box; border: 2px solid var(--ds-line); border-radius: 5px; background: white;
  display: flex; align-items: center; padding: 0 10px; color: var(--ds-ink);
  transition: background-color 300ms ease, border-color 300ms ease, color 300ms ease, opacity 300ms ease;
}
.clause code { flex: 1; font: 400 17px 'IBM Plex Mono', monospace; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; background: none; padding: 0; color: inherit; }
/* The status word sits on the clause's top border, so it costs no width. */
.clause small { position: absolute; right: 8px; top: -9px; padding: 0 5px; background: #f7f9fc; font-size: 12px; line-height: 15px; letter-spacing: .04em; white-space: nowrap; }
.clause small:empty { display: none; }
.clause.run { border-color: var(--ds-select); background: var(--ds-select-soft); }
.clause.raised { border-color: var(--ds-remove); background: var(--ds-remove-soft); }
.clause.raised small { color: var(--ds-remove); }
.clause.match { border-color: var(--ds-select); background: var(--ds-select-soft); }
.clause.match small { color: var(--ds-select); font-weight: 600; }
.clause.ran { background: var(--ds-panel); border-color: var(--ds-accent); }
.clause.unchecked, .clause.skip { border-style: dashed; color: var(--ds-muted); background: transparent; opacity: .7; }
.card {
  position: absolute; left: 0; top: 0; box-sizing: border-box; padding: 6px 12px 7px; border: 2px solid var(--ds-remove); border-radius: 6px;
  background: var(--ds-remove-soft); color: var(--ds-ink); display: flex; flex-direction: column; gap: 1px;
  opacity: 0; z-index: 1;
  transition: transform var(--ds-time) var(--ds-ease), opacity 300ms ease, background-color 300ms ease, border-color 300ms ease;
}
.card::before { content: ''; position: absolute; top: 20px; left: calc(-2px - var(--mid-gap)); width: var(--mid-gap); border-top: 2px dashed var(--ds-remove); transition: border-color 300ms ease; }
.card.shown { opacity: 1; }
.card strong { font-size: 17px; color: var(--ds-remove); transition: color 300ms ease; }
.card span { font-size: 14px; line-height: 1.35; overflow-wrap: anywhere; }
.card em { font-style: normal; font-size: 12px; letter-spacing: .06em; color: var(--ds-muted); }
.card.handled { border-color: var(--ds-select); background: var(--ds-select-soft); }
.card.handled::before { border-color: var(--ds-select); }
.card.handled strong { color: var(--ds-select); }
@media (prefers-reduced-motion: reduce) {
  .frame, .clause, .card, .card::before, .card strong { transition: none; }
}
</style>
