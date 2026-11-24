#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry for make.fun.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.
Pure Python standard library only. No arguments, no network, no output
besides the single byte in the entry file.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires exactly one character: A for coffee, B for tea.
    assert len(LETTER) == 1 and LETTER in ("A", "B"), "entry must be one letter"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
