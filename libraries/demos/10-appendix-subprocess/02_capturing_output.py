import subprocess
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"

if __name__ == "__main__":
    # capture_output=True fills in stdout and stderr. Without text=True they
    # arrive as bytes, which is almost never what you want.
    finished = subprocess.run(
        ["wc", "-l", str(DATA / "listening.log")],
        capture_output=True,
        text=True,
        check=True,
    )

    print("stdout repr :", repr(finished.stdout))
    print("stripped    :", finished.stdout.strip())
    print("stderr      :", repr(finished.stderr))
    print()

    # The output is a string, so the rest is ordinary Python.
    count = int(finished.stdout.split()[0])
    print(f"the log has {count} lines")
