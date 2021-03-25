from app.apis.api_google_map import ApiGoogle

test = ApiGoogle("mairie rouen")


def test_api_google():
    test = ApiGoogle("mairie rouen")
    assert test.latitude == 49.44323199999999

    assert test.longitude == 1.099971

    assert test.address == "2 Place du Général de Gaulle, 76000 Rouen, France"

    assert test.wiki == "Place du Général de Gaulle"
