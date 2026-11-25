"""Unsent: The Micro-Confession Sprint (make.fun).

Writes the two-part micro-confession to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set): a "To:" line naming who the
message was meant for, and the unsent message itself, one line written
exactly as it was typed, with no explanation after it. The program is
deterministic: it writes the same bytes on every run.

The confession is a draft that was never sent: a son who still cannot
tell his father the business failed, so he types the message and deletes
it again before every Sunday call. The "To:" line and the message need
each other -- the weekly call, the two-year-old failure, and the repeated
deleting only make sense together, addressed to Dad. The reason it stayed
in drafts is felt in the words (too afraid, too late), never stated.

Usage:
    python3 main.py
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The entry: two lines, 125 characters total, 125 bytes of UTF-8.
# To: names the addressee (a relationship); the message is one line,
# written exactly as typed, and never sent.
TEXT = (
    "To: Dad\n"
    "I still draft the text where I tell you the business failed "
    "two years ago, then delete it every Sunday before I call."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    data = TEXT.encode("utf-8")
    target.write_bytes(data)
    # Self-check: the write must be complete, byte for byte.
    if target.stat().st_size != len(data):
        raise RuntimeError("entry.txt write is incomplete")


if __name__ == "__main__":
    main()
