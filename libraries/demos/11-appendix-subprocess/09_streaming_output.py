import subprocess
import sys

CHILD = (
    "import sys, time\n"
    "for step in range(1, 6):\n"
    "    print(f'step {step} of 5', flush=True)\n"
    "    time.sleep(0.3)\n"
)

if __name__ == "__main__":
    print("run() would show nothing until all of this had finished :")
    print()

    with subprocess.Popen(
        [sys.executable, "-c", CHILD],
        stdout=subprocess.PIPE,
        text=True,
        bufsize=1,
    ) as process:
        # Iterating the pipe yields lines as the child flushes them.
        for line in process.stdout:
            print("  received :", line.rstrip())

    print()
    print("returncode :", process.returncode)
