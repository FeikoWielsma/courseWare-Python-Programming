<!-- appendix -->

# Exercise 11 : Running Other Programs

A small appendix exercise, and the one most worth doing on your own Linux machine rather than in the classroom, because there the commands are real and the shell is a POSIX one. You will build a short report about a directory of files by asking other programs for the answers, and then replace half of it with Python that needs no other program at all.

Start from `exercises/starters/11-appendix-subprocess/`. Run from `libraries/`.

---

### Step 1 : Ask one program one question

:::hint
The slide *subprocess.run* shows the operation used in this step.
:::

Make a file `report.py`. Run `git --version` and print the version it reports, without the surrounding text :

```python
import subprocess

finished = subprocess.run(
    ["git", "--version"], capture_output=True, text=True, check=True
)
print(finished.stdout.strip())
```

Change `check=True` to `check=False` and run it against a command that does not exist, such as `["git", "nonsense"]`. Look at `returncode` and at `stderr`.

---

### Step 2 : Read an exit code that means something

:::hint
The slide *Exit Codes* shows the operation used in this step.
:::

Run `grep -c ERROR` against `data/listening.log` and print the count.

Then run it against a pattern that matches nothing. You will get a return code of 1 and a count of zero, and that is not a failure; it is `grep` telling you it found nothing.

Write a function that returns the number of matching lines, treating a return code of 0 or 1 as success and anything else as a real error :

```python
def count_matches(pattern: str, path: Path) -> int:
    found = subprocess.run(...)
    if found.returncode > 1:
        raise RuntimeError(f"grep failed: {found.stderr.strip()}")
    ...
```

---

### Step 3 : Make it fail safely

:::hint
The slide *Missing Programs* shows the operation used in this step.
:::

Add a check at the top of the script that `grep` is actually installed, using `shutil.which`. If it is missing, print a clear message to `stderr` and exit with a non-zero status, using what you built in block 02.

Test it by asking for a program you know is not there.

---

### Step 4 : Two commands, no shell

:::hint
The slide *Standard Input and Pipelines* shows the operation used in this step.
:::

Produce a count of each log level in `data/listening.log`, the way you would with `grep -o -E 'INFO|WARN|ERROR' file | sort | uniq -c`, but as separate `subprocess.run` calls passing text between them with `input=`.

Print the result as a small table.

---

### Step 5 : Give it a timeout

:::hint
The slide *Timeouts* shows the operation used in this step.
:::

Add `timeout=` to every call. Pick something generous, five seconds say, so it never fires in normal use.

Then prove it works by running a command that sleeps for longer than that, and catching `TimeoutExpired`. On Linux, `["sleep", "30"]` will do.

---

### Step 6 : Now throw half of it away

:::hint
The slide *pathlib Alternatives* shows the operation used in this step.
:::

Rewrite Step 4 in pure Python: read the file with `Path.read_text`, and count the levels with a dictionary or `collections.Counter`. No `subprocess` at all.

Compare the two versions. Time them if you like; the difference will be larger than you expect, because the first version starts three processes and the second starts none.

Which one you would rather maintain is the real question, and the answer is not the same for every script.

---

### Step 7 : Optional, something genuinely useful

Point the script at a directory of your own and have it report something you actually want to know, using a program that has no Python equivalent worth writing. Some possibilities :

- `git log --format=%an` piped into a count, for who has touched a repository.
- `systemctl is-active` for a list of services, reporting only the ones that are not running.
- `df -P` parsed into a warning for any filesystem over a threshold you choose.

Keep the rule from the last slide in mind : let the other program do what only it can do, and do the rest in Python.
