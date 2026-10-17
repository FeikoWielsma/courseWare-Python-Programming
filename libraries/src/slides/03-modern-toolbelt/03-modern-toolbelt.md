---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Modern Toolbelt
language: python
---

# Useful Libraries

- The standard library will do the job, but it will not do it nicely :
  - A long loop with no output looks identical to a hung program
  - Columns of numbers lined up by hand stop lining up the moment one grows
  - A traceback tells you what broke, but not what the data was
- Four small libraries fix all of that, and none of them changes how you think :
  - `tqdm` puts a progress bar around a loop you already wrote
  - `rich` prints colour, tables and readable errors
  - `httpx` fetches things off the web
  - `typer` builds a command line from a function signature
- None of them is required, and all of them are one `uv add` away


---

# tqdm Progress Bars

- `tqdm` takes an iterable and returns the same iterable, with a bar :
  - The loop body does not change, and neither does the result
- It measures the rate and estimates the time remaining as it goes

```python
from tqdm import tqdm

for server in tqdm(servers, desc="Checking", unit="host"):
    check(server)
```

- `desc` labels the bar, `unit` names the thing being counted
- It needs a length to show a percentage :
  - A list has one, a generator does not, so pass `total=` yourself

> `demo01 · tqdm_basics`

---

# Nested Bars

- Nested loops give nested bars, one line each :
  - The outer bar counts sites, the inner bar counts hosts within a site
- `leave=False` on the inner bar is the part people forget :
  - Without it every finished inner bar stays on screen forever

```python
for site, hosts in tqdm(sites.items(), desc="Sites"):
    for host in tqdm(hosts, desc=f"  {site}", leave=False):
        check(host)
```

- The outer bar's estimate gets better with every site it finishes

> `demo02 · tqdm_nested`

---

# Manual Bar Updates

- Not all work is a loop over items, so `tqdm` can be driven by hand :
  - Create it with a `total`, then call `update()` with how much you did
- Use it as a context manager so the bar is closed properly on the way out

```python
with tqdm(total=size, desc="Reading", unit="B", unit_scale=True) as bar:
    while chunk := handle.read(65536):
        process(chunk)
        bar.update(len(chunk))
```

- `unit_scale=True` turns 1500 into 1.50k, which keeps the width steady
- `bar.set_postfix(ok=12, failed=2)` hangs a live tally off the right-hand end

> `demo03 · tqdm_manual`

---

# tqdm.write

- A bar owns one line and repaints it by writing over itself
- A plain `print()` writes a newline into the middle of that :
  - The bar loses the line it was drawing on
  - Every repaint leaves another half-finished copy behind
- `tqdm.write()` clears the line, prints, and repaints the bar underneath

```python
for server in tqdm(servers, desc="Scanning"):
    if is_full(server):
        tqdm.write(f"{server['hostname']} is nearly full")
```

- Same arguments as `print`, so converting a script is a search and replace
- Once a bar exists, nothing in the program may call `print` again

> `demo04 · tqdm_write`

---

# rich Console

- `rich` replaces `print` with a `Console` that knows what it is printing :
  - Strings get markup, everything else gets pretty-printed and coloured
- Markup is square brackets, closed with a bare `[/]`, and it nests

```python
from rich.console import Console

console = Console()
console.print("[bold]disk usage [red]91%[/] on [blue underline]/srv[/][/]")
console.print({"host": "db01", "cores": 16, "roles": ["primary"]})
```

- It detects that output is being redirected and drops the colour by itself
- `Console(stderr=True)` writes to standard error, so pipelines still work
- `console.rule("Title")` draws a full-width divider, useful on a projector

> `demo05 · rich_console`

---

# rich Tables

- A `Table` is declared column by column, then fed one row at a time :
  - Alignment, width and style belong to the column, not to the row
- The widths are computed from the data, so nothing has to be guessed

```python
table = Table(title="Server inventory", header_style="bold magenta")
table.add_column("Host", style="cyan", no_wrap=True)
table.add_column("Used", justify="right")
table.add_row("db01", "[red]91%[/]")
console.print(table)
```

- Per-cell colour goes in the text as markup, not as an argument
- `row_styles=["", "dim"]` gives zebra striping for free
- `show_footer` plus `column.footer` produces a totals row

> `demo06 · rich_table`

---

# rich Progress

- `track()` is the one-line form, and behaves like `tqdm` :

```python
from rich.progress import track

for host in track(hosts, description="Collecting facts"):
    collect(host)
```

- `Progress` is the version for when one bar is not enough :
  - Several tasks on screen at once, each with its own total
  - The bar is assembled from column objects rather than a format string
- Inside a `Progress` block, `print` is redirected and cannot corrupt the display
- This is the one place `rich` is meaningfully easier than `tqdm`

> `demo07 · rich_progress`

---

# rich Tracebacks

- One line at the top of a program restyles every uncaught exception :

```python
from rich.traceback import install

install(show_locals=True)
```

- The frames get syntax highlighting and the surrounding lines of source
- `show_locals=True` is the reason to bother :
  - The standard traceback says a `ValueError` happened
  - This one shows the row of data that caused it, with no added `print`
- `console.print_exception()` does the same inside an `except` block

> `demo08 · rich_traceback`

---

# rich inspect

- The usual way to explore an unfamiliar object is `dir()` and a lot of squinting
- `rich.inspect` prints the same information as a readable panel :
  - The repr at the top, then every attribute with its current value

```python
from rich import inspect

inspect(connection, methods=True)
```

- `methods=True` adds the call signatures, for "what can I do with this"
- `help=True` adds the docstrings, for "what does this one mean"
- Worth memorising, because it works on anything, including modules

> `demo09 · rich_inspect`

---

# rich Logging Handler

- Nothing about the `logging` API changes, only the handler does :

```python
import logging
from rich.logging import RichHandler

logging.basicConfig(level="INFO", format="%(message)s",
                    handlers=[RichHandler(rich_tracebacks=True)])
log = logging.getLogger("patchrun")
```

- Levels get colour, times get a column, and the source line is shown
- `rich_tracebacks=True` means `log.exception()` renders the pretty traceback
- Every library that logs through `logging` is improved at the same time
- The format string shrinks to `"%(message)s"` because the handler adds the rest

> `demo10 · rich_logging`

---

# HTTP with httpx

- `httpx.Client` sends HTTP requests and reuses connections.
- `MockTransport` supplies a local response for this offline example.

```python
import httpx


def example_response(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"host": "db01", "disk_pct": 73})


transport = httpx.MockTransport(example_response)
with httpx.Client(transport=transport, timeout=10.0) as client:
    response = client.get("https://example.org/hosts/db01")
    response.raise_for_status()
    print(response.json())  # {'host': 'db01', 'disk_pct': 73}
```

- `raise_for_status()` raises an exception for an HTTP error response.
- For a live service, remove `transport=transport` and use its URL.

> `demo11 · httpx_client`

---

# requests and httpx

<div class="two-col">
<div>

- `requests` :
  - Installed with `uv add requests`
  - Unchanged and stable for a decade
  - Synchronous only
  - No timeout unless you set one

</div>
<div>

- `httpx` :
  - Same names, same shapes
  - Also does `async` and HTTP/2
  - Has a default timeout
  - Testable without a network

</div>
</div>

- Either is fine for a synchronous script that fetches a few pages
- Choose `httpx` when you need `async`, HTTP/2, or tests that never leave the machine
- The scraping module uses `requests`, because that is what the examples use

> `demo12 · requests_or_httpx`

---

# typer

- `typer` builds the parser out of the function it is decorating :
  - The parameter name becomes the option name
  - The annotation becomes the type conversion
  - The default becomes the default, and the docstring becomes the help

```python
@app.command()
def show(
    hostname: Annotated[str, typer.Argument(help="The host to describe.")],
    site: Annotated[str | None, typer.Option("--site", "-s")] = None,
) -> None:
    """Show one host in full."""
```

- There is no parser object, no `add_argument`, and no `dest` to spell twice
- `--help` is generated, coloured, and correct without being written

> `demo13 · typer_cli`

---

# typer Trade-offs

- It is a dependency, and `argparse` is not :
  - A script using `argparse` runs on any Python anywhere, forever
  - A script using `typer` needs an environment, which is what `uv` is for
- It is a thin layer over the same ideas from module 2 :
  - Positionals, options, flags, types, defaults, subcommands, exit codes
  - `typer.Exit(code=1)` is how a command reports failure
- Learn `argparse` first, because it is always there and always readable
- Reach for `typer` when a tool grows past a handful of options


---

# Finding Libraries

- Almost everything is on PyPI, and the search there is the starting point :
  - `pypi.org`, then the project's own documentation site
- Better signals than the search ranking :
  - What the documentation of a library you already trust recommends
  - What comes up repeatedly in answers to the question you are asking
- Adding one is a single command, and it records the decision :

```bash
uv add rich
```

- That writes the dependency into `pyproject.toml` and pins it in `uv.lock`
- Anyone who runs `uv sync` afterwards gets exactly the versions you had

---

# Judging a Library

- Before depending on something, look for five things :
  - A release within the last year or so, and a visible changelog
  - Real documentation rather than a README with three examples
  - An OSI licence, stated plainly, that your employer can live with
  - Issues that get answered, even if not always fixed
  - A dependency list you would be willing to own
- Every dependency is code you are trusting and will have to keep updated
- Much of this is readable from the metadata already on your disk

```python
import importlib.metadata as metadata

metadata.distribution("rich").version
```

> `demo14 · judging_a_library`


---

# Summary : Modern Toolbelt

- Four imports that will make your next script look finished :

```python
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from rich import inspect
```

- A loop that takes more than a second or two should show a bar
- A report with more than two columns should be a `Table`
- An object you do not understand should be handed to `inspect`
- Everything else here is optional, and none of it changes how Python works
