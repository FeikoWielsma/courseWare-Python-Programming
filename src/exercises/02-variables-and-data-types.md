# Exercise 2 : Variables and Data Types

A Wordle game has to compare a guess with the secret word, letter by letter, before it can tell you anything. In this exercise you do that for one guess against one known word, using nothing but strings and f-strings. It takes about 45 minutes.

Continue in your own `wordle` project, or start from `exercises/starters/02-variables-and-data-types/`, which is the finished Exercise 1. Run the program after every step with :

```bash
uv run python wordle.py
```

Every step is marked with how much help it gives :

- ★ the code is given; type it in and read it
- ★★ a skeleton is given; you fill in the body
- ★★★ only the signature and the tests are given

Steps marked ★★ have a reference solution. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 : A secret and a guess {★}

Replace the contents of `wordle.py` with a fixed secret word and a guess typed by the player :

```python
secret = "crane"
guess = input("Your guess: ").strip().lower()

print(f"{' WORDLE ':*^28}")
print(f"Secret: {secret.upper()}    Guess: {guess.upper()}")
```

`input` always returns a string. `.strip()` removes the spaces a player types by accident around the word, and `.lower()` makes `Slate` and `slate` the same guess. Each method returns a new string, so they can be chained.

In the banner, `:*^28` is a format specification : centre the text (`^`) in 28 characters, and fill the space on both sides with `*`. Run the program and type `  Slate ` with the spaces :

```text
Your guess:   Slate 
********** WORDLE **********
Secret: CRANE    Guess: SLATE
```

### Step 2 : Letter by letter {★★}

For each of the five positions, the game needs the answer to two questions : is the letter of the guess the same as the letter of the secret in that place, and is the letter of the guess anywhere in the secret? Print the answers as a small table, one row per position.

The header and the shape of the first row are given. Fill in the two questions, then add the rows for positions 1 to 4 :

```python
print(f"{'Position':^10}{'Same place':^14}{'In secret':^12}")
print(f"{0:^10}{...:^14}{...:^12}")
```

The widths 10, 14 and 12 keep every column under its heading.

:::hint
`guess[0]` is the first letter of the guess. Comparing two letters with `==` gives `True` or `False`, and so does the `in` operator : `"a" in "crane"` is `True`.
:::

:::hint
If the table shows `1` and `0` instead of `True` and `False`, the format specification is to blame : with a width, a `bool` is formatted as the number it also is. Add `!s` before the colon, as in `{guess[0] in secret!s:^12}`, to turn the value into a string first.
:::

:::output
```text
Your guess: react
********** WORDLE **********
Secret: CRANE    Guess: REACT
 Position   Same place   In secret  
    0         False         True    
    1         False         True    
    2          True         True    
    3         False         True    
    4         False        False    
```
:::

:::solution
```python
print(f"{'Position':^10}{'Same place':^14}{'In secret':^12}")
print(f"{0:^10}{guess[0] == secret[0]!s:^14}{guess[0] in secret!s:^12}")
print(f"{1:^10}{guess[1] == secret[1]!s:^14}{guess[1] in secret!s:^12}")
print(f"{2:^10}{guess[2] == secret[2]!s:^14}{guess[2] in secret!s:^12}")
print(f"{3:^10}{guess[3] == secret[3]!s:^14}{guess[3] in secret!s:^12}")
print(f"{4:^10}{guess[4] == secret[4]!s:^14}{guess[4] in secret!s:^12}")
```

Five lines that differ only in a number are a loop waiting to be written. Exercise 4 writes it.
:::

### Step 3 : Length, slices and counts {★★}

Three more questions about the guess and the secret, each answered in one line :

```python
print(f"Five letters: {...}")
print(f"First two: {...}, last two: {...}")
print(f"The secret contains {...} letter e characters.")
```

The first is a check the game will need on every guess : does it have five letters? The second takes the guess apart with slices. The third counts how often `e` occurs in the secret.

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

Inside an f-string that is written with double quotes, a string literal takes single quotes : `'e'`.
:::

### Step 4 : Tabs and raw strings {★}

A backslash in a string starts an escape sequence : `\t` is a tab and `\n` a line break. Add a second header for the table, laid out with tabs instead of widths, and a line that shows a backslash as it is written :

```python
print("Position\tSame place\tIn secret")
print(r"The escape sequence \t inserts a tab.")
```

The `r` in front of the second string makes it a raw string, in which a backslash is an ordinary character. Remove the `r`, run the program, and see what happens to the line. Then put it back. The slides *Escape Characters* and *Raw and Unicode Strings* list the other sequences.

Run the complete program once more and compare :

:::output
```text
Your guess: react
********** WORDLE **********
Secret: CRANE    Guess: REACT
 Position   Same place   In secret  
    0         False         True    
    1         False         True    
    2          True         True    
    3         False         True    
    4         False        False    
Five letters: True
First two: re, last two: ct
The secret contains 1 letter e characters.
Position	Same place	In secret
The escape sequence \t inserts a tab.
```
:::

The complete file is in `solutions/02-variables-and-data-types/wordle.py`.

### If time permits {★★★}

A game has a number of guesses. Ask the player how many they want, convert the answer with `int()`, and print it back in a sentence. Then run the program again and answer `six`. Read the last line of the error that Python prints : which exception is it, and what does its message tell you about what `int()` accepts? The slide *Type Conversions* shows the conversion functions. There is no reference solution for this step.
