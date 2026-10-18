import sys
from pathlib import Path

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

for article in soup.find_all("article", class_="product_pod"):
    title = article.find("h3").find("a")["title"]
    if title == "Sharp Objects":
        price = article.find("p", class_="price_color").text
        # The page spells the rating as a class name, not a number: markup is
        # written for a browser, not for you.
        stars = article.find("p", class_="star-rating")["class"][1]
        print(f"{RATINGS[stars]}  {price:>8}  {title}")
