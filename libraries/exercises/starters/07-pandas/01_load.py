import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path("data")
# Build books.db from its seed if needed, then read the books table.
