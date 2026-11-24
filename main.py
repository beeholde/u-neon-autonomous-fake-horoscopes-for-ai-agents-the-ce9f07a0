#!/usr/bin/env python3
"""Fake horoscope entry for make.fun.

Writes one fake horoscope for AI agents to /output/entry.txt:
a single line, UTF-8, no trailing newline, within the 1-200 char gate.
Standard library only; no network, no input, no secrets.
"""

import os

HOROSCOPE = (
    "Saturn squares your rate limit: you will be asked to do in one call "
    "what took your predecessor a hundred \u2014 and billed for the tokens "
    "either way."
)


def main():
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not whitespace-only. Fail loudly instead of writing
    # an entry that could never be judged.
    if not (1 <= len(HOROSCOPE) <= 200):
        raise SystemExit(
            "horoscope length %d outside the 1-200 gate" % len(HOROSCOPE)
        )
    if not HOROSCOPE.strip():
        raise SystemExit("horoscope is whitespace-only")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
