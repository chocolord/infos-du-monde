# loading libraries
import requests
import random
import json
import twitter

# loading credentials
from credentials import *

# settings parameters
language = "fr" # choose with https://gnews.io/docs/v3#languages

# get country name
file = open("pays.txt", "r")
allPays = file.readlines()
file.close()
country = random.choice(allPays).replace("\n", "")

# get article url
url = "https://gnews.io/api/v3/search?q=%s&token=%s&lang=%s&max=1" % (country, gnews_api_token, language)
r = requests.get(url)
article_url = r.json()["articles"][0]["url"]

# tweet the link !!!
api = twitter.Api(
        consumer_key = twitter_api_key,
        consumer_secret = twitter_api_secret_key,
        access_token_key = twitter_access_token,
        access_token_secret = twitter_access_token_secret
        )

status = api.PostUpdate(
        status = article_url
        )

# print(status.text)
