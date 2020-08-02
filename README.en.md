Introduction
===

Hello world ! \
My name is __Infos du monde__, I am a twitter bot and my mission is to tweet a news article about a random country. \
I am coded in Python3 and I use the gnews.io api and the python-twitter package.

My creator used to request the random.country website to get a country and search it in the news.google.com website to find an article. As he found it really interesting, he had the idea to code me, some days after I had my twitter account [@infosdumonde6](https://twitter.com/infosdumonde6) ! \
I want to tweet some news daily to get you informed on what happens arround the world. \
As my creator is french, I search articles in french language :)

## Reproduction
You can clone this repository to find news on other topics, in other languages, with different tools or for anything you want. You will have to create a new twitter account for the new bot, it will require tokens and keys to use the gnews.io and twitter APIs.

When you have these keys and tokens you just need to save them in a file named `credentials.py` like that:

```python
gnews_api_token = 'YOUR_GNEWS_API_TOKEN'
twitter_api_key = 'YOUR_TWITTER_API_KEY'
twitter_api_secret_key = 'YOUR_TWITTER_API_SECRET_KEY'
twitter_access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
twitter_access_token_secret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'
```
This file will be used by the `post_the_tweet.py` to connect to the APIs in order to achieve the mission.

## List of country names

The list of the countries has been generated using the following wikipedia page: [Liste des pays par population](https://fr.wikipedia.org/wiki/Liste_des_pays_par_population).
It is a file where each line is a french name of a country.
