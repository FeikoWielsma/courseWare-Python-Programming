# Exercise 10 : Database Access

The moment a game ends, its result is gone. How many games have you played? What is your win rate? In how many guesses do you usually win? How many games in a row have you won? A database keeps every game and answers each question with one query. In this exercise you move the statistics into SQLite and let the game report them. The SQL statements are given, because the course is about Python : your work is the Python around them, which passes the values in, fetches the rows and turns them into numbers, a bar chart and a streak.

Continue in your own `wordle` project, or start from `exercises/starters/10-database-access/`. The starter is the finished Exercise 9; this exercise hands out nothing. The solution is in `solutions/10-database-access/`. Start a game by pressing Play on `main.py`, with the project folder open in VS Code, so that the database file lands in the project folder.

Some steps give you the code, some a skeleton to complete, and some only a description and a few examples of what it should return. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 : Open the database

:::task
Create `wordle/stats.py` with a function `connect` that opens `wordle.db` and creates the `games` table.
:::

```text
wordle/
    main.py
    wordle.db            <- created by connect
    wordle/
        stats.py         <- new
```

Create `wordle/stats.py`, the module that owns everything to do with the database :

```python
"""Store and summarize completed games in SQLite."""

import sqlite3
from datetime import datetime


def connect(path: str = "wordle.db") -> sqlite3.Connection:
    """Open a database and create the games table when needed."""
    connection = sqlite3.connect(path)
    connection.execute(
        """CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            played_at TEXT,
            secret TEXT,
            guesses INTEGER,
            won INTEGER
        )"""
    )
    return connection
```

`sqlite3.connect` opens the file, and creates it when it does not exist. `CREATE TABLE IF NOT EXISTS` makes the function safe to call at the start of every game : the first call makes the table, later calls find it. SQLite stores Boolean values as integers, so `won` holds `0` for a loss and `1` for a win. Read *DB API Concepts* if you want the picture of connection, cursor and result. Creating the table does not need a `commit()`; only statements that change rows do, and the next step says who commits those.

Check it in a Python session :

```bash
uv run python
```

```python
from wordle.stats import connect

connection = connect()
connection.execute("SELECT name FROM sqlite_master").fetchall()
connection.close()
```

```text
[('games',)]
```

A connection holds the file open until you close it. Closing it explicitly is the habit to keep, and the last step of this exercise makes it automatic.

:::hint
The slide *DB API Concepts* shows connecting to SQLite and creating a table with `execute`. *Check Database Version* shows fetching a result and closing the connection.
:::

There is now a file `wordle.db` in the project folder. It is created in the working directory, so start the game from the project folder. Finding a fixed location for it is left to the last step, If time permits.

### Step 2 : Record a finished game

:::task
Add `record_game` to `wordle/stats.py`. It inserts one finished game with a parameterized statement and leaves the commit to its caller.
:::

```text
wordle/
    main.py
    wordle.db            created by connect
    wordle/
        stats.py         <- add record_game
```

Add a function that stores one game. The time is given, in the ISO text format SQLite sorts correctly :

The slide *Recording a Timestamp* shows `datetime.now().isoformat(timespec="seconds")`. Keep that supplied expression while implementing the database insert.

```python
def record_game(connection: sqlite3.Connection, secret: str, guesses: int, won: bool) -> None:
    """Insert one game using a parameterized statement; the caller commits."""
    played_at = datetime.now().isoformat(timespec="seconds")
    ...
```

Insert a row with the time, the secret, the number of guesses and the result. Do not build the SQL text with an f-string, however convenient. Write `?` for each value in the statement and pass the values as a tuple to `execute`; the driver then handles quoting and nobody can sneak SQL in through a value. See *Inserting Data* and *Parameterized Queries*. The function does **not** commit. A transaction has exactly one owner : the code that calls `record_game` decides when the work becomes permanent, so that several inserts can succeed or fail together. Step 6 shows the caller. See *Committing Data* and *Transactions*.

Try it in the Python session :

```python
from wordle.stats import connect, record_game

connection = connect()
record_game(connection, "crane", 2, True)
connection.execute("SELECT * FROM games").fetchall()
connection.close()
```

```text
[(1, '2026-10-17T10:08:15', 'crane', 2, 1)]
```

The `id` is filled in by the database, and your time is of course a different one. Nothing was committed, so closing the connection threw the row away; this experiment leaves no game behind in `wordle.db`.

:::hint
The slide *Parameterized Queries* writes `?` in the statement and passes the values as a tuple after it.
:::

:::hint
The statement is `INSERT INTO games (played_at, secret, guesses, won) VALUES (?, ?, ?, ?)`. Store the Boolean as an integer with `int(won)`.
:::

:::solution
```python
def record_game(connection: sqlite3.Connection, secret: str, guesses: int, won: bool) -> None:
    """Insert one game using a parameterized statement; the caller commits."""
    played_at = datetime.now().isoformat(timespec="seconds")
    connection.execute(
        "INSERT INTO games (played_at, secret, guesses, won) VALUES (?, ?, ?, ?)",
        (played_at, secret, guesses, int(won)),
    )
```
:::

### Step 3 : Totals

:::task
Add `summary` to `wordle/stats.py`. It returns a dictionary with the games played, the games won and the win percentage.
:::

```text
wordle/
    main.py
    wordle.db            created by connect
    wordle/
        stats.py         <- add summary
```

Now ask the database a question. Write `summary`, which returns a dictionary with how many games were played, how many were won and the win percentage :

```python
def summary(connection: sqlite3.Connection) -> dict:
    """Return totals, guess distribution and the current winning streak."""
    played, won = connection.execute(
        "SELECT COUNT(*), COALESCE(SUM(won), 0) FROM games"
    ).fetchone()
    ...
```

The docstring already names all that the function will return after Step 5. For now the dictionary has three keys : `"played"`, `"won"` and `"win_percentage"`.

The query is in the skeleton. `COUNT(*)` counts the rows of the table, and `SUM(won)` adds up the `won` column, so the `1`s are the wins. One query gives both numbers as a single result row. On an empty table `SUM` has nothing to add and returns `NULL`, which Python sees as `None`; `COALESCE(x, 0)` replaces a `NULL` by `0`. See *Filtering and Grouping Data*. What is left for you is the Python : `fetchone()` returns that row as a tuple, which the skeleton unpacks into two names, and then you build the dictionary and work out the percentage.

With no games the percentage would divide by zero. Divide only when there are games :

```python
percentage = won / played * 100 if played else 0.0
```

This is a conditional expression : it is the value before `if` when the condition is true, and the value after `else` when it is not.

Try it in a Python session on a throwaway database. `connect(":memory:")` builds one in memory, which disappears when the connection does; the slide *Last inserted row id* uses one too. Record four games, three of them won, and ask for the totals; then ask an empty database :

```python
from wordle.stats import connect, record_game, summary

connection = connect(":memory:")
record_game(connection, "crane", 2, True)
record_game(connection, "crane", 6, False)
record_game(connection, "crane", 4, True)
record_game(connection, "crane", 4, True)
summary(connection)
summary(connect(":memory:"))
```

```text
{'played': 4, 'won': 3, 'win_percentage': 75.0}
{'played': 0, 'won': 0, 'win_percentage': 0.0}
```

:::hint
The slide *Retrieving Data* shows `fetchone()`, and *Dictionaries*, in module 03, builds a dictionary from keys and values.
:::

:::hint
`played, won = connection.execute("...").fetchone()` unpacks the one result row into two names.
:::

:::solution
```python
def summary(connection: sqlite3.Connection) -> dict:
    """Return totals, guess distribution and the current winning streak."""
    played, won = connection.execute(
        "SELECT COUNT(*), COALESCE(SUM(won), 0) FROM games"
    ).fetchone()
    percentage = won / played * 100 if played else 0.0
    return {
        "played": played,
        "won": won,
        "win_percentage": percentage,
    }
```
:::

### Step 4 : The guess distribution

:::task
Add the key `"distribution"` to the dictionary of `summary` : the number of games won in each number of guesses.
:::

```text
wordle/
    main.py
    wordle.db            created by connect
    wordle/
        stats.py         <- extend summary
```

How quickly do you win? Add a key `"distribution"` to the dictionary `summary` returns : a dictionary from the number of guesses to the number of games **won** in that many, in order of guesses. Losses are left out. Four games won in 2, 4, 4 and lost, for example, give `{2: 1, 4: 2}`.

The chart comes in Step 6, where `print_stats` turns each count into a row of `#` characters.

The query is given :

```python
"SELECT guesses, COUNT(*) FROM games WHERE won = 1 GROUP BY guesses ORDER BY guesses"
```

Read it from the inside out. `WHERE won = 1` keeps only the won games. `GROUP BY guesses` makes one result row for each distinct value of `guesses`, and `COUNT(*)` counts the games in that group. `ORDER BY guesses` puts the rows in ascending order. Each result row is a `(guesses, count)` tuple. Your work is to run it and turn the rows into the dictionary, then add it to what `summary` returns :

```python
    rows = connection.execute(
        "SELECT guesses, COUNT(*) FROM games WHERE won = 1 GROUP BY guesses ORDER BY guesses"
    ).fetchall()
    distribution = ...
```

The Python session reads `stats.py` once, so start a new one after the change and record the same four games as in Step 3. `summary(connection)["distribution"]` is then `{2: 1, 4: 2}`, and the three totals are as before.

:::hint
The slide *Dictionary Construction with zip*, in module 07, passes pairs of keys and values to `dict`.
:::

:::hint
`fetchall()` returns a list of `(guesses, count)` tuples, and `dict(...)` turns a list of pairs straight into a dictionary.
:::

:::solution
```python
    rows = connection.execute(
        "SELECT guesses, COUNT(*) FROM games WHERE won = 1 GROUP BY guesses ORDER BY guesses"
    ).fetchall()
    distribution = dict(rows)
```

Add `"distribution": distribution` to the dictionary that `summary` returns.
:::

### Step 5 : The current streak

:::task
Add the key `"streak"` to the dictionary of `summary` : the number of games won in a row, up to the latest game.
:::

```text
wordle/
    main.py
    wordle.db            created by connect
    wordle/
        stats.py         <- extend summary
```

The last statistic is the one players care about : how many games in a row have you won, up to now? Add the key `"streak"` to the dictionary : the number of wins since the most recent loss, `0` if the last game was lost or there are no games.

SQL can do this too, but the clearest solution reads the games newest first and counts in Python until it meets a loss. The query is given :

```python
"SELECT won FROM games ORDER BY id DESC"
```

`id` grows with every game, so `ORDER BY id DESC` puts the newest game first. A cursor can be looped over directly, without `fetchall`. Every result row is a tuple, even with one column, so `row[0]` is the `won` value of that game : `1` for a win, `0` for a loss. Look at the rows first, with the four games of Step 3 recorded :

```python
connection.execute("SELECT won FROM games ORDER BY id DESC").fetchall()
```

```text
[(1,), (1,), (0,), (1,)]
```

The loop goes over the same rows, newest first :

```python
for row in connection.execute("SELECT won FROM games ORDER BY id DESC"):
```

In a new Python session, record the four games of Step 3 : the last two were won, so the streak is `2`. Record one more lost game and it drops to `0`. An empty database has a streak of `0` too :

```python
summary(connection)["streak"]                          # 2
record_game(connection, "crane", 6, False)
summary(connection)["streak"]                          # 0
summary(connect(":memory:"))["streak"]                 # 0
```

:::hint
The slide *break and continue Statements*, in module 04, leaves a loop early with `break`.
:::

:::hint
Start the streak at `0`. In the loop, `break` when `row[0]` is `0`, and add one to the streak otherwise.
:::

:::solution
```python
    streak = 0
    for row in connection.execute("SELECT won FROM games ORDER BY id DESC"):
        if not row[0]:
            break
        streak += 1
```

Add `"streak": streak` to the dictionary. The finished function is in `solutions/10-database-access/wordle/stats.py`.
:::

### Step 6 : Use the database in the game

:::task
Let `play` return the number of guesses with the result, record every finished game from `main.py`, and add a `stats` command that prints the numbers of `summary`.
:::

```text
wordle/
    main.py              <- record the game
    wordle.db
    wordle/
        game.py          <- play returns two values, add stats
        stats.py
```

#### 6a

Everything is ready to use the database in the game. In `wordle/game.py`, import `closing` from `contextlib`, and `connect` and `summary` from `wordle.stats`; `print_stats` in 6c needs all three. If you did the optional history steps of Exercise 9, remove `history_path`, `record_history`, its two calls, the old `print_stats` and the `csv` and `pathlib` imports : the database takes over.

`play` has returned a `bool` since Exercise 5, and nothing has used it yet. It is what the last argument of `record_game` needs, but `record_game` also needs the number of guesses, and `play` is the only place that knows it. Let `play` return both, as a tuple, and let the program that called `play` record the game :

```python
def play(secret: str, words: list[str], max_guesses: int = 6) -> tuple[int, bool]:
    """Play one game and return the guesses used and whether the secret was found."""
    ...
        if guess == secret:
            print(f"Got it in {guess_count}!")
            return guess_count, True
    print(f"The word was {secret.upper()}.")
    return guess_count, False
```

:::hint
The slide *return Statement* shows that a function returns values to its caller, and *Usage of Tuples*, in module 03, shows unpacking a pair. Return the count with the Boolean on both exit paths.
:::

#### 6b

In `main.py`, keep the secret in a variable, unpack what `play` returns and record the game. Add `from wordle.stats import connect, record_game` :

```python
        secret = "crane"
        guesses, won = play(secret, words)
        with closing(connect()) as connection:
            with connection:
                record_game(connection, secret, guesses, won)
```

Add `from contextlib import closing` at the top. Each `with` has one job :

- The outer `with closing(connect()) as connection:` closes the connection when its block ends. The `with` of a connection does not close it; it only manages the transaction, and a connection that is never closed is reported by Python 3.14 as an unclosed database. `closing` from the standard library calls `close()` for any object that has one.
- The inner `with connection:` is the transaction. When its block ends without an error the changes are committed, and when it ends with an error they are rolled back. This is the single place in the program where a game is committed : `record_game` only inserts, and the caller decides. The inner block ends first, so the commit comes before the close.

A game you stop with Ctrl+C or Ctrl+D never reaches the `record_game` line, so it is not recorded. A game you give up with `quit` ends the loop and counts as lost.

:::hint
The slide *Using with*, in the database module, nests the connection's transaction block inside `closing(...)`. Keep `record_game` inside the inner block so it commits before the connection closes.
:::

#### 6c

Add a `stats` command to `play`, next to `hint`. Like the other commands, it does not use a turn :

```python
            case "stats":
                print_stats()
                continue
```

In `main.py`, list the new command in the welcome message : `"Guess the five-letter word. Type 'quit', 'letters', 'hint' or 'stats'."`. Then write `print_stats` in `wordle/game.py`, below `play`. It must print three lines : the totals and win rate with one decimal, the wins per guess count as `#` bars, and the streak :

```python
def print_stats() -> None:
    """Print database totals, a guess chart and the current winning streak."""
    with closing(connect()) as connection:
        totals = summary(connection)
    print(...)  # Games played: 4; won: 3; win rate: 75.0%.
    chart = ...
    print(...)  # Wins by guesses: 1: # 2: # 3: #
    print(...)  # Current streak: 1
```

Play four games with `secret = "crane"` in `main.py` : win in two (`slate`, `crane`), win in one (`crane`), give up (`quit`) and win in three (`slate`, `trace`, `crane`). Type `stats` at the first prompt of a fifth game :

```text
Games played: 4; won: 3; win rate: 75.0%.
Wins by guesses: 1: # 2: # 3: #
Current streak: 1
```

:::hint
The slide *String Operators*, in module 02, lists `*` for repetition, *Format Specifications* shows a number with a fixed count of decimals, and *Generator Expressions*, in module 07, writes an expression inside `join`.
:::

:::hint
A chart for one guess count is `f"{guesses}: {'#' * count}"`, and a string can be multiplied by a number. Join the pieces with `" ".join(...)` over `totals["distribution"].items()`.
:::

:::hint
With no wins the chart is an empty string, which prints a confusing nothing. `chart or 'none'` prints `none` instead.
:::

:::solution
```python
def print_stats() -> None:
    """Print database totals, a guess chart and the current winning streak."""
    with closing(connect()) as connection:
        totals = summary(connection)
    print(
        f"Games played: {totals['played']}; won: {totals['won']}; "
        f"win rate: {totals['win_percentage']:.1f}%."
    )
    chart = " ".join(
        f"{guesses}: {'#' * count}"
        for guesses, count in totals["distribution"].items()
    )
    print(f"Wins by guesses: {chart or 'none'}")
    print(f"Current streak: {totals['streak']}")
```

The finished project is in `solutions/10-database-access/`.
:::

---

### If time permits

- If you kept a `history.txt` in the optional steps of Exercise 9, import it into the database once, with a small script. Read the file with `csv.reader` and insert each row; the old file has no time, so store an empty `played_at`.
- Keep `wordle.db` in a fixed place. Build the path with `Path(__file__)`, the way `load_words` finds the word list in Exercise 9, so the statistics are the same wherever you start the game. There is no reference solution for these steps.
