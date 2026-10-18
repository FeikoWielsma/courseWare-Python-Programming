from pathlib import Path

import requests
from bs4 import BeautifulSoup

DATA = Path("data")
URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
# Fetch a page or read books-fixture.html, then parse its book records.
