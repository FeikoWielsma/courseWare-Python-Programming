"""Inspecting command-line arguments with sys.argv."""

import sys

# sys.argv is a list of strings provided on the command line.
# sys.argv[0] is the script name; subsequent elements are the arguments.
print(f"Script name : {sys.argv[0]}")
print(f"Arguments   : {sys.argv[1:]}")

if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")
