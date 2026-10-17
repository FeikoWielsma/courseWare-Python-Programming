# Exercise 10 : Database Access

The history file of Exercise 9 can tell you how many games you played, but not much more. What is your win rate? In how many guesses do you usually win? How many games in a row have you won? Every question means another loop over the file. A database answers them in one query. In this exercise you move the statistics into SQLite and let the game report them. The SQL statements are given, because the course is about Python : your work is the Python around them, which passes the values in, fetches the rows and turns them into numbers, a bar chart and a streak.

Continue in your own `wordle` project, or start from `exercises/starters/10-database-access/`. The starter is the finished Exercise 9; this exercise hands out nothing, you write the tests yourself.

Every step is marked with how much help it gives :

- ★ the code is given; type it in and read it
- ★★ a skeleton is given; you fill in the body
- ★★★ only the signature and the tests are given

Steps marked ★★ and ★★★ have a solution that is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards. Allow about 60 minutes.

---

### Step 1 : Open the database {★}

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

`sqlite3.connect` opens the file, and creates it when it does not exist. `CREATE TABLE IF NOT EXISTS` makes the function safe to call at the start of every game : the first call makes the table, later calls find it. SQLite has no `BOOLEAN`, so `won` is an `INTEGER` holding `0` or `1`, the same convention as the history file. Read *DB API Concepts* if you want the picture of connection, cursor and result. Creating the table does not need a `commit()`; only statements that change rows do, and the next step says who commits those.

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

There is now a file `wordle.db` in the project folder. Like the `words.txt` of Exercise 9 used to be, it is created in the working directory, so start the game from the project folder. Finding a fixed location for it is left to the last step, If time permits.

### Step 2 : Record a finished game {★★}

Add a function that stores one game. The time is given, in the ISO text format SQLite sorts correctly :

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
The statement is `INSERT INTO games (played_at, secret, guesses, won) VALUES (?, ?, ?, ?)`. The database has no `bool`, so pass `int(won)`.
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

### Step 3 : Totals {★★}

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

The query is in the skeleton. `COUNT(*)` counts the rows of the table, and `SUM(won)` adds up the `won` column, so the `1`s are the wins. One query gives both numbers as a single result row. On an empty table `SUM` has nothing to add and returns `NULL`, which Python sees as `None`; `COALESCE(x, 0)` replaces a `NULL` by `0`. See *Retrieving Data*. What is left for you is the Python : `fetchone()` returns that row as a tuple, which the skeleton unpacks into two names, and then you build the dictionary and work out the percentage.

Start a test file, `tests/test_stats.py`. It builds a throwaway database in memory, which disappears when the connection does :

```python
"""Checks for the game statistics."""

import sqlite3

from wordle.stats import connect, record_game, summary


def make_db(results: list[tuple[int, bool]]) -> sqlite3.Connection:
    """Return an in-memory database holding one game per result."""
    connection = connect(":memory:")
    for guesses, won in results:
        record_game(connection, "crane", guesses, won)
    return connection


def test_summary_counts_games_and_wins() -> None:
    totals = summary(make_db([(2, True), (6, False), (4, True), (3, True)]))
    assert totals["played"] == 4
    assert totals["won"] == 3
    assert totals["win_percentage"] == 75.0


def test_summary_of_an_empty_database() -> None:
    totals = summary(connect(":memory:"))
    assert totals["played"] == 0
    assert totals["win_percentage"] == 0.0
```

The second test is there for a reason : with no games the percentage would divide by zero. Run `uv run pytest tests/test_stats.py` and make both pass.

:::hint
`played, won = connection.execute("...").fetchone()` unpacks the one result row into two names.
:::

:::hint
Guard the division : `won / played * 100 if played else 0.0`.
:::

:::output
```text
..                                                                       [100%]
2 passed in 0.02s
```
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

### Step 4 : The guess distribution {★★}

How quickly do you win? Add a key `"distribution"` to the dictionary `summary` returns : a dictionary from the number of guesses to the number of games **won** in that many, in order of guesses. Losses are left out. Four games won in 2, 4, 4 and lost, for example, give `{2: 1, 4: 2}`.

The test goes in `tests/test_stats.py` :

```python
def test_distribution_counts_wins_per_guess_count() -> None:
    totals = summary(make_db([(2, True), (4, True), (4, True), (6, False)]))
    assert totals["distribution"] == {2: 1, 4: 2}
```

Make it pass without breaking the first two. The chart comes in Step 6, where `print_stats` turns each count into a row of `#` characters.

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

:::hint
`fetchall()` returns a list of `(guesses, count)` tuples, and `dict(...)` turns a list of pairs straight into a dictionary.
:::

:::output
```text
...                                                                      [100%]
3 passed in 0.02s
```
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

### Step 5 : The current streak {★★★}

The last statistic is the one players care about : how many games in a row have you won, up to now? Add the key `"streak"` to the dictionary : the number of wins since the most recent loss, `0` if the last game was lost or there are no games.

The test goes in `tests/test_stats.py` :

```python
def test_streak_counts_wins_since_the_last_loss() -> None:
    assert summary(make_db([(6, False), (3, True), (4, True)]))["streak"] == 2
    assert summary(make_db([(3, True), (6, False)]))["streak"] == 0
    assert summary(make_db([]))["streak"] == 0
```

SQL can do this too, but the clearest solution reads the games newest first and counts in Python until it meets a loss. The query is given :

```python
"SELECT won FROM games ORDER BY id DESC"
```

`id` grows with every game, so `ORDER BY id DESC` puts the newest game first. A cursor can be looped over directly, without `fetchall`, and every result row is a tuple, even with one column.

:::hint
`for (game_won,) in connection.execute("SELECT won FROM games ORDER BY id DESC"):` gives one `won` value per loop; the parentheses unpack the one-item tuple. Count the wins, and `break` at the first `0`.
:::

:::output
```text
....                                                                     [100%]
4 passed in 0.02s
```
:::

:::solution
```python
    streak = 0
    for (game_won,) in connection.execute("SELECT won FROM games ORDER BY id DESC"):
        if not game_won:
            break
        streak += 1
```

Add `"streak": streak` to the dictionary. The finished function is in `solutions/10-database-access/wordle/stats.py`.
:::

### Step 6 : Use the database in the game {★★}

Everything is ready to replace the history file. In `wordle/game.py`:

- import `closing` from `contextlib`, and `connect` and `summary` from `wordle.stats`; `print_stats` needs all three
- remove `history_path`, `record_history` and the `csv` and `pathlib` imports that only they used
- in `play`, remove the two `record_history(...)` calls

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

In `wordle/__main__.py`, keep the secret in a variable, unpack what `play` returns and record the game. Add `from wordle.stats import connect, record_game` :

```python
        secret = os.environ.get("WORDLE_SECRET", random.choice(words))
        guesses, won = play(secret, words)
        with closing(connect()) as connection, connection:
            record_game(connection, secret, guesses, won)
```

Add `from contextlib import closing` at the top. The `with` line has two parts, and each one has a job :

- `closing(connect())` closes the connection when the block ends. The `with` of a connection does **not** close it; it only manages the transaction, and a connection that is never closed is reported by Python 3.14 as an unclosed database. `closing` from the standard library calls `close()` for any object that has one.
- The second part, `connection`, is the transaction. When the block ends without an error the changes are committed, and when it ends with an error they are rolled back. This is the single place in the program where a game is committed : `record_game` only inserts, and the caller decides. The parts leave in reverse order, so the commit comes before the close.

A game you stop with Ctrl+C or Ctrl+D never reaches the `record_game` line, so it is not recorded. A game you give up with `quit` ends the loop and counts as lost.

Now rewrite `print_stats` so that the `stats` command reports the new numbers. It must print three lines : the totals and win rate with one decimal, the wins per guess count as `#` bars, and the streak :

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

Play four games with `WORDLE_SECRET=crane` : win in two (`slate`, `crane`), win in one (`crane`), give up (`quit`) and win in three (`slate`, `trace`, `crane`). Type `stats` at the first prompt of a fifth game :

```text
Games played: 4; won: 3; win rate: 75.0%.
Wins by guesses: 1: # 2: # 3: #
Current streak: 1
```

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

Delete `history.txt` if you want : the database has taken over. The finished project is in `solutions/10-database-access/`.
:::

---

### If time permits

- Import the `history.txt` of Exercise 9 into the database once, with a small script. Read the file with `csv.reader` and insert each row; the old file has no time, so store an empty `played_at`.
- Keep `wordle.db` in a fixed place. Build the path with `Path(__file__)`, the way you did for the history file in Exercise 9, so the statistics are the same wherever you start the game. There is no reference solution for these steps.
