#!/usr/bin/python3
"""
Function that queries the Reddit API
and returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": "custom"},
    )
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
