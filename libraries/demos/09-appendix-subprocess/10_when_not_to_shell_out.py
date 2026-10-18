import shutil
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"

if __name__ == "__main__":
    # Starting a process costs milliseconds and brings quoting, portability
    # and error handling with it. These all avoid that entirely.
    print("instead of shelling out :")
    print()

    logs = sorted(DATA.glob("*.log"))
    print(f"  ls *.log        -> Path.glob            {[p.name for p in logs]}")

    text = (DATA / "listening.log").read_text(encoding="utf-8")
    print(f"  wc -l           -> str.splitlines       {len(text.splitlines())}")

    errors = [line for line in text.splitlines() if "ERROR" in line]
    print(f"  grep ERROR      -> a comprehension      {len(errors)} lines")

    print(f"  basename        -> Path.name            {(DATA / 'listening.log').name}")
    print(f"  dirname         -> Path.parent          {(DATA / 'listening.log').parent.name}")
    print(f"  test -f         -> Path.exists          {(DATA / 'listening.log').exists()}")
    print(f"  du -sb          -> Path.stat            {(DATA / 'listening.log').stat().st_size}")
    print(f"  which           -> shutil.which         {bool(shutil.which('git'))}")
    print("  cp / mv / rm    -> shutil.copy, Path.rename, Path.unlink")
    print("  mkdir -p        -> Path.mkdir(parents=True, exist_ok=True)")
    print("  find            -> Path.rglob")
