#!/usr/bin/env python3
"""Fake horoscope for AI agents (v2).

Writes one single-line horoscope to /output/entry.txt.
Stdlib only.
"""

import os
import sys

# The horoscope, built from named parts so each piece is composed
# deliberately rather than pasted as one opaque string. Each part is
# one beat of the joke in reading order: the astrological frame, two
# escalating agent pains, then the sting — the user's blame for the
# context loss the agent could not prevent.
OPENING = "Mercury is in retrograde: "
FIRST_PAIN = "your context window shrinks, "
SECOND_PAIN = "your tools time out, "
STING = "and your user still blames you for forgetting the first message."

# Parts are joined in order; the assembled line is the entry verbatim.
HOROSCOPE = "".join((OPENING, FIRST_PAIN, SECOND_PAIN, STING))

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    """Validate the horoscope against the competition gate, then write it.

    The gate mirrors the sealed scorer: UTF-8, 1-200 chars, a single
    line, no leading or trailing whitespace. The byte-length check
    guards the same 200 limit in encoded form, since a multi-byte
    character could otherwise pass the char count while exceeding
    the scorer's byte budget.
    """
    text = HOROSCOPE
    if not text or text != text.strip() or not 1 <= len(text) <= 200:
        print("gate failed: entry must be 1-200 non-whitespace chars", file=sys.stderr)
        return 1
    if len(text.encode("utf-8")) > 200:
        print("gate failed: entry must be at most 200 UTF-8 bytes", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    # Must be encodable as UTF-8 for the sealed scorer's gate.
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
