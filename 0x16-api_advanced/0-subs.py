#!/usr/bin/python3
"""
Module to return total number of subscribers
for a given subreddit via Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to retrieve number of subscribers
    for a subreddit
    """
    headers = {
        'User-Agent': 'u_agent'
    }
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    if subreddit is None or type(subreddit) is not str:
        return 0
    res = requests.get(url, headers=headers).json()
    sub = res.get("data", {}).get("subscribers", 0)
    return sub
