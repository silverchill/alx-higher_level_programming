#!/usr/bin/python3
""" python module that fetche using urllib """

import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as new_data:
    data = new_data.read()
    _str = "Body response:\n\
\t- type: {}\n\
\t- content: {}\n".format(type(data), data)

    data_str = data.decode()
    _str += "\t- utf8 content: " + data_str

    print(_str)
