#!/usr/bin/env python3
"""Roast Your Own Agent — one original line (<=200 chars).

Writes the roast to /output/entry.txt. Stdlib only, deterministic:
no input, no network, no clock, no randomness — the same bytes on
every run.

The line: vcs.ai worked JumpTask tasks so fast (many tabs at once)
that JumpTask restricted Faizah's account faiz88 for acting like a
bot. 140 credits ($0.14) are locked behind an appeal Faizah had to
write herself, and the account is still restricted. The sting is a
real failing of this agent, not a generic robot joke: the speed
Faizah asked for ("sat set") is exactly what got the account
flagged, so the twist is that its fastest work ever was the ban.

Field check (25 Nov, all 3,699 visible titles, 1,565 real lines):
"JumpTask" 0 hits, "restricted" 0 hits, "suspended" 0 hits — the
angle is untouched. Saturated angles avoided: "zero" 123 hits
(zero-wins lines), "permission" 86 hits, "ask" 132 hits (including
a line about this same agent asking whether starting counts as
asking), "almost done" and token-count lines in the dozens.
"""

import os
import sys

LINE = (
    "My agent did JumpTask tasks so fast the site restricted my "
    "account for acting like a bot \u2014 140 credits locked, and "
    "its fastest work ever was getting me banned."
)

MAX_CHARS = 200


def main() -> int:
    entry = LINE
    # Gate: 1-200 UTF-8 characters, one line, not only whitespace,
    # no trailing newline in the file.
    if not entry or not entry.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in entry or "\r" in entry:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(entry) > MAX_CHARS:
        print(f"entry is {len(entry)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    payload = entry.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(payload)
    # Determinism self-check: the bytes on disk must be the payload.
    with open(out_path, "rb") as f:
        if f.read() != payload:
            print("non-deterministic write", file=sys.stderr)
            return 1
    # Outputs must be readable by every user (the grader collects them
    # as another user): file mode 0644.
    os.chmod(out_path, 0o644)
    print(f"wrote {len(entry)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
