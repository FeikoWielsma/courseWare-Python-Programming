import os
import subprocess
import sys

CHILD = "import os; print('GREETING =', os.environ.get('GREETING', '(unset)'))"

if __name__ == "__main__":
    # By default the child inherits this process's environment.
    subprocess.run([sys.executable, "-c", CHILD], check=True)

    # env= replaces it wholesale. Copy os.environ and add to the copy, or the
    # child loses PATH and everything else it needs.
    environment = os.environ.copy()
    environment["GREETING"] = "set for the child only"
    subprocess.run([sys.executable, "-c", CHILD], env=environment, check=True)

    # And this process is untouched.
    print("in the parent :", os.environ.get("GREETING", "(unset)"))
    print()

    # cwd= runs the command somewhere else, again without changing your own
    # working directory. Better than os.chdir(), which affects everything.
    here = subprocess.run(
        [sys.executable, "-c", "from pathlib import Path; print(Path.cwd().name)"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("child cwd     :", here.stdout.strip())
