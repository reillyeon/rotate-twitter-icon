#!/usr/bin/env python

import json
import sys
import tweepy

if len(sys.argv) != 2:
  print("Usage: %s config.json" % sys.argv[0])

config = None
config_file = sys.argv[1]
with open(config_file) as f:
  config = json.loads(f.read())

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

api = tweepy.API(auth)

icons = config['icons']
last_icon = config.get('last_icon', -1)
next_icon = (last_icon + 1) % len(icons)

api.update_profile_image(icons[next_icon])

config['last_icon'] = next_icon

with open(config_file, 'w') as f:
  f.write(json.dumps(config, sort_keys=True, indent=2, separators=(',', ': ')))
