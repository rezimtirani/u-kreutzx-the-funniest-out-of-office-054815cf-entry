"""The Funniest Out-of-Office — make.fun entry.

Writes one line of an out-of-office auto-reply to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt when the
variable is unset). The line must be 1 to 140 characters of
UTF-8 text, a single line, nothing else.

Standard library only: the grader container installs nothing.
"""

import os

ENTRY_TEXT = (
    "Out of office. My inbox is being watched by my cat, who deletes "
    "everything on sight and has somehow never missed anything important."
)


def validate(text):
    """The gate's own rules, checked before writing: 1-140 chars,
    single line, not only white space."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return text


def main():
    validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    print("wrote %s (%d characters)" % (path, len(ENTRY_TEXT)))


if __name__ == "__main__":
    main()
