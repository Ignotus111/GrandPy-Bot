from app.apis.api_wiki_media import ApiWiki


def test_api_wiki():
    test = ApiWiki("Place du Général de Gaulle")
    assert test.pagerequest["query"]["search"][0]["pageid"] == 1019357
    assert len(test.result) >= 50


def test_error():
    test = ApiWiki("ejhzejg")
    assert test.result == "Ma mémoire me joue des tours! Je n'ai rien à te raconter sur ce lieu."
