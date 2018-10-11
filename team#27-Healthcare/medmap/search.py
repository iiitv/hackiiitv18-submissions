import sqlite3

import tweepy
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut
from tweepy import OAuthHandler

ckey = "yLwQrYRlPendBPViLfuqDCv7P"
csecret = "ipyvrNL0H6RvJPik84YbqdSNw7ItFq9JOtZ0qKmxvrk00H5QNq"
atoken = "792114043951714304-mVc2j6GH4K7lPlFWLewDxSFlnw3kClf"
asecret = "ECaWRWJQYqCp7GtWbdDaiqEqcDCDpbxplgfpFyplZUGkH"

DISEASES = ["dengue", "malaria", "flu", "ebola", "lyphoma"]

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

conn = sqlite3.connect('test.db')
geolocator = Nominatim(user_agent="Pauva")

for tweet in tweepy.Cursor(api.search, q="flu").items(1000):
    try:
        status_text = str(tweet.text)
        status_timestamp = str(tweet.created_at)
        temp_str = status_text.split(" ")
        status_disease = str([item for item in temp_str if item.lower() in DISEASES])
        if tweet.coordinates is None:
            user_loc = tweet.user.location
            if user_loc is None:
                continue
            location = geolocator.geocode(user_loc)
            if location is None:
                continue
            status_geo_lat, status_geo_long = str(location.latitude), str(location.longitude)
        else:
            status_geo_lat, status_geo_long = tweet.coordinates
        conn.execute("INSERT INTO APP (STATUS, TIMESTAMP, GEO_LAT, GEO_LONG, DISEASE) VALUES (?, ?, ?, ?, ?)",
                     (status_text, status_timestamp, status_geo_lat, status_geo_long, status_disease))
        conn.commit()
        print(status_text)
    except UnicodeEncodeError:
        pass
    except GeocoderTimedOut:
        pass
