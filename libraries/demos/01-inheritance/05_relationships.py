class Scraper:
    def __init__(self, name: str) -> None:
        self.name: str = name


class BooksScraper(Scraper):
    pass


class QuotesScraper(Scraper):
    pass


class PagedBooksScraper(BooksScraper):
    """Two levels down, which is where the difference starts to matter."""


def show(question: str, answer: bool) -> None:
    print(f"{question:<44} {answer}")


def main() -> None:
    books = BooksScraper("books.toscrape.com")
    paged = PagedBooksScraper("books.toscrape.com, all pages")

    print("Relationships between the classes:")
    show("issubclass(BooksScraper, Scraper)", issubclass(BooksScraper, Scraper))
    show("issubclass(PagedBooksScraper, Scraper)", issubclass(PagedBooksScraper, Scraper))
    show("issubclass(BooksScraper, QuotesScraper)", issubclass(BooksScraper, QuotesScraper))
    show("issubclass(Scraper, object)", issubclass(Scraper, object))

    print("\nRelationships between an object and the classes:")
    show("isinstance(books, BooksScraper)", isinstance(books, BooksScraper))
    show("isinstance(books, Scraper)", isinstance(books, Scraper))
    show("isinstance(books, QuotesScraper)", isinstance(books, QuotesScraper))
    show("isinstance(paged, BooksScraper)", isinstance(paged, BooksScraper))

    print("\nisinstance accepts a subclass, an exact type check does not:")
    show("isinstance(paged, BooksScraper)", isinstance(paged, BooksScraper))
    show("type(paged) is BooksScraper", type(paged) is BooksScraper)

    # isinstance takes a tuple, which is the readable way to ask about several types.
    show(
        "isinstance(books, (QuotesScraper, BooksScraper))",
        isinstance(books, (QuotesScraper, BooksScraper)),
    )


if __name__ == "__main__":
    main()
