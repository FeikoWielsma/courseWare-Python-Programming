from abc import ABC, abstractmethod

BOOK_ROWS: list[tuple[str, str]] = [
    ("A Light in the Attic", "  $51.77 "),
    ("Tipping the Velvet", " $53.74"),
    ("Soumission", "$50.10  "),
]

QUOTE_ROWS: list[tuple[str, str]] = [
    ("The world as we have created it is a process of our thinking.", " Albert Einstein "),
    ("It is our choices that show what we truly are.", "J.K. Rowling "),
]


class Scraper(ABC):
    def __init__(self, name: str, source: str) -> None:
        self.name: str = name
        self.source: str = source
        self.rows: list[dict[str, str]] = []

    @abstractmethod
    def parse(self) -> list[dict[str, str]]:
        """Return the rows found in one page of this particular site."""

    def clean(self, value: str) -> str:
        return value.strip()

    def collect(self) -> None:
        self.rows = self.parse()

    def row_count(self) -> int:
        return len(self.rows)

    def __str__(self) -> str:
        return f"{self.name} with {self.row_count()} rows"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r}, rows={self.row_count()})"


class BooksScraper(Scraper):
    def clean(self, value: str) -> str:
        return super().clean(value).removeprefix("$")

    def parse(self) -> list[dict[str, str]]:
        return [
            {"key": self.clean(title), "value": self.clean(price)} for title, price in BOOK_ROWS
        ]


class QuotesScraper(Scraper):
    def parse(self) -> list[dict[str, str]]:
        return [
            {"key": self.clean(text), "value": self.clean(author)} for text, author in QUOTE_ROWS
        ]


def run_all(scrapers: list[Scraper]) -> list[dict[str, str]]:
    everything: list[dict[str, str]] = []
    for scraper in scrapers:
        scraper.collect()
        print(f"{scraper!r:<52} {scraper}")
        everything.extend(scraper.rows)
    return everything


def main() -> None:
    scrapers: list[Scraper] = [
        BooksScraper("books", "https://books.toscrape.com/"),
        QuotesScraper("quotes", "https://quotes.toscrape.com/"),
    ]

    rows = run_all(scrapers)

    print(f"\n{'value':<18} key")
    print(f"{'-' * 18} {'-' * 50}")
    for row in rows:
        print(f"{row['value']:<18} {row['key'][:50]}")

    print(f"\n{len(rows)} rows from {len(scrapers)} sites, no network involved")


if __name__ == "__main__":
    main()
