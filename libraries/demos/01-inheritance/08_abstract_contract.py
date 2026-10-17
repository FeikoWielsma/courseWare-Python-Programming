from abc import ABC, abstractmethod

BOOK_ROWS: list[dict[str, str]] = [
    {"title": "A Light in the Attic", "price": "51.77"},
    {"title": "Soumission", "price": "50.10"},
]


class Scraper(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rows: list[dict[str, str]] = []

    @abstractmethod
    def parse(self) -> list[dict[str, str]]:
        """Return the rows found on one page. Every subclass must supply this."""

    def collect(self) -> None:
        self.rows = self.parse()

    def report(self) -> str:
        return f"{self.name}: {len(self.rows)} rows"


class BooksScraper(Scraper):
    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in BOOK_ROWS]


class HalfFinishedScraper(Scraper):
    def report(self) -> str:
        return f"{self.name}: nothing yet"


def main() -> None:
    books = BooksScraper("books.toscrape.com")
    books.collect()
    print(books.report())

    missing = sorted(HalfFinishedScraper.__abstractmethods__)
    print(f"\nStill missing on HalfFinishedScraper: {missing}")
    try:
        HalfFinishedScraper("quotes.toscrape.com")
    except TypeError as error:
        # The failure lands at construction, not three hours later inside collect().
        print(f"TypeError: {error}")

    print("\nThe base class refuses to be built at all:")
    try:
        Scraper("nothing in particular")  # type: ignore[abstract]
    except TypeError as error:
        print(f"TypeError: {error}")

    print(f"\nBooksScraper is still an ordinary subclass: {issubclass(BooksScraper, Scraper)}")


if __name__ == "__main__":
    main()
