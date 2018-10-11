import tweepy
from geopy.exc import GeocoderTimedOut
from tweepy import Stream
from tweepy import OAuthHandler
import sqlite3
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Pauva")

DISEASES = ["dengue", "malaria", "flu", "ebola", "lyphoma"]

conn = sqlite3.connect('test.db')
print("Opened database successfully")

# conn.execute('''CREATE TABLE APP
#          (ID INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL,
#          STATUS             TEXT     NOT NULL,
#          TIMESTAMP          TEXT    NOT NULL,
#          GEO_LAT   TEXT     NOT NULL,
#          GEO_LONG  TEXT     NOT NULL,
#          DISEASE    TEXT
#          );''')
print("Table created successfully")

# consumer key, consumer secret, access token, access secret.
ckey = "yLwQrYRlPendBPViLfuqDCv7P"
csecret = "ipyvrNL0H6RvJPik84YbqdSNw7ItFq9JOtZ0qKmxvrk00H5QNq"
atoken = "792114043951714304-mVc2j6GH4K7lPlFWLewDxSFlnw3kClf"
asecret = "ECaWRWJQYqCp7GtWbdDaiqEqcDCDpbxplgfpFyplZUGkH"


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            status_text = str(status.text).encode('ascii', 'ignore')
            status_timestamp = str(status.created_at)
            temp_str = status_text.decode('ascii').split(" ")
            status_disease = ""
            for item in temp_str:
                if item.lower() in DISEASES:
                    status_disease = item.lower()
                    break
            if status.coordinates is None:
                user_loc = status.user.location
                if user_loc is None:
                    return
                location = geolocator.geocode(user_loc)
                if location is None:
                    return
                status_geo_lat, status_geo_long = str(location.latitude), str(location.longitude)
            else:
                status_geo_lat, status_geo_long = status.coordinates
            conn.execute("INSERT INTO APP (STATUS, TIMESTAMP, GEO_LAT, GEO_LONG, DISEASE) VALUES (?, ?, ?, ?, ?)",
                         (status_text, status_timestamp, status_geo_lat, status_geo_long, status_disease))
            conn.commit()
            print("Commited")
        except UnicodeEncodeError:
            pass
        except GeocoderTimedOut:
            return

    def on_error(self, status_code):
        if status_code == 420:
            return False


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, StreamListener())
twitterStream.filter(languages=["en"], track=DISEASES)
