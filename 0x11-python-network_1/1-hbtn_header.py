#!/usr/bin/python3
"""URL, sends request to the URL and displays the value of the X-Request-Id"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(x_request_id)
