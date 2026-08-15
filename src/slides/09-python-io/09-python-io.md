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
print ("Python is really a great language,", "isn't it? ")
```

- Major difference between version 2 and 3 of the language :
  - In version 3 print is a function
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

```python
file_object = open(file ,mode=r, buffering=-1, Encoding=None )
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
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
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
fw = open('binaryfile04.txt', mode='wb')
```

- Use `pack` method of `struct` module to prepare buffer for writing :
  - Format string determines how packing takes place

```python
nr1 = 1; nr2 = 2; result = nr1 + nr2
buffer = pack("iii", nr1, nr2, result)
fw.write(buffer)
```

- Data must be read like it is written using same format string :

```python
fr = open('binaryfile04.txt', mode='rb')
buffer = fr.read()
data = unpack("iii", buffer)
```

- Returned data is a tuple that can be accessed as follows :

```python
num1 = data[0], num2 = data[1], res = data[2]
```

> `demo05 · writebinaryfile`


---

# Writing Text Files

- Open file for writing specifying mode and encoding :

```python
fw = open('textfilepolish.txt', mode='w', encoding='UTF-8')
```

- `write` method writes any string to an open file :
  - Parameter is the content to be written into the opened file
  - Does not add a newline character ('\n') to the end of the string

```python
s = 'Polish text: ąćęłńóśźżĄĆĘŁŃÓŚŹŻ'
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
fr = open('textfilepolish.txt', mode='r', encoding='UTF-8')
```

- `read` method reads a string from an open file :
  - Parameter is the number of bytes to be read from the opened file

```python
file_object.read([count]);
```

- `read()` starts reading from the beginning of the file :
  - If count is missing then it tries to read as much as possible, may be until end of file
- Example of reading and closing file `textfilepolish.txt` :

```python
data = fr.read()
print (data)
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
file_object.close();
```

- Example :

```python
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
fo.close()
```

- Result :

```text
Name of the file: foo.txt
```

- Good practice to use `close()` method to close a file

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
str = fo.read(10);
print ("Read String is : ", str)
# Check current position
position = fo.tell();
print ("Current file position : ", position)
# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print ("Again read String is : ", str)
fo.close()
```

- Result :

```text
Read String is : Python is
Current file position : 10
Again read String is : Python is
```

---

# Renaming and Deleting Files

- Files can be renamed and deleted :
  - `os` module has methods for file-processing operations like renaming and deleting
  - `os` module must first be imported before methods can be called
- `rename` method takes two arguments :
  - Current filename and new filename

```python
os.rename(current_file_name, new_file_name)
```

- Rename an existing file from `test1.txt` to `test2.txt` :

```python
import os
os.rename( "test1.txt", "test2.txt" )
```

- Delete an existing file `test2.txt` :

```python
import os
os.remove("text2.txt")
```

> `demo07 · renaming_files`


---

# Creating and Removing Directories

- Files are in directories and Python can handle directories too :
  - os module has methods to create, remove, and change directories
- `mkdir()` method creates directory in the current directory :
  - Argument is name of the directory to be created
- Syntax : `os.mkdir("newdir")`
- Example to create a directory test in current directory :

```python
import os
os.mkdir("test")
```

- `rmdir()` method deletes the directory passed as an argument :
  - Before removing a directory, all the contents in it should be removed
- Syntax : `os.rmdir('dirname')`
- Example to remove `"/tmp/test"` directory :
  - Give fully qualified name of directory otherwise search directory in current directory

```python
import os
os.rmdir("/tmp/test")
```

> `demo08 · creatingandremoving_directories`


---

# Directory Methods

- `chdir()` changes the current directory :
  - Argument is the name of the directory that you want to make the current directory
- Syntax :

```python
os.chdir("newdir")
```

- Example changing a directory to `"/home/newdir"` :

```python
import os
os.chdir("/home/newdir")
```

- `getcwd()` displays the current working directory
- Syntax :

```python
os.getcwd()
```

- Example to give location of the current directory :

```python
import os
os.getcwd()
```

> `demo09 · directorymethods`


---

# Summary : Python IO

- Simplest way to produce output is to use the `print` statement :
  - Allows you to pass zero or more expressions, separated by commas
- Two built-in functions read a line of text from standard input :
  - `raw_input` reads one line from standard input and returns it as string
  - `input` assumes input is a valid Python expression and returns evaluated result
- Python also has File Object methods to manipulate files :
  - Creating, opening files, closing files, reading, writing, renaming and deleting files
- Files can be opened in several modes :
  - For reading, for writing, for appending or combinations thereof
- File Positioning :
  - Methods can retrieve and change the current file position
- Python also has OS Object Methods to manipulate directories :
  - Creating and deleting directories
  - Changing and displaying the current directory

> `exercise09 · Python IO`
