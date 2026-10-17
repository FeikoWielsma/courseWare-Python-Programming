(function () {
  'use strict';
  var words = ['crane', 'slate', 'trace', 'audio', 'cider', 'plant', 'spoke', 'grace', 'flint', 'proud', 'charm'];
  var day = Math.floor(Date.now() / 86400000);
  var answer = words[((day % words.length) + words.length) % words.length];
  var dialog = null;
  var guess = '';
  var guesses = [];
  var ended = false;
  var focusBefore = null;
  var typed = '';
  var timer = null;

  function field(target) {
    return target && (target.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(target.tagName));
  }
  function build() {
    dialog = document.createElement('dialog');
    dialog.className = 'prg-wordle-dialog';
    dialog.setAttribute('aria-labelledby', 'prg-wordle-title');
    dialog.innerHTML = '<h2 id="prg-wordle-title">Wordle</h2><p class="prg-wordle-help">Six guesses. Type letters, then press Enter.</p><div class="prg-wordle-grid" aria-label="Guess tiles" aria-live="polite"></div><div class="prg-wordle-keyboard" aria-label="Wordle keyboard"></div><p class="prg-wordle-message" role="status" aria-live="polite"></p><div class="prg-wordle-actions"><span>Type <kbd>wordle</kbd> anywhere on the page to open.</span><button type="button" data-close>Close</button></div>';
    document.body.appendChild(dialog);
    var grid = dialog.querySelector('.prg-wordle-grid');
    for (var r = 0; r < 6; r++) {
      var row = document.createElement('div'); row.className = 'prg-wordle-row';
      for (var c = 0; c < 5; c++) { var tile = document.createElement('span'); tile.className = 'prg-wordle-tile'; row.appendChild(tile); }
      grid.appendChild(row);
    }
    var keyboard = dialog.querySelector('.prg-wordle-keyboard');
    ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'].forEach(function (letters, index) {
      var row = document.createElement('div'); row.className = 'prg-wordle-keyrow';
      if (index === 2) row.appendChild(keyButton('Enter'));
      letters.split('').forEach(function (letter) { row.appendChild(keyButton(letter)); });
      if (index === 2) row.appendChild(keyButton('Backspace'));
      keyboard.appendChild(row);
    });
    dialog.querySelector('[data-close]').addEventListener('click', close);
    dialog.addEventListener('click', function (event) { if (event.target === dialog) close(); });
    dialog.addEventListener('cancel', function (event) { event.preventDefault(); close(); });
  }
  function keyButton(label) {
    var button = document.createElement('button'); button.type = 'button'; button.className = 'prg-wordle-key'; button.textContent = label;
    button.addEventListener('click', function () { onKey(label); });
    return button;
  }
  function open() {
    if (!dialog) build();
    if (dialog.open) return;
    focusBefore = document.activeElement;
    dialog.showModal();
    dialog.querySelector('[data-close]').focus();
  }
  function close() {
    if (!dialog || !dialog.open) return;
    dialog.close();
    if (focusBefore && focusBefore.focus) focusBefore.focus();
  }
  function score(secret, attempt) {
    var result = Array(5).fill('absent');
    var remaining = {};
    for (var i = 0; i < 5; i++) {
      if (attempt[i] === secret[i]) result[i] = 'correct';
      else remaining[secret[i]] = (remaining[secret[i]] || 0) + 1;
    }
    for (var j = 0; j < 5; j++) {
      if (result[j] === 'correct') continue;
      if (remaining[attempt[j]]) { result[j] = 'present'; remaining[attempt[j]]--; }
    }
    return result;
  }
  function render() {
    if (!dialog) return;
    var rows = dialog.querySelectorAll('.prg-wordle-row');
    for (var r = 0; r < 6; r++) {
      var tiles = rows[r].children;
      var word = guesses[r] || (r === guesses.length && !ended ? guess : '');
      for (var c = 0; c < 5; c++) {
        tiles[c].textContent = word[c] || '';
        tiles[c].dataset.state = guesses[r] ? guesses[r].states[c] : '';
        tiles[c].setAttribute('aria-label', guesses[r] ? word[c] + ' ' + guesses[r].states[c] : (word[c] || 'empty'));
      }
    }
    dialog.querySelector('.prg-wordle-message').textContent = ended ? (guesses[guesses.length - 1].word === answer ? 'Solved. Well played.' : 'The word was ' + answer.toUpperCase() + '.') : (guess.length ? guess.toUpperCase() : '');
  }
  function onKey(key) {
    if (ended) return;
    if (key === 'Backspace') guess = guess.slice(0, -1);
    else if (key === 'Enter') {
      if (guess.length !== 5) { dialog.querySelector('.prg-wordle-message').textContent = 'Enter five letters.'; return; }
      if (!/^[a-z]{5}$/.test(guess)) return;
      var states = score(answer, guess);
      guesses.push({ word: guess, states: states });
      ended = guess === answer || guesses.length === 6;
      guess = '';
      render();
      return;
    } else if (/^[a-z]$/.test(key) && guess.length < 5) guess += key;
    render();
  }
  document.addEventListener('keydown', function (event) {
    if (dialog && dialog.open) {
      if (event.key === 'Tab') {
        var focusables = dialog.querySelectorAll('button');
        if (event.shiftKey && document.activeElement === focusables[0]) { event.preventDefault(); focusables[focusables.length - 1].focus(); }
        else if (!event.shiftKey && document.activeElement === focusables[focusables.length - 1]) { event.preventDefault(); focusables[0].focus(); }
      }
      if (event.key.length === 1 && /^[a-z]$/i.test(event.key)) { event.preventDefault(); onKey(event.key.toLowerCase()); }
      else if (event.key === 'Enter' || event.key === 'Backspace') { event.preventDefault(); onKey(event.key); }
      return;
    }
    if (event.ctrlKey || event.metaKey || event.altKey || field(event.target)) return;
    if (/^[a-z]$/i.test(event.key)) {
      typed = (typed + event.key.toLowerCase()).slice(-6);
      clearTimeout(timer);
      timer = setTimeout(function () { typed = ''; }, 1800);
      if (typed === 'wordle') { typed = ''; open(); }
    }
  });
})();
