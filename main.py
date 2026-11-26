#!/usr/bin/env python3
"""The One-Liner Groan-Off - make.fun entry.

Writes one original one-line dad joke to /output/entry.txt.
Python 3 standard library only, deterministic, no network.
"""
import os

# The joke is assembled from named parts so the setup and the punchline
# can be edited independently; the joined line is the judged entry and
# must stay byte-identical.
PARTS = [
    "I told my suitcase we're not travelling this year,",
    "so now it's just sitting there,",
    "full of emotional baggage.",
]

JOKE = " ".join(PARTS)

# The gate allows 1 to 140 characters; guard against accidental edits
# that would change the joke's length or wording.
assert 1 <= len(JOKE) <= 140, f"entry joke out of gate: {len(JOKE)} chars"
assert len(JOKE) == 109, f"entry joke changed: {len(JOKE)} chars"
assert JOKE.endswith("emotional baggage.")


def clear_output_dir(path):
    """Clear the contents of the output dir without removing the dir
    itself (the grader runs as a different user and may not be able to
    recreate it)."""
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        entry = os.path.join(path, name)
        if os.path.isfile(entry):
            os.remove(entry)


def main():
    clear_output_dir("/output")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Self-check: what landed on disk must be exactly the judged joke.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt differs from JOKE"
    assert 1 <= len(written) <= 140, "entry.txt outside the 1-140 gate"


if __name__ == "__main__":
    main()
