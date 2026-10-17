import csv
import time
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__).resolve().parents[2] / "data"


def read_servers() -> list[dict[str, str]]:
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def check(server: dict[str, str]) -> bool:
    time.sleep(0.18)
    # The fixture has a blank used_gb on purpose; a host we cannot measure is
    # not a host we can call healthy.
    if not server["used_gb"]:
        return False
    return float(server["used_gb"]) / float(server["disk_gb"]) < 0.9


def main() -> None:
    servers: list[dict[str, str]] = read_servers()

    # The whole API is this: put tqdm() around the thing you were already
    # looping over. The loop body does not change at all.
    healthy: int = 0
    for server in tqdm(servers, desc="Checking servers", unit="host"):
        if check(server):
            healthy += 1

    print(f"\n{healthy} of {len(servers)} servers below 90% disk")

    # tqdm needs a length to show a percentage.
    rows = (row for row in servers)
    for _ in tqdm(rows, total=len(servers), desc="From a generator", unit="host"):
        time.sleep(0.02)


if __name__ == "__main__":
    main()
