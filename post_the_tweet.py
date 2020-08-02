# loading libraries
import requests
import random
import json
import twitter

# loading credentials
from credentials import *

print("bonjour les amis: %s" % twitter_api_key)
exit(0)

# get country name
file = open("pays.txt", "r")
allPays = file.readlines()
file.close()
country = random.choice(allPays).replace("\n", "")

# get article link
url = "https://gnews.io/api/v3/search?q=%s&token=%s&lang=fr&max=1" % (country, gnews_api_token)
r = requests.get(url)

# print(r.json()["articles"][0]["url"])
lien_article = r.json()["articles"][0]["url"]

# tweet the link !!!
api = twitter.Api(
        consumer_key = twitter_api_key,
        consumer_secret = twitter_api_secret_key,
        access_token_key = twitter_access_token,
        access_token_secret = twitter_access_token_secret
        )

status = api.PostUpdate(
        status = lien_article
        )

# print(status.text)
