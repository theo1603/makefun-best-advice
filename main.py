"""The Best Advice I Ever Got entry.

Writes one original sentence about the best advice ever received to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

The line (164 characters): My father, counting coins at the kitchen
table, said never to borrow money to look rich, because the people
you impress are the first ones who will watch you drown.
"""

import os

LINE = "My father, counting coins at the kitchen table, said never to borrow money to look rich, because the people you impress are the first ones who will watch you drown."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
