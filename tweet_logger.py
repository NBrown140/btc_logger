""" Inspired from: https://github.com/llSourcell/twitter_sentiment_challenge """

import tweepy, csv
import numpy as np
from textblob import TextBlob
from bitstampy import api

# Define number of tweets to search
tweet_count = 100
# Define tags to search
tags = ['bitcoin', 'btc', 'eur', 'xrp', 'ltc', 'eth']
# Define path to output csv
root_path = r"D:\Bitcoin\twitterSentiment.csv"

# Authenticate Twitter API
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'
access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api_tweet = tweepy.API(auth)


# Retrieve Tweets
search_results = [api_tweet.search(q=tag, count=tweet_count) for tag in tags]

for search_result,tag in zip(search_results, tags):
    pol_sub_array = np.empty((tweet_count,2))   #Polarity and subjectivity array
    count = 0
    for tweet in search_result:
        # Perform Sentiment Analysis on Tweet, save in array
        analysis = TextBlob(tweet.text)
        pol_sub_array[count,0] = analysis.sentiment.polarity
        pol_sub_array[count,1] = analysis.sentiment.subjectivity
        count += 1
    # Remove excess lines in case less than tweet_count were found
    pol_sub_array = pol_sub_array[:count,:]
    # Compute statistics
    avg = np.around(np.mean(pol_sub_array, axis=0), decimals=3)
    median = np.around(np.median(pol_sub_array, axis=0), decimals=3)
    std = np.around(np.std(pol_sub_array, axis=0), decimals=3)
    # Make row
    ticker = api.ticker()
    row = [ticker['timestamp'], avg[0], median[0], std[0], avg[1], median[1], std[1]]
    # Save statistics
    specific_path = root_path.split('.')[0]+'_'+tag+'.'+root_path.split('.')[1]
    with open(specific_path, 'ab') as f:
        w = csv.writer(f)
        w.writerow(row)
