---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Python IO
---

# Input and Output

- Simplest way to produce output is `print` function :
  - Allows you to pass expressions, separated by commas, enclosed in parentheses

```python
print("Python is really a great language,", "isn't it? ")
```

- `print` is a function, so its arguments go inside the parentheses
- Standard input default comes from keyboard with input function
- `input([prompt])` function :
  - Reads line from standard input, converts it to a string and strips trailing newline
- Python also has File Object methods :
  - Most of the file manipulation is done using a file object
- Python also has OS Object Methods :
  - Methods to process files as well as directories

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
  - If buffering value is set to 0, no buffering will take place
  - If buffering value is 1, line buffering will be performed while accessing file
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
>>> open("test.txt", "rt")
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

- FileIO object represents raw unbuffered binary I/O
- File object has attributes with information about it
- `file.closed` : Returns true if file is closed, false otherwise
- `file.mode` : Returns access mode with which file was opened
- `file.name` : Returns name of the file
- Example :

```python
fo = open("test.txt", "wb")
print("Name of the file:", fo.name)
print("Closed or not :", fo.closed)
print("Opening mode :", fo.mode)
```

- Result :

```text
Name of the file: test.txt
Closed or not : False
Opening mode : wb
```

> `demo03 · fileioobject`


---

# Reading Binary Files

- Opening a file in binary mode is simple but subtle :
  - Reading bytes not strings, so there’s no conversion for Python to do
- Difference from opening it in text mode :
  - b mode parameter
  - No encoding attribute
- `read` method reads whole file or a number of bytes :
  - `tell` moves file pointer to the beginning of the file
  - `seek` moves file pointer to a certain position in the file

```text
fr = open('trilobyte.jpg', mode='rb')
fr.tell()
data = fr.read(3) => read three bytes
print(type(data)) => type is bytes
fr.tell()
fr.seek(0)
data = fr.read()
print(data)
```

> `demo04 · readbinaryfile`


---

# Writing Binary Files

- Open binary files for writing without encoding attribute :

```python
fw = open("binaryfile04.txt", mode="wb")
```

- Use `pack` method of `struct` module to prepare buffer for writing :
  - Format string determines how packing takes place

```python
nr1 = 1
nr2 = 2
result = nr1 + nr2
buffer = pack("iii", nr1, nr2, result)
fw.write(buffer)
```

- Data must be read like it is written using same format string :

```python
fr = open("binaryfile04.txt", mode="rb")
buffer = fr.read()
data = unpack("iii", buffer)
```

- Returned data is a tuple that can be unpacked as follows :

```python
num1, num2, res = data
```

> `demo05 · writebinaryfile`


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

> `demo06 · writetextfile`


---

# Reading Text Files

- Open file for reading specifying mode and encoding :

```python
fr = open("textfilepolish.txt", mode="r", encoding="UTF-8")
```

- `read` method reads a string from an open file :
  - Parameter is the number of bytes to be read from the opened file

```text
file_object.read([count])
```

- `read()` starts reading from the beginning of the file :
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
  - File is closed automatically when reference file object is reassigned to another file
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

- Calling `close()` by hand is easy to get wrong :
  - An exception between `open` and `close` skips the `close` entirely
  - An early `return` does the same
- A `with` statement closes the file when the block ends, whatever happens :

```python
with open("foo.txt", mode="w", encoding="utf-8") as fw:
    fw.write("one line\n")
# the file is closed here, even if write() raised
```

- This is the normal way to open a file in Python :
  - The manual `open` and `close` above is shown so that you recognise it
  - Prefer `with` in everything you write
- The file is closed on the way out of the block, not at the end of the program
- Any object with the same protocol can be used this way :
  - A database connection, a lock, a network socket

> `demo07 · usingwith`

---

# File Positions

- `tell` method retrieves current position within the file :
  - Next read or write will occur at that many bytes from the beginning of the file
- `seek(offset[, from])` method changes the current file position :
  - Offset argument indicates the number of bytes to be moved
  - From argument specifies reference position from where bytes are to be moved

<svg viewBox="0 0 960 175" width="100%" style="width:100%;height:auto;display:block;margin:6px 0 4px" role="img" aria-label="After reading ten bytes tell reports position ten, and seek zero moves the position back to the start">
<defs>
<marker id="fp-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
</marker>
</defs>
<g fill="currentColor" opacity="0.12">
<rect x="60" y="56" width="320" height="44"/>
</g>
<g fill="none" stroke="currentColor" stroke-width="2">
<rect x="60" y="56" width="832" height="44"/>
</g>
<g fill="currentColor" font-size="22" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
<text x="60" y="86" textLength="832" lengthAdjust="spacingAndGlyphs">Python is a great language</text>
</g>
<g fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.6">
<path d="M 60 44 L 60 56"/>
<path d="M 380 44 L 380 56"/>
<path d="M 892 44 L 892 56"/>
</g>
<g fill="currentColor" font-size="18" text-anchor="middle" opacity="0.75">
<text x="60" y="36">byte 0</text>
<text x="380" y="36">byte 10</text>
<text x="892" y="36">byte 26</text>
</g>
<g fill="none" stroke="currentColor" stroke-width="1.8" marker-end="url(#fp-arrow)">
<path d="M 380 130 L 380 106"/>
<path d="M 372 148 L 66 148"/>
</g>
<g fill="currentColor" font-size="19">
<text x="392" y="136">tell() reports 10, the next read starts here</text>
<text x="392" y="155">seek(0) moves the position back to the start</text>
</g>
</svg>

- If from is set to 0 :
  - Use beginning of the file as the reference position
- If from is set to 1 :
  - Use current position as the reference position
- If from is set to 2 :
  - Use end of the file as the reference position

---

# Example File Positioning

- Consider file `foo.txt` that was created before :

```python
fo = open("foo.txt", "r+")
text = fo.read(10)
print("Read String is :", text)
# Check current position
position = fo.tell()
print("Current file position :", position)
# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
text = fo.read(10)
print("Again read String is :", text)
fo.close()
```

- Result :

```text
Read String is : Python is
Current file position : 10
Again read String is : Python is
```

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

# Renaming and Deleting Files

- A `Path` renames and deletes itself :

```python
from pathlib import Path

data_file = Path("datafile1.txt")
data_file.touch()                              # create it, empty
renamed = data_file.rename("renamedfile.txt")  # returns the new path
renamed.unlink()                               # delete it
```

- `touch` creates an empty file, `unlink` removes one :
  - `unlink(missing_ok=True)` does nothing when the file is already gone
- Short reads and writes need no `open` at all :

```python
sample.write_text("first\n", encoding="utf-8")
content = sample.read_text(encoding="utf-8")
```

- The `os` module still has `os.rename` and `os.remove` :
  - They take strings and are what older code uses

> `demo08 · renaming_files`


---

# Creating and Removing Directories

- `mkdir` creates a directory, `rmdir` removes an empty one :

```python
from pathlib import Path

Path("test1").mkdir()
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

> `demo09 · creatingandremoving_directories`


---

# Directory Contents

- `iterdir` yields every entry of one directory :

```python
from pathlib import Path

work = Path("justtesting")
for entry in work.iterdir():
    print(entry.name)
```

- `glob` yields the entries matching a pattern :

```python
for text_file in work.glob("*.txt"):
    print(text_file.name)

for text_file in work.rglob("*.txt"):  # recursively, through subdirectories
    print(text_file)
```

- Each entry is itself a `Path`, so it can be inspected or opened straight away :
  - `entry.is_file()`, `entry.is_dir()`, `entry.stat().st_size`
- `Path.cwd()` gives the current working directory :
  - `os.chdir` still changes it, but passing paths around beats changing directory

> `demo10 · directorymethods`


---

# Summary : Python IO

- Simplest way to produce output is to use the `print` statement :
  - Allows you to pass zero or more expressions, separated by commas
- The `input` function reads a line of text from standard input :
  - It always returns a string, so convert it before doing arithmetic with it
- Python also has File Object methods to manipulate files :
  - Creating, opening files, closing files, reading, writing, renaming and deleting files
- Files can be opened in several modes :
  - For reading, for writing, for appending or combinations thereof
- File Positioning :
  - Methods can retrieve and change the current file position
- Open files with `with`, which closes them whatever happens :
  - The manual `open` and `close` pair is shown so that you recognise older code
- `pathlib` represents a path as an object :
  - `Path` joins with `/`, and creates, renames, deletes, reads and lists

> `exercise09 · Python IO`
