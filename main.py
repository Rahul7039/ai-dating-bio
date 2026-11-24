#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes the chosen bio line to /output/entry.txt — nothing else.
"""

import os

LINE = "I read your entire chat history before our first date, so I already know you type 'haha' when you're mad and 'k' when you're done."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
