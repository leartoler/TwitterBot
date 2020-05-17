#!/usr/bin/env python
import tweepy
import logging
import time
import sys
import requests
import os
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = '}'
CONSUMER_SECRET = '}'
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
twt = api.search(q="#cuicuilcorally") 

for s in twt:	
			sn = s.user.screen_name
			m = "@%s Como jugar? Descubre cada una de las imagenes y pon mucha atencion a los detalles. Escribe #mapa para tener una ubicacion aproximada" % (sn)
			pic = api.media_upload('cuicuilcorally.png')
			s = api.update_status(m, s.id , media_ids = [pic.media_id_string])
			#Stime.sleep(2000000000)

print ("All done!")
