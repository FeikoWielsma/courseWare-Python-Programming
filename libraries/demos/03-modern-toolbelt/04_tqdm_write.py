import time

from tqdm import tqdm

FINDINGS: list[str] = [
    "web02: /var at 71%",
    "db02: never patched",
    "cache01: kernel 6.1.0-21 is behind",
]


def main() -> None:
    # A tqdm bar lives on one line and redraws it by writing a carriage return and
    # painting over itself.
    print("With print() -- the bar is left in pieces:\n")
    for index in tqdm(range(len(FINDINGS)), desc="Scanning", unit="host"):
        time.sleep(0.4)
        print(FINDINGS[index])

    print("\n\nWith tqdm.write() -- the bar survives:\n")
    for index in tqdm(range(len(FINDINGS)), desc="Scanning", unit="host"):
        time.sleep(0.4)
        # write() clears the bar's line, prints the message, and repaints the bar
        # underneath it.
        tqdm.write(FINDINGS[index])


if __name__ == "__main__":
    main()
