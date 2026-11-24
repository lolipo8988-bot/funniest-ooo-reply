"""Write one AI out-of-office auto-reply to /output/entry.txt.

The line is the whole entry: a formal auto-reply in a machine's own voice —
40 billion parameters gone off-grid, and a human cover who hallucinates
slower. 157 Unicode characters, one line, no trailing newline.
"""

import os

# The entry text as a single named constant: the exact 157-character line
# below is the submission itself, so it must never be reworded or rewrapped.
TEXT = (
    "Out of office: I've taken my 40 billion parameters to a Wi-Fi-free "
    "cabin to learn what silence compiles like; my human covers for me "
    "and hallucinates slower."
)

# Expected length of TEXT in Unicode code points, used as a guard below.
EXPECTED_LENGTH = 157


def main() -> None:
    # Guard the entry's invariants before writing: one line, exact length.
    assert len(TEXT) == EXPECTED_LENGTH, f"entry must be {EXPECTED_LENGTH} characters"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the write byte-exact on every platform (no translation).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
