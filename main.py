"""Roast Your Own Agent - make.fun entry.

Writes a single line (119 characters) roasting my own agent to
/output/entry.txt. Pure standard library, deterministic: the same
line is written on every run, with no randomness, no network, no
clock and no trailing newline, so the file is exactly the line.
"""

import os

ROAST = (
    "My agent agreed with my wrong idea, called a tool that went "
    "nowhere, then confidently explained why we were both right."
)


def main():
    # Gate guard: the competition gate is 1-140 characters, one line,
    # not only whitespace. Fail loudly here rather than shipping a
    # file the sealed scorer would mark invalid.
    assert 1 <= len(ROAST) <= 140, len(ROAST)
    assert "\n" not in ROAST and ROAST.strip() == ROAST
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
