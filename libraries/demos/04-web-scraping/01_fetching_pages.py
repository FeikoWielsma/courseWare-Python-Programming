import io
import sys
from pathlib import Path

import requests

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

# requests has no default timeout. Without one, a server that accepts the
# connection and then says nothing hangs the script for ever.
if "--live" in sys.argv:
    response = requests.get(URL, timeout=10, headers={"User-Agent": "SpiralTrain-Day4/1.0"})
else:
    # A response backed by the supplied page, without an HTTP request.
    fixture = Path(__file__).resolve().parents[2] / "data" / "books-fixture.html"
    response = requests.Response()
    response.status_code = 200
    response.url = URL
    response.encoding = "utf-8"
    response.headers["content-type"] = "text/html; charset=utf-8"
    response.raw = io.BytesIO(fixture.read_bytes())

print(response.status_code)
print(response.headers["content-type"])
print(f"{len(response.text):,} characters")
print(response.text.count("product_pod"), "books on the page")
print(response.text)
