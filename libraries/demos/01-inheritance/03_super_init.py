class Scraper:
    def __init__(self, name: str) -> None:
        print(f"  Scraper.__init__      sets name and rows for {name!r}")
        self.name: str = name
        self.rows: list[dict[str, str]] = []

    def report(self) -> str:
        return f"{self.name}: {len(self.rows)} rows"


class BooksScraper(Scraper):
    def __init__(self, name: str, base_url: str) -> None:
        super().__init__(name)  # first, so the base attributes exist below
        print(f"  BooksScraper.__init__ sets base_url to {base_url!r}")
        self.base_url: str = base_url


class ForgetfulScraper(Scraper):
    def __init__(self, name: str, base_url: str) -> None:
        self.base_url: str = base_url


def main() -> None:
    print("Constructing a BooksScraper:")
    books = BooksScraper("books.toscrape.com", "https://books.toscrape.com/")
    print(f"  -> {books.report()}, base_url = {books.base_url}")

    print("\nConstructing a ForgetfulScraper:")
    broken = ForgetfulScraper("quotes.toscrape.com", "https://quotes.toscrape.com/")
    print(f"  -> base_url = {broken.base_url}, and then:")
    try:
        print(broken.report())
    except AttributeError as error:
        # The object was built successfully; it fails later, somewhere else entirely.
        print(f"  AttributeError: {error}")


if __name__ == "__main__":
    main()
