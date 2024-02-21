#!/usr/bin/python3
"""Defines read_file."""


def read_file(filename=""):
    """open function."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

