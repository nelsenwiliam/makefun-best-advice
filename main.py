#!/usr/bin/env python3
"""Best Advice I Ever Got — one sentence, up to 200 characters.

Writes the entry to /output/entry.txt. Pure standard library only.
"""

import os

ENTRY = (
    "My father, a man of few words, told me on my wedding day: "
    "'Say sorry first, even when you are right, "
    "because being right is a lonely room'."
)


def main():
    text = ENTRY.strip()
    # One sentence: exactly one terminal full stop, at the very end.
    assert text.endswith(".") and text.count(".") == 1, "must be a single sentence"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
