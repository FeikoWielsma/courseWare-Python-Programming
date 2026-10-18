---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Running Other Programs
language: python
appendix: true
---

# Running Other Programs

- Some work belongs to a program that already exists :
  - `git`, `systemctl`, `rsync`, a vendor's command-line tool
- `subprocess` starts it, waits for it, and reports back
- This is the module for the script that has outgrown its shell :
  - The logic got complicated, the quoting got worse
  - The commands themselves were never the problem
- Everything here is standard library, so there is nothing to install


---

# subprocess.run

- `run()` starts the program, waits, and returns a `CompletedProcess`
- The command is a list : the program, then each argument separately
- Nothing is captured unless you ask, so output goes straight to the terminal

```python
finished = subprocess.run(["git", "--version"], check=False)

print()
print("type       :", type(finished).__name__)
print("args       :", finished.args)
print("returncode :", finished.returncode)
print("stdout     :", finished.stdout)
```

> `demo01 · running_a_command`


---

# Capturing Output

- `capture_output=True` fills in `stdout` and `stderr`
- `text=True` makes them strings rather than bytes :
  - Without it you get `b'18\n'`, which is almost never wanted
- After that it is ordinary Python, not a shell pipeline

```python
finished = subprocess.run(
    ["wc", "-l", str(DATA / "listening.log")],
    capture_output=True,
    text=True,
    check=True,
)

print("stdout repr :", repr(finished.stdout))
print("stripped    :", finished.stdout.strip())
print("stderr      :", repr(finished.stderr))
```

> `demo02 · capturing_output`


---

# Exit Codes

- A non-zero exit is information, not always a failure :
  - `grep` exits 1 when it did not match
- `check=False` and read `returncode` yourself when the code is meaningful
- `check=True` raises `CalledProcessError` when it is not

```python
for pattern in ("ERROR", "NOTHING-MATCHES-THIS"):
    found = subprocess.run(
        ["grep", "-c", pattern, str(LOG)], capture_output=True, text=True, check=False
    )
    print(f"{pattern:<22} returncode={found.returncode}  matched={found.stdout.strip()}")
```

> `demo03 · exit_codes`


---

# Argument Lists

- A list hands the arguments to the program directly :
  - No shell starts, so nothing splits and nothing expands
- `shell=True` hands the whole string to a shell first :
  - A space in a filename becomes two arguments
  - Punctuation becomes syntax

```python
listed = subprocess.run(
    ["wc", "-l", str(awkward)], capture_output=True, text=True, check=False
)
print(f"as a list  : rc={listed.returncode}  {listed.stdout.strip()}")
```

> `demo04 · a_list_not_a_string`


---

# Standard Input and Pipelines

- `input=` writes to the child's stdin and closes it
- Two commands join without a shell :
  - Run the first, capture it, hand the text to the second
- Clearer than a pipeline string, with nothing for a shell to misread

```python
tallied = subprocess.run(
    ["sort"], input=levels.stdout, capture_output=True, text=True, check=True
)
summary = subprocess.run(
    ["uniq", "-c"], input=tallied.stdout, capture_output=True, text=True, check=True
)
```

> `demo05 · input_and_pipes`


---

# Timeouts

- A child that hangs will hang the parent for ever
- `timeout=` kills it and raises `TimeoutExpired` :
  - Nothing is left running behind you
- Any command touching a network, a device or another machine wants one

```python
try:
    subprocess.run(slow, timeout=1.5, check=True)
except subprocess.TimeoutExpired as error:
    print("raised   :", type(error).__name__)
    print("command  : a sleep of 30 seconds")
    print("waited   :", error.timeout, "seconds")
    print("running behind you.")
```

> `demo06 · timeouts`


---

# Environment and Working Directory

- The child inherits this process's environment by default
- `env=` replaces it wholesale :
  - Copy `os.environ` and add to the copy, or the child loses `PATH`
- `cwd=` runs the command elsewhere without moving yourself :
  - Better than `os.chdir()`, which changes it for everything

```python
environment = os.environ.copy()
environment["GREETING"] = "set for the child only"
subprocess.run([sys.executable, "-c", CHILD], env=environment, check=True)
```

> `demo07 · environment`


---

# Missing Programs

- A missing command raises `FileNotFoundError`, not a non-zero exit
- `shutil.which()` answers the question without running anything
- Check dependencies at the start of a script, not at the point of use :
  - Failing immediately with a clear message beats failing halfway through

```python
for program in ("git", "grep", "definitely-not-installed"):
    location = shutil.which(program)
    print(f"{program:<26} {location or '-- not on PATH'}")
```

> `demo08 · finding_the_program`


---

# Popen and Streaming Output

- `run()` returns nothing until the command has finished
- `Popen` starts the process and hands back control immediately :
  - Iterating `stdout` yields lines as the child flushes them
- Use it for anything long enough that silence looks like a hang

```python
with subprocess.Popen(
    [sys.executable, "-c", CHILD],
    stdout=subprocess.PIPE,
    text=True,
    bufsize=1,
) as process:
    # Iterating the pipe yields lines as the child flushes them.
    for line in process.stdout:
        print("  received :", line.rstrip())
```

> `demo09 · streaming_output`


---

# pathlib Alternatives

- Starting a process costs time and brings quoting with it
- Python already does most of what the small commands do :

```text
ls *.log     ->  Path.glob            basename  ->  Path.name
wc -l        ->  str.splitlines       test -f   ->  Path.exists
grep         ->  a comprehension      find      ->  Path.rglob
cp / mv / rm ->  shutil.copy, Path.rename, Path.unlink
```

- Reach for `subprocess` when the work belongs to another program

> `demo10 · when_not_to_shell_out`


---

# Summary : Running Other Programs

- `subprocess.run()` starts a program, waits, and reports back
- Pass a list, not a string, and leave `shell=True` alone
- `capture_output=True` with `text=True` to read what it printed
- `check=True` to raise on failure, `check=False` when the code means something
- `timeout=` on anything that could hang
- `shutil.which()` to fail early with a clear message
- `Popen` when you need the output as it arrives
- And `pathlib` instead, for anything the filesystem already does
