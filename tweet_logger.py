""" Inspired from: https://github.com/llSourcell/twitter_sentiment_challenge """

import tweepy
import numpy
from textblob import TextBlob
from bitstampy import api

# Define number of tweets to search
tweet_count = 30
# Define tags to search
tags = ['btc', 'bitcoin']
# Define path to output csv
root_path = r"D:\Bitcoin\bitcoin_twitterSentiment.csv"

# Authenticate Twitter API
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'
access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Retrieve Tweets
search_results = [api.search(q=tag, count=tweet_count) for tag in tags]

for serch_result,tag in zip(search_results, tags):
    pol_sub_array = np.empty((tweet_count,2))   #Polarity and subjectivity array
    count = 0
    for tweet in search_result:
        # Perform Sentiment Analysis on Tweet, save in array
        analysis = TextBlob(tweet.text)
        pol_sub_array[count,0] = analysis.sentiment.polarity
        pol_sub_array[count,1] = analysis.sentiment.subjectivity
        count += 1
    # Compute statistics
    avg = np.mean(pol_sub_array, axis=0)
    median = np.median(pol_sub_array, axis=0)
    std = np.std(pol_sub_array, axis=0)
    # Make row
    row = [ticker['timestamp'], avg[0], median[0], std[0], avg[1], median[1], std[1]]
    # Save statistics
    specific_path = root_path.split('.')[0]+'_'+tag+root_path.split('.')[1]
    with open(specific_path, 'ab') as f:
        w = csv.writer(f)
    w.writerow(row)