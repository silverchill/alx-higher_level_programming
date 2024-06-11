#!/usr/bin/python3
"""URL, sends a request to the URL and displays the body
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as data:
            _str = data.read().decode("utf-8")
            print(_str)

    except urllib.error.HTTPError as e:
        print("Error code: " + str(e.status))
        sys.exit()
