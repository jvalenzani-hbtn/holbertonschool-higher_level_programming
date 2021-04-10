#!/usr/bin/python3
""" Can I get your URL? """

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        r = response.read()
    print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'.format(type(r),r,str(r, 'UTF-8')))

