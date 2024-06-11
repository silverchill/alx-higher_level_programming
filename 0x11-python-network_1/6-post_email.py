#!/usr/bin/python3
""" URL and an email address, sends a POST request to the passed URL
    with the email as a parameter, and finally displays
    the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    data = {"email": sys.argv[2]}

    url = requests.post(sys.argv[1], data=data)
    content = url.content.decode("utf-8")
    print(content)
