# Exercise 7 : Pandas

In this exercise you take the book catalogue that the scraping module put into SQLite, pull it into pandas, and turn it into the spreadsheet somebody upstairs actually asked for. You will read a database with `read_sql`, filter it, add a column, summarise it with `groupby`, and write the answer out as an Excel workbook with two sheets. The report uses the same selection, grouping and export operations as the track demos.

Start from `exercises/starters/07-pandas/`. Work from `libraries/`, with your own scripts in `work/book_report/`. The solution files are in `solutions/solution07-pandas/`. Keep one script per step. Each step reloads the data at the top, which costs nothing on twenty rows and means any file runs on its own.

> **If `data/books.db` is not there yet**, the scraping module has not been run on this machine. Build it with `uv run demos/04-web-scraping/12_rebuilding_from_seed.py`, which recreates the table from the checked-in `data/books-seed.sql` without scraping anything.

---

### Step 1 : Open the database

:::hint
*read_sql* and demo `read_sql` show a query result becoming a frame.
:::

Create `01_load.py`.

Connect to the database, ask it what tables it has, and read one of them into a DataFrame :

```python
import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path("data")

conn = sqlite3.connect(DATA / "books.db")
print(pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'", conn))
books = pd.read_sql("SELECT * FROM books", conn)
conn.close()

print(books.shape)
print(books.head())
```

You should see the `books` table and a shape of `(20, 9)` when using the supplied seed.



---

### Step 2 : Look at what you loaded

:::hint
*info and describe* and *Missing Values* show the inspection methods.
:::

Create `02_inspect.py` and read the table again.

Print `books.info()` and `books.describe()`. Between them they answer the three questions worth asking about the catalogue : how many rows are there, what type is each column, and is anything missing.

Then answer these questions :

1. How many missing values are there in each column? `isna()` gives a mask and a mask sums to a count.
2. What distinct values does the `category` column hold, and how many books are in each? `value_counts()` does both at once.

Note the dtype of `price_gbp` and the dtype of `rating`. One is a float and one is an integer, and pandas worked that out from the database rather than being told.

---

### Step 3 : Filter down to the rows that matter

:::hint
*Combining Filters* shows masks, `isin` and `between`.
:::

Create `03_filter.py`.

Build the filters as named variables first, then combine them. A mask with a name is a mask you can read six weeks later :

```python
well_rated = books["rating"] >= 4
in_stock = books["availability"] == "In stock"
affordable = books["price_gbp"] < 40.0
```

Print how many rows each single filter matches, then print the rows that satisfy all three. Remember `&` rather than `and`, and remember the parentheses around each comparison when you write the combination in one line.

Then do the same thing two other ways, using the same masks :

1. `books[books["rating"].isin([4, 5])]`, which replaces a chain of ORs.
2. `books[books["price_gbp"].between(20.0, 40.0)]`, which replaces two comparisons and includes both ends.

---

### Step 4 : Add the columns the report needs

:::hint
*Deriving a Column* and demo `np_where` show column calculations.
:::

Create `04_derive.py`.

The catalogue is priced in pounds and the report wants euros. Add a column, rounded to two decimals :

```python
books["price_eur"] = (books["price_gbp"] * RATE).round(2)
```

Use the fixed teaching rate `RATE = 1.17`; it is an example value, not a current exchange rate.

Then add a `band` column that says `budget` under 20 euros, `mid` under 45, and `premium` above that. `np.where` nested inside another `np.where` does it in one expression, as shown in the NumPy demo `np_where`.

Finally sort the whole thing by price, most expensive first, and print the top five titles with their two prices. `sort_values("price_eur", ascending=False).head(5)` is the whole of it, and `nlargest(5, "price_eur")` says the same thing in fewer words.

---

### Step 5 : Summarise by rating

:::hint
*Named Aggregation* shows named output columns and `reset_index`.
:::

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

:::hint
*Writing Files* shows `ExcelWriter` and `index=False`.
:::

Create `06_export.py`.

Build both frames again : the filtered list of well-rated books from step 3 with the derived columns from step 4, and the per-rating summary from step 5. Then put them in one workbook, one sheet each :

```python
with pd.ExcelWriter(DATA / "book-report.xlsx", engine="openpyxl") as workbook:
    shortlist.to_excel(workbook, sheet_name="shortlist", index=False)
    per_rating.to_excel(workbook, sheet_name="by rating", index=False)
```

Pass `index=False` on both, because the row numbers are pandas' business and not the reader's. Write a CSV of the shortlist as well with `to_csv`, for a program that reads CSV.

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

`merge` it onto the summary on `rating` and print the result, so the report reads in English rather than in integers. Then try the same merge with `how="left"` after deleting one row from the lookup, and use `indicator=True` to see exactly which rows failed to match.
