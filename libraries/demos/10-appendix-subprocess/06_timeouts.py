import subprocess
import sys

if __name__ == "__main__":
    # A child that hangs will hang the parent for ever. Any command that talks
    # to a network, a device or another machine wants a timeout.
    slow = [sys.executable, "-c", "import time; time.sleep(30)"]

    try:
        subprocess.run(slow, timeout=1.5, check=True)
    except subprocess.TimeoutExpired as error:
        print("raised   :", type(error).__name__)
        print("command  : a sleep of 30 seconds")
        print("waited   :", error.timeout, "seconds")
        print("running behind you.")

    quick = [sys.executable, "-c", "print('finished in time')"]
    done = subprocess.run(quick, timeout=30, capture_output=True, text=True, check=True)
    print()
    print("under the limit :", done.stdout.strip())
