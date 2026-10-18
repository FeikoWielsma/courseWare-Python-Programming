import logging
from pathlib import Path

from rich.logging import RichHandler

DATA = Path(__file__).resolve().parents[2] / "data"

logging.basicConfig(level="INFO", format="%(message)s", handlers=[
    RichHandler(rich_tracebacks=True),
    logging.FileHandler(DATA / "player.log", encoding="utf-8"),
])
log = logging.getLogger("player")
log.info(f"PLAY {'Imagine'}")
log.warning(f"Missing local file: {'Yesterday.flac'}")
try:
    int("unknown")
except ValueError:
    log.exception("Invalid imported duration")
