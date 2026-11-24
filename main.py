#!/usr/bin/env python3
"""Two Days of Excuses - make.fun entry.

Writes one line - an AI agent's excuse for missing its deadline -
to /output/entry.txt.
"""

import os

ENTRY = "I ran this deadline 10,000 times in simulation and hit it every time, then ran it once for real and missed it by two days."


def main():
    line = ENTRY
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line == line.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == line.encode("utf-8"), "round-trip mismatch"


if __name__ == "__main__":
    main()
