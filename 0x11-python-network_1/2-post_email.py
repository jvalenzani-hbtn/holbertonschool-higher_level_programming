#!/usr/bin/python3
'''
Wait a minute Mr Postman
'''

import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = { 'email' : email }

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)    
    with urllib.request.urlopen(req) as response:
        r = response.read()
        print(str(r, 'UTF-8'))
