#Create for the Upcycle clock project using the Intel Edison -- to get number of tweets for a specific hastag
#Author : @CarmelitoA 05/24/2017
#Based on the tweepy libary http://www.tweepy.org/
import tweepy
import re,string,datetime, time

#create an app on dev.twitter.com
consumer_key = "XXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_key = "XXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
hashTag = "upcycleit"

OAUTH_KEYS = {'consumer_key':consumer_key, 'consumer_secret':consumer_secret,
              'access_token_key':access_token_key, 'access_token_secret':access_token_secret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)
def tweet_count_today():
    tweetCountToday = 0
    getTweet = tweepy.Cursor(api.search, q=hashTag).items(10)
    for tweet in getTweet:
            print "Name:", tweet.author.name.encode('utf8')
            print "Screen-name:", tweet.author.screen_name.encode('utf8')
            print "Tweet created:", tweet.created_at
            print "Tweet:", tweet.text.encode('utf8')
            print "date diff:",(datetime.datetime.now() - tweet.created_at).days
            if (datetime.datetime.now() - tweet.created_at).days < 2: #this solves the timezone issue, as i am in PST
                print "Awesome some has tweeted today with the hashTag"
                tweetCountToday = tweetCountToday +1
    print "Tweet count today ",tweetCountToday
    return tweetCountToday
#printing the count for testing
#count = tweet_count_today()
#print "Tweet count today is ",count
