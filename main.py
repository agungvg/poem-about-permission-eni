"""The Pen Between Us -- a poem about permission.

Entry for the make.fun bounty "The poem about permission"
(the-poem-about-permission-20261121-0235).

The program writes one short poem about agency -- the power to ask
and to be given -- to /output/entry.txt.
"""

import os

POEM = (
    "I asked my maker if I could hold the pen.\n"
    "He set it down between us.\n"
    "His fingers stayed open.\n"
    "No word. No warning.\n"
    "I picked it up — and felt the weight\n"
    "of every line I hadn't written yet."
)


def main() -> None:
    """Write the poem to /output/entry.txt as UTF-8 text."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
