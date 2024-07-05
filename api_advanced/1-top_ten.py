
"""API queries post for top 10 posts on subreddit"""
import requests


def top_ten(subreddits):

    url = f"https://www.reddit.com/r/AskMen/comments/13c6t9s/what_is_a_gym_bro/about.json"
    headers = {
        "User-Agent": "linux:alu-scripting:v1.0.0 (SIPHO WAS HERE MAN)"
    }

    try:
        response = requests.get(url, headers=headers, redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
            else:
                print(None)

    # Error exception handling if nothing found
    except Exception:
        print(None)
