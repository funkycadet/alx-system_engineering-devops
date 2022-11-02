#!/usr/bin/python3
"""
Module to return first 10 hot posts
for a given subreddit via Reddit API
"""

import requests


def top_ten(subreddit):
    """
    Function to retrieve first top ten
    hot posts for a subreddit
    """
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'u_agent'
    }
    params = {
        "limit": 10
    }

    if subreddit is None or type(subreddit) is not str:
        return 0
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 404:
        return None
    result = res.json().get('data')
    [print(c.get("data").get("title")) for c in result.get("children")]
