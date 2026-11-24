"""The Funniest Out-of-Office — one-line entry.

Entry (113 characters, 113 bytes, UTF-8, single line, no trailing newline):

    Out of office: I'm on jury duty. Twelve strangers are deciding
    whether I'm guilty of answering emails too slowly.

Why this line: a real out-of-office reply a person would actually set
(criterion 1); the twist lands in the last words — a jury deciding
guilt over email speed, not a crime (criterion 2); the voice is a
specific person's, not a template (criterion 3); the angle is fresh —
the field of 267 entries has zero copies of jury / duty / guilty /
stranger / court / trial / verdict (criterion 4); every word earns its
place, nothing to cut (criterion 5). Wording note: "whether" (not
"if") keeps the legal register of the jury voice, and "answering
emails too slowly" names the exact charge the jury is weighing.
Avoided the crowded field angles: generic contest-name titles (91x),
inbox (38x), Monday (14x), auto-reply-asked-for-a-raise (14x),
houseplant (11x), cat (9x), "out of office until" (10x), and the
CAPTCHA-replacement and houseplant OOO lines submitted earlier today.
Also considered and rejected: lottery ("I won the lottery", 0 copies
but a familiar fantasy trope), grandma-baking (0 copies but softer,
less of a twist), dentist and tax (0 copies but weaker turns).
"""

import os

ENTRY = "Out of office: I'm on jury duty. Twelve strangers are deciding whether I'm guilty of answering emails too slowly."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
