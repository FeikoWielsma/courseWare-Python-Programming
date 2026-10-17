# Exercise 2 : Command-line Programs

In this exercise you take a script that reads one hard-coded log file and turn it into a small command-line tool called `logtool`, with two subcommands, generated help, and an exit status the shell can act on.

---

### Step 1 : Take an argument

Create a directory `exercise2` and a Python module `logtool.py` in it, and copy `data/cli-sample.log` into the same directory so that everything you need is in one place. Start from the script below, which is also shipped as `solutions/solution02-command-line-programs/logreport_start.py`, where the only difference is that it looks for the log in the course's `data/` directory rather than next to itself. It counts how many lines of the sample log carry each level, and the filename is written into the source :

```python
from collections import Counter
from pathlib import Path

LOGFILE = Path(__file__).parent / "cli-sample.log"


def count_levels(path: Path) -> Counter[str]:
    return Counter(line.split()[2] for line in path.read_text(encoding="utf-8").splitlines())


def main() -> None:
    for level, count in count_levels(LOGFILE).most_common():
        print(f"{level:<6}{count}")


if __name__ == "__main__":
    main()
```

Run it once so that you know what its output looks like. Then give it an `ArgumentParser` with a single positional argument for the file to read, converted to a `Path` :

```python
import argparse

parser = argparse.ArgumentParser(description="Summarise a log file.")
parser.add_argument("logfile", type=Path, help="the log file to read")
args = parser.parse_args()
```

Use `args.logfile` instead of the `LOGFILE` constant, and run the script again, this time passing `cli-sample.log` on the command line. Then run it with `--help` and confirm that the help text you never wrote is there.

### Step 2 : Two subcommands

The tool is going to do two jobs, so it needs two verbs : `count`, which is the report you already have, and `errors`, which prints the lines at one level.

Move the body of the current program into a function `cmd_count`, and write a second function `cmd_errors` next to it. Both take the parsed arguments and return an integer :

```python
def cmd_count(args: argparse.Namespace) -> int:
    ...
    return 0


def cmd_errors(args: argparse.Namespace) -> int:
    matches = [line for line in read_lines(args.logfile) if f" {args.level} " in line]
    ...
```

Now register the two verbs with `add_subparsers`, and attach each function to its verb with `set_defaults`, so that no `if` statement over the verb name is needed :

```python
verbs = parser.add_subparsers(dest="command")

counting = verbs.add_parser("count", help="count the lines per level")
counting.set_defaults(handler=cmd_count)
```

Give the `errors` verb a `--level` option with a default of `ERROR`, so that `logtool errors --level WARN` works too. Both verbs need the `logfile` argument. You can add it to each subparser separately, or declare it once on a parent parser and pass `parents=[common]` to both, which is what the solution does.

Calling the handler is then a single line :

```python
return args.handler(args)
```

Check that `logtool.py count`, `logtool.py errors` and `logtool.py errors --level WARN` all work, and that `logtool.py count --help` shows the help for that verb only.

### Step 3 : An exit status that means something

Give the program the standard entry point, so that the value it returns becomes the exit status of the process :

```python
def main(argv: list[str] | None = None) -> int:
    ...


if __name__ == "__main__":
    raise SystemExit(main())
```

Use three statuses, following the usual convention :

- `0` when the tool did its job and there is nothing to report
- `1` from `errors` when it actually found lines at the requested level
- `2` when the file cannot be read at all

For the last one, wrap the call to the handler in a `try` block, catch `OSError`, and print the reason to **stderr** rather than stdout, because a message is not data :

```python
except OSError as error:
    print(f"logtool: {error.strerror}: {args.logfile}", file=sys.stderr)
    return 2
```

Now test it the way the shell would, running each command and asking for the status afterwards :

```bash
uv run logtool.py errors cli-sample.log ; echo $?                 # 1, there are ERROR lines
uv run logtool.py errors cli-sample.log --level FATAL ; echo $?   # 0, there are none
uv run logtool.py count /no/such/file ; echo $?                   # 2, message on stderr
```

Finally, run the tool with no arguments at all. Decide what should happen, and make it happen deliberately : either print the help and return `0`, or let `add_subparsers(required=True)` refuse the call with status `2`.

### Step 4 : Optional, make it a standalone command

Turn the file into a program that needs nothing but `uv` to run. Add a shebang and a PEP 723 metadata block as the very first lines, above the docstring :

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
```

On Linux or macOS, `chmod +x logtool.py` and then run `./logtool.py count` directly. Then add `rich` to the `dependencies` list and use a `rich.table.Table` for the output of `count`, as demo 12 does. The dependency is installed the first time the script runs and cached afterwards, and the file is still one file.
