import csv
import sqlite3
from pathlib import Path

from rich import inspect
from rich.console import Console

DATA = Path(__file__).resolve().parents[2] / "data"
console = Console()


def main() -> None:
    console.rule("[bold]What is this thing?")

    # Faced with an unfamiliar object, the reflex is dir() and a lot of squinting.
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        inspect(reader, title="csv.DictReader")

    console.rule("[bold]methods=True adds the call signatures")

    # methods=True is the one you want when the question is 'what can I do
    # with this', rather than 'what is in it'.
    connection = sqlite3.connect(":memory:")
    inspect(connection, methods=True, docs=False, title="sqlite3.Connection")
    connection.close()

    console.rule("[bold]help=True prints the docstrings too")
    inspect(Path, help=True, methods=False)

    console.print(
        "\n[green]Worth memorising:[/] "
        "[bold]from rich import inspect[/] then [bold]inspect(x, methods=True)[/]."
    )


if __name__ == "__main__":
    main()
