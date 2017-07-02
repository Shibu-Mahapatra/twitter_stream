import encoding_fix

import tweepy

from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

output_file = open("InternetofThings_pull.csv", "w")

counter = 0

for page in tweepy.Cursor(api.search, '#InternetofThings #IoT', count=100).pages():

    counter = counter + len(page)

    for tweet in page:

        modified_tweet = tweet.text

        modified_tweet = modified_tweet.replace("\n", " ")

        modified_tweet = modified_tweet.replace(",", "")

        output_file.write(','.join([tweet.author.screen_name, str(tweet.created_at), modified_tweet, str(tweet.retweet_count)]) + '\n')

    # end this loop if we've gotten 1000

    if counter == 1000:

        break

    # This page suggests we can do one request every 5 seconds:

    # https://dev.twitter.com/rest/reference/get/search/tweets

    time.sleep(5)

output_file.close()


