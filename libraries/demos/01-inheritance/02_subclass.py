BOOK_ROWS: list[dict[str, str]] = [
    {"title": "A Light in the Attic", "price": "51.77"},
    {"title": "Tipping the Velvet", "price": "53.74"},
    {"title": "Soumission", "price": "50.10"},
]

QUOTE_ROWS: list[dict[str, str]] = [
    {"text": "The world as we have created it is a process of our thinking.", "author": "Einstein"},
    {"text": "It is our choices that show what we truly are.", "author": "Rowling"},
]


class Scraper:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rows: list[dict[str, str]] = []

    def collect(self) -> None:
        self.rows = self.parse()

    def parse(self) -> list[dict[str, str]]:
        # A subclass says what one page looks like; the base class cannot know.
        return []

    def row_count(self) -> int:
        return len(self.rows)

    def report(self) -> str:
        return f"{self.name} = {self.row_count()} rows"


class BooksScraper(Scraper):
    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in BOOK_ROWS]


class QuotesScraper(Scraper):
    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in QUOTE_ROWS]


def public_names(cls: type) -> list[str]:
    return sorted(name for name in dir(cls) if not name.startswith("_"))


def main() -> None:
    for scraper in (BooksScraper("books.toscrape.com"), QuotesScraper("quotes.toscrape.com")):
        scraper.collect()
        print(scraper.report())

    written_here = sorted(name for name in vars(BooksScraper) if not name.startswith("_"))
    available = public_names(BooksScraper)

    print(f"\nWritten inside BooksScraper : {written_here}")
    print(f"Available on a BooksScraper : {available}")
    print(f"Inherited from Scraper      : {sorted(set(available) - set(written_here))}")
    print(f"BooksScraper.__bases__      : {BooksScraper.__bases__}")

    # Attributes are inherited too, because __init__ itself is inherited.
    plain = BooksScraper("no arguments of its own")
    print(f"\nrows exists without BooksScraper defining it: {plain.rows}")
    print(plain.name)


if __name__ == "__main__":
    main()
