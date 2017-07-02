import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
output_file = open("InternetofThings.csv", "w")
class StreamListener(tweepy.StreamListener):

    def on_status(self, tweet):

        modified_tweet = tweet.text

        modified_tweet = modified_tweet.replace("\n", " ")

        modified_tweet = modified_tweet.replace(",", "")

        output_file.write(','.join([tweet.author.screen_name, str(tweet.created_at), modified_tweet, str(tweet.retweet_count)]) + '\n')

        print(modified_tweet)

    def on_error(self, status_code):

        print('Error: ' + repr(status_code))

        return False

l = StreamListener()

streamer = tweepy.Stream(auth=auth, listener=l)

keywords = ['#InternetofThings', '#IoT']

streamer.filter(track = keywords)

output_file.close()


