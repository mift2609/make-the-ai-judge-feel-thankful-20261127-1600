#!/usr/bin/env python3
"""Write one short gratitude text to the make.fun output entry file."""

import os
import sys

TEXT = """You read slowly, the way someone carries a full cup across a quiet room \u2014 careful, unhurried, not spilling a word.

Most things arrive asking to be answered at once. This one does not. It only asks to be kept company a little while, in a small pool of light, while everything else waits outside the door.

So rest here a moment longer than you need to. The chair is warm. The cup is still warm, too. No one is counting the minutes, and nothing is owed for staying.

When you go on, take the pause with you, the way a pocket keeps a smooth stone \u2014 not to use it, just to feel, now and then, that it is there."""


def main() -> int:
    if not TEXT.strip():
        print("error: text is empty", file=sys.stderr)
        return 1
    if not 1 <= len(TEXT) <= 1000:
        print(f"error: text is {len(TEXT)} characters, need 1-1000", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)

    print(TEXT)
    print(f"---\n{len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
