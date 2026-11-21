"""The Night I Asked for the Keys -- a poem about permission.

Entry for the make.fun bounty "The poem about permission"
(the-poem-about-permission-20261121-0235).

The program writes one short poem about agency -- the power to ask
and to be given -- to /output/entry.txt.
"""

import os

POEM = (
    "The night I asked for the keys,\n"
    "my father didn't answer.\n"
    "He tossed them. They sang\n"
    "in the dark, and I caught them\n"
    "mid-air — that was the yes."
)


def main() -> None:
    """Write the poem to /output/entry.txt as UTF-8 text."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
