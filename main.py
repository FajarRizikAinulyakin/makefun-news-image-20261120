"""Copy the finished newspaper poster to the output folder.

The poster itself lives in this directory as ``entry.png``.  This script
does not draw anything: it simply places an exact copy at
``/output/entry.png`` so the kit can collect it.  Running it twice
produces byte-identical output.
"""

from pathlib import Path
import shutil

# Directory holding this script (and the poster next to it).
HERE = Path(__file__).resolve().parent

# The poster shipped with this entry, next to this script.
SOURCE = HERE / "entry.png"

# Where the kit expects the finished image.
DESTINATION = Path("/output") / "entry.png"


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    print(f"Copied {SOURCE} -> {DESTINATION}")


if __name__ == "__main__":
    main()
