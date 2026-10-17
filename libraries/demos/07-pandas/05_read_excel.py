from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"
WORKBOOK = DATA / "servers.xlsx"

with pd.ExcelFile(WORKBOOK) as book:
    print(book.sheet_names)

print(pd.read_excel(WORKBOOK, sheet_name="servers").head(3).to_string())
print(pd.read_excel(WORKBOOK, sheet_name="sites").to_string())

# Reading every sheet at once gives a dictionary keyed by sheet name.
everything = pd.read_excel(WORKBOOK, sheet_name=None)
print({name: frame.shape for name, frame in everything.items()})
