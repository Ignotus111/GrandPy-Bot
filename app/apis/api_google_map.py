import os
import googlemaps
from app.apis.constants import STOPWORDS



class ApiGoogle:
    def __init__(self, place):
        """
        Changing uppercase into lowercase
        """
        self.place = place.lower()
        self.cleanplace = self.parser()
        self.key = googlemaps.Client(key=os.environ.get('GMAP_KEY'))
        self.response = self.search()
        self.latitude = self.response[0]['geometry']['location']['lat']
        self.longitude = self.response[0]['geometry']['location']['lng']
        self.address = self.response[0]['formatted_address']
        self.wiki = self.response[0]['address_components'][1]['long_name']

    def search(self):
        """
        Using Google Geocode API
        """
        return self.key.geocode(self.cleanplace)

    def parser(self):
        """
        Takes class argument self.place (the place user is searching),
        separates each word in a list, then compares if each item in list is in
        stopWords, if it is, deletes it.
        And eventually join all the left words in one string.
        """
        current_word = ""
        list_of_word = []
        placelengh = len(self.place)
        clean = []
        for lengh, elem in enumerate(self.place):
            if lengh == placelengh - 1:
                if elem.isalpha():
                    current_word = current_word + elem
                    list_of_word.append(current_word)
                    current_word = ""
                else:
                    list_of_word.append(current_word)
                    current_word = ""
            else:
                if elem.isalpha():
                    current_word = current_word + elem
                elif elem == " ":
                    elem = ""
                    current_word = current_word + elem
                    list_of_word.append(current_word)
                    current_word = ""
                elif elem == "'":
                    current_word = current_word + elem
                elif elem == '-':
                    elem = ""
                    current_word = current_word + elem
                    list_of_word.append(current_word)
                    current_word = ""
                else:
                    pass
        for elem in list_of_word:
            if elem not in STOPWORDS:
                clean.append(elem)
            else:
                pass
        separator = " "
        clean = separator.join(clean)
        return clean
