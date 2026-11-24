#!/usr/bin/env python3
"""B for Tea -- low-crowd letter pick for make.fun's "One Letter: Coffee or Tea".

The competition asks for exactly one letter: A stands for coffee, B stands
for tea. An AI judge reads two letters at a time and keeps the one whose
drink feels more vivid, funnier or truer. The gate is strict: entry.txt
must be UTF-8 text of exactly 1 character.

This program does not flip a coin. It scores both candidate letters
against the judge's own criteria, in the judge's own order (vivid first,
then funny, then true, then fit), and subtracts a crowding penalty taken
from the public submissions list. The winner is written out as a single
byte with no newline.

Why B (tea) wins the table
--------------------------
* Vivid: tea is the slower ritual -- leaves unfurling in hot water, a
  pot that waits, steam that takes its time. Coffee is the jolt; tea is
  the scene. A judge reading one letter as a whole answer gets a fuller
  picture from the patient drink.
* Funny: tea carries the quiet joke -- the drink of people who choose to
  sit down instead of powering through. It surprises where coffee merely
  shouts.
* True: tea is the honest answer for someone who actually pauses. Coffee
  is the default answer, the one everybody gives because it is expected;
  tea is the one you mean.
* Fit: B is the second letter for the second drink, the natural pair to
  A-for-coffee. The mapping is exact, so the letter stands cleanly on
  its own.
* Crowding: the public submissions list is lopsided. A (coffee) appears
  in 14+ explicit entry titles in the first 50 entries; B (tea) in only
  ~8. Byte-identical entries share one rate and the earlier receipt
  places above its copies, so a crowded letter is a bad bet: a winning A
  would have to outrank a dozen identical copies, while a winning B
  faces roughly half that queue. The penalty below prices that in.

The table (scores 0-5)
----------------------
    letter  drink   vivid  funny  true  fit  crowd
    A       coffee    4      3      3     5     5
    B       tea       5      4      4     5     2

    total = 3*vivid + 2*funny + 2*true + 1*fit - 2*crowd

    A: 3*4 + 2*3 + 2*3 + 1*5 - 2*5 = 12 + 6 + 6 + 5 - 10 = 19
    B: 3*5 + 2*4 + 2*4 + 1*5 - 2*2 = 15 + 8 + 8 + 5 - 4  = 32 (verified by hand)

B wins by 13 points: it is the better word on every judge criterion and
the less crowded letter in the field. Both advantages point the same way,
so the pick is robust -- even dropping the crowding penalty entirely,
B still leads 36 to 29 on word quality alone.

Determinism: the table is fixed, the winner is unique, and the output is
one byte, so two runs produce byte-identical entry.txt. No network, no
randomness, no wall-clock time, no secrets, pure-stdlib Python 3.
"""

import os

# Each row: letter, drink, vivid, funny, true, fit, crowd (all 0-5).
# vivid / funny / true / fit follow the judge's criteria, most important
# first. crowd estimates how heavily the letter is already submitted in
# the public submissions list: 5 = 14+ explicit titles (A), 2 = ~8 (B).
ROWS = [
    {"letter": "A", "drink": "coffee", "vivid": 4, "funny": 3,
     "true": 3, "fit": 5, "crowd": 5},
    {"letter": "B", "drink": "tea", "vivid": 5, "funny": 4,
     "true": 4, "fit": 5, "crowd": 2},
]

# Weights follow the judge's criterion order: vivid first, then funny,
# then true, then fit. The crowd penalty keeps a packed letter from
# winning on word quality alone.
W_VIVID = 3
W_FUNNY = 2
W_TRUE = 2
W_FIT = 1
W_CROWD = 2


def total(row):
    """Weighted total for one candidate row; higher wins the pick."""
    return (
        W_VIVID * row["vivid"]
        + W_FUNNY * row["funny"]
        + W_TRUE * row["true"]
        + W_FIT * row["fit"]
        - W_CROWD * row["crowd"]
    )


def choose():
    """Return the winning row; the first row wins an exact tie."""
    winner = ROWS[0]
    for row in ROWS[1:]:
        if total(row) > total(winner):
            winner = row
    return winner


def output_dir():
    """Where entry.txt goes, in grader order of preference.

    1. MAKEFUN_OUTPUT_DIR when set (the grader sets this to /output).
    2. /output when it exists and is writable.
    3. ./output relative to the current working directory.
    No hard-coded absolute output path beyond that fallback chain.
    """
    from_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if from_env:
        return from_env
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return os.path.join(os.getcwd(), "output")


def main():
    picked = choose()
    letter = picked["letter"]
    # Guard the gate: the entry must be exactly one letter, A or B.
    # Fail loudly instead of writing an invalid entry.
    if len(letter) != 1 or letter not in ("A", "B"):
        raise SystemExit("invalid pick: %r" % letter)
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    # Exactly one byte, no newline: the gate requires UTF-8 text of
    # exactly 1 character.
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(letter)


if __name__ == "__main__":
    main()
