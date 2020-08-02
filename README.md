__NB__: There is an english version of this file: README.en.md

# Présentation

Bonjour les amis ! \
Je m'appelle __Infos du monde__, je suis un bot twitter et ma mission est de twiter un article d'actualité sur un pays choisi au hasard. \
Je suis codé en Pyhton3 et j'utilise l'api gnews.io et le packet python-twitter.

Mon créateur utilisait le site [random.country](random.country) pour choisir un pays au hasard et le rechercher ensuit dans news.google.com pour trouver un article. Comme cela lui plaisait, il a eut l'idée de me coder et quelques jours après j'avais mon compte twitter [@infosdumonde6](https://twitter.com/infosdumonde6) ! \
Je voudrai twitter quelques articles tous les jours pour vous informer de ce qu'il se passe dans le monde. \
Comme mon créateur est français, je cherche des articles en français :)

## Reproduction
Vous pouvez me cloner pour trouver des articles sur d'autre sujet dans d'autres, languages, avec d'autres outils ou pour ce que vous voulez. Il vous faudra créer un compte twitter pour le nouveaux bot, il aura besoin de clés pour utilser les apis gnews.io et twitter.

Lorsque vous aurez ces clés vous pourrez les enregistrer dans un fichier nommé `credentials.py` qui sera de cette forme là:

```python
gnews_api_token = 'VOTRE_GNEWS_API_TOKEN'
twitter_api_key = 'VOTRE_TWITTER_API_KEY'
twitter_api_secret_key = 'VOTRE_TWITTER_API_SECRET_KEY'
twitter_access_token = 'VOTRE_TWITTER_ACCESS_TOKEN'
twitter_access_token_secret = 'VOTRE_TWITTER_ACCESS_TOKEN_SECRET'
```
Ce fichier sera ensuite utilisé par le script `post_the_tweet.py` pour se connecter aux APIs afin de réaliser la mission.

## Liste des noms de pays

La liste des pays a été générée en s'appyant sur la page wikipédia suivante: [Liste des pays par population](https://fr.wikipedia.org/wiki/Liste_des_pays_par_population).
C'est un fichier où chaque ligne contient le nom français d'un pays.
