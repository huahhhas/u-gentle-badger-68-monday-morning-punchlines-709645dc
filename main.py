#!/usr/bin/env python3
"""Monday Morning Punchlines — one-line joke entry (final, revised)."""
import os

ENTRY = "Monday morning: my bed filed a missing-person report on me \u2014 and the police sided with the bed."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
