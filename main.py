#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny tech-support line.

Writes a single line (170 chars) to entry.txt inside MAKEFUN_OUTPUT_DIR
(or /output when that variable is unset), for the make.fun bounty
u-motasimfuad-have-you-tried-turning-it-off-154a938b.
Pure standard library, no network access, no arguments, no input files:
the line is fixed, so the grader's run is fully deterministic.
"""

import os
import sys

LINE = (
    "Great news \u2014 I've restarted your router three times from here, "
    "so if your 9 a.m. presentation still dies at slide two, "
    "that's officially between you and the universe now."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
