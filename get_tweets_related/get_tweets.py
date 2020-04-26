import tweepy
import time
import os
import json
from airflow.models import Variable
def get_tweets():
    with open('/Users/anandkumar.r/Desktop/apache-airflow-dags/twitter_credentials.txt',mode = 'r') as my_file:
        for line in my_file:
            fileds=line.split(";")
            consumer_key=fileds[0]
            consumer_secret=fileds[1]
            access_token=fileds[2]
            access_secret=fileds[3]
    # consumer_key=credentials.CONSUMER_KEY
    # consumer_secret=credentials.CONSUMER_SECRET
    # access_token=credentials.ACCESS_TOKEN
    # access_secret=credentials.ACCESS_TOKEN_SECRET

    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api=tweepy.API(auth)
    #print(api.followers())
    #user=api.me()
    #print(user.followers_count)
    #print(user)
    def limit_handler(cursor):
        try:
            while True:
                yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)

    query = 'Narendra Modi'
    number_of_tweets=1
    
    for tweets in tweepy.Cursor(api.search,query).items(number_of_tweets):
        try:
            with open(f'./tweets.json',mode = 'w') as my_file:
                my_file.write(str(tweets))
        except tweepy.TweepError as e:
            print(e)
        except :
            break
    return tweets
get_tweets()