import shutil
import subprocess
import tempfile
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"

if __name__ == "__main__":
    # A filename with a space in it. Perfectly ordinary, and the commonest
    # way this goes wrong in real life.
    with tempfile.TemporaryDirectory() as workspace:
        awkward = Path(workspace) / "last week.log"
        shutil.copy(DATA / "cli-sample.log", awkward)

        # A list hands the arguments to the program directly. No shell starts,
        # so nothing splits on the space.
        listed = subprocess.run(
            ["wc", "-l", str(awkward)], capture_output=True, text=True, check=False
        )
        print(f"as a list  : rc={listed.returncode}  {listed.stdout.strip()}")

        # shell=True hands the whole string to a shell first, and the shell splits on
        # whitespace.
        shelled = subprocess.run(
            f"wc -l {awkward}", shell=True, capture_output=True, text=True, check=False
        )
        print(f"with shell : rc={shelled.returncode}  {shelled.stderr.strip()[:60]}")

    # Punctuation is worse than whitespace. `&` separates commands in every
    # shell this is likely to meet; on a POSIX shell `;` and `|` do too.
    hostile = "nowhere.log & echo INJECTED"
    injected = subprocess.run(
        f"wc -l {hostile}", shell=True, capture_output=True, text=True, check=False
    )
    print()
    if "INJECTED" in injected.stdout:
        print("The shell ran the second command : ", injected.stdout.strip().splitlines()[-1])
