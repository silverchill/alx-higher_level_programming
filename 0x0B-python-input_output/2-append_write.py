#!/usr/bin/python3
"""This module defines a method that appends to a file"""


def append_write(filename="", text=""):
    """method to append to a file"""
    with open(filename, "a") as file:
        for c in text:
            file.write(c)
    return len(text)
