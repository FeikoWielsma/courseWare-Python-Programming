import time
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__).resolve().parents[2] / "data"


def main() -> None:
    log_file: Path = DATA / "cli-sample.log"
    total_bytes: int = log_file.stat().st_size

    # Reading a file in chunks has no item count, only a byte count.
    lines: int = 0
    with (
        tqdm(total=total_bytes, desc="Reading log", unit="B", unit_scale=True) as bar,
        log_file.open("rb") as handle,
    ):
        while chunk := handle.read(64):
            lines += chunk.count(b"\n")
            bar.update(len(chunk))
            time.sleep(0.02)

    print(f"\n{lines} lines in {total_bytes} bytes")

    # set_postfix hangs live counters off the right-hand end of the bar, which
    # is where a running tally of successes and failures belongs.
    with tqdm(total=20, desc="Applying patches", unit="pkg") as bar:
        ok: int = 0
        failed: int = 0
        for index in range(20):
            time.sleep(0.05)
            if index % 7 == 6:
                failed += 1
            else:
                ok += 1
            bar.set_postfix(ok=ok, failed=failed)
            bar.update(1)


if __name__ == "__main__":
    main()
