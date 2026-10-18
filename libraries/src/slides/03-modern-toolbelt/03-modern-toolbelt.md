---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Modern Toolbelt
language: python
---

# Useful Libraries

- `tqdm` adds progress bars to loops
- `rich` renders tables, progress, object details and tracebacks
- `httpx` supplies an HTTP client and an offline mock transport
- `typer` builds command-line interfaces from annotated functions

---

# tqdm Progress Bars

- `tqdm` wraps an iterable without changing its values
- `desc` labels the work; `unit` labels each item
- Pass `total=` when the iterable has no known length

```python
for _track in tqdm(tracks, desc="Converting", unit="track"):
    time.sleep(0.01)  # Simulated conversion; no audio files are read.
print(f"Converted {len(tracks)} track records")
rows = (track for track in tracks)
for _track in tqdm(rows, total=len(tracks), desc="From a generator"):
    pass
```

> `demo01 · tqdm_basics`

---

# Nested Bars

- An outer bar can count albums and an inner bar tracks
- `leave=False` removes each completed inner bar

```python
albums = {"Imagine": ["Imagine", "Jealous Guy"],
          "Thriller": ["Thriller", "Billie Jean"]}
for album, titles in tqdm(albums.items(), desc="Albums"):
    for _title in tqdm(titles, desc=album, leave=False):
        time.sleep(0.02)
```

> `demo02 · tqdm_nested`

---

# Manual Bar Updates

- Create a bar with a known total, then call `update`
- A context manager closes the bar when the work finishes
- `set_postfix` displays additional progress values

```python
with tqdm(total=len(tracks), desc="Converting", unit="track") as bar:
    for track in tracks:
        time.sleep(0.01)
        bar.update(1)
        bar.set_postfix(title=track["title"][:12])
```

> `demo03 · tqdm_manual`

---

# tqdm.write

- `tqdm.write` prints a message while preserving the progress display
- Ordinary terminal writes can interrupt a running bar

```python
for track in tqdm(tracks, desc="Checking"):
    if not track["last_played"]:
        tqdm.write(f"Never played: {track['title']}")
```

> `demo04 · tqdm_write`

---

# rich Console

- `Console.print` handles markup and Python objects
- Markup uses bracketed style names and `[/]` to close a style
- `Console(stderr=True)` sends diagnostics to standard error

```python
console = Console()
console.rule("Playlist")
console.print("[bold]Now playing [cyan]Imagine[/][/] ")
console.print({"title": "Imagine", "duration_s": 183})
```

> `demo05 · rich_console`

---

# rich Tables

- Declare columns, then add rows
- Column options control alignment and wrapping
- Row styles and footers can distinguish and summarise entries

```python
table = Table(title="Top tracks", row_styles=["", "dim"])
table.add_column("Title", style="cyan")
table.add_column("Plays", justify="right")
for track in sorted(tracks, key=lambda row: int(row["plays"]), reverse=True)[:5]:
    table.add_row(track["title"], track["plays"])
table.show_footer = True
table.columns[0].footer = "Shown"
table.columns[1].footer = "5"
Console().print(table)
```

> `demo06 · rich_table`

---

# rich Progress

- `track` wraps an iterable with a progress display
- `Progress` supports several tasks and explicit updates
- Its console keeps messages aligned with progress bars

```python
for _song in track(tracks[:3], description="Converting"):
    time.sleep(0.02)
with Progress() as progress:
    task = progress.add_task("Preparing playlist", total=3)
    for _ in range(3):
        time.sleep(0.02)
        progress.update(task, advance=1)
```

> `demo07 · rich_progress`

---

# rich Tracebacks

- `install(show_locals=True)` replaces the uncaught-exception display
- `console.print_exception` renders an exception inside an `except` block
- Locals help identify the input value that failed

```python
install(show_locals=True)
row = {"title": "Imported track", "duration_s": "unknown"}
try:
    duration = int(row["duration_s"])
except ValueError:
    Console().print_exception(show_locals=True, max_frames=2)
```

> `demo08 · rich_traceback`

---

# rich inspect

- `inspect` displays an object's attributes and values
- `methods=True` adds method signatures
- `help=True` includes documentation

```python
class Track:
    def __init__(self, title: str, duration_s: int) -> None:
        self.title: str = title
        self.duration_s: int = duration_s

    def minutes(self) -> float:
        """Return the duration in minutes."""
        return self.duration_s / 60

song = Track("Imagine", 183)
inspect(song, methods=True, help=True)
```

> `demo09 · rich_inspect`

---

# rich Logging Handler

- `RichHandler` renders messages from the standard `logging` API
- A file handler can also keep a plain log
- `log.exception` includes a traceback for a caught exception

```python
logging.basicConfig(level="INFO", format="%(message)s", handlers=[
    RichHandler(rich_tracebacks=True),
    logging.FileHandler(DATA / "player.log", encoding="utf-8"),
])
log = logging.getLogger("player")
log.info(f"PLAY {'Imagine'}")
log.warning(f"Missing local file: {'Yesterday.flac'}")
try:
    int("unknown")
except ValueError:
    log.exception("Invalid imported duration")
```

> `demo10 · rich_logging`

---

# HTTP with httpx

- `Client` sends requests and reuses connections
- `MockTransport` supplies responses without a network request
- `raise_for_status` turns error responses into exceptions

```python
def example_response(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"title": "Imagine", "duration_s": 183})

transport = httpx.MockTransport(example_response)
with httpx.Client(transport=transport, timeout=10.0) as client:
    response = client.get("https://example.org/now-playing")
    response.raise_for_status()
    print(response.json())
```

> `demo11 · httpx_client`

---

# requests and httpx

- `requests` provides a synchronous client and requires an explicit timeout
- `httpx` also supports async clients, HTTP/2 and mock transports
- Both return response objects with status, headers and body data

> `demo12 · requests_or_httpx`

---

# typer

- `typer` derives arguments, conversions and help from function signatures
- `Annotated` supplies option descriptions
- `@app.command()` registers a function as a subcommand

```python
@app.command("list")
def list_tracks(
    genre: Annotated[str | None, typer.Option("--genre")] = None,
    limit: Annotated[int, typer.Option("--limit")] = 5,
) -> None:
    """List tracks, optionally filtered by genre."""
    show_tracks(genre, limit)
```

> `demo13 · typer_cli`

---

# typer Trade-offs

- `argparse` is in the standard library; `typer` is a dependency
- Both support positional arguments, options and subcommands
- `typer.Exit(code=...)` sets an exit status
- The playlist `list`, `stats` and `top` commands have the same jobs in both APIs

---

# Finding Libraries

- PyPI lists Python distributions and their project links
- A dependency declaration records the requested package
- The lockfile records the resolved versions

```bash
uv add rich
```

---

# Judging a Library

- Read its documentation, changelog and licence
- Check maintenance activity and dependency requirements
- Installed distribution metadata provides version and project information

```python
from importlib import metadata

print(metadata.distribution("rich").version)
```

> `demo14 · judging_a_library`

---

# Summary : Modern Toolbelt

- Wrap loops with progress displays
- Use `rich` for structured reports and diagnostic detail
- Test HTTP examples with an offline transport
- Build a CLI with annotated functions when using `typer`
