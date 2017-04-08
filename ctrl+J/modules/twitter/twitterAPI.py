from core.api import api


def getTweets(username):
    try:
        tweets = api.GetUserTimeline(screen_name=username)
    except Exception:
        return -1
    return tweets
