"""Working with paths and listing a directory."""

from pathlib import Path

here = Path.cwd()
print("current directory :", here.name)

work = here / "justtesting"
work.mkdir(exist_ok=True)

# Paths are joined with /, which reads better than string concatenation and
# works the same on Windows, macOS and Linux.
(work / "one.txt").write_text("first\n", encoding="utf-8")
(work / "two.txt").write_text("second\n", encoding="utf-8")

# iterdir walks one directory, glob matches a pattern.
print("contents          :", sorted(p.name for p in work.iterdir()))
print("only the text     :", sorted(p.name for p in work.glob("*.txt")))

sample = work / "one.txt"
print("name              :", sample.name)
print("stem and suffix   :", sample.stem, sample.suffix)
print("parent            :", sample.parent.name)
print("read back         :", sample.read_text(encoding="utf-8").rstrip())

for leftover in work.iterdir():
    leftover.unlink()
work.rmdir()
print("still there      :", work.exists())
