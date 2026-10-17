import csv
import time
from collections import defaultdict
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__).resolve().parents[2] / "data"


def servers_by_site() -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            grouped[row["site"]].append(row["hostname"])
    return dict(grouped)


def main() -> None:
    sites: dict[str, list[str]] = servers_by_site()

    # leave=False on the inner bar is the trick. Without it every finished
    # inner bar stays on screen and the terminal fills up with dead bars.
    for site, hosts in tqdm(sites.items(), desc="Sites", unit="site"):
        for host in tqdm(hosts, desc=f"  {site}", unit="host", leave=False):
            time.sleep(0.15)
            _ = host

    print(f"\nVisited {len(sites)} sites, {sum(len(h) for h in sites.values())} hosts")


if __name__ == "__main__":
    main()
