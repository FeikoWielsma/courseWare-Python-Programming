import time

from rich.console import Console
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    track,
)

console = Console()

HOSTS: list[str] = ["web01", "web02", "web03", "db01", "db02", "cache01"]


def main() -> None:
    for host in track(HOSTS, description="Collecting facts", console=console):
        time.sleep(0.2)
        _ = host

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=30),
        TaskProgressColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        download = progress.add_task("download", total=len(HOSTS))
        parse = progress.add_task("parse", total=len(HOSTS))
        store = progress.add_task("store", total=len(HOSTS))

        # Three tasks moving at different speeds, all on screen at once. This
        # is the thing tqdm makes hard and rich makes ordinary.
        for step in range(len(HOSTS)):
            progress.advance(download)
            if step >= 1:
                progress.advance(parse)
            if step >= 2:
                progress.advance(store)
            time.sleep(0.35)

        progress.update(parse, completed=len(HOSTS))
        progress.update(store, completed=len(HOSTS))

    # Inside a Progress block, print() is redirected and does not corrupt the
    # display, which is the one place rich is friendlier than tqdm.
    console.print("[green]All three stages finished.[/]")


if __name__ == "__main__":
    main()
