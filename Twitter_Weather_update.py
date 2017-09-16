# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime

# Twitter API Keys
consumer_key = "fN5urFVP44YC6iwSkzMfimK9S"
consumer_secret = "iOmeKttVNNqxyz98DynXQKHRnrcxLxMmu1gp5i1DYlld7ptiAm"
access_token = "229598666-1ssIZxKh1DIZDImO0GfdttBPLbY9Q9BtNF3V0Fo9"
access_token_secret = "Ry1yXratQdsElBT3pSQcVbznDdpWljrCrxwhdB9yiSOq7"

# Save config information
api_key = "572ecb9cf7bb5d1eccdea81f6bd8913d"
# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "NewYork"
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "London Weather as of %s: %s F" %
        (datetime.datetime.now().strftime("%I:%M %p"),
         weather_json["main"]["temp"]))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every 1 hour
while(True):
    WeatherTweet()
    time.sleep(900)