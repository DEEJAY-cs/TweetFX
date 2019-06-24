# -*- coding: utf-8 -*-
"""
@author: dvo
@class: TwitterClient
"""

import re
import tweepy
from tweepy import OAuthHandler
import matplotlib.pyplot as plt

import pandas as pd
import datetime


class TwitterClient(object):
    """
        Twitter Class
    """
    def __init__(self):
        """
            Class constructor or initialization method.
        """
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'Nj9Dq0oDSmfSAuV37qsOBkqpA'
        consumer_secret = 'zLBuBzuBAd31SOYAsRcwCZCkSqyDnlx7IiMy5Jn0fS1oCvTZYF'
        access_token = '2650941386-cPGzevCDhJF8j3p6FC7zjVnO1CkH7hAotdHj2QC'
        access_token_secret = 'nPavooMqJDG3mRU1PYv0ay0sVvHyUJ7zuXG5C89pYyFza'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    """
        Get Tweets
        Used to fetch tweets and parse them.
        @query is the search string
        @count
    """
    def get_tweets(self, query):
        # Empty list to store parsed tweets
        tweets = []
 
        try:
            # Call twitter api to fetch tweets for the current day
            fetched_tweets = self.api.search(q = query ,since=datetime.date.today(),lang="en")
    
            # Parsing tweets one by one
            for tweet in fetched_tweets:
                # Empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # Saving text of tweet
                parsed_tweet['text'] = self.clean_tweet(tweet.text)
                
 
                # Appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # If tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 
def main():
    # Creating object of TwitterClient Class
    api = TwitterClient()
    # Calling function to get tweets
    search=input("Search: ")
    plt.title(search)
    tweets = api.get_tweets(query = search)
    
if __name__ == "__main__":
    # calling main function
    main()