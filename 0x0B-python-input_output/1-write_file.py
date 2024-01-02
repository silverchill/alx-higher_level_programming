#!/usr/bin/python3
"""This module defines a file writer"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w") as file:
        for c in text:
            file.write(c)
        return len(text)
