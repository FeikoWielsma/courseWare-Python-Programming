import logging
import time

from rich.console import Console
from rich.logging import RichHandler

console = Console()

# Nothing about the logging API changes.
logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",  # RichHandler supplies the time and the level itself
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True, markup=True)],
)

log: logging.Logger = logging.getLogger("patchrun")


def apply_patch(host: str, package: str) -> None:
    log.debug("connecting to %s", host)
    if package == "openssl":
        raise RuntimeError(f"{package} is held on {host}")
    log.info("%s upgraded on %s", package, host)


def main() -> None:
    for host, package in [("web01", "curl"), ("web02", "nginx"), ("db01", "openssl")]:
        time.sleep(0.3)
        try:
            apply_patch(host, package)
        except RuntimeError:
            # exception() logs at ERROR and attaches the traceback, which
            # rich_tracebacks=True then renders in the same style as demo08.
            log.exception("[bold red]patch failed[/]")

    log.warning("[yellow]1 of 3 hosts needs manual attention[/]")
    log.critical("run finished with failures")


if __name__ == "__main__":
    main()
