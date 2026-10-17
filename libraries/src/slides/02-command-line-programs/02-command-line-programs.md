---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Command-line Programs
language: python
---

# Command-line Programs

- A script does one job, to one file, with the settings typed into the source
- A tool takes its settings from the command line :
  - The same code serves every file, every level and every output format
- Three things separate the two :
  - It explains itself when asked
  - It refuses a wrong command line clearly, instead of crashing later
  - It reports success or failure in a way another program can read
- Everything in this module is standard library, so it ships with Python
- The end of the module is a checklist you can hold a script up against


---

# sys.argv

- Everything typed after the program name arrives in `sys.argv` :
  - A plain list of strings, in the order they were given
  - `sys.argv[0]` is the program itself, so the real arguments start at `1`
- Nothing is converted, so a number arrives as text

```python
import sys

print(sys.argv)          # ['tool.py', 'report', '--limit', '5']
print(sys.argv[1:])      # ['report', '--limit', '5']
```

- This is the whole interface between the shell and the program
- Every argument library in Python is a layer over this one list

> `demo01 · sys_argv`


---

# Manual Argument Parsing

- Reading the list yourself works, right up until it does not :
  - An option whose value is missing walks off the end of the list
  - A value that should be a number is still a string
  - A mistyped option is silently taken for something else
  - Nobody wrote `--help`, so there is none
- Each of those is a few more lines of defensive code

```python
if item == "--limit":
    index += 1
    limit = int(argv[index])   # IndexError, or ValueError
```

- The handwritten version grows faster than the program it serves

> `demo02 · argv_by_hand`


---

# ArgumentParser

- `argparse` inverts the work : you describe the command line, it does the rest
- A positional argument is named and required by position

```python
import argparse

parser = argparse.ArgumentParser(description="Print the square of a number.")
parser.add_argument("number", type=int, help="the number to square")
args = parser.parse_args()

print(args.number ** 2)
```

- `type=` is a conversion, so `args.number` is an `int` and not `"12"`
- `help=` is the text that appears under `--help`
- The result is a namespace whose attributes are the argument names

> `demo03 · first_parser`


---

# Options and Flags

- A name starting with a dash is optional, and gets a default

```python
parser.add_argument("--dry-run", action="store_true")
parser.add_argument("-v", "--verbose", action="count", default=0)
parser.add_argument("--format", choices=["dec", "hex"], default="dec")
```

- `action="store_true"` makes a flag, present or absent, no value
- `action="count"` counts repeats, so `-vv` gives `2`
- `choices=` rejects anything outside the list and advertises the options
- `nargs="?"` makes a positional optional, with a default of its own
- A dashed name becomes an underscored attribute : `--dry-run` is `args.dry_run`

> `demo04 · options_and_flags`


---

# Mutually Exclusive Options

- Some options make no sense together, and the parser can say so

```python
loudness = parser.add_mutually_exclusive_group()
loudness.add_argument("-v", "--verbose", action="store_true")
loudness.add_argument("-q", "--quiet", action="store_true")
```

- Passing both is refused before a single line of your code runs :
  - The message names the conflict and the process exits with status `2`
- This is validation you would otherwise write, forget, or get subtly wrong
- The group is only about the command line, not about the values

> `demo05 · mutually_exclusive`


---

# Generated Help and Errors

- `--help` is generated from the `add_argument` calls, never written by hand

```text
usage: squares [-h] [-v] number

positional arguments:
  number         the number to square

options:
  -h, --help     show this help message and exit
  -v, --verbose  explain the answer
```

- A wrong command line prints a usage line to stderr and exits with status `2`
- Both behaviours are free, and both match what every other tool does
- `prog=`, `description=` and `epilog=` fill in the surrounding text

> `demo06 · help_and_errors`


---

# Subcommands

- One program, several verbs, the shape of `git`, `apt` and `systemctl`

```python
verbs = parser.add_subparsers(dest="command", required=True)

add = verbs.add_parser("add", help="add a host")
add.add_argument("host")
add.set_defaults(handler=cmd_add)
```

- Each verb is a parser of its own, with its own arguments and its own help
- `dest=` names the attribute holding the chosen verb
- `required=True` refuses a call with no verb at all
- `set_defaults(handler=...)` attaches the function that implements the verb

> `demo07 · subcommands`


---

# Path Arguments

- `type=` accepts any callable, and `Path` is one

```python
from pathlib import Path

parser.add_argument("logfile", type=Path)
args = parser.parse_args()

print(args.logfile.name, args.logfile.stat().st_size)
```

- The argument arrives as a `Path`, ready to be read, joined or inspected
- A converter of your own can validate at the same time :
  - Return the converted value, or raise `argparse.ArgumentTypeError`
  - The parser turns that into an ordinary usage error, at status `2`

> `demo08 · paths`


---

# FileType

- `argparse.FileType` opens the file during parsing, and looks convenient
- Python 3.14 deprecates it, with an unusually direct message :

```text
FileType is deprecated. Simply open files after parsing arguments.
```

- The reasons :
  - The file is opened even when a later argument turns out to be wrong
  - Nothing ever closes it
- Take a `Path`, then open it yourself, in a `with` block
- Handle the single dash yourself when you want to read standard input

> `demo09 · filetype`


---

# main and the Exit Status

- Give the program one entry point that returns an integer

```python
def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    ...
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

- `argv=None` means "take the real command line", and a list means "take this one"
- That default makes the program callable from a test, or from another program
- `SystemExit(0)` is success, and any other number is not
- The convention : `0` fine, `1` ran but found trouble, `2` unusable

> `demo10 · main_exit_codes`


---

# Standard Output and Standard Error

- Two streams, two purposes :
  - `stdout` carries the result, the part another program will read
  - `stderr` carries progress, warnings and reasons

```python
print(record)                              # data
print("reading log", file=sys.stderr)      # everything else
```

- Mixing them is what makes a tool unpleasant to use in a pipeline
- `sys.stdout.isatty()` is `False` when the output is a pipe or a file :
  - The usual signal to drop colour, banners and progress bars
- A reader that stops early raises `BrokenPipeError`, which is normal, not a bug

> `demo11 · stderr_and_pipes`


---

# Inline Script Metadata

- PEP 723 lets a single file declare what it needs, in a comment block

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["rich>=13.9"]
# ///
```

- `uv run script.py` reads that block, builds an environment and runs the file
- No virtual environment to create, activate, remember or clean up
- The file stays one file, so it can be mailed, pasted or dropped in `~/bin`
- This is the current answer to "a small program that needs one library"

> `demo12 · pep723_script`


---

# Executable Scripts

- Add a shebang above the metadata block and the file becomes a command :

```bash
#!/usr/bin/env -S uv run --script
```

- Then the usual two steps, and it runs from anywhere :

```bash
chmod +x logtool.py
./logtool.py count /var/log/syslog
```

- `env -S` is what allows the extra arguments after the interpreter name
- The environment is cached, so only the first run pays for the install
- Pin the versions in `dependencies` and the script still works next year


---

# Command-line Checklist

- It accepts its input on the command line, with sensible defaults
- It has `--help`, and the help is generated rather than maintained
- It refuses a wrong command line clearly, and exits `2` when it does
- It prints data on stdout and everything else on stderr
- It exits `0` on success and non-zero when the answer is bad news
- It reads standard input when the filename is a single dash
- It has one `main(argv) -> int`, so it can be called as well as run

> `demo13 · unix_citizen`


---

# Summary : Command-line Programs

- `sys.argv` is the raw list of strings the shell handed over
- `argparse` turns a description of the command line into a parser :
  - Positionals, options, flags, `type=`, `choices=`, `default=` and `help=`
  - The `--help` text and the usage errors come with it
- `add_subparsers` gives one program several verbs, each with its own arguments
- Take a `Path`, then open the file yourself inside a `with` block
- `main(argv: list[str] | None = None) -> int` plus `SystemExit` gives real exit codes
- Data goes to stdout, diagnostics go to stderr, and a broken pipe is normal
- PEP 723 metadata plus `uv run` makes one file a complete program

> `exercise02 · Command-line Programs`
