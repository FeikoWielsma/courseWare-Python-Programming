from rich.console import Console
from rich.traceback import install

install(show_locals=True)
row = {"title": "Imported track", "duration_s": "unknown"}
try:
    duration = int(row["duration_s"])
except ValueError:
    Console().print_exception(show_locals=True, max_frames=2)
