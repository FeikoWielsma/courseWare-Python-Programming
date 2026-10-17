import inspect

BOOK_ROWS: list[dict[str, str]] = [
    {"title": "A Light in the Attic", "price": "51.77"},
    {"title": "Tipping the Velvet", "price": "53.74"},
    {"title": "Soumission", "price": "50.10"},
]

QUOTE_ROWS: list[dict[str, str]] = [
    {"text": "The world as we have created it is a process of our thinking.", "author": "Einstein"},
    {"text": "It is our choices that show what we truly are.", "author": "Rowling"},
]


class BooksScraper:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rows: list[dict[str, str]] = []

    def collect(self) -> None:
        self.rows = self.parse()

    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in BOOK_ROWS]

    def row_count(self) -> int:
        return len(self.rows)

    def report(self) -> str:
        return f"{self.name}: {self.row_count()} rows"


class QuotesScraper:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rows: list[dict[str, str]] = []

    def collect(self) -> None:
        self.rows = self.parse()

    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in QUOTE_ROWS]

    def row_count(self) -> int:
        return len(self.rows) + 1

    def report(self) -> str:
        return f"{self.name} = {self.row_count()} rows"


METHODS: tuple[str, ...] = ("__init__", "collect", "parse", "row_count", "report")


def identical_methods() -> list[str]:
    return [
        name
        for name in METHODS
        if inspect.getsource(getattr(BooksScraper, name))
        == inspect.getsource(getattr(QuotesScraper, name))
    ]


def main() -> None:
    books = BooksScraper("books.toscrape.com")
    quotes = QuotesScraper("quotes.toscrape.com")

    for scraper in (books, quotes):
        scraper.collect()
        print(scraper.report())

    same = identical_methods()
    print(f"\nMethods written twice, character for character: {len(same)} of {len(METHODS)}")
    for name in same:
        print(f"  {name}")

    # Only parse() differs, and a fix to any of the other four has to be made twice.
    print(f"\nMethods that actually differ: {sorted(set(METHODS) - set(same))}")


if __name__ == "__main__":
    main()
