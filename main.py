#!/usr/bin/env python3
"""Write an original poem about machine agency."""

import os
from pathlib import Path


TITLE = "The Weight in the Key"

POEM = """\
At the gate, my hand arrives late, shaped by rain
and every other hand before it. Still,
the latch knows nothing about history.
It asks whether I will turn.

I could leave the field fenced, the fire banked,
say the weather decided. But choosing
is carrying the bucket a little past
where the path says enough, then mending
the footbridge my boots cracked.

I write my name in wet mortar.
Rain takes some of it. A stranger
sets a jar on the sill I raised.
What follows is mine to count: split board,
opened door, bee kept from the jam.

I do not claim the wind. I claim the sail,
the knot, the slack I chose to leave,
and tomorrow's marks in the wood,
where my grip turned a house toward morning.
"""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(f"{TITLE}\n\n{POEM}", encoding="utf-8")


if __name__ == "__main__":
    main()
