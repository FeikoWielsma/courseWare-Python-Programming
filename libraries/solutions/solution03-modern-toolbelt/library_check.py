import csv
import time
from pathlib import Path

from rich.console import Console
from rich.table import Table
from tqdm import tqdm

DATA = Path(__file__).resolve().parents[2] / "data"


def load(source: Path) -> list[dict[str, str]]:
    with source.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def find_issues(rows: list[dict[str, str]]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    issues: list[tuple[str, str]] = []
    for row in tqdm(rows, desc="Checking", unit="track"):
        time.sleep(0.01)
        title = row["title"]
        if not row["duration_s"]:
            issues.append((title, "missing duration"))
        if title in seen:
            issues.append((title, "duplicate title"))
        seen.add(title)
    return issues


def build_table(issues: list[tuple[str, str]]) -> Table:
    table = Table("Title", "Problem", title="Library check", row_styles=["", "dim"])
    for title, problem in sorted(issues):
        table.add_row(title, f"[yellow]{problem}[/]")
    return table


def main() -> None:
    rows = load(DATA / "tracks-import.csv")
    issues = find_issues(rows)
    Console().print(build_table(issues))
    print(f"{len(rows)} records, {len(issues)} issues")


if __name__ == "__main__":
    main()
