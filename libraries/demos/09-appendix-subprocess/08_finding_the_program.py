import shutil
import subprocess

if __name__ == "__main__":
    # which() answers the question without running anything, so a script can
    # check its dependencies up front and say something useful.
    for program in ("git", "grep", "definitely-not-installed"):
        location = shutil.which(program)
        print(f"{program:<26} {location or '-- not on PATH'}")

    print()
    # Without the check, a missing program is a FileNotFoundError, and the
    # message names the program rather than the argument list.
    try:
        subprocess.run(["definitely-not-installed", "--help"], check=True)
    except FileNotFoundError as error:
        print("raised :", type(error).__name__)
        print("        ", error)
