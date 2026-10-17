import subprocess
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
LOG = DATA / "cli-sample.log"

if __name__ == "__main__":
    # input= writes to the child's stdin and closes it. No shell involved.
    text = LOG.read_text(encoding="utf-8")
    counted = subprocess.run(["wc", "-l"], input=text, capture_output=True, text=True, check=True)
    print("piped in    :", counted.stdout.strip(), "lines")

    # Two commands joined without a shell :
    levels = subprocess.run(
        ["grep", "-o", "-E", "INFO|WARN|ERROR", str(LOG)],
        capture_output=True,
        text=True,
        check=True,
    )
    tallied = subprocess.run(
        ["sort"], input=levels.stdout, capture_output=True, text=True, check=True
    )
    summary = subprocess.run(
        ["uniq", "-c"], input=tallied.stdout, capture_output=True, text=True, check=True
    )
    print()
    print("grep | sort | uniq -c, without a shell :")
    for line in summary.stdout.strip().splitlines():
        print("  ", line.strip())
