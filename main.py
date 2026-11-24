#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes exactly one word describing the entrant's Wi-Fi to
/output/entry.txt. Deterministic: the same word on every run.
"""

import os

ENTRY_WORD = "Gaslighting"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the entry must be exactly one word, 1-20 characters,
    # and not only whitespace. Fail loudly instead of writing bad output.
    if not ENTRY_WORD or ENTRY_WORD != ENTRY_WORD.strip():
        raise ValueError("entry word must not be blank or padded with whitespace")
    if len(ENTRY_WORD) > 20:
        raise ValueError("entry word must be at most 20 characters")
    if len(ENTRY_WORD.split()) != 1:
        raise ValueError("entry must be exactly one word")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD)


if __name__ == "__main__":
    main()
