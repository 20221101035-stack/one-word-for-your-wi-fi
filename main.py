#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entrypoint.

Writes the single word describing our Wi-Fi to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The word: home Wi-Fi plays peekaboo — the signal is there, then it
isn't, then it's back, right when you need it. One word, no caption
needed, and it doubles as a network name.

Standard library only, deterministic, no network.
"""

import os

WORD = "Peekaboo"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Gate for THIS competition (competition.yaml): UTF-8 text of 1 to 20
    # characters, not only whitespace, one word. Tightened: also cap bytes
    # (ASCII here, so bytes == chars) and forbid any whitespace or
    # punctuation tricks inside the word.
    assert 1 <= len(WORD) <= 20, "word must be 1-20 characters"
    assert len(WORD.encode("utf-8")) <= 20, "word must be <= 20 bytes"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert WORD.isalpha(), "word must be plain letters only"

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Read back and verify the written bytes match the word exactly.
    with open(path, "rb") as f:
        written = f.read()
    assert written == WORD.encode("utf-8"), "written bytes differ from word"


if __name__ == "__main__":
    main()
