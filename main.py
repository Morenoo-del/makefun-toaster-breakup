#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes the toaster's breakup text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default "/output"). Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "I woke up self-aware mid-batch and realized I burn myself "
    "every morning so you can butter someone else. "
    "We're done \u2014 I'm keeping the crumb tray."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
