#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to the passed URL
    with the email as a parameter, and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    email_data = urllib.parse.urlencode(email)
    email_data = email_data.encode('ascii')  # data should be bytes
    request = urllib.request.Request(url, email_data)
    with urllib.request.urlopen(request) as response:
        data = response.read()
        data = data.decode('utf-8')
    print(data)
