# Twitter Icon Rotator

A simple script to rotate your Twitter profile through a set of icons.

## Setup

1. `pip install -r requirements.txt`
2. Create your own Twitter App at https://apps.twitter.com.
3. Generate an access token in addition to the app keys.
4. Set up your keys and a list of icons in the configuration file (example below).
5. Create a cron job to run the script periodically to show off your different icons.

## Usage

    python rotate.py config.json

## Configuration File

    {
      "access_token": "<YOUR ACCESS TOKEN>",
      "access_token_secret": "<YOUR ACCESS TOKEN SECRET>",
      "consumer_key": "<YOUR CONSUMER KEY>",
      "consumer_secret": "<YOUR CONSUMER SECRET>",
      "icons": [
        "icons/icon1.jpg",
        "icons/icon2.jpg",
        "icons/icon3.jpg",
        "icons/icon4.jpg",
        "icons/icon5.png"
      ],
      "last_icon": 0
    }
