# Exercise 2 : Variables and Data Types

A Wordle game compares a guess with the secret word before it can give feedback. Start by reading and displaying a guess, then clean the text and compare its letters with one known secret.

Continue in your own `wordle` project, or start from `exercises/starters/02-variables-and-data-types/`, which is the finished Exercise 1. Run the program after every change with :

```bash
uv run python wordle.py
```

Some steps give you the code and some leave a part to complete. Try each part before opening its solution. The early checks use temporary `print()` lines; the instructions say when to replace them.

---

### Step 1 : A secret and a guess

#### 1a

Replace the contents of `wordle.py` with :

```python
secret = "crane"
guess = input("Your guess: ")
print(guess)
```

Run it, type `Slate` and press Enter. The program waits for the answer, stores it in `guess`, and then displays it :

```text
Your guess: Slate
Slate
```

Change the typed answer and run it again. The value of `secret` stays fixed in the file; the value of `guess` comes from the player.

:::hint
The slide *Reading Keyboard Input* shows `input()` storing text in a variable, followed by `print()` displaying that variable.
:::

#### 1b

Add a line between `input()` and `print()` that removes surrounding whitespace and converts the guess to lower case. Store the cleaned text back in `guess`.

Run it and type `  Slate `, including the spaces. The displayed answer should now be `slate` :

```text
slate
```

:::hint
The slide *Cleaning Photo Filenames* shows `.strip().lower()`. Apply those methods to `guess`, then assign their result back to `guess`.
:::

:::solution
```python
guess = guess.strip().lower()
```
:::

#### 1c

Replace the temporary `print(guess)` with these two supplied display lines. Keep them as written; the comparisons come in Step 2.

```python
print("WORDLE")
print(f"Secret: {secret.upper()}    Guess: {guess.upper()}")
```

The first line is a heading. The second displays the secret and the cleaned guess in upper case. Run it with `  Slate ` again. The two display lines after the prompt are :

```text
WORDLE
Secret: CRANE    Guess: SLATE
```

The stored guess is still lower case: `.upper()` produces the text used for display.

:::hint
The slide *f-Strings* places values inside braces. Plain text outside the braces is printed as written.
:::

### Step 2 : Letter by letter

Type a guess of exactly five letters for the rest of this exercise. A shorter guess would stop the table with an `IndexError`, because `guess[4]` would not exist. Exercise 4 adds a condition that rejects such input before indexing it.

#### 2a

Below the display lines, add two temporary `print()` statements. The first should display whether the first letter of `guess` equals the first letter of `secret`. The second should display whether that guess letter occurs anywhere in the secret.

Run the program with `react`. Its first letter is `r`, while the secret starts with `c`; `r` does occur elsewhere in `crane`. The two new lines should therefore be :

:::output
```text
False
True
```
:::

:::hint
The slide *String Operations* selects the first character with index `0`. *Comparison Operators* shows `==`, and *Logical, Membership, Identity Operators* shows `in`.
:::

:::solution
```python
print(guess[0] == secret[0])
print(guess[0] in secret)
```
:::

#### 2b

Replace those two temporary statements with this supplied header and first row. The row asks the same two questions, with labels separating their answers :

```python
print("Position / Same place / In secret")
print(f"0 / {guess[0] == secret[0]} / {guess[0] in secret}")
```

Copy the first row four times and change each copy to the next position, from `1` to `4`. Change the printed position and both `guess[...]` indexes; change the `secret[...]` index in the same-place comparison too. Keep the two comparisons in each line.

:::hint
The slide *String Operations* indexes individual characters. In every row, use the same position for the printed number, the selected guess letter and the selected secret letter.
:::

:::output
```text
Your guess: react
WORDLE
Secret: CRANE    Guess: REACT
Position / Same place / In secret
0 / False / True
1 / False / True
2 / True / True
3 / False / True
4 / False / False
```
:::

:::solution
```python
print(f"1 / {guess[1] == secret[1]} / {guess[1] in secret}")
print(f"2 / {guess[2] == secret[2]} / {guess[2] in secret}")
print(f"3 / {guess[3] == secret[3]} / {guess[3] in secret}")
print(f"4 / {guess[4] == secret[4]} / {guess[4] in secret}")
```

Exercise 4 replaces these repeated rows with a loop. For now, keeping each position visible makes the two comparisons easier to check.
:::

### Step 3 : Length, slices and counts

Three more questions about the guess and the secret, each answered in one line :

```python
print(f"Five letters: {...}")
print(f"First two: {...}, last two: {...}")
print(f"The secret contains {...} letter e characters.")
```

The first is a check the game will need on every guess : does it have five letters? It only prints `True` or `False` for now. It does not protect the table of Step 2, which indexes the guess before this line runs, so keep typing five letters. The second takes the guess apart with slices. The third counts how often `e` occurs in the secret.

:::hint
The slide *String Operations* shows slices, including ones that count from the end, and *Built-in String Methods* has `len` and the string methods.
:::

:::hint
`len` gives the length of a string, and comparing it with `==` gives `True` or `False`. A slice `word[start:stop]` can leave out either end, and a negative index counts from the end : `word[-1]` is the last letter.
:::

:::hint
Strings have a method that counts how often a piece of text occurs in them, and it is named after what it does. You call it on the secret, with the letter as its argument.
:::

:::solution
```python
print(f"Five letters: {len(guess) == 5}")
print(f"First two: {guess[:2]}, last two: {guess[-2:]}")
print(f"The secret contains {secret.count('e')} letter e characters.")
```

Inside this double-quoted f-string, single quotes make the inner string literal easy to distinguish : `'e'`. Python 3.14 also allows double quotes inside the expression.
:::

### Step 4 : Line breaks and raw strings

A backslash in a string starts an escape sequence : `\t` is a tab and `\n` a line break. Print two lines with one call, then print a sentence that shows a backslash as it is written :

```python
print("First line\nSecond line")
print(r"The escape sequence \t inserts a tab.")
```

The `r` in front of the second string makes it a raw string, in which a backslash is an ordinary character. Remove the `r`, run the program, and see what happens to the line. Then put it back. The slides *Escape Characters* and *Raw and Unicode Strings* list the other sequences.

:::hint
The slides *Escape Characters* and *Raw and Unicode Strings* compare an escape sequence with the same characters inside a raw string.
:::

Run the complete program once more and compare :

:::output
```text
Your guess: react
WORDLE
Secret: CRANE    Guess: REACT
Position / Same place / In secret
0 / False / True
1 / False / True
2 / True / True
3 / False / True
4 / False / False
Five letters: True
First two: re, last two: ct
The secret contains 1 letter e characters.
First line
Second line
The escape sequence \t inserts a tab.
```
:::

The complete file is in `solutions/02-variables-and-data-types/wordle.py`.

### If time permits

Try aligning the comparison output in columns. The appendix slide *Formatting Text Columns* and `demo06 · text_columns` show widths and alignment. For example, replace the heading with `print(f"{' WORDLE ':*^28}")`, or try `print(f"{guess[0] == secret[0]!s:^14}")` for one comparison. Keep this display experiment separate from the comparisons themselves.


A game has a number of guesses. Ask the player how many they want, convert the answer with `int()`, and print it back in a sentence. Then run the program again and answer `six`. Read the last line of the error that Python prints : which exception is it, and what does its message tell you about what `int()` accepts? The slide *Type Conversions* shows the conversion functions. There is no reference solution for this step.
