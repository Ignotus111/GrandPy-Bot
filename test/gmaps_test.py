
from app.apis.api_google_map import ApiGoogle

test = ApiGoogle("mairie rouen")
def test_latitude():
    assert test.latitude == 49.44323199999999

def test_longitude():
    assert test.longitude == 1.099971

def test_complete_adress():
    assert test.address == "2 Place du Général de Gaulle, 76000 Rouen, France"

def test_wiki_part():
    assert test.wiki == "Place du Général de Gaulle"
