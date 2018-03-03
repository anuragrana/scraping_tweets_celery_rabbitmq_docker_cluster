from __future__ import absolute_import
from celery_main.celery import app
import time
import random
import json
import proxy
from bs4 import BeautifulSoup
import database
import traceback


@app.task(bind=True,default_retry_delay=10)
def do_work(self, handle):
    print('handle received ' + handle)
    url = "https://twitter.com/" + handle
    session = proxy.get_session()
    response = session.get(url, timeout=5)
    print("-- STATUS " + str(response.status_code) + " -- " + url)
    if response.status_code == 200:
        parse_tweets(response, handle)


def parse_tweets(response, handle):
    soup = BeautifulSoup(response.text, 'lxml')
    tweets_list = list()
    tweets = soup.find_all("li", {"data-item-type": "tweet"})
    for tweet in tweets:
        tweets_list.append(get_tweet_text(tweet))

    return tweets_list
    print(str(len(tweets_list)) + " tweets found.")
    database.save_tweets(tweets_list)


def get_tweet_text(tweet):
    try:
        tweet_text_box = tweet.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
        images_in_tweet_tag = tweet_text_box.find_all("a", {"class": "twitter-timeline-link u-hidden"})
        tweet_text = tweet_text_box.text
        for image_in_tweet_tag in images_in_tweet_tag:
            tweet_text = tweet_text.replace(image_in_tweet_tag.text, '')
        return tweet_text
    except Exception as e:
        return None
