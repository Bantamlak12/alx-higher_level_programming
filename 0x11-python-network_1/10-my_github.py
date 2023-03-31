#!/usr/bin/python3
""" Takes your GitHub credentials (username and password) and uses
    the GitHub API to display your id.
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    name = sys.argv[1]
    passwd = sys.argv[2]

    response = requests.get(url, auth=(name, passwd))
    if response.status_code == 200:
        data = response.json()
        print("{}".format(data['id']))
    else:
        print("None")
