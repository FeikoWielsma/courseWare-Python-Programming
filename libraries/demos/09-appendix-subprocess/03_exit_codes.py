import subprocess
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
LOG = DATA / "cli-sample.log"

if __name__ == "__main__":
    # grep exits 0 when it matched, 1 when it did not, 2 on a real error.
    # That is a normal convention, so check=False and read the code yourself.
    for pattern in ("ERROR", "NOTHING-MATCHES-THIS"):
        found = subprocess.run(
            ["grep", "-c", pattern, str(LOG)], capture_output=True, text=True, check=False
        )
        print(f"{pattern:<22} returncode={found.returncode}  matched={found.stdout.strip()}")

    print()
    # check=True turns a non-zero exit into an exception. Use it when a failure
    # genuinely means the program cannot continue.
    try:
        subprocess.run(["grep", "NOTHING-MATCHES-THIS", str(LOG)], capture_output=True, check=True)
    except subprocess.CalledProcessError as error:
        print("raised     :", type(error).__name__)
        print("returncode :", error.returncode)
        print("command    :", error.cmd[:2], "...")
