import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

if "--live" in sys.argv:
    html = requests.get(URL, timeout=10).text
else:
    fixture = Path(__file__).resolve().parents[2] / "data" / "books-fixture.html"
    html = fixture.read_text(encoding="utf-8")
soup = BeautifulSoup(html, "lxml")
category = soup.select_one("ul.breadcrumb li.active").get_text(strip=True)

books = []
for pod in soup.select("article.product_pod"):
    link = pod.select_one("h3 a")
    books.append(
        {
            "title": link["title"],
            "price_gbp": float(re.sub(r"[^\d.]", "", pod.select_one("p.price_color").text)),
            "rating": RATINGS[pod.select_one("p.star-rating")["class"][1]],
            "availability": pod.select_one("p.availability").get_text(strip=True),
            "category": category,
            # Links in a page are relative to that page. urljoin turns them into
            # something you can store, sort, and still click a year later.
            "url": urljoin(URL, link["href"]),
        }
    )

for book in books[:3]:
    print(book)

print(len(books), "books")
print(f"{sum(book['price_gbp'] for book in books) / len(books):.2f} average price")
