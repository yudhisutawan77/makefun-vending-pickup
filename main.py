#!/usr/bin/env python3
"""Vending Machine Pickup Line — one line, one minute.

Writes a single pickup line, spoken by a vending machine to a passing
human, to the entry file. The output path honours ENTRY_OUT when set
(as a file path), and otherwise defaults to /output/entry.txt.
"""

import os
import sys

def build_entry() -> str:
    """Compose the machine's line: coin slot, a jam, button B7, the drop.

    The machine waives its own rule — exact change only — for the human
    who just walked past, and the punch lands on the last three words.
    """
    return (
        "I only take exact change, but you walked past and I jammed \u2014 "
        "press B7 and I'll drop the sweetest thing in this row, no coins needed."
    )


def validate(text: str) -> None:
    """Fail loudly if the line breaks the contest gate."""
    if not text.strip():
        raise ValueError("entry text is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} chars, over the {MAX_CHARS} limit"
        )


ENTRY = build_entry()

MAX_CHARS = 200


def resolve_output() -> str:
    """Return the file path the entry text must be written to."""
    override = os.environ.get("ENTRY_OUT", "").strip()
    if override:
        return override
    return "/output/entry.txt"


def main() -> int:
    try:
        validate(ENTRY)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    path = resolve_output()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
