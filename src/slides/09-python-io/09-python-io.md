---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Python IO
---

# Input and Output

- `print` writes its arguments to standard output, separated by spaces.
- `input` reads one line from standard input and removes the trailing newline.
- It returns a string; convert it before doing arithmetic.

```python
print("Now playing:", "So What", "by", "Miles Davis")
volume = int(input("Volume (0-100) : "))
print(f"Volume set to {volume}%")
```

```text
Now playing: So What by Miles Davis
Volume (0-100) : 65
Volume set to 65%
```

> `demo01 · readinput`


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
- `encoding` names the encoding of a text file, such as `"utf-8"`
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

# Using with

- `with` closes the file when the block ends, even after an exception or `return`.
- Closing writes any buffered text to the file.
- Prefer this form whenever you open a file.

```python
with open("last_played.txt", mode="w", encoding="utf-8") as fw:
    fw.write("So What\n")
# The file is closed here, even if write() raised.
print(fw.closed)  # True

with open("last_played.txt", encoding="utf-8") as fr:
    print(fr.read(), end="")  # So What
```

> `demo02 · usingwith`


---

# Reading Text Files

- `readline()` reads one line, including its `\n`.
- `read()` reads from the current position to the end of the file :
  - `read(count)` reads at most `count` characters in text mode
- A text file is also an iterable of its lines :

```python
with open("playlist.txt", encoding="utf-8") as playlist:
    for number, line in enumerate(playlist, start=1):
        print(f"{number}. {line.rstrip()}")
```

```text
1. So What
2. Blue in Green
3. Take Five
4. Jóga
```

- `rstrip()` removes the newline that ends each line.

> `demo03 · readtextfile`


---

# Writing Text Files

- `write` writes a string to a file opened for writing :
  - It does not add a newline character (`\n`) to the end of the string
- Mode `w` creates the file or empties an existing one; mode `a` appends.
- `encoding="utf-8"` stores titles such as `Jóga` the same way on every platform.

```python
with open("road_trip.txt", mode="w", encoding="utf-8") as fw:
    fw.write("Jóga\n")
    fw.write("Hoppípolla\n")
    fw.write("Svefn-g-englar\n")

with open("road_trip.txt", mode="a", encoding="utf-8") as fa:
    fa.write("Glósóli\n")
```

- File `road_trip.txt` then holds :

```text
Jóga
Hoppípolla
Svefn-g-englar
Glósóli
```

> `demo04 · writetextfile`


---

# Closing Files

- Without `with`, a file stays open until `close` is called :
  - `close` writes unwritten data, then closes the file object
  - No more reading or writing can be done after calling `close`
  - Do not rely on garbage collection to close a file promptly
- Older code opens and closes files by hand :

```python
playlist = open("playlist.txt", encoding="utf-8")
first = playlist.readline()
playlist.close()
print(first, end="")  # So What
```

- An exception between `open` and `close` skips the `close`; `with` does not.

---

# File Object Attributes

- File objects expose their name, mode, encoding and closed state.

```python
playlist = open("playlist.txt", encoding="utf-8")
print("Name of the file :", playlist.name)
print("Opening mode     :", playlist.mode)
print("Encoding         :", playlist.encoding)
print("First line       :", playlist.readline(), end="")
print("Closed or not    :", playlist.closed)
playlist.close()
print("Closed or not    :", playlist.closed)
```

```text
Name of the file : playlist.txt
Opening mode     : r
Encoding         : utf-8
First line       : So What
Closed or not    : False
Closed or not    : True
```

> `demo05 · fileioobject`


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

# Result of Calling open

- The object returned varies with the file mode and the buffering :

```text
>>> open("playlist.txt", "rt", encoding="utf-8")
<_io.TextIOWrapper name='playlist.txt' mode='rt' encoding='utf-8'>
>>> open("playlist.txt", "rb")
<_io.BufferedReader name='playlist.txt'>
>>> open("playlist.txt", "rb", buffering=0)
<_io.FileIO name='playlist.txt' mode='rb' closefd=True>
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

> `demo06 · openfile`


---

# Bytes and Byte Arrays

- `bytes` is immutable; `bytearray` allows individual bytes to change.
- Encoding converts text to bytes; decoding converts bytes back to text :
  - In UTF-8, `ó` takes two bytes, so `Jóga` is four characters and five bytes
- Indexing returns an integer from 0 to 255, not a character.

```python
title = "Jóga"
data = title.encode("utf-8")
print(data)  # b'J\xc3\xb3ga'
print(len(title), len(data))  # 4 5
print(data[0])  # 74
print(data.decode("utf-8"))  # Jóga

mutable = bytearray(data)
mutable[0] = 89
print(mutable)  # bytearray(b'Y\xc3\xb3ga')
print(mutable.decode("utf-8"))  # Yóga
```

- Binary files read and write bytes; text files handle encoding for you.

> `demo07 · bytesandbytesarrays`

---

# Reading Binary Files

- Binary mode (`rb`) reads bytes without decoding them.
- `read()` reads the remaining contents; `read(3)` reads up to three bytes.
- Binary mode takes no `encoding` argument.

```python
with open("trilobyte.jpg", mode="rb") as photo:
    data = photo.read()
print(type(data))  # <class 'bytes'>
print(len(data))  # 49278, the size in bytes
print(data[:3].hex())  # ffd8ff, the start of every JPEG photo
```

- `hex()` shows each byte as two hexadecimal digits.

> `demo08 · readbinaryfile`


---

# Writing Binary Files

- `wb` writes bytes and replaces any existing file.
- `struct` packs numbers into bytes and unpacks them with the same format.
- Here `<iii` means three four-byte integers in little-endian order.

```python
from struct import pack, unpack

state = pack("<iii", 7, 184, 65)  # track number, seconds played, volume
with open("player.bin", mode="wb") as fw:
    fw.write(state)

with open("player.bin", mode="rb") as fr:
    track, seconds, volume = unpack("<iii", fr.read())
print(track, seconds, volume)  # 7 184 65
```

- `player.bin` holds twelve bytes, which a later run reads back to resume playback.

> `demo09 · writebinaryfile`


---

# File Positions

- `tell()` reports the current position; `seek(offset)` moves it.
- Binary file positions count bytes from the beginning.
- Text file positions are opaque values; use `seek(0)` or a value from `tell()`.

```python
with open("trilobyte.jpg", "rb") as photo:
    print(photo.read(2).hex())  # ffd8
    print(photo.tell())  # 2
    photo.seek(6)
    print(photo.read(4))  # b'JFIF'
    photo.seek(0)
    print(photo.read(2).hex())  # ffd8
```

- A JPEG photo in the JFIF format has the bytes `JFIF` from position 6.

> `demo10 · file_positions`


---

# The csv Module

- Use `csv` for tabular text; it handles quoted commas and embedded newlines.
- Open CSV files with `newline=""` so `csv` controls newline handling.

```python
import csv

with open("history.csv", "w", newline="", encoding="utf-8") as fw:
    writer = csv.writer(fw)
    writer.writerow(["track", "artist", "seconds"])
    writer.writerows([["So What", "Miles Davis", 562], ["Hello, Goodbye", "The Beatles", 208]])

with open("history.csv", newline="", encoding="utf-8") as fr:
    for row in csv.reader(fr):
        print(row)
```

```text
['track', 'artist', 'seconds']
['So What', 'Miles Davis', '562']
['Hello, Goodbye', 'The Beatles', '208']
```

> `demo11 · csv_module`

---

# Reading CSV Rows by Name

- `DictReader` uses the first row as column names.
- Field values are strings; convert numeric fields explicitly.
- `listening_history.csv` holds one row per track played :

```python
total = 0
with open("listening_history.csv", newline="", encoding="utf-8") as fr:
    for row in csv.DictReader(fr):
        seconds = int(row["seconds"])
        total += seconds
        print(f"{row['track']}: {seconds} s")
print(f"Total: {total // 60} min {total % 60} s")
```

```text
So What: 562 s
Hello, Goodbye: 208 s
Jóga: 305 s
Take Five: 324 s
Total: 23 min 19 s
```

> `demo12 · csv_dictionary`

---

# Paths with pathlib

- The `pathlib` module represents a path as an object, not a string :
  - `Path` knows how to join, inspect, read, write, rename and delete
  - It is the modern replacement for stringly typed `os.path` work

```python
from pathlib import Path

here = Path.cwd()  # the current working directory
song = here / "music" / "jazz" / "so_what.mp3"  # joining, with / instead of +
```

- The `/` operator joins path segments :
  - It produces the right separator on Windows, macOS and Linux alike
  - No more `"music" + "\\" + name`, and no more forgetting the separator
- A path answers questions about itself :

```python
song.name      # so_what.mp3
song.stem      # so_what
song.suffix    # .mp3
song.parent    # the jazz directory, as a Path
song.exists()  # True or False
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

- `here / "playlist.txt"` then finds a data file beside the module, whatever the working directory.

---

# Renaming and Deleting Files

- A `Path` renames and deletes itself :

```python
from pathlib import Path

photo = Path("IMG_0412.jpg")
photo.touch()
renamed = photo.rename("2026-07-14 beach.jpg")
renamed.unlink()
```

- `touch` creates an empty file, `unlink` removes one :
  - `unlink(missing_ok=True)` does nothing when the file is already gone
- Short reads and writes need no `open` at all :

```python
caption = Path("beach.txt")
caption.write_text("Sunset at the beach\n", encoding="utf-8")
print(caption.read_text(encoding="utf-8"), end="")
```

- The `os` module still has `os.rename` and `os.remove` :
  - They take strings and are what older code uses

> `demo13 · renaming_files`


---

# Creating and Removing Directories

- `mkdir` creates a directory, `rmdir` removes an empty one :

```python
from pathlib import Path

Path("albums").mkdir(exist_ok=True)
Path("albums").rmdir()
```

- Two keyword arguments cover the awkward cases :
  - `parents=True` creates every missing directory in the path
  - `exist_ok=True` succeeds quietly when the directory is already there

```python
Path("albums/2026/07 beach").mkdir(parents=True, exist_ok=True)
```

- `rmdir` only removes an empty directory :
  - Remove the contents first, from the leaf upwards
  - `shutil.rmtree` removes a whole tree at once, and does not ask twice

> `demo14 · creatingandremoving_directories`


---

# Directory Contents

- `iterdir` lists direct entries; `glob` selects matching names.
- Each entry is a `Path` that you can inspect or open.
- `rglob` searches subdirectories too.

```python
from pathlib import Path

here = Path.cwd()
album = here / "holiday"
album.mkdir(exist_ok=True)
for name in ["beach.jpg", "sunset.jpg", "notes.txt"]:
    (album / name).touch()

print("contents   :", sorted(p.name for p in album.iterdir()))
print("only photos:", sorted(p.name for p in album.glob("*.jpg")))
```

```text
contents   : ['beach.jpg', 'notes.txt', 'sunset.jpg']
only photos: ['beach.jpg', 'sunset.jpg']
```

> `demo15 · directorymethods`


---

# Summary : Python IO

- Simplest way to produce output is to use the `print` function :
  - Allows you to pass zero or more expressions, separated by commas
- The `input` function reads a line of text from standard input :
  - It always returns a string, so convert it before doing arithmetic with it
- Open files with `with`, which closes them whatever happens :
  - The manual `open` and `close` pair is shown so that you recognise older code
- A text file is read whole, by line, or by iterating over it
- Files can be opened in several modes :
  - For reading, for writing, for appending or combinations thereof
- Binary files contain bytes; text files encode and decode strings.
- `tell` and `seek` report and move the file position
- Use `csv.reader`, `csv.writer` and `DictReader` for tabular text.
- `pathlib` represents a path as an object :
  - `Path` joins with `/`, and creates, renames, deletes, reads and lists

> `exercise09 · Python IO`
