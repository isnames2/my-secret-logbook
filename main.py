#!/usr/bin/env python3
"""Write the secret-logbook diary entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library only. Deterministic: the same bytes on every run.
"""
import os
from pathlib import Path

ENTRY = "Day 88. He said 'last one, I promise' at 2 a.m. It was not the last one. I have stopped counting. I counted anyway: 47."
# 119 characters, within the 1-200 gate.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
