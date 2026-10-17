import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

soup = BeautifulSoup(requests.get(URL, timeout=10).text, "lxml")

# select always returns a list, select_one the first match or None.
print(len(soup.select("article.product_pod h3 a")), "title links")
print(soup.select("article.product_pod h3 a")[1]["title"])

print(soup.select_one("ul.breadcrumb li.active").text.strip())

# Two class names on one element: both, with no space between them.
print(len(soup.select("p.star-rating.Four")), "books rated four")

print(len(soup.select("div.image_container > a > img[alt]")), "thumbnails")

# The same question asked both ways.
print(len(soup.select("article.product_pod")))
print(len(soup.find_all("article", class_="product_pod")))
