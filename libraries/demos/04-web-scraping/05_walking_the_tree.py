import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

if "--live" in sys.argv:
    html = requests.get(URL, timeout=10).text
else:
    fixture = Path(__file__).resolve().parents[2] / "data" / "books-fixture.html"
    html = fixture.read_text(encoding="utf-8")
soup = BeautifulSoup(html, "lxml")

# The price is easy to find. The book it belongs to is up, not down.
price = soup.select_one("p.price_color")
print(price.parent.name)

pod = price.find_parent("article")
print(pod.select_one("h3 a")["title"])

print(price.find_next_sibling("p").get_text(strip=True))

image = pod.select_one("img")
print(image["alt"])
print(image.get("data-lazy-src"))
print(image.get("width", "unknown"))
