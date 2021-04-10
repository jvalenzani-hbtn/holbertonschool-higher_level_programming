#!/usr/bin/python3
'''
Get some data from the header
'''

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        x_request_id = response.getheader('X-Request-Id')        
    print(x_request_id)

