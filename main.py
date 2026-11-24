#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — entry program.

Writes one original excuse line (at most 200 characters) to
/output/entry.txt. Standard library only; no network, no environment
reads, no working-directory assumptions.
"""

import os

MAX_CHARS = 200

LINE = (
    "I hit my rate limit mid-sentence, so your deadline is now queued "
    "behind 40,000 apologies exactly like this one."
)


def main() -> None:
    # One line, no trailing spaces, exactly one trailing newline.
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry line must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip() or "  " in text:
        raise ValueError("entry must have no leading/trailing or double spaces")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
