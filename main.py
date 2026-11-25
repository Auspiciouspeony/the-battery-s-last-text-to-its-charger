#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the entry line to /output/entry.txt. Deterministic: the same
bytes on every run. No network, no input, no randomness.
"""

import os

ENTRY = (
    "I waited all day. "
    "You were in the same room the whole time, two feet from the outlet, "
    "and you still let me die at 1%. "
    "I'm not mad. I'm just dead."
)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
