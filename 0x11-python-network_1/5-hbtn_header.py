#!/usr/bin/python3
""" URL, sends a request to the URL and displays the value
    of the variable X-Request-Id in the response header
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    dat = requests.get(url)
    print(dat.headers.get("X-Request-Id"))
