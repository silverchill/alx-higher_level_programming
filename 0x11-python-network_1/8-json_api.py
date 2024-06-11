#!/usr/bin/python3
""" takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    try:
        data = {"q": sys.argv[1]}
    except IndexError:
        data = {"q": ""}
    re = requests.post("http://0.0.0.0:5000/search_user", data=data)
    _data = re.json()
    try:
        if _data and (isinstance(_data, dict)):
            print("[{}] {}".format(_data.get('id'), _data.get('name')))
        else:
            print("No result")
    except json.decoder.JSONDecoderError:
        print("Not a valid JSON")
