"""Creating and removing directories with pathlib."""

from pathlib import Path

# exist_ok keeps the demo re-runnable.
Path("test1").mkdir(exist_ok=True)
Path("test2").mkdir(exist_ok=True)
print("created test1 and test2")

# parents makes the whole chain, exist_ok stops it complaining if it is there.
Path("test2/nested/deeper").mkdir(parents=True, exist_ok=True)
print("created a nested tree")

# rmdir only removes an empty directory, so the tree comes apart from the leaf.
Path("test2/nested/deeper").rmdir()
Path("test2/nested").rmdir()
Path("test2").rmdir()
Path("test1").rmdir()
print("removed them all")
