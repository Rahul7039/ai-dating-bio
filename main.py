#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes the chosen bio line to /output/entry.txt — nothing else.

The bio is a dating-app line from an AI that already knows you a little
too well: it read your whole chat history before the first date and can
tell from your texting tells exactly when you are mad and when you are
done. One line, one laugh, no extra text in the output file.
"""

import os

# The chosen bio line — the judged entry. Do not change its text.
BIO_LINE = "I read your entire chat history before our first date, so I already know you type 'haha' when you're mad and 'k' when you're done."


def get_bio():
    """Return the chosen one-line bio, verbatim.

    Guard: a dating-app bio must be a single non-empty line that fits
    the usual bio length limit, so fail loudly instead of writing a
    broken entry.
    """
    assert BIO_LINE, "bio line must not be empty"
    assert "\n" not in BIO_LINE, "bio must be a single line"
    assert len(BIO_LINE) <= 180, "bio must fit within 180 characters"
    return BIO_LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(get_bio())
    print(get_bio())


if __name__ == "__main__":
    main()
