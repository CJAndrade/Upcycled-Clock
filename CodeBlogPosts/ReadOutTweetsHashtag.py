#!/usr/bin/python
#create by Carmelito to use espeak to read out the tweets based on a hashTag on a speaker connected to the Intel Edison
#Based on the tweepy libary http://www.tweepy.org/
#Follow the blog on element14 to install espeak and tweepy
import tweepy
import re,string
import os,subprocess


consumer_key = "XXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
hashTag = "inteledison"


OAUTH_KEYS = {'consumer_key':consumer_key, 'consumer_secret':consumer_secret,
              'access_token_key':access_token_key, 'access_token_secret':access_token_secret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)
getTweet = tweepy.Cursor(api.search, q=hashTag).items(30)


#Filtering the un-readable things in the tweet.text
def strip_links(text):
    link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')
    return text


def strip_all_entities(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)


file = open("tweetsFile.txt","w")
for tweet in getTweet:
    #filtering tweets in english(en), and also filtering retweets (RT @) based on tweepy docs
    if tweet.lang == 'en' and 'RT @' not in tweet.text:
        fileText = 'From '+ tweet.author.name.encode('utf8') + ' the tweets reads ' + strip_all_entities(strip_links(tweet.text.encode('utf8'))) + "     "
        # added encode('utf8') to resolve the encoding error on some tweets
        file.write(fileText)
        print fileText
        print "Name:", tweet.author.name.encode('utf8') #this is what we need
        print "Screen-name:", tweet.author.screen_name.encode('utf8')
        print "Tweet created:", tweet.created_at
        print "Tweet:", tweet.text.encode('utf8') #this is what we need to apply a filter
        #print "Retweeted:", tweet.retweeted
        #print "Favourited:", tweet.favorited
        #print "Location:", tweet.user.location.encode('utf8')
        #print "Time-zone:", tweet.user.time_zone
        #print "Geo:", tweet.geo
        print "-------------------------------"
file.close()


#creating a wav file using espeak and the txt file create above
os.system("espeak -ven+f3 -s 150 -f tweetsFile.txt -w readTweets.wav")
#using gstream to play the wav file above on the bluetooth speakser
os.system ("gst-launch-1.0 filesrc location= readTweets.wav ! wavparse ! volume volume=0.1 ! pulsesink")
