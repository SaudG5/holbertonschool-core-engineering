#!/usr/bin/env python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append text to a file and return the character count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
