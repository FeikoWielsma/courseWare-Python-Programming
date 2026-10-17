BOOK_ROWS: list[dict[str, str]] = [
    {"title": "A Light in the Attic", "price": "51.77"},
    {"title": "Soumission", "price": "50.10"},
]


class RowStore:
    def __init__(self, label: str) -> None:
        self.label: str = label
        self.rows: list[dict[str, str]] = []

    def add_all(self, rows: list[dict[str, str]]) -> None:
        self.rows.extend(rows)

    def as_lines(self) -> list[str]:
        return [f"{self.label} | {row['title']:<24} {row['price']:>6}" for row in self.rows]


class Scraper:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def parse(self) -> list[dict[str, str]]:
        return []


class DictScraper(dict[str, str]):
    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in BOOK_ROWS]


class BooksScraper(Scraper):
    def __init__(self, name: str, store: RowStore) -> None:
        super().__init__(name)
        self.store: RowStore = store

    def parse(self) -> list[dict[str, str]]:
        return [row.copy() for row in BOOK_ROWS]

    def collect(self) -> None:
        self.store.add_all(self.parse())


def public_names(cls: type) -> set[str]:
    return {name for name in dir(cls) if not name.startswith("_")}


def main() -> None:
    store = RowStore("books")
    books = BooksScraper("books.toscrape.com", store)
    books.collect()
    for line in store.as_lines():
        print(line)

    # A wrong base class is not a style question; it is a public interface nobody asked for.
    borrowed = sorted(public_names(DictScraper) - {"parse"})
    print(f"\nDictScraper now answers to {len(borrowed)} dict methods: {borrowed}")
    print(f"BooksScraper answers to: {sorted(public_names(BooksScraper))}")

    # Nothing stops a caller from emptying a scraper, because a dict can be emptied.
    scraper = DictScraper()
    scraper["title"] = "Soumission"
    scraper.clear()
    print(f"scraper.clear() was allowed, and left {scraper}")

    print("\nThe test, said out loud:")
    print(f"  a BooksScraper is a Scraper   -> {isinstance(books, Scraper)}   so inherit")
    print(f"  a BooksScraper is a RowStore  -> {isinstance(books, RowStore)}  so do not")
    print(f"  a BooksScraper has a RowStore -> {isinstance(books.store, RowStore)}   so hold one")


if __name__ == "__main__":
    main()
