#!/usr/bin/python3
"""
Queries the reddit API and returns the top 10 hot posts in the subreddit

"""


import requests
import json


def top_ten(subreddit):
    """ This method queries the reddit API and returns the list of top 10
        subreddit
    """
    uri = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
        subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16)'}
    response = requests.get(uri, headers=headers)
    try:
        top_ten = response.json()['data']['children']
        for post in top_ten:
            print(post['data']['title'])
    except KeyError:
        print("None")
