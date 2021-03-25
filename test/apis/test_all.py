from app.apis.api_google_map import ApiGoogle
from app.apis.api_wiki_media import ApiWiki
from app.apis.parsefunc import parser


def test_all():
    testgoogle = ApiGoogle("Où est la mairie de Rouen ?")
    testwiki = ApiWiki(testgoogle.wiki)
    assert testgoogle.address == "2 Place du Général de Gaulle, 76000 Rouen, France"
    assert len(testwiki.result) >= 50
