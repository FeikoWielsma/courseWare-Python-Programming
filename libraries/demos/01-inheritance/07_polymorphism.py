class Shape:
    def area(self) -> float:
        return 0

    pass


class Circle(Shape):
    def area(self):
        r = 2
        return 3.14 * r * r

    pass


class Square(Shape):
    def area(self):
        length = 4
        return length * length

    pass


my_shapes = [Square(), Square(), Circle(), Shape()]
for shape in my_shapes:
    print(shape.area())


BOOK_ROWS: list[dict[str, str]] = [
    {"title": "A Light in the Attic", "price": "51.77"},
    {"title": "Tipping the Velvet", "price": "53.74"},
    {"title": "Soumission", "price": "50.10"},
]

QUOTE_ROWS: list[dict[str, str]] = [
    {"text": "The world as we have created it is a process of our thinking.", "author": "Einstein"},
    {"text": "It is our choices that show what we truly are.", "author": "Rowling"},
]

AUTHOR_ROWS: list[dict[str, str]] = [
    {"name": "Albert Einstein", "born": "1879"},
    {"name": "J.K. Rowling", "born": "1965"},
]


class Scraper:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rows: list[dict[str, str]] = []

    def collect(self) -> None:
        self.rows = self.parse()

    def parse(self) -> list[dict[str, str]]:
        return []

    def report(self) -> str:
        return f"{self.name:<28} {len(self.rows):>3} rows"


class BooksScraper(Scraper):
    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in BOOK_ROWS]


class QuotesScraper(Scraper):
    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in QUOTE_ROWS]


class AuthorsScraper(Scraper):
    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in AUTHOR_ROWS]


def run_all(scrapers: list[Scraper]) -> int:
    total = 0
    for scraper in scrapers:
        scraper.collect()  # a different parse() runs each time round
        print(scraper.report())
        total += len(scraper.rows)
    return total


def main() -> None:
    scrapers: list[Scraper] = [
        BooksScraper("books.toscrape.com"),
        QuotesScraper("quotes.toscrape.com"),
        AuthorsScraper("quotes.toscrape.com/authors"),
    ]

    total = run_all(scrapers)
    print(f"\n{'total':<28} {total:>3} rows")

    # Adding a fourth scraper changes nothing in run_all; it changes the list only.
    print(f"\nrun_all handled {len(scrapers)} classes and knows the name of none of them")


if __name__ == "__main__":
    main()
