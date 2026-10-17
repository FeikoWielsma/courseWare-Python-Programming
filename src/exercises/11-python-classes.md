# Exercise 11 : Python Classes

Look at `play` in `wordle/game.py`. The state of one game is spread over a handful of loose variables : `secret`, `words`, `history`, `guess_count`, `max_guesses`. Every new feature, the hint, the statistics and the next one you add, has to pass them around or reach into them, and nothing stops a function from putting a nonsense value in one of them. In this exercise you gather them in a class, `Game`, which owns its state and the rules about it. On the way you meet properties and the one question that decides when to use them.

Continue in your own `wordle` project, or start from `exercises/starters/11-python-classes/`. The starter is the finished Exercise 10 plus the test file this exercise hands out, `tests/test_game.py`. If you continue in your own project, copy that file in from `exercises/handouts/11-python-classes/`.

Some steps give you the code, some a skeleton to complete, and some only the tests to pass. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 : A Game with plain attributes

Add the class to `wordle/game.py`, above `play`. For now it only stores what a game needs :

```python
class Game:
    """Keep one game's state."""

    def __init__(self, secret: str, words: list[str], max_guesses: int = 6) -> None:
        self.secret = secret
        self.words = words
        self.history: list[tuple[str, list[str]]] = []
        self.max_guesses = max_guesses
```

`__init__` runs when you write `Game(...)`, and `self` is the new object. Every `self.name = ...` makes an attribute on that object. `secret` is the word to find, `words` is the list of words the game accepts as a guess, and `history` collects each guess with its marks, which is the list that `candidates` in `wordle/solver.py` already expects. See *Creating Classes* and *Class Members*.

Start a Python session in the project folder and look at an object :

```bash
uv run python
```

```python
from wordle.game import Game

game = Game("crane", ["crane", "slate"])
print(game.secret, game.max_guesses, game.history)
game.max_guesses = 3
print(game.max_guesses)
```

```text
crane 6 []
3
```

An attribute is read and assigned like a variable. There is nothing else to write, and for now that is how it should be. See *Attributes Are Public*.

### Step 2 : A method that plays a guess

A class is the data together with the functions that work on it. The first of those is the heart of the game : take a guess, check it, score it, remember it. Add a method to `Game` :

```python
    def guess(self, word: str) -> list[str]:
        """Validate, score and record one guess, then return its marks."""
        ...
```

The functions `check_guess` and `score_guess` already exist, and `game.py` already imports them. Use `self.words`, `self.secret` and `self.history` instead of arguments, because the object has them. An invalid word must raise `InvalidGuess` before anything is recorded.

Try it in the session :

```python
game = Game("crane", ["crane", "slate"])
game.guess("slate")
game.history
game.guess("zzzzz")
```

```text
['grey', 'grey', 'green', 'grey', 'green']
[('slate', ['grey', 'grey', 'green', 'grey', 'green'])]
wordle.scoring.InvalidGuess: That word is not in the word list.
```

Run `uv run pytest tests/test_game.py`. One of the four tests passes, the one that checks that a rejected guess leaves the history alone. The other three need the next steps.

:::hint
The method has three lines of real work : `check_guess(word, self.words)`, then `marks = score_guess(self.secret, word)`, then an `append` of the pair `(word, marks)` to `self.history`. Return `marks`.
:::

:::solution
```python
    def guess(self, word: str) -> list[str]:
        """Validate, score and record one guess, then return its marks."""
        check_guess(word, self.words)
        marks = score_guess(self.secret, word)
        self.history.append((word, marks))
        return marks
```

`check_guess` comes first on purpose : when it raises, the exception leaves the method before the history changes.
:::

### Step 3 : Values that work themselves out

Callers will keep asking three things : has the player won, is the game over, how many guesses are left. All three can be worked out from `history` and `max_guesses`, so none of them needs to be stored. As methods they would be called `game.is_won()`. With `@property` above the `def` they are read as `game.is_won`, like an attribute that is always correct. See *A Computed Attribute*.

Add these three to `Game`, above `guess` :

```python
    @property
    def is_won(self) -> bool:
        """Return whether the latest guess found the secret."""
        ...

    @property
    def is_over(self) -> bool:
        """Return whether the game was won or has no guesses left."""
        ...

    @property
    def guesses_left(self) -> int:
        """Return how many guesses remain."""
        ...
```

If you stored `is_won` as an attribute you would have to remember to update it in `guess`, and one forgotten line leaves it wrong. A computed value cannot go stale.

Now use `is_over` in `guess` as well : a finished game should refuse another guess. Put this at the top of the method :

```python
        if self.is_over:
            raise ValueError("The game is over.")
```

Try the three, and see that they cannot be assigned to :

```python
game = Game("crane", ["crane", "slate"], max_guesses=2)
print(game.is_won, game.is_over, game.guesses_left)
game.guess("slate")
print(game.is_won, game.is_over, game.guesses_left)
game.guess("crane")
print(game.is_won, game.is_over, game.guesses_left)
game.is_won = False
```

```text
False False 2
['grey', 'grey', 'green', 'grey', 'green']
False False 1
['green', 'green', 'green', 'green', 'green']
True True 0
AttributeError: property 'is_won' of 'Game' object has no setter
```

:::hint
`is_won` is true when there is at least one guess and the last one is the secret. `self.history[-1][0]` is the word of the last guess. An empty list has no last item, so check `self.history` first; `bool(self.history and ...)` returns a real `bool`.
:::

:::hint
`guesses_left` is `self.max_guesses - len(self.history)`. `is_over` is `self.is_won` or no guesses left; one property can use another. Test for `<= 0` rather than `== 0`, so that a game that somehow has more guesses than its limit counts as over too.
:::

:::solution
```python
    @property
    def is_won(self) -> bool:
        """Return whether the latest guess found the secret."""
        return bool(self.history and self.history[-1][0] == self.secret)

    @property
    def is_over(self) -> bool:
        """Return whether the game was won or has no guesses left."""
        return self.is_won or self.guesses_left <= 0

    @property
    def guesses_left(self) -> int:
        """Return how many guesses remain."""
        return self.max_guesses - len(self.history)
```
:::

### Step 4 : When a plain attribute is not enough

`max_guesses` is a plain attribute, so anybody can assign anything to it. Find out what that allows :

```python
game = Game("crane", ["crane", "slate"])
game.max_guesses = 0
print(game.max_guesses, game.guesses_left, game.is_over)
game.max_guesses = -3
print(game.max_guesses, game.guesses_left, game.is_over)
```

```text
0 0 True
-3 -3 True
```

Both games are over before they start, and the second one claims to have minus three guesses left. The class has no way to stop either. This is the situation the slide *When a Plain Attribute Is Not Enough* is about.

The fix is to turn `max_guesses` into a property with a setter, and to let the setter refuse values that are not between 1 and 10. Here are the signatures. Both methods are called `max_guesses`, and the second is decorated with `@max_guesses.setter` :

```python
    @property
    def max_guesses(self) -> int:
        """Return the configured guess limit."""

    @max_guesses.setter
    def max_guesses(self, value: int) -> None:
        """Keep the guess limit between one and ten."""
```

The setter raises `ValueError("max_guesses must be between 1 and 10")` for any other value, and stores a valid one in `self._max_guesses`. The leading underscore says that the attribute is the property's own storage and not for outside use; see *The Rule of Thumb*.

The tests are in `tests/test_game.py` already :

```python
def test_max_guesses_is_validated() -> None:
    game = Game("crane", WORDS)
    game.max_guesses = 10
    with pytest.raises(ValueError):
        game.max_guesses = 0
    with pytest.raises(ValueError):
        Game("crane", WORDS, max_guesses=11)
```

Make it pass **without changing a line anywhere else**. `__init__` still says `self.max_guesses = max_guesses`, and `play` still reads `game.max_guesses`. That is the lesson : callers could not tell the plain attribute from the property, so nobody had to write `get_max_guesses` and `set_max_guesses` in advance. You start with the plain attribute, and you turn it into a property on the day it needs a rule.

:::hint
The getter returns `self._max_guesses`. The setter checks `1 <= value <= 10`, raises `ValueError` when that is false and assigns `self._max_guesses = value` otherwise.
:::

:::hint
Assign to `self._max_guesses` in the setter, with the underscore. `self.max_guesses = value` inside the setter calls the setter again, forever, until Python stops with a `RecursionError`.
:::

:::output
```text
.                                                                        [100%]
1 passed, 3 deselected in 0.03s
```

That is the run of `uv run pytest tests/test_game.py -k max_guesses`.
:::

:::solution
```python
    @property
    def max_guesses(self) -> int:
        """Return the configured guess limit."""
        return self._max_guesses

    @max_guesses.setter
    def max_guesses(self, value: int) -> None:
        """Keep the guess limit between one and ten."""
        if not 1 <= value <= 10:
            raise ValueError("max_guesses must be between 1 and 10")
        self._max_guesses = value
```

`Game("crane", words, max_guesses=11)` fails too, because `__init__` assigns through the property.
:::

### Step 5 : Draw the board and shrink play

A `Game` that can draw itself helps you debug it. Python asks an object for its text with `__str__`; `print(game)` and f-strings call it. Add one to `Game` that draws every scored guess on its own row with `render`. The slide *Class Attributes and Instance Attributes* leads into the one on `__str__` and `__repr__` in module 11.

```python
    def __str__(self) -> str:
        """Draw every scored guess on its own row."""
        ...
```

```python
game = Game("crane", ["crane", "slate"])
game.guess("slate")
game.guess("crane")
print(game)
```

```text
['grey', 'grey', 'green', 'grey', 'green']
['green', 'green', 'green', 'green', 'green']
 S  L [A] T [E]
[C][R][A][N][E]
```

Now let `play` do less. Change it so that it creates a `Game` and loops until the game is over :

- create the game after loading the allowed list : `game = Game(secret, allowed_words, max_guesses)`
- loop with `while not game.is_over`, and remove the variables `history` and `guess_count`
- show the prompt number with `len(game.history) + 1` and the limit with `game.max_guesses`
- give `candidates(words, game.history)` the history for the hint
- in the `try` block, keep the `check_guess(guess, allowed_words)` line, and let `marks = game.guess(guess)` replace the scoring and recording below it
- after the loop, `game.is_won` decides the message : `Got it in N!` after a win, and `The word was ...` after a loss
- return `len(game.history), game.is_won`, the same two values as in Exercise 10, so that `__main__` still has what it needs for `record_game`

Run `uv run pytest`. All four tests of `tests/test_game.py` pass now, and so does the rest of the project. Then play a game with `WORDLE_SECRET=crane`; it must behave as before.

:::hint
The loop body shrinks to : read the guess, handle the commands, `check_guess` and `marks = game.guess(guess)` inside `try`, update `used_letters`, print `render(guess, marks)`. The win test and the counter are gone, because the loop condition and `game.is_won` now know.
:::

:::hint
A single `"\n".join(...)` over a generator expression is the whole of `__str__`. The expression is `render(word, marks)` for each `word, marks` pair in `self.history`, and `\n` is the newline that puts each row on its own line.
:::

:::solution
```python
    def __str__(self) -> str:
        """Draw every scored guess on its own row."""
        return "\n".join(render(word, marks) for word, marks in self.history)
```

```python
def play(secret: str, words: list[str], max_guesses: int = 6) -> tuple[int, bool]:
    """Play one game and return the guesses used and whether the secret was found."""
    allowed_words = load_allowed()
    game = Game(secret, allowed_words, max_guesses)
    used_letters = set()
    while not game.is_over:
        guess = input(f"Guess {len(game.history) + 1}/{game.max_guesses} : ").strip().lower()
        match guess:
            case "quit":
                break
            case "letters":
                print("Tried :", " ".join(sorted(used_letters)))
                continue
            case "hint":
                possible = candidates(words, game.history)
                print(f"{len(possible)} words left, try {best_guess(possible).upper()}")
                continue
            case "stats":
                print_stats()
                continue
        try:
            check_guess(guess, allowed_words)
            marks = game.guess(guess)
        except InvalidGuess as error:
            print(error)
            continue
        used_letters.update(guess)
        print(render(guess, marks))
    if game.is_won:
        print(f"Got it in {len(game.history)}!")
    else:
        print(f"The word was {secret.upper()}.")
    return len(game.history), game.is_won
```
:::

---

### If time permits

- Add a `board` command to `play` that prints the game with `print(game)`.
- Write a `class Stats` that wraps the database connection of Exercise 10, with methods `record(secret, guesses, won)` and `summary()`, and let `__main__` use a `Stats` object instead of calling `connect()` and `record_game` itself. There is no reference solution for these steps.
