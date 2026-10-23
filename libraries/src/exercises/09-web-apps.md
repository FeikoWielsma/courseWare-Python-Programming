# Exercise 9 : Web Applications

Your Wordle game from the course runs in a terminal. In this exercise you put it in the browser : a FastAPI backend keeps the game, and an HTML page shows the board and a box to type a guess. The page and its colours are supplied, so all the code you write is Python.

Start from `exercises/starters/09-web-apps/`. It contains the `wordle` package from Exercise 13 of the course, a template `templates/index.html` and a short `app.py`. You can replace the `wordle` folder with your own. The solution is in `solutions/solution09-web-apps/`.

The server runs until you stop it with `Ctrl+C` in the terminal. Python reads `app.py` only when the server starts, so stop and start it again after every change.

---

### Step 1 : Show the board

:::task
Add a function `page` and a route for `/` to `app.py`, so that the browser shows an empty board.
:::

```text
09-web-apps/
    app.py               <- change
    templates/
        index.html
    wordle/
```

:::hint
The slide *HTML Templates* shows the operation used in this step.
:::

The starter already creates the application, the templates and a game whose secret is `crane`. Add these two functions below the line `game = ...` :

```python
def page(request: Request, message: str = "") -> HTMLResponse:
    """Draw the board, with an optional message about the last guess."""
    rows = [list(zip(word.upper(), marks, strict=True)) for word, marks in game.history]
    return templates.TemplateResponse(
        request, "index.html", {"game": game, "rows": rows, "message": message},
    )


@app.get("/")
def home(request: Request) -> HTMLResponse:
    return page(request)
```

`page` turns the game's history into rows of `(letter, mark)` pairs, which is what the template draws as coloured tiles. Every route in this exercise answers with `page`.

Press Play on `app.py`, then open `http://127.0.0.1:8000` in a browser. You should see six rows of five empty tiles and a box with a Guess button. The button does not work yet.

There is one `game` in the program, so every browser that opens the page plays the same game, and restarting the server starts it again from the beginning.

---

### Step 2 : Take a guess

:::task
Add a route that receives the form and plays the guess.
:::

:::hint
The slide *Forms* shows the operation used in this step.
:::

The form in `index.html` sends a `POST` request to `/guess`, with the typed word in a field called `word`. Complete this function :

```python
@app.post("/guess")
def guess(request: Request, word: Annotated[str, Form()]) -> HTMLResponse:
    # play the word with game.guess, then answer with the page
    ...
```

Remember to clean up the word first : the player may type capitals or a space.

Restart the server and guess `slate`. The first row fills in : `A` and `E` turn green, the other letters grey.

Pressing the browser's reload button after a guess asks whether to send the form again. Sending it again plays the same word a second time.

:::solution
```python
@app.post("/guess")
def guess(request: Request, word: Annotated[str, Form()]) -> HTMLResponse:
    game.guess(word.strip().lower())
    return page(request)
```
:::

---

### Step 3 : Explain a rejected guess

:::task
Show the reason on the page when a guess is not allowed.
:::

Guess `xxxxx`. The browser shows `Internal Server Error`, and the terminal shows the `InvalidGuess` traceback. `game.guess` raises `InvalidGuess` for a word that cannot be played, and `ValueError` once the game is over; `InvalidGuess` is a kind of `ValueError`.

Catch `ValueError` in `guess`, and pass the text of the error to `page` as the `message`. The template already shows the message under the board.

:::hint
Catch the error with `try` and `except ValueError as error`, as in Exercise 8 of the course. `str(error)` is the reason, for example `That word is not in the word list.`
:::

:::solution
```python
@app.post("/guess")
def guess(request: Request, word: Annotated[str, Form()]) -> HTMLResponse:
    try:
        game.guess(word.strip().lower())
    except ValueError as error:
        return page(request, str(error))
    return page(request)
```
:::

Play a whole game. After a win the page says `Got it in 3!` or similar; after six wrong guesses it shows the word. Both end with a New game button, which you connect in the next step.

---

### Step 4 : A new game

:::task
Add a route for `/new` that starts a new game with a random secret.
:::

:::hint
The slide *Forms* shows the operation used in this step. This form has no fields, so the function takes only `request`.
:::

At the end of a game the template shows a New game button, which sends a `POST` request to `/new`. Write the route : choose a new secret from `load_words()` with `random.choice`, empty the game's history, and answer with the page.

:::solution
```python
@app.post("/new")
def new_game(request: Request) -> HTMLResponse:
    game.secret = random.choice(load_words())
    game.history.clear()
    return page(request)
```
:::

---

### Step 5 : Test without a browser (optional)

:::task
Create `test_app.py` with tests that play the game through `TestClient`.
:::

```text
09-web-apps/
    app.py
    test_app.py          <- new
```

:::hint
The slide *Testing with TestClient* shows the operation used in this step.
:::

`client.post("/guess", data={"word": "slate"})` sends the form just as the browser does. The response's `text` is the HTML page, so a test can look for a tile in it :

```python
from fastapi.testclient import TestClient

from app import app, game

client = TestClient(app)


def test_guess_draws_a_row() -> None:
    game.history.clear()
    response = client.post("/guess", data={"word": "slate"})
    assert '<span class="tile green">A</span>' in response.text
```

The test empties the history first, because every test shares the one `game`. Add a test that an unknown word shows `That word is not in the word list.`, then run the tests from the exercise folder with `uv run pytest`.
