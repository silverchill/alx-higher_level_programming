#!/usr/bin/python3
"""This module gets the object representaion of a JSON"""


def to_json_string(my_obj):
    """method to return the string version of a json"""
    import json
    return json.dumps(my_obj)
