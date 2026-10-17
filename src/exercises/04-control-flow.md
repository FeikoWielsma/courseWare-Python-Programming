# Exercise 4 : Control Flow

Everything so far answers questions about a single guess, and then the program ends. With loops and conditions you can finally write the game itself : six guesses, a row of marks after each one, and a win or a loss at the end. At the end you have a game you can play.

Continue in your own `wordle` project, or start from `exercises/starters/04-control-flow/`, which is the finished Exercise 3. Run the game after every step with :

```bash
uv run python wordle.py
```

Some steps give you the code, some a skeleton to complete, and one only the rules and three games to check it with. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 : Six guesses

Exercise 3's script explored the data; this exercise turns it into a game. Replace the contents of `wordle.py` with :

```python
import os
import random
from pathlib import Path

words = Path("words.txt").read_text(encoding="utf-8").split()
secret = os.environ.get("WORDLE_SECRET", random.choice(words))
max_guesses = 6

print("Guess the five-letter word.")

guess_count = 0
while guess_count < max_guesses:
    guess = input(f"Guess {guess_count + 1}/{max_guesses} : ").strip().lower()
    guess_count += 1
    print(guess.upper())

print(f"The word was {secret.upper()}.")
```

The `while` loop runs its indented block again and again for as long as its condition is true. Every pass reads a guess and adds one to `guess_count`, so after six passes the condition is false and the program carries on below the loop. The slide *while Loop* shows the shape.

A random secret makes a game you cannot check, so the secret can be fixed from outside the program. `os.environ` holds the environment variables of the process, and `get` returns the second argument when `WORDLE_SECRET` is not set. In PowerShell, set it for the rest of the session :

```powershell
$env:WORDLE_SECRET = "crane"
uv run python wordle.py
```

In bash, set it for a single run :

```bash
WORDLE_SECRET=crane uv run python wordle.py
```

The outputs in this exercise all use `crane`. In PowerShell, `Remove-Item Env:WORDLE_SECRET` brings the random secret back. Play once : the game takes any six answers, even ones that are not words, and does not yet tell you anything about them.

```text
Guess the five-letter word.
Guess 1/6 : Slate
SLATE
Guess 2/6 : hello
HELLO
```

### Step 2 : Rejecting a guess

A guess of the wrong length, or one that is not in the word list, should not cost the player a turn. Before `guess_count` goes up, check the guess, and when it is not acceptable print a message and go straight back to the top of the loop for another one :

```python
    if ...:
        print("That is not a five-letter word I know.")
        continue

    guess_count += 1
```

`continue` ends the current pass of the loop and starts the next one, so nothing below it runs for a rejected guess. The slide *break and continue Statements* shows it next to `break`, which you need in Step 5.

:::hint
The slide *if Statement* shows the shape of the check. *Logical, Membership, Identity Operators*, in module 02, has `or` and `not in`.
:::

:::hint
There are two reasons to reject a guess, and either one is enough, so join them with `or`. `len(guess) != 5` is the first. For the second, `not in` is the opposite of `in`.
:::

:::output
```text
Guess the five-letter word.
Guess 1/6 : slat
That is not a five-letter word I know.
Guess 1/6 : abcde
That is not a five-letter word I know.
Guess 1/6 : slate
SLATE
```
:::

:::solution
```python
    if len(guess) != 5 or guess not in words:
        print("That is not a five-letter word I know.")
        continue

    guess_count += 1
```

The check comes before `guess_count += 1`. Put it after, and a rejected guess still uses up a turn.
:::

### Step 3 : A row of marks

Now the game should say something about each letter. Replace `print(guess.upper())` with a row that marks every letter :

- `[A]` : the letter is in the right place
- `(A)` : the letter is in the word, somewhere else
- ` A ` : the letter is not in the word

Build the row one letter at a time, starting from an empty string :

```python
    # [A] is in the right place, (A) is in the word elsewhere, A is not in it.
    row = ""
    for position, letter in enumerate(guess):
        if ...:
            row += f"[{letter.upper()}]"
        elif ...:
            row += ...
        else:
            row += ...
    print(row)
```

`enumerate` gives each letter together with its position, 0 to 4, which is what you need to compare it with the letter in the same place of the secret.

:::hint
The slide *Iterating with enumerate* shows the loop, and *elif Statement* shows the chain of conditions.
:::

:::hint
The first condition is the "same place" question of Exercise 2, asked with `letter` and `position` : `letter == secret[position]`. The second is the "in secret" question.
:::

:::hint
Each mark is three characters wide, so the rows line up under each other. The last case is a space, the letter, and a space : `f" {letter.upper()} "`.
:::

:::output
```text
Guess the five-letter word.
Guess 1/6 : slate
 S  L [A] T [E]
Guess 2/6 : error
(E)[R](R) O (R)
Guess 3/6 : crane
[C][R][A][N][E]
Guess 4/6 :
```
:::

:::solution
```python
    # [A] is in the right place, (A) is in the word elsewhere, A is not in it.
    row = ""
    for position, letter in enumerate(guess):
        if letter == secret[position]:
            row += f"[{letter.upper()}]"
        elif letter in secret:
            row += f"({letter.upper()})"
        else:
            row += f" {letter.upper()} "
    print(row)
```
:::

The game still asks for a fourth guess after `crane`, because nothing tells the loop that the word has been found. Step 5 does that.

### Step 4 : Commands

Two words are not guesses but commands : `quit` gives up, and `letters` shows the letters tried so far, in alphabetical order. A set is the natural place to keep the letters tried, because each letter only needs to be in it once.

Create the set before the loop, and add the letters of every accepted guess to it. Change the welcome line, so the player knows about the commands :

```python
max_guesses = 6
used_letters: set[str] = set()

print("Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.")
```

```python
    guess_count += 1
    used_letters.update(guess)
```

Then check for the commands straight after reading the guess, before the check of Step 2 :

```python
    match guess:
        case "quit":
            ...
        case "letters":
            ...
```

For now, `quit` only has to leave the loop; the line below the loop then prints the word.

:::hint
The slide *match Statement* shows the syntax, and *break and continue Statements* shows `break`. *Built-in String Methods* has `sep.join(words)`, and *Set Operations* turns a set into a sorted list with `sorted()`.
:::

:::hint
`break` leaves the loop at once. For `letters`, `sorted(used_letters)` gives a list of the letters in alphabetical order, and `" ".join(...)` turns that list into one string with a space between the letters : `print("Tried :", " ".join(sorted(used_letters)))`.
:::

:::hint
Without a `continue` after printing the letters, the program goes on to the check of Step 2, and `letters` is not a five-letter word.
:::

:::output
```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 : slate
 S  L [A] T [E]
Guess 2/6 : letters
Tried : a e l s t
Guess 2/6 : error
(E)[R](R) O (R)
Guess 3/6 : quit
The word was CRANE.
```
:::

:::solution
```python
    match guess:
        case "quit":
            break
        case "letters":
            print("Tried :", " ".join(sorted(used_letters)))
            continue
```

`set()` is an empty set; `{}` would be an empty dictionary. `update` adds every item of what it is given, so `used_letters.update("slate")` adds five letters.
:::

### Step 5 : Winning and losing

The game has to end properly. These are the rules :

- when the guess is the secret, print `Got it in N!`, with the number of guesses it took, and end the game
- when the six guesses are used up without finding the word, print `Out of guesses. The word was CRANE.`
- when the player types `quit`, print `The word was CRANE.` and end the game
- in every case, the program prints exactly one of those lines

The line below the loop that prints the word goes. Win with `break`, and lose with an `else:` on the `while` loop. Check it with three games against `crane` : one won, one given up and one lost. Play all three and compare with the expected output.

```text
Game 1 : slate, error, crane
Game 2 : slate, quit
Game 3 : slate, error, house, ghost, world, money
```

:::hint
The slide *Loop with else Combination* shows it : a loop can have an `else:` block, at the same indentation as the `while`. It runs when the loop ends because its condition became false, and it does not run when the loop is left with `break`. That is exactly the difference between running out of guesses and finding the word.
:::

:::hint
`quit` leaves the loop with `break` as well, so it skips the `else:` too. That is why the `quit` case now prints the word itself.
:::

:::output
```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 : slate
 S  L [A] T [E]
Guess 2/6 : error
(E)[R](R) O (R)
Guess 3/6 : crane
[C][R][A][N][E]
Got it in 3!
```

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 : slate
 S  L [A] T [E]
Guess 2/6 : quit
The word was CRANE.
```

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 : slate
 S  L [A] T [E]
Guess 2/6 : error
(E)[R](R) O (R)
Guess 3/6 : house
 H  O  U  S [E]
Guess 4/6 : ghost
 G  H  O  S  T 
Guess 5/6 : world
 W  O (R) L  D 
Guess 6/6 : money
 M  O (N)(E) Y 
Out of guesses. The word was CRANE.
```
:::

:::solution
```python
import os
import random
from pathlib import Path

words = Path("words.txt").read_text(encoding="utf-8").split()
secret = os.environ.get("WORDLE_SECRET", random.choice(words))
max_guesses = 6
used_letters: set[str] = set()

print("Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.")

guess_count = 0
while guess_count < max_guesses:
    guess = input(f"Guess {guess_count + 1}/{max_guesses} : ").strip().lower()

    match guess:
        case "quit":
            print(f"The word was {secret.upper()}.")
            break
        case "letters":
            print("Tried :", " ".join(sorted(used_letters)))
            continue

    if len(guess) != 5 or guess not in words:
        print("That is not a five-letter word I know.")
        continue

    guess_count += 1
    used_letters.update(guess)

    # [A] is in the right place, (A) is in the word elsewhere, A is not in it.
    row = ""
    for position, letter in enumerate(guess):
        if letter == secret[position]:
            row += f"[{letter.upper()}]"
        elif letter in secret:
            row += f"({letter.upper()})"
        else:
            row += f" {letter.upper()} "
    print(row)

    if guess == secret:
        print(f"Got it in {guess_count}!")
        break
else:
    print(f"Out of guesses. The word was {secret.upper()}.")
```

The file is also in `solutions/04-control-flow/wordle.py`.
:::

You have a game. Play a few rounds with a random secret : remove the environment variable, or start a new terminal.

### If time permits

Add a third command, `hint`, which reveals one letter of the secret that the player has not found yet, in its place : for example `Letter 4 is N.` A player may use it once per game; a second `hint` says so instead. Think about what counts as found : a letter the player has already had marked `[A]` in that position is not worth revealing. There is no reference solution for this step.
