# Exercise 4 : Scraping a Page Into a Database

In this exercise you build the three steps of a scraper against a real site : you fetch a page from `books.toscrape.com`, parse the twenty books out of the markup, write them into a SQLite database with parameterised inserts, and query the result back. The site exists to be scraped, so you are welcome there as long as you are polite about it.

Work in a file of your own, for example `scrape_books.py`, and run it with `uv run scrape_books.py` from the repository root. The reference answer is in `solutions/solution04-web-scraping/`.

---

### Step 1 : Prove the fetch and the parser work

Fetch the page and make a soup from it. Always pass a `timeout`, because `requests` has no default and a server that goes quiet would hang your script for ever :

```python
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
html = requests.get(URL, timeout=10).text
soup = BeautifulSoup(html, "lxml")
```

Print two things : the page title, and how many `article` elements with class `product_pod` the page contains. You should see the word `Mystery` and the number `20`. That is the whole of step one.

If the title comes out full of newlines, tidy it with `" ".join(soup.title.text.split())`.

---

### Step 2 : One book

Take the first `article.product_pod` and pull three fields out of it :

- the title, which is the `title` attribute of the link inside the `h3`
- the price, which is the text of the `p` with class `price_color`
- the rating, which is the second class name on the `p` with class `star-rating`

```python
pod = soup.select_one("article.product_pod")
link = pod.select_one("h3 a")
print(link["title"], link["href"])
print(pod.select_one("p.price_color").text)
print(pod.select_one("p.star-rating")["class"])
```

Note that the price text carries a currency sign and the rating is a word rather than a number. Deal with both : strip everything that is not a digit or a dot out of the price and turn it into a `float`, and map the words `One` to `Five` onto the numbers 1 to 5 with a dictionary.

---

### Step 3 : All twenty, as records

Write a function that does step 2 for every book on the page and returns a list of dictionaries, one per book :

```python
def parse_books(html: str, page_url: str) -> list[dict]:
    ...
```

Each record should carry `title`, `price_gbp` as a `float`, `rating` as an `int`, `availability` as text, and `url`. Build the url with `urllib.parse.urljoin` against the page address so the stored link is absolute :

```python
url = urljoin(page_url, link["href"])
```

Print the first three records and the number of records. After this function returns, no part of your program should ever mention HTML again.

---

### Step 4 : Into the database

Create `data/exercise-books.db` if it is not there, with one table. Give `url` a `UNIQUE` constraint, because one page is one book :

```python
SCHEMA = """
CREATE TABLE IF NOT EXISTS books (
    id        INTEGER PRIMARY KEY,
    title     TEXT    NOT NULL,
    price_gbp REAL    NOT NULL,
    rating    INTEGER NOT NULL,
    url       TEXT    NOT NULL UNIQUE,
    last_seen TEXT    NOT NULL
);
"""
```

Insert the records with `executemany` and placeholders, never with a formatted string. Named placeholders take your dictionaries directly, once you have added the timestamp :

```python
INSERT = "INSERT INTO books (title, price_gbp, rating, url, last_seen) VALUES (...)"
seen_at = datetime.now(UTC).isoformat(timespec="seconds")
conn.executemany(INSERT, [book | {"seen_at": seen_at} for book in books])
conn.commit()
```

Remember that `sqlite3` does not commit for you. Print how many rows the table holds when you are done.

---

### Step 5 : Query it back

With the data in a table, the questions are ordinary SQL. Answer three of them and print the results :

- the five most expensive books, title and price
- how many books there are at each rating, and the average price per rating
- the number of books priced under twenty

```python
rows = conn.execute(
    "SELECT rating, COUNT(*), ROUND(AVG(price_gbp), 2) FROM books GROUP BY rating"
).fetchall()
```

Setting `conn.row_factory = sqlite3.Row` before the query lets you write `row["rating"]` instead of `row[0]`, which is worth it as soon as a query has more than two columns.

---

### Step 6 : Run it twice

Run your script a second time. If it fails with `sqlite3.IntegrityError` on the unique url, that is the constraint doing its job.

Make the script safe to re-run by turning the insert into an upsert :

```sql
INSERT INTO books (...) VALUES (...)
ON CONFLICT(url) DO UPDATE SET
    price_gbp = excluded.price_gbp,
    last_seen = excluded.last_seen
```

Run it twice more and confirm the row count stays at twenty while `last_seen` moves.

---

### Step 7 : Optional, the second page, politely

The Mystery category has a second page of twelve more books :

```python
PAGE_URLS = [
    "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html",
]
```

Loop over both, parse each, and upsert the lot. Three things make the difference between a scraper a site tolerates and one it blocks :

```python
session = requests.Session()
session.headers["User-Agent"] = "MyScraper/1.0 (you@example.com)"
time.sleep(2)          # between requests, not before the first one
```

Use one `Session` so the connection is reused, name your program in the `User-Agent`, and sleep between the two requests. The row count should go from twenty to thirty two, and running the whole thing again should leave it at thirty two.
