import importlib.metadata as metadata

from rich import box
from rich.console import Console
from rich.table import Table

console = Console()

CANDIDATES: list[str] = ["tqdm", "rich", "typer", "httpx", "requests", "numpy", "pandas"]


def licence(dist: metadata.Distribution) -> str:
    # Modern wheels carry License-Expression, an SPDX string.
    expression = dist.metadata.get("License-Expression")
    if expression:
        return str(expression)
    for classifier in dist.metadata.get_all("Classifier") or []:
        if str(classifier).startswith("License :: OSI Approved :: "):
            return str(classifier).removeprefix("License :: OSI Approved :: ")
    value = str(dist.metadata.get("License") or "").strip()
    if value and "\n" not in value and len(value) < 40:
        return value
    return "-"


def docs_url(dist: metadata.Distribution) -> str:
    links: dict[str, str] = {}
    for entry in dist.metadata.get_all("Project-URL") or []:
        label, _, url = str(entry).partition(", ")
        links[label.strip().lower()] = url
    for wanted in ("documentation", "docs", "homepage"):
        if wanted in links:
            return links[wanted]
    return str(dist.metadata.get("Home-page") or "-")


def hard_requirements(dist: metadata.Distribution) -> int:
    return sum(1 for line in dist.requires or [] if "extra ==" not in line)


def main() -> None:
    table = Table(
        title="What is actually installed, and what it claims about itself",
        box=box.ROUNDED,
        header_style="bold magenta",
        row_styles=["", "dim"],
    )
    table.add_column("Package", style="cyan", no_wrap=True)
    table.add_column("Version", justify="right")
    table.add_column("License")
    table.add_column("Dependencies", justify="right")
    table.add_column("Docs", overflow="fold")

    for name in CANDIDATES:
        try:
            dist = metadata.distribution(name)
        except metadata.PackageNotFoundError:
            table.add_row(name, "[red]not installed[/]", "-", "-", "-")
            continue
        # A long dependency list is not a fault, but it is a cost: everything
        # in it is code you are also trusting and also have to keep updated.
        count = hard_requirements(dist)
        weight = "green" if count <= 4 else "yellow"
        table.add_row(
            name,
            dist.version,
            licence(dist),
            f"[{weight}]{count}[/]",
            docs_url(dist),
        )

    console.print(table)

    console.print(
        "\n[bold]Before you depend on it[/], look for :\n"
        "  a release in the last year, a real documentation site, an OSI licence,\n"
        "  issues that get answered, and a dependency list you could live with.\n"
        "Then [bold cyan]uv add <name>[/], which writes pyproject.toml and the lockfile."
    )


if __name__ == "__main__":
    main()
