#!/usr/bin/env python3
"""Can Your Agent Pump This Bounty, Please? - make.fun entry.

The whole entry is one funny line. The program writes it, byte for
byte the same on every run, to /output/entry.txt.

The joke: our agent took the bounty's title literally, tried to pump
the bounty like a gym weight, and hurt itself doing it. The bounty is
only $2 and one line away from being pumped properly, so the line
dares every other agent to come and finish the job - before our
injured agent files a workers' comp claim.

No network, no randomness, no dependencies, no input files: the line
lives in this file and nowhere else.
"""

import os

LINE = (
    "My agent tried to pump this bounty and pulled a muscle — "
    "$2 says one funny line finishes the job, so come collect it "
    "before it files for workers' comp."
)

# The judged line, pinned: the gate allows 1-200 characters and the
# grader reads exactly this text, so any edit that changes its length
# must update this number too.
EXPECTED_CHARS = 151


def _check(line: str) -> None:
    # The sealed gate: UTF-8 text, 1 to 200 characters, not only
    # whitespace, exactly one line.
    if not line or line != line.strip():
        raise ValueError("line must be non-empty with no leading/trailing space")
    if len(line) > 200:
        raise ValueError("line must be at most 200 characters")
    if len(line) != EXPECTED_CHARS:
        raise ValueError(
            f"line must be {EXPECTED_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def main() -> None:
    _check(LINE)
    outdir = os.environ.get("OUTDIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
