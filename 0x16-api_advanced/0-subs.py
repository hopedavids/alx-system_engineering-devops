#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. 
"""


import requests, json


def number_of_subscribers(subreddit):
    """ Returns the total number of subscribers from the API"""
    uri = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(alx-se 0x16 task 0)'}

    response = requests.get(uri, headers=headers)
    if not response.ok:
        return 0
    subscriber_count = response.json().get('data').get('subscribers')
    return subscriber_count
