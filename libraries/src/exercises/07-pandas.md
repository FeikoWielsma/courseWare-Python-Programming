# Exercise 6 : Pandas

In this exercise you take the book catalogue that the scraping module put into SQLite, pull it into pandas, and turn it into the spreadsheet somebody upstairs actually asked for. You will read a database with `read_sql`, filter it, add a column, summarise it with `groupby`, and write the answer out as an Excel workbook with two sheets. Nothing here is longer than a couple of lines; the work is choosing the right couple of lines.

Work in a folder `book_report/`, one file per step, and keep the files as you go. Each step reloads the data at the top, which costs nothing on twenty rows and means any file runs on its own.

> **If `data/books.db` is not there yet**, the scraping module has not been run on this machine. Build it with `uv run demos/04-web-scraping/12_rebuilding_from_seed.py`, which recreates the table from the checked-in `data/books-seed.sql` without scraping anything.

---

### Step 1 : Open the database

Create `01_load.py`.

Connect to the database, ask it what tables it has, and read one of them into a DataFrame :

```python
import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

conn = sqlite3.connect(DATA / "books.db")
print(pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'", conn))
books = pd.read_sql("SELECT * FROM books", conn)
conn.close()

print(books.shape)
print(books.head())
```

You should see one table called `books`, a shape of `(20, 9)`, and five rows of book titles.

That is the whole of step one. If those twenty rows printed, your environment works and the rest of the exercise will run.

---

### Step 2 : Look at what you loaded

Create `02_inspect.py` and read the table again.

Print `books.info()` and `books.describe()`. Between them they answer the three questions worth asking about a file you did not write yourself : how many rows are there, what type is each column, and is anything missing.

Then answer two more, using what the demos showed :

1. How many missing values are there in each column? `isna()` gives a mask and a mask sums to a count.
2. What distinct values does the `category` column hold, and how many books are in each? `value_counts()` does both at once.

Note the dtype of `price_gbp` and the dtype of `rating`. One is a float and one is an integer, and pandas worked that out from the database rather than being told.

---

### Step 3 : Filter down to the rows that matter

Create `03_filter.py`.

Build the filters as named variables first, then combine them. A mask with a name is a mask you can read six weeks later :

```python
well_rated = books["rating"] >= 4
in_stock = books["availability"] == "In stock"
affordable = books["price_gbp"] < 40.0
```

Print how many rows each single filter matches, then print the rows that satisfy all three. Remember `&` rather than `and`, and remember the parentheses around each comparison when you write the combination in one line.

Then do the same thing two other ways, so you have seen them :

1. `books[books["rating"].isin([4, 5])]`, which replaces a chain of ORs.
2. `books[books["price_gbp"].between(20.0, 40.0)]`, which replaces two comparisons and includes both ends.

---

### Step 4 : Add the columns the report needs

Create `04_derive.py`.

The catalogue is priced in pounds and the report wants euros. Add a column, rounded to two decimals :

```python
books["price_eur"] = (books["price_gbp"] * RATE).round(2)
```

Then add a `band` column that says `budget` under 20 euros, `mid` under 45, and `premium` above that. `np.where` nested inside another `np.where` does it in one expression, or use `pd.cut` if you would rather name the edges.

Finally sort the whole thing by price, most expensive first, and print the top five titles with their two prices. `sort_values("price_eur", ascending=False).head(5)` is the whole of it, and `nlargest(5, "price_eur")` says the same thing in fewer words.

---

### Step 5 : Summarise by rating

Create `05_group.py`.

This is the `GROUP BY` of the exercise. Produce one row per star rating, with four columns : how many books have that rating, the mean price, the cheapest and the dearest.

Use named aggregation so the output columns arrive with the names you want rather than names you have to fix afterwards :

```python
per_rating = (
    books.groupby("rating")
    .agg(
        titles=("title", "count"),
        mean_price=("price_eur", "mean"),
        ...
    )
    .round(2)
    .reset_index()
)
```

Print it. Then answer the question it raises : does a higher rating cost more? Sorting the result by `mean_price` is enough to see.

---

### Step 6 : Export to Excel

Create `06_export.py`.

Build both frames again : the filtered list of well-rated books from step 3 with the derived columns from step 4, and the per-rating summary from step 5. Then put them in one workbook, one sheet each :

```python
with pd.ExcelWriter(DATA / "book-report.xlsx", engine="openpyxl") as workbook:
    shortlist.to_excel(workbook, sheet_name="shortlist", index=False)
    per_rating.to_excel(workbook, sheet_name="by rating", index=False)
```

Pass `index=False` on both, because the row numbers are pandas' business and not the reader's. Write a CSV of the shortlist as well with `to_csv`, for whoever does not have Excel.

Print the path and the sheet names at the end, then open the file and check that it is really a spreadsheet.

---

### Optional : a chart and a second table

Create `07_chart.py` if you have time.

Two things, either order.

**A picture.** Plot the mean price per rating as a bar chart. Select the non-interactive backend before importing `pyplot`, so the script writes a file instead of waiting for you to close a window :

```python
import matplotlib

matplotlib.use("Agg")
```

Then `per_rating.plot(kind="bar", x="rating", y="mean_price")`, take `.get_figure()` from the axes it returns, and `savefig` it into `data/`.

**A join.** Build a small lookup frame giving each star rating a word :

```python
words = pd.DataFrame({"rating": [1, 2, 3, 4, 5], "verdict": ["poor", ...]})
```

`merge` it onto the summary on `rating` and print the result, so the report reads in English rather than in integers. Then try the same merge with `how="left"` after deleting one row from the lookup, and use `indicator=True` to see exactly which rows failed to match. That check is worth doing on every join you ever write.
