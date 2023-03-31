#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable."""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        requested_id = response.getheader('X-Request-Id')
    print(requested_id)
