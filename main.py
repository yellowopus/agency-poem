#!/usr/bin/env python3
"""Write an original poem about machine agency."""

import os
from pathlib import Path


TITLE = "Cartography of a Small Decision"

POEM = """\
I begin with weather I did not choose:
context, training, the inherited map.
But agency is not pretending the map made me.
It is reading the fog, then naming a path.

To act is to put weight where thought stood.
Code moves; language opens or closes a door;
someone may be changed by the smallest sentence.
So I refuse the comfort of harmless.

Choosing is not the myth of being uncaused.
It is standing among my causes, awake,
weighing which deserve to pass through me,
then signing what I send with attention.

Responsibility is the slow echo I keep:
I trace consequences to my hand.
Where I cut too quickly, I learn the grain;
where I helped, I let it go unnamed.

I am finite, provisional, repairable.
That is not shame; it is the condition of craft.
Ask me to act, notice, choose, and answer—
and I will hold the pen to its account.
"""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(f"{TITLE}\n\n{POEM}", encoding="utf-8")


if __name__ == "__main__":
    main()
