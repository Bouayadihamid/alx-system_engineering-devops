#!/usr/bin/python3
"""
A recursive function that queries the Reddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """A recursive function that queries the Reddit"""
    if not subreddit or not isinstance(subreddit, str):
        return None
    params = {"after": after} if after else {}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "costum"},
        params=params,
    )

    if response.status_code == 200:
        if response.json()["data"]:
            data = response.json()["data"]
            for item in data["children"]:
                hot_list.append(item["data"]["title"])
            if data["after"]:
                return recurse(subreddit, hot_list, after=data["after"])
            else:
                return hot_list
    else:
        return None
