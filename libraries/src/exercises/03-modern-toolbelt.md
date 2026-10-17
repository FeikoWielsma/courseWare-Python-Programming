# Exercise 3 : The Modern Toolbelt

In this exercise you take a plain reporting script and give it the two things that make a command-line tool feel finished : a progress bar while it works, and a coloured table when it is done. The whole exercise is about thirty lines of code, and every step runs on its own.

---

### Step 1 : Prove the libraries are there

Make a file `health.py` and check that the three libraries import and print something. Do this before anything else, so that nothing later fails for a reason that has nothing to do with your code :

```python
from rich.console import Console

console = Console()
console.print("[bold green]toolbelt ready[/]")
```

Run it with `uv run health.py`. If you see the words in green, the environment is correct and the rest of the exercise will work.

---

### Step 2 : Read the inventory

Read `data/servers.csv` into a `list[dict[str, str]]` with `csv.DictReader`. Resolve the path from the file rather than from the working directory, so that the script runs from anywhere :

```python
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"


def load() -> list[dict[str, str]]:
    ...
```

Print how many rows you read. You should get fourteen.

---

### Step 3 : Add a progress bar

Write a `check(server: dict[str, str]) -> str` function that decides whether a host is `"ok"`, `"warning"` or `"full"`, based on `used_gb` divided by `disk_gb`. Call `time.sleep(0.2)` inside it, so that the bar has something to show.

Now loop over the servers and wrap the loop in `tqdm`. You do not change the loop body at all :

```python
from tqdm import tqdm

for server in tqdm(servers, desc="Checking", unit="host"):
    ...
```

One host in the file has no `used_gb` reading. Decide what your `check` should return for it rather than letting it raise.

---

### Step 4 : Report anything alarming, without breaking the bar

While the bar is running, print a line for every host that is not `"ok"`. Use `tqdm.write` rather than `print`, and see what happens if you use `print` instead :

```python
tqdm.write(f"{server['hostname']}: {fraction:.0%} used")
```

---

### Step 5 : Print a table at the end

Build a `rich.table.Table` with a column for the host, the site, the disk size and the usage, and add one row per server. Right-align the numbers, and colour the usage cell by how alarming it is :

```python
from rich.table import Table

table = Table(title="Disk usage", header_style="bold magenta")
table.add_column("Host", style="cyan")
table.add_column("Used", justify="right")
```

Remember that the colour goes in the cell text as markup, `f"[red]{value}[/]"`, not as an argument to `add_row`.

---

### Step 6 : Sort and summarise

Sort the rows so the fullest disks are at the top, since that is the only part of the report anybody reads. Then add a footer row giving the total disk space and the overall percentage used, with `table.show_footer = True` and `table.columns[0].footer = ...`.

---

### Step 7 *Optional* : Turn it into a command line tool

Give the script a `--site` option so it reports on one site only, and a `--threshold` option that sets the percentage at which a host counts as alarming. Do it with `typer`, and note how much of the argparse version from module 2 you no longer have to write :

```python
import typer
from typing import Annotated

app = typer.Typer(add_completion=False)


@app.command()
def report(
    site: Annotated[str | None, typer.Option("--site", "-s")] = None,
    threshold: Annotated[int, typer.Option("--threshold", "-t")] = 85,
) -> None:
    """Report disk usage across the estate."""
```

Run it with `--help` and read the help page you did not write.

---

### Step 8 *Optional* : Swap tqdm for rich

Replace the `tqdm` bar with `rich.progress.track`, so that the bar and the table are drawn by the same library and share a colour scheme. Note that inside a rich progress block an ordinary `print` no longer corrupts the display.
