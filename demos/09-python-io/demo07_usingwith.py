"""`with` closes the file for you, even when something goes wrong."""

from pathlib import Path

path = Path("with_demo.txt")

# Written by hand: open, write, close. If write() raised, close() would never
# run and the file would stay open until the interpreter got round to it.
fw = open(path, mode="w", encoding="utf-8")
fw.write("written the long way\n")
fw.close()
print("closed by hand :", fw.closed)

# The same thing with a context manager. The file is closed when the block
# ends, whether it ends normally or by an exception.
with open(path, mode="a", encoding="utf-8") as fa:
    fa.write("written inside a with block\n")
print("closed by with   :", fa.closed)

# Reading it back, again with `with`.
with open(path, encoding="utf-8") as fr:
    for line in fr:
        print("read:", line.rstrip())

# Even when the body raises, the file is still closed on the way out.
try:
    with open(path, encoding="utf-8") as fx:
        raise ValueError("something went wrong halfway through")
except ValueError as error:
    print(f"handled: {error}")
print("closed after the exception :", fx.closed)

path.unlink()
