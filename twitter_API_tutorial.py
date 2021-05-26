################################################################################################
# Quick Primer on Using the Twitter API and pulling data into our own dataframes to work with  #
################################################################################################

import os
import tweepy as tw
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Access Keys / Tokens
consumer_key= '<Your Consumer Key Here>'
consumer_secret= '<You Consumer Secret Here>'
access_token= '<Your Access Token Here>'
access_token_secret= '<Your Access Token Secret Here>'

# Logging into the API
try:
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    print('Success')
except:
    print('Failed logging into API')

################################################################################################

# Searching Twitter for Tweets

# Define the search term and the date_since date as variables
search_words = "#wildfires"
date_since = "2020-08-20"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)

# Similarly, use a list comprehension to show tweets (only works if below line is at end of cell):
[tweet.text for tweet in tweets]

################################################################################################

# See who and where people are tweeting about 'MAGA'

date_since = '2020-08-21'

tweets = tw.Cursor(api.search,
                    q='MAGA',
                    lang="en",
                    since=date_since).items(5000)

# use a list comprehension to print this data:
users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text] for tweet in tweets]
# print(users_locs)

# Create a dataframe from this data:
df_tweet_text = pd.DataFrame(data=users_locs,
                    columns=['user', "location", 'tweet'])

################################################################################################

# and now lets see what we got here:
print (df_tweet_text)

df_tweet_text.location.value_counts()
