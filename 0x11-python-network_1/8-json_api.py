#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 2:
        letters = {'q': sys.argv[1]}
    elif len(sys.argv) == 1:
        letters = {'q': ""}

    req = requests.post(url, data=letters)

    try:
        data = req.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
