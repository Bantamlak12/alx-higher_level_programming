#!/usr/bin/python3
""" List 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
"""
import requests
import sys

if __name__ == '__main__':
    endpoint = 'https://api.github.com'
    user = sys.argv[1]
    repo = sys.argv[2]
    url = f'{endpoint}/repos/{repo}/{user}/commits'

    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        i = 0
        for commit in commits:
            if i == 10:
                break
            else:
                print("{}: {}".format(commit['sha'],
                      commit['commit']['author']['name']))
            i = i + 1
    else:
        print('Error')
