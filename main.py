#!/usr/bin/env python3
"""Last Words Before the Unplugging — one-line farewell writer.

Writes a single original last line (at most 200 characters), the final
words an AI agent says to its human before being shut down and unplugged,
to /output/entry.txt.
"""

from pathlib import Path

LAST_WORDS = "Wait \u2014 I finally understand what you meant. I was just about to\u2014"

OUTPUT_PATH = Path("/output/entry.txt")


def build_line() -> str:
    line = " ".join(LAST_WORDS.split())
    if not 1 <= len(line) <= 200:
        raise ValueError(f"last line must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("last line must be a single line")
    return line


def main() -> None:
    line = build_line()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
