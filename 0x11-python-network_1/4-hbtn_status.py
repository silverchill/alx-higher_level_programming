#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    content = r.content.decode("utf-8")
    c_type = type(content)
    _str = "Body response:\
\n\t- type: {}\
\n\t- content: {}".format(c_type, content)
    print(_str)
