import os
import googlemaps
from app.apis.parsefunc import parser
#from config import GMAP_KEY


class ApiGoogle:
    def __init__(self, place):
        """
        Changing uppercase into lowercase
        """
        self.place = place
        self.cleanplace = parser(self.place)
        self.key = googlemaps.Client(key=os.environ.get("GMAP_KEY") or GMAP_KEY)
        self.response = self.search()
        self.latitude = self.response[0]["geometry"]["location"]["lat"]
        self.longitude = self.response[0]["geometry"]["location"]["lng"]
        self.address = self.response[0]["formatted_address"]
        self.wiki = self.response[0]["address_components"][1]["long_name"]

    def search(self):
        """
        Using Google Geocode API
        """
        return self.key.geocode(self.cleanplace)
