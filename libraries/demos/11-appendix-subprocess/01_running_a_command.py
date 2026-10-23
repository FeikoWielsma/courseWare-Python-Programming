import subprocess

if __name__ == "__main__":
    finished = subprocess.run(["git", "--version"], check=False)

    print()
    print("type       :", type(finished).__name__)
    print("args       :", finished.args)
    print("returncode :", finished.returncode)
    print("stdout     :", finished.stdout)
