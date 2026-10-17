from rich.console import Console
from rich.panel import Panel

# One Console per program, created at module level, is the usual shape.
console = Console()


def main() -> None:
    console.rule("[bold]Console basics")

    # Markup is square brackets, closed with a bare [/]. It nests.
    console.print("[bold cyan]bold cyan[/], [red]red[/], [green on white]green on white[/]")
    console.print("[bold]disk usage [red]91%[/] on [blue underline]/srv/backup[/][/]")

    # Anything that is not a string gets pretty-printed and syntax coloured,
    # which is the cheapest debugging upgrade in Python.
    console.print({"host": "db01", "cores": 16, "roles": ["primary", "backup"], "up": True})

    console.rule("[bold]Panels and alignment")
    console.print(Panel("Nightly backup finished in 418s", title="backup", border_style="green"))
    console.print("centred", justify="center", style="italic")

    # Escaping: a literal bracket needs doubling, or markup=False.
    console.print("sed -n '1,5p' file[0]", markup=False)

    console.rule("[bold]Status and logging")
    console.log("finished", {"healthy": 12, "degraded": 2})

    # A Console with stderr=True writes to stderr, so a program can be noisy
    # on screen and still behave inside a pipeline.
    errors = Console(stderr=True)
    errors.print("[bold red]ERROR[/] db02 has no last_patched date")


if __name__ == "__main__":
    main()
