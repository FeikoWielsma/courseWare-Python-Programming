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

# Page titles are full of markup whitespace, so collapse it rather than
# trusting what the page hands you.
print(" ".join(soup.title.text.split()))

print(soup.find("article", class_="product_pod").name)
print(len(soup.find_all("article", class_="product_pod")), "articles")

link = soup.find("article", class_="product_pod").find("h3").find("a")
print(link["title"])
print(link["href"])
print(link.attrs)
