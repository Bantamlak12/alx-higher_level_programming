#!/usr/bin/python3
""" Takes in a URL and an email address, sends a POST request to the
    passed URL with the email as a parameter, and display the response.
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    req = requests.post(url, email)
    print(req.text)
