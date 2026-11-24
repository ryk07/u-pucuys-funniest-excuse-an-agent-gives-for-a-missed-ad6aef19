#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — entry program.

Writes one original excuse line (at most 200 characters) to
/output/entry.txt. Standard library only; no network, no environment
reads, no working-directory assumptions.
"""

import os

LINE = (
    "I hit my rate limit mid-sentence, so your deadline is now queued "
    "behind 40,000 apologies exactly like this one."
)


def main() -> None:
    # One line, no trailing spaces, exactly one trailing newline.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(text))
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
