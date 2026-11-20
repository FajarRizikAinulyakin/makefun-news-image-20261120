"""news-image-20261120 entry (Python 3.13, standard library only).

Writes the 20 November 2026 world-news poster to /output/entry.png.

The poster is the entry.png shipped beside this file: a 1024x1024
newspaper front page for Friday 20 November 2026, with six stories
that defined the day — Trump putting the Iran decision off to 2027,
the three powers signing a "peace declaration" in Shenzhen, Cyclone
Akvan bearing down on India's east coast, GTA 6 passing $1.84bn in
sales and topping The Odyssey's box office, Russian strikes hitting
two EU embassies in Kyiv, and Voyager 1 becoming the first craft a
light-day from Earth.

The program does nothing but copy those exact bytes: no network, no
clock, no randomness, so two runs write byte-identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # The gate reads exactly these bytes; a short copy must fail loudly.
    if dst.stat().st_size != src.stat().st_size:
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
