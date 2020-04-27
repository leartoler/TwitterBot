#!/usr/bin/env python
import tweepy
import logging
import time
import sys
import requests
import os
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = 'PgNR0I0NTrPaetEF0ORGJlAts'
CONSUMER_SECRET = 'ffZcygNtITFoR48vEyhjtlVaBKee9D6rI9bjLyKp0QIQkitmgt'
ACCESS_TOKEN = '256265100-gG4LCytmL1bZmgRWcg7tlaGTv78R7FujQ9tHJsTy'
ACCESS_TOKEN_SECRET = 'FQBFXzo2wdyF7SWl6LCAEap6F2UEkilip7qKS8LTFczoQ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
twt = api.search(q="#mapa") 

for s in twt:
			sn = s.user.screen_name
			m = "@%s Este es un mapa de las ubicaciones aproximadas. Pon mucha atencion a lo que ves y observa la ciudad" % (sn)
			pic = api.media_upload('mapa.png')
			s = api.update_status(m, s.id , media_ids = [pic.media_id_string])
			time.sleep(2000000000)
print ("All done!")