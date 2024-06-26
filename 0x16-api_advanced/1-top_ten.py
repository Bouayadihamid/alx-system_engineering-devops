#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddi
"""

import requests


def top_ten(subreddit):
    """A function that queries the Reddit API"""
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "costum"}
        )
    if response.status_code == 200:
        for item in response.json()["data"]["children"]:
            print(item["data"]["title"])
    else:
        print(None)
