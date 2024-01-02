#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
