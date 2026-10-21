"""Renaming and deleting a photo with pathlib."""

from pathlib import Path

photo = Path("IMG_0412.jpg")
photo.touch()
print("created  :", photo, photo.exists())

renamed = photo.rename("2026-07-14 beach.jpg")
print("renamed  :", renamed, renamed.exists())

renamed.unlink()
print("deleted  :", renamed.exists())
renamed.unlink(missing_ok=True)

caption = Path("beach.txt")
caption.write_text("Sunset at the beach\n", encoding="utf-8")
print(caption.read_text(encoding="utf-8"), end="")
caption.unlink()
