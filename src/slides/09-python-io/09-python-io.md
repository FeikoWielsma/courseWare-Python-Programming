---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Python IO
---

# Input and Output

- `print` writes its arguments to standard output.
- `input` reads one line from standard input and removes the trailing newline.
- It returns a string; convert it before doing arithmetic.

```python
print("Python is really a great language,", "isn't it?")
text = input("Enter some input : ")
print(text)
```

> `demo01 · readinput`


---

# IO Module

- Core of the I/O system is implemented in io library module
- Consists of a collection of different I/O classes :
  - `FileIO`
  - `BufferedReader`
  - `BufferedWriter`
  - `BufferedRWPair`
  - `BufferedRandom`
  - `TextIOWrapper`
  - `BytesIO`
  - `StringIO`
- Each class implements a different kind of I/O
- Classes get layered to add features

---

# Opening Files

- `open` function :
  - Opens a file to be able to read or write a file later
  - Creates file object which can be used to call other support methods

```text
file_object = open(file, mode="r", buffering=-1, encoding=None)
```

- `file` :
  - String value that contains the name of the file to be accessed
- `mode` :
  - Determines mode in which the file has to be opened, read, write, append etc.
  - `t` for text mode is default and optional, `b` is for byte mode
- `buffering` :
  - `0` disables buffering, but is allowed only in binary mode
  - `1` enables line buffering in text mode
  - If buffering > 1 : Buffering performed with indicated buffer size

---

# File Open Modes

- Python distinguishes between binary and text I/O :
  - In binary mode content is returned as bytes objects without any decoding
  - In text mode, as `str`, bytes decoded using given or platform-specific encoding

| Mode | Description |
|---|---|
| `r` / `rb` | Reading only, text or binary format. Default is text mode |
| `r+` / `rb+` | Both reading and writing, text or binary format |
| `w` / `wb` | Writing only, text or binary. Overwrites existing file or creates new file |
| `w+` / `wb+` | Both writing and reading, text or binary. Overwrites or creates file |
| `a` / `ab` | Appending, text or binary. File pointer is at the end of the file |
| `a+` / `ab+` | Both appending and reading, text or binary format |

---

# Result of Calling open

- The object returned varies with the file mode and the buffering :

```text
>>> open("test.txt", "rt", encoding="utf-8")
<_io.TextIOWrapper name='test.txt' mode='rt' encoding='utf-8'>
>>> open("test.txt", "rb")
<_io.BufferedReader name='test.txt'>
>>> open("test.txt", "rb", buffering=0)
<_io.FileIO name='test.txt' mode='rb'>
```

- Opening a text file stacks three objects, and you are handed the outermost :

<svg viewBox="0 0 960 140" width="100%" style="width:100%;height:auto;display:block;margin:10px 0 4px" role="img" aria-label="Opening a text file layers TextIOWrapper over BufferedReader over FileIO">
<defs>
<marker id="io-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
</marker>
</defs>
<g fill="none" stroke="currentColor" stroke-width="2">
<rect x="230" y="42" width="196" height="46" rx="4"/>
<rect x="466" y="42" width="196" height="46" rx="4"/>
<rect x="702" y="42" width="130" height="46" rx="4"/>
</g>
<g fill="none" stroke="currentColor" stroke-width="1.8" marker-end="url(#io-arrow)">
<path d="M 196 65 L 224 65"/>
<path d="M 426 65 L 460 65"/>
<path d="M 662 65 L 696 65"/>
<path d="M 832 65 L 900 65"/>
</g>
<g fill="currentColor" font-size="20" text-anchor="middle">
<text x="328" y="72">TextIOWrapper</text>
<text x="564" y="72">BufferedReader</text>
<text x="767" y="72">FileIO</text>
</g>
<g fill="currentColor" font-size="17" text-anchor="middle" opacity="0.75">
<text x="328" y="30">"rt"</text>
<text x="564" y="30">"rb"</text>
<text x="767" y="30">buffering=0</text>
<text x="328" y="112">text and bytes</text>
<text x="564" y="112">buffered bytes</text>
<text x="767" y="112">raw bytes</text>
</g>
<g fill="currentColor" font-size="19">
<text x="20" y="72">open(...)</text>
<text x="908" y="72">disk</text>
</g>
</svg>

> `demo02 · openfile`


---

# File Object Attributes

- File objects expose their name, mode and closed state.

```python
fo = open("test_02.txt", "wb")
print("Name of the file:", fo.name)
print("Closed or not :", fo.closed)
print("Opening mode :", fo.mode)
fo.close()
```

```text
Name of the file: test_02.txt
Closed or not : False
Opening mode : wb
```

> `demo03 · fileioobject`


---

# Bytes and Byte Arrays

- `bytes` is immutable; `bytearray` allows individual bytes to change.
- Indexing returns an integer from 0 to 255, not a character.
- Encoding converts text to bytes; decoding converts bytes back to text.

```python
text = "ABCDE"
arr = bytes(text, "utf-8")
print(arr)  # b'ABCDE'
print(arr[0])  # 65
print(arr.decode("utf-8"))  # ABCDE

mutable = bytearray(arr)
mutable[0] = 70
print(mutable)  # bytearray(b'FBCDE')
print(mutable.decode("utf-8"))  # FBCDE
```

- Binary files read and write bytes; text files handle encoding for you.

> `demo04 · bytesandbytesarrays`

---

# Reading Binary Files

- Binary mode (`rb`) reads bytes without decoding them.
- `read(3)` reads up to three bytes; `read()` reads the remaining contents.
- Binary mode takes no `encoding` argument.

```python
fr = open("trilobyte.jpg", mode="rb")
data = fr.read(3)
print(type(data))  # <class 'bytes'>
print(data.hex())  # ffd8ff
fr.close()
```

> `demo05 · readbinaryfile`


---

# Writing Binary Files

- `wb` writes bytes and replaces any existing file.
- `struct` packs numbers into bytes and unpacks them with the same format.
- Here `<iii` means three four-byte integers in little-endian order.

```python
from struct import pack, unpack

payload = pack("<iii", 1, 2, 3)
fw = open("numbers.bin", mode="wb")
fw.write(payload)
fw.close()

fr = open("numbers.bin", mode="rb")
print(unpack("<iii", fr.read()))  # (1, 2, 3)
fr.close()
```

> `demo06 · writebinaryfile`


---

# Writing Text Files

- Open file for writing specifying mode and encoding :

```python
fw = open("textfilepolish.txt", mode="w", encoding="UTF-8")
```

- `write` method writes any string to an open file :
  - Parameter is the content to be written into the opened file
  - Does not add a newline character ('\n') to the end of the string

```python
s = "Polish text: ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
fw.write(s)
```

- Always close the file when you are done :

```python
fw.close()
```

- File `textfilepolish.txt` with following content is created :

```text
Polish text: ąćęłńóśźżĄĆĘŁŃÓŚŹŻ
```

> `demo07 · writetextfile`


---

# Reading Text Files

- Open file for reading specifying mode and encoding :

```python
fr = open("textfilepolish.txt", mode="r", encoding="UTF-8")
```

- `read` method reads a string from an open file :
  - In text mode the count is a number of characters, not bytes

```text
file_object.read([count])
```

- `read()` starts at the current file position :
  - If count is missing then it tries to read as much as possible, may be until end of file
- Example of reading and closing file `textfilepolish.txt` :

```python
data = fr.read()
print(data)
fr.close()
```

- Result :



```text
Polish text: ąćęłńóśźżĄĆĘŁŃÓŚŹŻ
```


---

# Closing Files

- `close` method flushes unwritten data and closes file object :
  - No more writing can be done after calling `close`
  - Do not rely on garbage collection to close a file promptly
- Syntax :

```python
file_object.close()
```

- Example :

```python
fo = open("foo.txt", "wb")
print("Name of the file:", fo.name)
fo.close()
```

- Result :

```text
Name of the file: foo.txt
```

- Good practice to use `close()` method to close a file, but see the next slide

---

# Using with

- `with` closes the file when the block ends, even after an exception or `return`.
- Prefer this form whenever you open a file.

```python
with open("foo.txt", mode="w", encoding="utf-8") as fw:
    fw.write("one line\n")
# The file is closed here, even if write() raised.
print(fw.closed)  # True

with open("foo.txt", encoding="utf-8") as fr:
    print(fr.read(), end="")  # one line
```

> `demo08 · usingwith`


---

# File Positions

- `tell()` reports the current position; `seek(0)` returns to the start.
- Binary file positions count bytes from the beginning.
- Text file positions are opaque values; use `seek(0)` or a value from `tell()`.

```python
with open("positions.bin", "wb") as fw:
    fw.write(b"ABCDE")

with open("positions.bin", "rb") as fr:
    print(fr.read(2))  # b'AB'
    print(fr.tell())  # 2
    fr.seek(0)
    print(fr.read(2))  # b'AB'
```

> `demo09 · file_positions`


---

# The csv Module

- Use `csv` for tabular text; it handles quoted commas and embedded newlines.
- Open CSV files with `newline=""` so `csv` controls newline handling.

```python
import csv

with open("planets.csv", "w", newline="", encoding="utf-8") as fw:
    writer = csv.writer(fw)
    writer.writerow(["name", "moons"])
    writer.writerows([["Earth", 1], ["Mars", 2]])

with open("planets.csv", newline="", encoding="utf-8") as fr:
    for row in csv.reader(fr):
        print(row)
```

> `demo10 · csv_module`

---

# Reading CSV Rows by Name

- `DictReader` uses the first row as column names.
- Field values are strings; convert numeric fields explicitly.
- The demo creates the same CSV file, then reads it by column name :

```python
with open("planets.csv", newline="", encoding="utf-8") as fr:
    for row in csv.DictReader(fr):
        name = row["name"]
        moons = int(row["moons"])
        print(f"{name}: {moons} moons")
```

```text
Earth: 1 moons
Mars: 2 moons
```

- `csv.reader` returns lists instead : `['Earth', '1']`.

> `demo11 · csv_dictionary`

---

# Paths with pathlib

- The `pathlib` module represents a path as an object, not a string :
  - `Path` knows how to join, inspect, read, write, rename and delete
  - It is the modern replacement for stringly typed `os.path` work

```python
from pathlib import Path

here = Path.cwd()                   # the current working directory
sample = here / "data" / "one.txt"  # joining, with / instead of concatenation
```

- The `/` operator joins path segments :
  - It produces the right separator on Windows, macOS and Linux alike
  - No more `"dir" + "\\" + name`, and no more forgetting the separator
- A path answers questions about itself :

```python
sample.name      # one.txt
sample.stem      # one
sample.suffix    # .txt
sample.parent    # the containing directory, as a Path
sample.exists()  # True or False
```

---

# Paths Relative to a Module

- `Path(__file__)` is the path of the running module, so `parent` is its folder :
  - `resolve()` makes the path absolute, and follows any symbolic links
- `path.open()` works like `open()`, and takes the same arguments :

```python
from pathlib import Path

here = Path(__file__).resolve().parent  # the folder of this module
print(here.is_absolute())  # True

with Path(__file__).open(encoding="utf-8") as source:
    print(source.readline().strip())  # from pathlib import Path
```

---

# Renaming and Deleting Files

- A `Path` renames and deletes itself :

```python
from pathlib import Path

data_file = Path("datafile1.txt")
data_file.touch()
renamed = data_file.rename("renamedfile.txt")
renamed.unlink()
```

- `touch` creates an empty file, `unlink` removes one :
  - `unlink(missing_ok=True)` does nothing when the file is already gone
- Short reads and writes need no `open` at all :

```python
sample = Path("sample.txt")
sample.write_text("first\n", encoding="utf-8")
content = sample.read_text(encoding="utf-8")
```

- The `os` module still has `os.rename` and `os.remove` :
  - They take strings and are what older code uses

> `demo12 · renaming_files`


---

# Creating and Removing Directories

- `mkdir` creates a directory, `rmdir` removes an empty one :

```python
from pathlib import Path

Path("test1").mkdir(exist_ok=True)
Path("test1").rmdir()
```

- Two keyword arguments cover the awkward cases :
  - `parents=True` creates every missing directory in the path
  - `exist_ok=True` succeeds quietly when the directory is already there

```python
Path("test2/nested/deeper").mkdir(parents=True, exist_ok=True)
```

- `rmdir` only removes an empty directory :
  - Remove the contents first, from the leaf upwards
  - `shutil.rmtree` removes a whole tree at once, and does not ask twice

> `demo13 · creatingandremoving_directories`


---

# Directory Contents

- `iterdir` lists direct entries; `glob` selects matching names.
- Each entry is a `Path` that you can inspect or open.
- `rglob` searches subdirectories too.

```python
from pathlib import Path

here = Path.cwd()
work = here / "justtesting"
work.mkdir(exist_ok=True)
(work / "one.txt").write_text("first\n", encoding="utf-8")
(work / "two.txt").write_text("second\n", encoding="utf-8")
print("contents          :", sorted(p.name for p in work.iterdir()))
print("only the text     :", sorted(p.name for p in work.glob("*.txt")))
```

> `demo14 · directorymethods`


---

# Summary : Python IO

- Simplest way to produce output is to use the `print` function :
  - Allows you to pass zero or more expressions, separated by commas
- The `input` function reads a line of text from standard input :
  - It always returns a string, so convert it before doing arithmetic with it
- Python also has File Object methods to manipulate files :
  - Creating, opening files, closing files, reading, writing, renaming and deleting files
- Files can be opened in several modes :
  - For reading, for writing, for appending or combinations thereof
- Binary files contain bytes; text files encode and decode strings.
- Use `csv.reader`, `csv.writer` and `DictReader` for tabular text.
- Open files with `with`, which closes them whatever happens :
  - The manual `open` and `close` pair is shown so that you recognise older code
- `pathlib` represents a path as an object :
  - `Path` joins with `/`, and creates, renames, deletes, reads and lists

> `exercise09 · Python IO`
