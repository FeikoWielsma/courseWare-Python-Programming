RAW_PRICE: str = "  $51.77  "


class Scraper:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def clean(self, value: str) -> str:
        return value.strip()

    def describe(self) -> str:
        return f"{type(self).__name__} for {self.name}"


class BooksScraper(Scraper):
    def clean(self, value: str) -> str:
        return value.removeprefix("$")


class CarefulBooksScraper(Scraper):
    def clean(self, value: str) -> str:
        return Scraper.clean(self, value).removeprefix("$")

    def describe(self) -> str:
        return f"{super().describe()}, currency aware"


def main() -> None:
    scrapers: list[Scraper] = [
        Scraper("base"),
        BooksScraper("replaces"),
        CarefulBooksScraper("extends"),
    ]

    print(f"raw value from the page: {RAW_PRICE!r}\n")
    for scraper in scrapers:
        print(f"{scraper.name:<10} clean() -> {scraper.clean(RAW_PRICE)!r}")

    # The replacing version never removed the pound sign, because the leading
    # spaces were still there when removeprefix() looked at the first character.
    print()
    for scraper in scrapers:
        print(scraper.describe())


if __name__ == "__main__":
    main()
