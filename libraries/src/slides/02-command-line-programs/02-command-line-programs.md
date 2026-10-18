---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Command-line Programs
language: python
---

# Command-line Programs

- A command-line tool accepts arguments and options
- Standard output carries results; standard error carries diagnostics
- Exit statuses let the shell distinguish success, matches and errors
- A playlist report can share one interface across scripts and pipelines

---

# sys.argv

- `sys.argv[0]` is the script name
- The remaining entries are strings supplied by the caller
- Parsing and validation are separate from receiving those strings

```python
arguments = sys.argv[1:] or ["tracks.csv", "--genre", "Rock", "--limit", "3"]
print(f"program: {Path(sys.argv[0]).name}")
for position, value in enumerate(arguments, start=1):
    print(f"argv[{position}] = {value!r}")

line = "2026-10-12 08:00:00 INFO PLAY Imagine"
print(line.split(maxsplit=4))
```

> `demo01 · sys_argv`

---

# Manual Argument Parsing

- Manual parsing must recognise every option and its values
- Missing values, invalid conversions and unknown options need error handling
- `argparse` supplies these checks and generated help

```python
elif argv[index] == "--limit":
            index += 1
            limit = int(argv[index])
```

> `demo02 · argv_by_hand`

---

# ArgumentParser

- A positional argument is required unless configured otherwise
- `type=int` converts its text before the program uses it
- A duration in seconds can be formatted as minutes and seconds

```python
def format_duration(seconds: int) -> str:
    return f"{seconds // 60}:{seconds % 60:02d}"

parser = argparse.ArgumentParser(description="Format a track duration.")
parser.add_argument("seconds", type=int, help="duration in seconds")
args = parser.parse_args(sys.argv[1:] or ["183"])
print(format_duration(args.seconds))
```

> `demo03 · first_parser`

---

# Options and Flags

- Dashed names define optional arguments
- `default` supplies a value when an option is absent
- `store_true` creates a flag; `count` counts repeated flags
- `choices` rejects unsupported values

```python
parser.add_argument("file", type=Path, nargs="?", default=DATA / "tracks.csv")
parser.add_argument("--genre", choices=["Rock", "Pop", "Soul", "Country", "Electronic"])
parser.add_argument("--limit", type=int, default=5)
parser.add_argument("-v", "--verbose", action="count", default=0)
parser.add_argument("--dry-run", action="store_true")
```

> `demo04 · options_and_flags`

---

# Mutually Exclusive Options

- A mutually exclusive group accepts at most one member
- Supplying both duration-order flags is a usage error
- Parsing rejects the conflict with exit status 2

```python
order = parser.add_mutually_exclusive_group()
order.add_argument("--longest", action="store_true")
order.add_argument("--shortest", action="store_true")
```

> `demo05 · mutually_exclusive`

---

# Generated Help and Errors

- `--help` describes declared arguments and options
- A missing required value or invalid conversion writes a usage error to stderr
- Help exits with status 0; usage errors exit with status 2

```python
parser = argparse.ArgumentParser(prog="duration", description="Format seconds.")
parser.add_argument("seconds", type=int)
```

> `demo06 · help_and_errors`

---

# Subcommands

- `add_subparsers` registers verbs such as `list`, `stats` and `top`
- Each subparser owns its arguments
- `set_defaults(handler=...)` attaches the implementation function

```python
verbs = parser.add_subparsers(dest="command", required=True)
    listing = verbs.add_parser("list", help="list tracks")
    listing.add_argument("--genre")
    listing.add_argument("--limit", type=int, default=5)
    listing.set_defaults(handler=cmd_list)
```

> `demo07 · subcommands`

---

# Path Arguments

- `type=Path` converts an argument into a path object
- Conversion does not prove that a file exists or is readable
- Open files after parsing, inside a context manager

```python
parser = argparse.ArgumentParser()
parser.add_argument("file", type=Path, nargs="?", default=DATA / "tracks.csv")
args = parser.parse_args()
if not args.file.is_file():
    print(f"Missing file: {args.file}", file=sys.stderr)
    raise SystemExit(2)
```

> `demo08 · paths`

---

# FileType

- `argparse.FileType` opens a file while parsing
- It is pending deprecation in Python 3.14
- A later parsing failure can leave the file open
- A `Path` argument followed by `with path.open(...)` gives control over its lifetime

```python
with args.source.open(encoding="utf-8") as stream:
    print(f"opened {args.source.name}, first line: {stream.readline().strip()}")
```

> `demo09 · filetype`

---

# main and the Exit Status

- `raise SystemExit(main(...))` forwards a result to the shell
- Status 0 means success; nonzero statuses describe other outcomes
- This playlist tool returns 2 when its input cannot be read

```python
try:
        rows = load(args.file)
    except OSError as error:
        print(f"playlist: {error}", file=sys.stderr)
        return 2
```

> `demo10 · main_exit_codes`

---

# Standard Output and Standard Error

- Stdout carries results that another program can read
- Stderr carries diagnostics without mixing them into the data
- `BrokenPipeError` can occur when a downstream program stops reading

```python
def emit(path: Path) -> None:
    print(f"Reading {path.name}", file=sys.stderr)
    for row in load(path):
        print(row["title"])
    print("Finished", file=sys.stderr)
```

> `demo11 · stderr_and_pipes`

---

# Inline Script Metadata

- PEP 723 records script dependencies in a comment block
- `uv run script.py` reads the metadata and prepares an environment
- The script can remain one file

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["rich>=13.9"]
# ///
```

> `demo12 · pep723_script`

---

# Executable Scripts

- A shebang selects the interpreter on systems that support it
- A script still needs executable permission on Linux and macOS
- On Windows, invoke the script through `uv run`

```python
#!/usr/bin/env -S uv run --script
```

---

# Command-line Checklist

- Provide generated help and validate arguments
- Accept an input path or a documented stdin marker
- Keep diagnostic messages on stderr
- Use exit statuses consistently; handle missing files and broken pipes

> `demo13 · unix_citizen`

---

# Summary : Command-line Programs

- Read arguments with `argparse`
- Declare positionals, options, exclusive flags and subcommands
- Convert paths while parsing; open files afterwards
- Separate stdout, stderr and exit status
- PEP 723 can declare dependencies beside the script
