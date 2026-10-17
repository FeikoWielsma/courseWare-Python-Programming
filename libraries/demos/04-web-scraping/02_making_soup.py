import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

html = requests.get(URL, timeout=10).text
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
