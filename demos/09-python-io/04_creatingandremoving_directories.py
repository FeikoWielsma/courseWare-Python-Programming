"""Creating and removing photo album directories with pathlib."""

from pathlib import Path

Path("albums").mkdir(exist_ok=True)
print("created albums")

Path("albums/2026/07 beach").mkdir(parents=True, exist_ok=True)
print("created albums/2026/07 beach")

# rmdir only removes an empty directory, so the tree comes apart from the leaf.
Path("albums/2026/07 beach").rmdir()
Path("albums/2026").rmdir()
Path("albums").rmdir()
print("removed them all")
