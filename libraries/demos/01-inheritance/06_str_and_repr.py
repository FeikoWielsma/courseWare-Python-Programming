class BareScraper:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rows: list[dict[str, str]] = []


class Scraper:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rows: list[dict[str, str]] = []

    def __str__(self) -> str:
        return f"{self.name} with {len(self.rows)} rows"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r}, rows={len(self.rows)})"


class BooksScraper(Scraper):
    pass


def main() -> None:
    bare = BareScraper("books.toscrape.com")
    print("Without the two methods:")
    print(f"  print()  -> {bare}")

    books = BooksScraper("books.toscrape.com")
    books.rows = [
        {"title": "Soumission", "price": "50.10"},
        {"title": "Tipping the Velvet", "price": "53.74"},
    ]

    print("\nWith them, inherited from Scraper:")
    print(f"  print()  -> {books}")
    print(f"  str()    -> {str(books)}")
    print(f"  repr()   -> {books!r}")

    # A container prints the repr of what is inside it, never the str. This is why
    # a list of objects shows angle brackets and hex addresses without a __repr__.
    print(f"\n  in a list, with __repr__    -> {[books]}")
    print(f"  in a list, without one      -> {[bare]}")

    print(f"\n  f-string {{value}}  uses __str__  -> {books}")
    print(f"  f-string {{value!r}} uses __repr__ -> {books!r}")


if __name__ == "__main__":
    main()
