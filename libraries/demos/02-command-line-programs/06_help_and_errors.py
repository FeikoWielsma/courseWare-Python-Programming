import argparse

parser = argparse.ArgumentParser(prog="duration", description="Format seconds.")
parser.add_argument("seconds", type=int)
for sample in (["--help"], [], ["unknown"], ["183"]):
    try:
        args = parser.parse_args(sample)
        print(f"{args.seconds // 60}:{args.seconds % 60:02d}")
    except SystemExit as stop:
        print(f"argparse status: {stop.code}")
