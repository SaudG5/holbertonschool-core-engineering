#!/usr/bin/env python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a file and return the character count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)