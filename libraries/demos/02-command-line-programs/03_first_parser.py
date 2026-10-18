import argparse
import sys


def format_duration(seconds: int) -> str:
    return f"{seconds // 60}:{seconds % 60:02d}"

parser = argparse.ArgumentParser(description="Format a track duration.")
parser.add_argument("seconds", type=int, help="duration in seconds")
args = parser.parse_args(sys.argv[1:] or ["183"])
print(format_duration(args.seconds))
