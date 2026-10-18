import httpx
import requests
from rich.console import Console
from rich.table import Table

console = Console()

PAYLOAD: dict[str, object] = {"title": "Imagine", "duration_s": 183}


def fake_httpx(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json=PAYLOAD)


def with_requests() -> dict[str, object]:
    with requests.Session() as session:
        session.headers.update({"user-agent": "day4-tour/1.0"})
        # Offline stand-in for session.get(...).
        return dict(PAYLOAD)


def with_httpx() -> dict[str, object]:
    with httpx.Client(
        base_url="https://player.example",
        transport=httpx.MockTransport(fake_httpx),
        headers={"user-agent": "day4-tour/1.0"},
        timeout=10.0,
    ) as client:
        response = client.get("/now-playing")
        response.raise_for_status()
        return response.json()


def main() -> None:
    console.rule("[bold]Same call, two libraries")
    console.print({"requests": with_requests(), "httpx": with_httpx()})

    table = Table(title="Choosing between them", header_style="bold magenta")
    table.add_column("Question", style="cyan")
    table.add_column("requests", justify="center")
    table.add_column("httpx", justify="center")
    for question, req, hx in [
        ("Sync API you already know", "[green]yes[/]", "[green]yes[/]"),
        ("async / await", "[red]no[/]", "[green]yes[/]"),
        ("HTTP/2", "[red]no[/]", "[green]yes[/]"),
        ("Timeout by default", "[red]no[/]", "[green]yes[/]"),
        ("Testable without a network", "[yellow]add-on[/]", "[green]built in[/]"),
        ("Installed separately", "[green]yes[/]", "[green]yes[/]"),
    ]:
        table.add_row(question, req, hx)
    console.print(table)

    console.print(
        "[green]Either is fine[/] for a synchronous script that fetches a few pages. "
        "Reach for httpx when you need async, HTTP/2, or tests without a network."
    )


if __name__ == "__main__":
    main()
