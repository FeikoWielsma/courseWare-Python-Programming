import requests

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

# requests has no default timeout. Without one, a server that accepts the
# connection and then says nothing hangs the script for ever.
response = requests.get(URL, timeout=10, headers={"User-Agent": "SpiralTrain-Day4/1.0"})

print(response.status_code)
print(response.headers["content-type"])
print(f"{len(response.text):,} characters")
print(response.text.count("product_pod"), "books on the page")
print(response.text)
