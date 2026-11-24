#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single one-line joke to /output/entry.txt.

The joke is a fixed string. The program only validates it (one line,
1-280 chars, not only whitespace) and writes it out.
"""

import os
import sys

JOKE = "I bought a standing desk to get healthier; now I'm just unhealthy at a greater altitude."


def main() -> int:
    joke = JOKE.strip()
    if not joke or len(joke) > 280 or "\n" in joke:
        print("joke is not a valid one-liner", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(f"wrote {len(joke)}-char one-liner to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
