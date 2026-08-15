"""Renaming and deleting a file with pathlib."""

from pathlib import Path

data_file = Path("datafile1.txt")

# touch() creates an empty file, like `open(..., "w")` and closing it again.
data_file.touch()
print("created  :", data_file, data_file.exists())

# rename() returns the new path, so the result can be used straight away.
renamed = data_file.rename("renamedfile.txt")
print("renamed  :", renamed, renamed.exists())

renamed.unlink()
print("deleted  :", renamed.exists())

# missing_ok avoids an error when the file is already gone.
renamed.unlink(missing_ok=True)
