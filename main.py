"""Write one joke about working beside AI coding agents to /output/entry.txt.

The joke is a single constant so every run writes byte-identical output.
A length guard enforces the competition gate (1-280 Unicode code points)
before anything is written.
"""

import os

JOKE = "I told my agent the demo is at 2; it shipped at 1:59 and spent the last minute rewriting my slides to match the bug."

OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    """Write JOKE to OUTPUT_PATH as UTF-8 with no trailing newline."""
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-280")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
