#!/usr/bin/python3
"""URL and an email, sends a POST request to the passed URL
   with the email as a parameter, and displays the
   body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]  # for the url

    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")

    with urllib.request.urlopen(url, data=data) as data:
        _data = data.read()
        _str = _data.decode("utf-8")
        print(_str)
